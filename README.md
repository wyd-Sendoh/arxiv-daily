# 📰 arXiv 每日论文追踪

按关键词每日自动检索 [arXiv](https://arxiv.org) 最新论文，去重后按主题分类，
结果提交到本仓库的 [`papers/`](papers/) 目录。全程由 GitHub Actions 在云端运行，
**无需本地电脑常开，无需任何 API 密钥**。

## 🚀 工作原理

1. [`config.yaml`](config.yaml) 定义追踪的主题、关键词和 arXiv 学科分类。
2. [`fetch_papers.py`](fetch_papers.py) 调用 arXiv 官方 API 检索每个主题的最新论文。
3. 通过 [`data/seen.json`](data/seen.json) 记录已收录的论文 ID，**自动去重**。
4. 新论文以「最新在上」追加进 `papers/<主题>.md`，并刷新 [`papers/README.md`](papers/README.md) 索引。
5. [GitHub Actions 工作流](.github/workflows/daily.yml) 每天定时运行并自动提交。

## ⚙️ 自定义追踪内容

编辑 [`config.yaml`](config.yaml) 即可，**无需改代码**：

```yaml
topics:
  - name: "你的主题名"          # 会生成 papers/你的主题名.md
    keywords:                   # 关键词之间是「或」关系
      - "keyword one"
      - "keyword two"

categories:                    # 限定 arXiv 学科（留空 [] 表示不限）
  - cs.AI
  - cs.LG

max_results_per_topic: 40      # 每主题每次最多收录篇数
days_lookback: 2               # 只保留最近 N 天的论文
```

## 🕒 调整运行时间

修改 [`.github/workflows/daily.yml`](.github/workflows/daily.yml) 里的 cron（UTC 时区）：

```yaml
schedule:
  - cron: "0 1 * * *"   # 每天 UTC 01:00 = 北京时间 09:00
```

也可在仓库 **Actions** 页面点击 **Run workflow** 手动触发。

## 🖥️ 本地试运行

```bash
pip install -r requirements.txt
python fetch_papers.py
```

---
_数据来源：arXiv.org。请遵守 [arXiv API 使用条款](https://info.arxiv.org/help/api/tou.html)。_
