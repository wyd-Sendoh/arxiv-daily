#!/usr/bin/env python3
"""
arXiv 每日论文追踪器。

按 config.yaml 里定义的主题/关键词检索 arXiv 最新论文，
去重后按主题分类写入 papers/<slug>.md，并刷新索引 papers/README.md。

仅依赖 arXiv 官方 API（免费、无需密钥）。
"""

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"
DATA_DIR = ROOT / "data"
SEEN_FILE = DATA_DIR / "seen.json"
CONFIG_FILE = ROOT / "config.yaml"

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"


def slugify(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def load_config() -> dict:
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_seen() -> set:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text(encoding="utf-8")))
    return set()


def save_seen(seen: set) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    # 只保留最近 5000 条，防止文件无限膨胀
    SEEN_FILE.write_text(
        json.dumps(sorted(seen)[-5000:], ensure_ascii=False, indent=0),
        encoding="utf-8",
    )


def build_query(keywords: list[str], categories: list[str]) -> str:
    kw_clause = " OR ".join(f'abs:"{k}" OR ti:"{k}"' for k in keywords)
    query = f"({kw_clause})"
    if categories:
        cat_clause = " OR ".join(f"cat:{c}" for c in categories)
        query = f"({cat_clause}) AND {query}"
    return query


def fetch(keywords: list[str], categories: list[str], max_results: int) -> list[dict]:
    params = {
        "search_query": build_query(keywords, categories),
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "arxiv-daily/1.0"})

    last_err = None
    for attempt in range(3):  # arXiv API 偶发 IncompleteRead/超时，重试 3 次
        try:
            with urlopen(req, timeout=60) as resp:
                raw = resp.read()
            root = ET.fromstring(raw)
            break
        except Exception as e:
            last_err = e
            time.sleep(5 * (attempt + 1))
    else:
        raise last_err

    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        arxiv_id = entry.findtext(f"{ATOM}id", "").rsplit("/", 1)[-1]
        published = entry.findtext(f"{ATOM}published", "")[:10]
        updated = entry.findtext(f"{ATOM}updated", "")[:10]
        title = " ".join(entry.findtext(f"{ATOM}title", "").split())
        summary = " ".join(entry.findtext(f"{ATOM}summary", "").split())
        authors = [
            a.findtext(f"{ATOM}name", "")
            for a in entry.findall(f"{ATOM}author")
        ]
        link = ""
        for ln in entry.findall(f"{ATOM}link"):
            if ln.get("rel") == "alternate":
                link = ln.get("href", "")
        papers.append({
            "id": arxiv_id,
            "title": title,
            "summary": summary,
            "authors": authors,
            "published": published,
            "updated": updated,
            "link": link or f"https://arxiv.org/abs/{arxiv_id}",
        })
    return papers


def render_entry(p: dict) -> str:
    authors = ", ".join(p["authors"][:6])
    if len(p["authors"]) > 6:
        authors += " et al."
    abstract = p["summary"]
    if len(abstract) > 600:
        abstract = abstract[:600].rsplit(" ", 1)[0] + "…"
    return (
        f"### [{p['title']}]({p['link']})\n\n"
        f"- **arXiv**: `{p['id']}`  |  **提交日期**: {p['published']}\n"
        f"- **作者**: {authors}\n\n"
        f"{abstract}\n\n"
        f"---\n\n"
    )


def update_topic_file(topic_name: str, slug: str, new_papers: list[dict], run_date: str) -> int:
    """把新论文以「最新在上」的方式插入主题文件，返回新增数量。"""
    path = PAPERS_DIR / f"{slug}.md"
    header = f"# {topic_name}\n\n_自动追踪 arXiv 最新论文，最新更新在最上方。_\n"

    block = f"\n## 📅 {run_date}\n\n"
    block += "".join(render_entry(p) for p in new_papers)

    if path.exists():
        existing = path.read_text(encoding="utf-8")
        existing = existing.replace(header, "", 1).lstrip("\n")
        content = f"{header}{block}{existing}"
    else:
        content = f"{header}{block}"

    path.write_text(content, encoding="utf-8")
    return len(new_papers)


def count_papers(slug: str) -> int:
    path = PAPERS_DIR / f"{slug}.md"
    if not path.exists():
        return 0
    return sum(1 for ln in path.read_text(encoding="utf-8").splitlines()
               if ln.startswith("### "))


def update_index(stats: dict, run_date: str) -> None:
    grand_total = sum(count_papers(slug) for _, slug, _ in stats["topics"])
    lines = [
        "# 📚 arXiv 每日论文索引\n",
        f"_最后更新：{run_date}（UTC）。每日由 GitHub Actions 自动运行。_\n",
        f"当前共收录 **{grand_total}** 篇论文，分为 {len(stats['topics'])} 个主题。\n",
        "## 主题分类\n",
        "| 主题 | 累计 | 本次新增 | 文件 |",
        "| --- | --- | --- | --- |",
    ]
    for topic_name, slug, count in stats["topics"]:
        total = count_papers(slug)
        delta = f"+{count}" if count else "—"
        lines.append(f"| {topic_name} | {total} | {delta} | [{slug}.md]({slug}.md) |")
    lines.append("")
    lines.append(f"> 本次运行新增 **{stats['total']}** 篇。\n")
    (PAPERS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    cfg = load_config()
    categories = cfg.get("categories", []) or []
    max_results = cfg.get("max_results_per_topic", 40)
    days_lookback = cfg.get("days_lookback", 2)

    PAPERS_DIR.mkdir(exist_ok=True)
    seen = load_seen()
    run_date = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days_lookback)).strftime("%Y-%m-%d")

    stats = {"topics": [], "total": 0}

    for topic in cfg["topics"]:
        name = topic["name"]
        slug = topic.get("slug") or slugify(name)
        keywords = topic["keywords"]
        print(f"[{name}] 检索中… 关键词={keywords}")

        try:
            papers = fetch(keywords, categories, max_results)
        except Exception as e:  # 网络/解析失败不影响其他主题
            print(f"  ⚠️  检索失败: {e}", file=sys.stderr)
            stats["topics"].append((name, slug, 0))
            time.sleep(3)
            continue

        fresh = [
            p for p in papers
            if p["id"] not in seen and p["published"] >= cutoff
        ]
        for p in fresh:
            seen.add(p["id"])

        if fresh:
            update_topic_file(name, slug, fresh, run_date)
        stats["topics"].append((name, slug, len(fresh)))
        stats["total"] += len(fresh)
        print(f"  ✅ 新增 {len(fresh)} 篇")

        time.sleep(3)  # 遵守 arXiv API 速率限制（约每 3 秒一次）

    update_index(stats, run_date)
    save_seen(seen)
    print(f"\n完成：共新增 {stats['total']} 篇论文。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
