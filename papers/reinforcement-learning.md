# Reinforcement Learning

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-06-27

### [Reinforcement Learning without Ground-Truth Solutions can Improve LLMs](https://arxiv.org/abs/2606.27369v1)

- **arXiv**: `2606.27369v1`  |  **提交日期**: 2026-06-25
- **作者**: Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, Xunpeng Huang, Kun Zhou, Tongtong Liang et al.

Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score…

---

### [Designing Reward Signals for Portable Query Generation: A Case Study in Industrial Semantic Job Search](https://arxiv.org/abs/2606.27291v1)

- **arXiv**: `2606.27291v1`  |  **提交日期**: 2026-06-25
- **作者**: Ping Liu, Qianqi Shen, Jianqiang Shen, Wenqiong Liu, Rajat Arora, Yunxiang Ren et al.

Job-search platforms rely on low-bandwidth query interfaces that often fail to capture the high-dimensional complexity of candidate profiles. We present an end-to-end RLAIF (Reinforcement Learning from AI Feedback) framework to generate \emph{portable} job search queries, terms that abstract away seeker-specific identifiers while preserving generalizable qualifications. This task introduces a highly adversarial reward surface where policy optimization frequently exploits flaws in LLM-as-judge rubrics, resulting in degenerate verbatim-copying behaviors. We conducted comprehensive empirical…

---

### [Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes](https://arxiv.org/abs/2606.27210v1)

- **arXiv**: `2606.27210v1`  |  **提交日期**: 2026-06-25
- **作者**: Jeremias Ferrao, Niclas Müller-Hof, Iustin Sîrbu, Traian Rebedea, Yftah Ziser

We argue that safety classifiers should model user intent as an explicit signal between the prompt and the final label. To study this, we introduce AIMS, a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label. We use AIMS to evaluate intent-aware training across supervised fine-tuning, preference learning, reasoning distillation, and reinforcement learning. Despite its size, AIMS enables competitive safety classifiers across training regimes: DPO from model-generated intent errors improves over SFT, and intent-conditioned…

---

### [Automating Potential-based Reward Shaping with Vision Language Model Guidance](https://arxiv.org/abs/2606.27180v1)

- **arXiv**: `2606.27180v1`  |  **提交日期**: 2026-06-25
- **作者**: Henrik Müller, Daniel Kudenko

Sparse rewards are inherently challenging for reinforcement learning agents as they lack intermediate feedback to guide exploration and to correctly attribute the sparse success rewards to relevant parts of the trajectory. Naive reward shaping can induce reward hacking, yielding policies that exploit auxiliary signals instead of solving the intended task. Potential-based reward shaping (PBRS) guarantees preservation of the optimal policy set, but requires the definition of a heuristic potential function over the state space. In this work, we introduce the VLM-guided PBRS framework VLM-PBRS…

---

### [Heavy-Ball Q-Learning with Residual Weighting Correction](https://arxiv.org/abs/2606.27112v1)

- **arXiv**: `2606.27112v1`  |  **提交日期**: 2026-06-25
- **作者**: Donghwan Lee

This paper proposes a corrected heavy-ball Q-learning method for reinforcement learning (RL) and establishes its convergence. It also identifies conditions under which the method is theoretically guaranteed to converge faster than standard Q-learning. The same construction is then extended to Q-learning with linear function approximation, where analogous convergence and acceleration statements are derived. The analysis is based on a switched linear system (SLS) representation of Q-learning algorithms and on the joint spectral radius (JSR) of the associated switching families. This SLS…

---

### [State Representation Matters in Deep Reinforcement Learning: Application to Energy Trading](https://arxiv.org/abs/2606.27032v1)

- **arXiv**: `2606.27032v1`  |  **提交日期**: 2026-06-25
- **作者**: Jesper Klicks, Sander Vržina, Vincent François-Lavet

Energy trading decisions depend not only on current market prices, but also on expected future market conditions, and operational constraints. This makes the state representation given to a reinforcement learning agent an important design choice. We study this in HydroDam, a pumped-storage arbitrage environment, using a fixed Double DQN agent. The environment, action space, reward function, network, and training protocol are kept fixed; only the market features are changed. We compare absolute price/calendar features, relative features that compare current prices with recent market history,…

---

### [Improving General Role-Playing Agents via Psychology-Grounded Reasoning and Role-Aware Policy Optimization](https://arxiv.org/abs/2606.27025v1)

- **arXiv**: `2606.27025v1`  |  **提交日期**: 2026-06-25
- **作者**: Zhenhua Xu, Dongsheng Chen, Jian Li, Yitong Lin, Zhebo Wang, Jiafu Wu et al.

Building general-purpose role-playing agents that faithfully portray any character from a natural-language profile remains challenging. The dominant paradigm -- supervised fine-tuning -- encourages behavioral mimicry without deep, human-like internal thought processes, resulting in poor out-of-distribution generalization. Therefore, we propose \textbf{Psy-CoT}, a psychology-grounded chain-of-thought framework that decomposes pre-response reasoning into three role-specific steps -- \emph{Interaction Perception}, \emph{Psychological Empathy}, and \emph{Logical Construction} -- so that the model…

---

### [Adaptive Utility driven Resource Orchestration for Resilient AI (AURORA-AI)](https://arxiv.org/abs/2606.27005v1)

- **arXiv**: `2606.27005v1`  |  **提交日期**: 2026-06-25
- **作者**: Rahul Umesh Mhapsekar, Ilias Cherkaoui, Lizy Abraham, Indrakshi Dey

Modern AI systems are increasingly deployed under non-stationary computational, demographic, and operational conditions in which static resource allocation strategies degrade both predictive performance and human-centric properties such as fairness and explainability. This paper presents AURORA-AI, an Adaptive Utility-driven Resource Orchestration framework for Resilient AI that unifies Hamilton-Jacobi-Bellman feedback control, Lyapunov-based stability monitoring, and a fairness-aware composite utility into a single closed-loop policy.The framework continuously redistributes computational…

---

### [RolloutPipe: Overlapping Pipelined Rollout and Training in Disaggregated On-Policy LLM Reinforcement Learning](https://arxiv.org/abs/2606.26997v1)

- **arXiv**: `2606.26997v1`  |  **提交日期**: 2026-06-25
- **作者**: Rongjian Chen, Jianmin Hu, Kejiang Ye, Minxian Xu

Large language model (LLM) post-training for reasoning increasingly relies on reinforcement learning with verifiable rewards (RLVR), where models learn from ground-truth feedback on mathematical, logical, and scientific tasks. To enable flexible resource allocation and support heterogeneous training setups, modern RLVR systems adopt disaggregated architectures that decouple rollout generation and policy training across independent GPU pools. However, existing synchronous on-policy GRPO (Group Relative Policy Optimization) RLVR systems finish an entire rollout before starting training, leaving…

---

### [Scaling Multi-Reference Image Generation with Dynamic Reward Optimization](https://arxiv.org/abs/2606.26947v1)

- **arXiv**: `2606.26947v1`  |  **提交日期**: 2026-06-25
- **作者**: Wenwang Huang, Yusen Fu, Junjie Wang, Mengfei Huang, Yulin Li, Gan Liu et al.

While personalized image generation has achieved remarkable progress, multi-reference image generation (MRIG) remains a challenging task. Most existing benchmarks fail to adequately evaluate complex MRIG scenarios, hindering further progress in this area. To better assess model performance on complex MRIG tasks, we introduce OmniRef-Bench, a benchmark that covers complex combinations of reference image types and a large number of reference images. Evaluations on OmniRef-Bench show that mainstream open-source models struggle in complex MRIG scenarios, and their performance deteriorates…

---

### [GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning](https://arxiv.org/abs/2606.26917v1)

- **arXiv**: `2606.26917v1`  |  **提交日期**: 2026-06-25
- **作者**: Ting Zhou, Zhenqing Ling, Yiyang Zhao, Ying Shen, Daoyuan Chen

Online reinforcement learning is widely used to align large language models (LLMs) with reward signals, yet training can be unstable under noisy or misspecified rewards. We identify a failure mode we call directional inconsistency: within a batch, a small set of high-reward rollouts induces representation-space preference directions that sharply disagree with the batch majority, resulting in high-variance and destabilizing updates. We propose geoalign, a lightweight plug-in for rollout curation in iterative policy optimization. Geoalign (i) forms within-prompt preference pairs, (ii) learns an…

---

### [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.26790v1)

- **arXiv**: `2606.26790v1`  |  **提交日期**: 2026-06-25
- **作者**: Shuo Yang, Jinyang Wu, Zhengxi Lu, Yuhao Shen, Fan Zhang, Lang Feng et al.

Outcome-based reinforcement learning provides a stable optimization backbone for language agents, but its sparse trajectory-level rewards provide little guidance on which intermediate decisions should be reinforced or suppressed. On-policy self-distillation offers dense token-level supervision, yet existing skill-conditioned variants often rely on external skill memories or retrieved privileged context, which are costly to maintain and can be mismatched with the state distribution induced by the current policy in multi-turn interaction. We propose \textbf{OPID} (\textbf{O}n-\textbf{P}olicy…

---

### [AIGP: An LLM-Based Framework for Long-Term Value Alignment in E-Commerce Pricing](https://arxiv.org/abs/2606.26787v1)

- **arXiv**: `2606.26787v1`  |  **提交日期**: 2026-06-25
- **作者**: Chennan Ma, Yanning Zhang, Siqi Hong, Xiuchong Wang, Fei Xiao, Keping Yang

Traditional dynamic pricing models in large-scale e-commerce suffer from limited interpretability, poor utilization of unstructured information, and misalignment with long-term business objectives such as cumulative Gross Merchandise Value (GMV), Return on Investment (ROI) and milestone achievement. We propose AIGP, a novel framework that leverages a Large Language Model (LLM) prompted with domain knowledge, structured data and textual context to make interpretable, knowledge-aware pricing decisions. For efficient deployment while maintaining high-quality outputs, we employ supervised…

---

### [NebulaExp-8B: An Empirical Post-Training Pipeline via Full-Scale Ablation Research](https://arxiv.org/abs/2606.26671v1)

- **arXiv**: `2606.26671v1`  |  **提交日期**: 2026-06-25
- **作者**: Qiaobo Hao, Yangqian Wu, Shunyi Wang, Zhongjian Zhang, Ziqun Li, Yayin He et al.

Post-training alignment determines the reasoning and human preference following capabilities of large language models, yet most existing works withhold detailed data construction, filtering rules and training recipes, which hinders community reproducibility and lightweight model optimization. This work presents NebulaExp, a fully transparent, ablation-driven post-training pipeline built on Qwen3-8B-base, covering two orthogonal model branches: general instruct model and complex reasoning-specialized model. We curate a raw corpus of 3.84M multi-source SFT samples and a 200K verifiable RL…

---

### [EvoOptiGraph: Weakness-Driven Coevolution via Graph-Based Structural Generation for Optimization Modeling](https://arxiv.org/abs/2606.26578v1)

- **arXiv**: `2606.26578v1`  |  **提交日期**: 2026-06-25
- **作者**: Qingcan Kang, Mingyang Liu, Xiaojin Fu, Shixiong Kai, Tao Zhong, Mingxuan Yuan

Automating optimization modeling from natural language with large language models (LLMs) faces two key challenges. First, training corpora lack structural diversity. Second, data generation pipelines remain static and decoupled from model learning. To address these challenges, we propose EvoOptiGraph, a novel framework where data and model co-evolve, driven by model weaknesses. EvoOptiGraph represents each mixed-integer linear program (MILP) as an attributed bipartite graph and applies validity-preserving evolutionary operators to generate structurally diverse instances. The evolved graphs…

---

### [Revisiting Action Factorization for Complex Action Spaces](https://arxiv.org/abs/2606.26574v1)

- **arXiv**: `2606.26574v1`  |  **提交日期**: 2026-06-25
- **作者**: Timothy Flavin, Sandip Sen

Many real-world control problems involve hybrid discrete-continuous action spaces. For example, steering and signaling in autonomous driving, and aiming and firing in robotics or video-games. Despite real-world hybrid factorization and reinforcement learning framework support for complex action spaces (e.g., Gymnasium, PettingZoo, TorchRL, SeedRL, Mujoco, etc), the default environments within those frameworks often implement uniform action space configurations (LunarLander, Walker2D, Cheetah, SMAC, SUMO, Ant, Atari). Landmark hybrid-action benchmarks (RoboCup 2D HFO, SC2LE, Platform, CARLA,…

---

### [Sample-efficient Transfer Reinforcement Learning via Adaptive Reward Shaping and Policy-Ratio Reweighting Strategy](https://arxiv.org/abs/2606.26527v1)

- **arXiv**: `2606.26527v1`  |  **提交日期**: 2026-06-25
- **作者**: Wenjie Huang, Yang Li, Jingjia Teng, Mingwei Jin, Kai Song, Yougang Bian et al.

Transfer learning improves policy learning efficiency by reusing knowledge from source tasks, providing a feasible paradigm for safe and efficient autonomous highway lane changing decision-making. Existing methods frequently encounter transfer mismatch induced by distribution shifts between source and target domains, leading to training oscillation and performance decline. Besides, target domain adaptation depends on exploratory interactions, which struggles to guarantee training safety in safety-critical lane changing cases. To tackle these limitations, this paper proposes a safe transfer…

---

### [Mean-Field PhiBE: Continuous-Time Mean-Field Reinforcement Learning from Discrete-Time Data](https://arxiv.org/abs/2606.26498v1)

- **arXiv**: `2606.26498v1`  |  **提交日期**: 2026-06-25
- **作者**: Erhan Bayraktar, Martin Hernandez, Qinxin Yan, Yuhua Zhu

This paper addresses model-free continuous-time mean-field control in a setting where the population dynamics evolve continuously according to an unknown McKean-Vlasov stochastic differential equation, while only discrete-time transition data are available. In the model-based formulation, policy evaluation is naturally described by a stationary Hamilton-Jacobi-Bellman equation on $\mathcal P_2(\mathbb R^d)$, but this equation involves the drift and diffusion coefficients of the controlled McKean-Vlasov dynamics, which are not identifiable when only discrete-time data are available. On the…

---

