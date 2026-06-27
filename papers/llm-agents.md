# LLM Agents

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-06-27

### [OpenRCA 2.0: From Outcome Labels to Causal Process Supervision](https://arxiv.org/abs/2606.27154v1)

- **arXiv**: `2606.27154v1`  |  **提交日期**: 2026-06-25
- **作者**: Aoyang Fang, Yifan Yang, Jin'ao Shang, Qisheng Lu, Junjielung Xu, Rui Wang et al.

Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities, such as long-context understanding, multi-step reasoning, and tool use. However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. The mechanism is forward verification: reasoning from…

---

### [Joint Learning of Experiential Rules and Policies for Large Language Model Agents](https://arxiv.org/abs/2606.27136v1)

- **arXiv**: `2606.27136v1`  |  **提交日期**: 2026-06-25
- **作者**: Shicheng Ye, Chao Yu

For LLM agents in multi-step interactive environments, a key challenge is to make effective use of accumulated interaction experience. Existing work has typically separated two uses of such experience: keeping it outside the model as natural-language rules for later prompting, or using trajectories and feedback to update the model parameters. The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. We present Joint Learning of Experiential…

---

### [Semantic Early-Stopping for Iterative LLM Agent Loops](https://arxiv.org/abs/2606.27009v1)

- **arXiv**: `2606.27009v1`  |  **提交日期**: 2026-06-25
- **作者**: Sahil Shrivastava

Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. We study semantic early-stopping: the loop halts when consecutive draft embeddings stop changing in meaning (cosine distance with a patience window) and the answer's measured quality stops improving. Our work makes three contributions. First, an honest theoretical…

---

### [Where Do CoT Training Gains Land in LLM based Agents?](https://arxiv.org/abs/2606.26935v1)

- **arXiv**: `2606.26935v1`  |  **提交日期**: 2026-06-25
- **作者**: Jingyu Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou, Yong Liu

Chain-of-thought (CoT) reasoning is widely used in language-model agents, but prior work has shown that verbalized CoT is not always faithful and may instead reflect post-hoc reasoning, which means the model already knows the answer before reasoning. We therefore ask what CoT training is actually improving: is the model getting better at changing its action through generated reasoning, or is it getting better at predicting the action directly from the prompt? We study this question by comparing \emph{prompt actions} (predicting action without CoT) with CoT actions (predicting action with…

---

### [Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents](https://arxiv.org/abs/2606.26627v1)

- **arXiv**: `2606.26627v1`  |  **提交日期**: 2026-06-25
- **作者**: Nada Lahjouji, Ashwin Gerard Colaco

Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce. An agent touches many data sources, runs multi-step workflows, keeps state across sessions, and acts with delegated permissions. Sensitive information can therefore leak not only through its final answer but through the queries it issues, the intermediate results it handles, the memory it writes, and the messages it exchanges…

---

### [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614v1)

- **arXiv**: `2606.26614v1`  |  **提交日期**: 2026-06-25
- **作者**: Kuangshi Ai, Patrick Phuoc Do, Chaoli Wang

Large language model (LLM) agents enable natural language interaction for scientific visualization (SciVis). Still, prior systems have essentially prioritized autonomy over human analytical control, thereby limiting transparency and human oversight. We present HiLSVA, a human-in-the-loop agentic system that supports mixed-initiative SciVis workflows. HiLSVA integrates a plan-first multi-agent architecture with explicit human oversight, stepwise provenance tracking, and learn-at-test-time adaptation from user feedback. The system supports fluid handoff between humans and agents through both…

---

### [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents](https://arxiv.org/abs/2606.26479v1)

- **arXiv**: `2606.26479v1`  |  **提交日期**: 2026-06-25
- **作者**: Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu

Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors, and several report near-elimination of attacks on the AgentDojo benchmark. We make two contributions. First, we organize these out-of-band defenses as instances of classical…

---

### [Localizing RL-Induced Tool Use to a Single Crosscoder Feature](https://arxiv.org/abs/2606.26474v1)

- **arXiv**: `2606.26474v1`  |  **提交日期**: 2026-06-25
- **作者**: Andrii Shportko, Shubham Bhokare, Ahmed Zeyad A Alzahrani, Bowen Cheng, Gustavo Mercier, Jessica Hullman

Fine-tuning through RL reshapes the internal representations of language models to enable agentic behaviors such as tool use, yet the mechanistic basis of these changes remains poorly understood. While RL substantially improves structured tool-call generation, it is unclear which features emerge, which are preserved, and whether identified features can be leveraged for retraining-free behavioral control. In this work, we show that $\textit{Dedicated Feature Crosscoders (DFC)}$ isolate a compact set of RL-specific features that mediate tool-calling capability in $\texttt{Qwen2.5-3B}$. Across a…

---

