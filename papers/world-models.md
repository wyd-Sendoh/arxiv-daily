# 世界模型 (World Models)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-07-01

### [DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation](https://arxiv.org/abs/2606.32028v1)

- **arXiv**: `2606.32028v1`  |  **提交日期**: 2026-06-30
- **作者**: Ziyu Shan, Zhenyu Wu, Xiaofeng Wang, Zheng Zhu, Ziwei Wang

Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video Generation World Model (DVG-WM), an…

---

### [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026v1)

- **arXiv**: `2606.32026v1`  |  **提交日期**: 2026-06-30
- **作者**: Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren

Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation…

---

### [LeCropFollow: Latent Space Planning for Navigation in Unstructured Crop Fields](https://arxiv.org/abs/2606.31941v1)

- **arXiv**: `2606.31941v1`  |  **提交日期**: 2026-06-30
- **作者**: Felipe Tommaselli, Francisco Affonso, Arthur Pompeu, Gianluca Capezzuto, Arun Narenthiran Sivakumar, Girish Chowdhary et al.

Unstructured navigational features, such as irregular planting or discontinuities, remain the primary failure mode for under-canopy agricultural robots. Existing geometric approaches often fail in these scenarios because they compress high-dimensional visual data into deterministic spatial references, effectively discarding the uncertainty and semantic context required to navigate ambiguous terrain. To address this, we present LeCropFollow, a visual navigation framework that bypasses explicit geometric modeling in favor of a learned latent representation. By integrating a self-supervised…

---

### [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734v1)

- **arXiv**: `2606.31734v1`  |  **提交日期**: 2026-06-30
- **作者**: Jiwen Yu, Jianxiong Gao, Jianhong Bai, Yiran Qin, Kaiyi Huang, Quande Liu et al.

Video World Models are interactive video generation models that predict future world states based on user actions and history video frames. A critical challenge in video world models is the lack of memory, causing inconsistent generated scenes over extended durations. Previous methods explored rule-based context frame retrieval as memory, but they fail to generalize in scenarios with scene occlusions and dynamic objects. We propose MemLearner, a learning-based adaptive context query method using query tokens to bridge context and predicted tokens. By leveraging the video generation model…

---

### [WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models](https://arxiv.org/abs/2606.31672v1)

- **arXiv**: `2606.31672v1`  |  **提交日期**: 2026-06-30
- **作者**: Ting-Bing Xu, Jiacheng Sui, Zhe Gao, Kewei Shi, Wenjin Yang, Zhicheng Liu et al.

Despite rapid progress in interactive world models (IWMs), existing benchmarks evaluate action following only at trajectory level and ignore memory and interaction physics. We introduce WorldRoamBench, an open-world benchmark for long-horizon stability across four dimensions, each with tailored innovations: (i) Action: per-frame action metric bypassing cross-model semantic scale disparity and exposing failures hidden by trajectory; (ii) Vision: segment-based drift metric capturing non-monotonic mid-sequence collapse missed by start-vs-end comparisons; (iii) Physics: controllability-gated…

---

### [Ask the World Before Acting: Budgeted Environment Probing for World-Model Calibration](https://arxiv.org/abs/2606.31422v1)

- **arXiv**: `2606.31422v1`  |  **提交日期**: 2026-06-30
- **作者**: Xinyuan Song, Zekun Cai

Long-horizon language agents do not only choose actions; they carry a private model of the world from one decision to the next. When that model drifts, a later failure can be decided before the failing action is ever taken. We study a direct repair mechanism: before committing to the next task action, an agent may ask the environment about one belief field and write the answer back into its world model. This makes environment interaction a scarce calibration resource, not merely a way to advance the task. We introduce \method, a budgeted probing operator for structured belief tables. The…

---

### [World-Model Collapse as a Phase Transition](https://arxiv.org/abs/2606.31399v1)

- **arXiv**: `2606.31399v1`  |  **提交日期**: 2026-06-30
- **作者**: Xinyuan Song, Zekun Cai

Water looks unchanged as it warms, then at a critical point it boils. We ask whether long-horizon language agents show an analogous transition in their implicit world models. In some parameter settings, changing state load by a small amount, or adding a single step of horizon, leaves behavior nearly unchanged; near a critical boundary, the same small change causes a sudden world collapse. We study this effect in a deterministic task family with exact per-step gold state. A large grid search over state cardinality, dependency density, horizon, branching, observation mode, and mutation rate…

---

### [One Video, One World: Turning Monocular Video into Physical 4D Scenes](https://arxiv.org/abs/2606.31388v1)

- **arXiv**: `2606.31388v1`  |  **提交日期**: 2026-06-30
- **作者**: Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang, Congcong Zhu et al.

We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-language model discovers, labels, and motion-classifies all instances; category-aware reconstruction…

---

### [Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding](https://arxiv.org/abs/2606.31232v1)

- **arXiv**: `2606.31232v1`  |  **提交日期**: 2026-06-30
- **作者**: Zhenghao Zhang, Yuanxiang Wang, Zhenyu Guan, Yujia Yang, Bingkang Shi, Tianyu Zong et al.

Learning visual world models for planning requires compact latent dynamics that remain sensitive to actions, yet reconstruction-free joint-embedding objectives can collapse to action-insensitive representations. We propose Delta-JEPA, an end-to-end reconstruction-free world model that augments latent forward prediction with a Latent Difference Action Decoder (LDAD). Unlike inverse decoders that infer actions from concatenated endpoint embeddings, LDAD reconstructs the executed action from the latent displacement between consecutive observations. This displacement-level supervision directly…

---

### [ForgeDrive: Bidirectional Cross-Conditioning for Unified Visual-Action Generation in Autonomous Driving](https://arxiv.org/abs/2606.31226v1)

- **arXiv**: `2606.31226v1`  |  **提交日期**: 2026-06-30
- **作者**: Xuchang Zhong, He Zheng, Chenxu Zhao, Tianxiong Lv, Hangqi Fan, Bohua Wang et al.

World-model-based autonomous driving endows the model with the ability to understand scene evolution. Yet this promise is undermined by the prevailing imagine-then-act paradigm, which allows errors from the more challenging visual generation stage to cascade into action planning. We introduce ForgeDrive, a unified autoregressive diffusion framework with visual-action cross-conditioning that closes this gap through act-then-imagine paradigm. ForgeDrive factorizes the future as a sequence of per-timestep frame-action pairs, intertwining each action with its corresponding visual observation.…

---

### [Long-term Traffic Simulation via Structured Autoregressive Modeling](https://arxiv.org/abs/2606.31209v1)

- **arXiv**: `2606.31209v1`  |  **提交日期**: 2026-06-30
- **作者**: Lingyu Xiao, Zexin Feng, Xintao Yan

Interactive traffic simulation is a vital world model for autonomous driving. A central challenge in long-horizon simulation is modeling sustained multi-agent interactions, which is further exacerbated by dynamic token cardinality as agents continuously enter and exit the scene. In this work, we propose that the solution lies in the synergy between the architectural inductive biases and statistical priors of large-scale sequence models, e.g., Large Language Models (LLMs). Our probing experiments reveal that the transferability of attention mechanisms and the distributional consistency between…

---

### [Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)

- **arXiv**: `2606.31050v1`  |  **提交日期**: 2026-06-30
- **作者**: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin et al.

How to accurately predict a high-fidelity future world? While the visual world is inherently continuous, existing deterministic video prediction models operate in discrete pixel space and are mainly optimized with pixel-wise mean squared error (MSE), which often leads to over-smoothed predictions and a lack of fine-grained visual details. To address these limitations, we propose Predictive Differentiable Rendering (PDR), a novel end-to-end video prediction paradigm that bridges the gap between discrete and continuous representations. Inspired by recent progress in 3D reconstruction with 3D…

---

### [LWDrive: Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879v2)

- **arXiv**: `2606.29879v2`  |  **提交日期**: 2026-06-29
- **作者**: Chen Yang, Yuhao Wei, Ze Xu, Ziheng Zou, Shuang Liang, Delin Ouyang et al.

Vision-Language Models (VLMs) provide powerful semantic understanding and commonsense reasoning for End-to-End Autonomous Driving (E2E-AD) planning. However, trajectories directly generated by VLMs often encode only coarse driving intentions and remain insufficient for geometrically accurate, future-aware, and multi-view-grounded planning. To address these limitations, we develop the Layer-Wise World-Model-Guided Driving framework (LWDrive). LWDrive is a VLM planning framework that refines coarse trajectories through layer-wise world-model guidance. Instead of treating the VLM output as the…

---

## 📅 2026-06-30

### [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)

- **arXiv**: `2606.30639v1`  |  **提交日期**: 2026-06-29
- **作者**: Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, Yang Deng

World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. WorldEvolver integrates three modules: (i) Episodic Memory, which exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory, which extracts…

---

### [OWMDrive: Causality-Aware End-to-End Autonomous Driving via 4D Occupancy World Model](https://arxiv.org/abs/2606.30421v1)

- **arXiv**: `2606.30421v1`  |  **提交日期**: 2026-06-29
- **作者**: Junjie Cheng, Ruiqi Song, Ye Wu, Nanxing Zeng, Ximiao Li, Yunfeng Ai

Autonomous driving systems are steadily moving toward end-to-end paradigms to mitigate the limited adaptability of rule-based pipelines in complex traffic environments. However, most existing learning-based methods still make decisions from static representations of the current scene, without explicit future rollouts or modeling of the temporal causal dynamics in traffic interactions. This limitation often results in unstable or overly conservative planning under high-uncertainty conditions, such as occlusions and unexpected events. To overcome these challenges, we introduce OWMDrive, a…

---

### [DreamForge-World 0.1 Preview: A Low-Compute Real-Time Controllable World Model](https://arxiv.org/abs/2606.30292v1)

- **arXiv**: `2606.30292v1`  |  **提交日期**: 2026-06-29
- **作者**: Daniyel Ayupov, Artur Markov-Tsoy

We present DreamForge-World 0.1 Preview, a preview foundational world model for real-time interactive world simulation. The system adapts the LongLive 1 autoregressive video stack, itself derived from Wan2.1-T2V-1.3B, with a residual action pathway inspired by the Matrix-Game family. DreamForge-World 0.1 Preview focuses on a complementary axis to frontier-scale world simulators: low-compute adaptation, consumer-GPU runtime, and broad interactive capability coverage. It supports live keyboard and mouse control, multimodal initialization, mid-stream reprompting, dual-view operation, and…

---

### [Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation](https://arxiv.org/abs/2606.29908v1)

- **arXiv**: `2606.29908v1`  |  **提交日期**: 2026-06-29
- **作者**: Hong Chen, Daqi Liu, Zehan Zhang, Haiguang Wang, Tianhao Lu, Longfei Yan et al.

Existing world model-based planners for visual navigation typically follow a verification-centric paradigm, decoupling goal intent from trajectory synthesis. This approach suffers from candidate dependence, heavy computational overhead, and inconsistencies between sampled actions and predicted visuals. To address these issues, we propose SWAM (Spatial-perceiving World Action Model), a task-centric joint observation-action generation framework. Given start and goal RGB observations, SWAM performs single-pass inference to simultaneously generate intermediate RGB-D sequences and corresponding…

---

### [LWDrive: Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879v1)

- **arXiv**: `2606.29879v1`  |  **提交日期**: 2026-06-29
- **作者**: Chen Yang, Yuhao Wei, Ze Xu, Ziheng Zou, Shuang Liang, Delin Ouyang et al.

Vision-Language Models (VLMs) provide powerful semantic understanding and commonsense reasoning for End-to-End Autonomous Driving (E2E-AD) planning. However, trajectories directly generated by VLMs often encode only coarse driving intentions and remain insufficient for geometrically accurate, future-aware, and multi-view-grounded planning. To address these limitations, we develop the Layer-Wise World-Model-Guided Driving framework (LWDrive). LWDrive is a VLM planning framework that refines coarse trajectories through layer-wise world-model guidance. Instead of treating the VLM output as the…

---

### [The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models](https://arxiv.org/abs/2606.29799v1)

- **arXiv**: `2606.29799v1`  |  **提交日期**: 2026-06-29
- **作者**: Rafael Kaufmann, Felix Neubürger, Michael Walters, Thomas Kopinski, Dimitrije Marković

This project introduces the CRISTAL Method (Coherent Reliable Intentional Synthesis of Truthful Analysis Logic), a neurosymbolic framework for automating complex analysis workflows, with fundamental investment analysis as a primary use case. This domain poses major challenges: high structural uncertainty, noisy and subjective data, tight attention budgets, and the need for justified, reproducible decisions. Human analysts often struggle in this domain due to cognitive biases and limitations, suggesting significant value in automation. But while LLM-based agents have been proposed as…

---

### [HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data](https://arxiv.org/abs/2606.29784v1)

- **arXiv**: `2606.29784v1`  |  **提交日期**: 2026-06-29
- **作者**: Xinrui Ruan, Zhenyu Zhao, Waverly Wei, Yueshan Zhang, Zeyu Zheng, Sui Huang et al.

Reliable generative AI models critically rely on expert human annotations to evaluate output quality, yet these "gold" labels are expensive to collect and limited in quantity. Organizations thus often turn to collecting vast but noisy "silver" labels from crowdsourced workers or vendor annotators as proxies for gold labels. Because gold remains the evaluation target, naively aggregating noisy silver labels may introduce bias, and estimators built on sparsely observed gold labels may have high variance to resolve the model performance gaps that guide practical decisions. Model evaluation has…

---

### [Learning Transferable Dynamics Priors from Action to World Modeling](https://arxiv.org/abs/2606.29501v1)

- **arXiv**: `2606.29501v1`  |  **提交日期**: 2026-06-28
- **作者**: Ze Huang, Jiahui Zhang, Hairuo Liu, Chenxi Zhang, Ran Cheng, Li Zhang

We study action-conditioned world modeling as a scalable way to learn transferable dynamics priors for robot learning. By pretraining a model to predict how actions drive visual scene evolution, the resulting world model captures reusable interaction dynamics beyond appearance-level video generation. Concretely, we pretrain a multi-view interactive base diffusion world model, A2World, on large-scale robot manipulation data with real action annotations. We validate the learned dynamics priors from two complementary perspectives. First, we adapt A2World into a task- or scene-specialized…

---

### [Cognitive World Models for Process-Level Social Influence Evaluation](https://arxiv.org/abs/2606.29495v1)

- **arXiv**: `2606.29495v1`  |  **提交日期**: 2026-06-28
- **作者**: Minghui Ma, Bin Guo, Han Wang, Mengqi Chen, Jingqi Liu, Yan Liu et al.

Social influence dialogue changes user behavior by altering internal cognitive states. The central evaluation question is whether the user's beliefs, desires, intentions, and emotions measurably change over the course of conversation, a process-oriented criterion that neither surface-level text metrics (BLEU/ROUGE) nor single-score LLM judgments can capture. We propose the \textbf{Cog}nitive \textbf{W}orld \textbf{M}odel \textbf{(CogWM)}, an LLM-based user model that reframes multi-turn dialogue evaluation from ``what did the user say'' to ``how did the user's internal cognitive state…

---

### [Prototype Latent World Model Replay for Class-Incremental Learning](https://arxiv.org/abs/2606.29465v1)

- **arXiv**: `2606.29465v1`  |  **提交日期**: 2026-06-28
- **作者**: Weizhi Nie, Hui Wang, Weijie Wang, Yuting Su

Class-incremental learning requires a model to learn new classes while preserving decision regions for old ones. This is difficult when raw old samples are no longer available. We propose Prototype Latent World Model Replay, a memory-free framework that stores old classes as distributions over stable hidden states rather than as images. A frozen ImageNet-pretrained encoder maps each image into a latent state space. In this space, each class is summarized by several prototype-centered distributions with class-specific variances. When new classes arrive, the model samples old latent states from…

---

### [L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction](https://arxiv.org/abs/2606.29374v1)

- **arXiv**: `2606.29374v1`  |  **提交日期**: 2026-06-28
- **作者**: Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He, Hangjun Ye et al.

High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense multi-view observations consistently. This paper presents L2D2-GS, a unified framework that…

---

### [ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving](https://arxiv.org/abs/2606.29286v1)

- **arXiv**: `2606.29286v1`  |  **提交日期**: 2026-06-28
- **作者**: Dingyi Yao, Xinqi Zhang, Lihui Peng, Jianming Hu, Danya Yao, Yi Zhang

Synthetic data mitigates the data scarcity problem in autonomous driving perception. However, the synthetic-to-real gap leads to performance degradation, hindering real-world model generalization. Although current methods leverage diffusion models for photorealistic style transfer to bridge this gap, they critically ignore a practical asymmetry: while synthetic data possesses perfect pixel-level annotations, real-world style reference images generally lack corresponding labels. Consequently, existing methods relying on symmetric semantic guidance suffer from either prohibitive annotation…

---

### [Flow Matching in Feature Space for Stochastic World Modeling](https://arxiv.org/abs/2606.29059v1)

- **arXiv**: `2606.29059v1`  |  **提交日期**: 2026-06-27
- **作者**: Francois Porcher, Nicolas Carion, Karteek Alahari, Shizhe Chen

World modeling requires forecasting uncertain futures while preserving information useful for downstream perception. Existing visual world models often struggle to satisfy both goals: VAE-based stochastic models operate in low-dimensional reconstruction latents, which can limit perception performance, while deterministic predictors using strong pretrained features collapse multimodal futures into a single blurry mean. In this work, we propose FlowWM, a stochastic world model that performs flow matching directly within pretrained feature space (e.g., DINOv3). This is challenging because…

---

### [A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models](https://arxiv.org/abs/2606.28757v1)

- **arXiv**: `2606.28757v1`  |  **提交日期**: 2026-06-27
- **作者**: Nuo Chen, Lulin Liu, Zihao Li, Ziyao Zeng, Zihao Zhu, Wenyan Cong et al.

Generative world models hold immense promise as scalable simulators for autonomous systems, particularly for synthesizing rare but safety-critical multi-agent interactions, such as vehicle collisions. However, current evaluation paradigms index heavily on visual fidelity and semantic alignment, leaving a critical blind spot: they cannot reliably quantify whether generated dynamics actually obey the fundamental physical laws required for reliable simulation. Assessing this physical plausibility is inherently difficult due to a lack of physical metrics and the challenge of extracting…

---

### [A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility](https://arxiv.org/abs/2606.28751v1)

- **arXiv**: `2606.28751v1`  |  **提交日期**: 2026-06-27
- **作者**: Gunn Kim

We propose a path-space formulation of prediction in AI world models. Rather than sequences of one-step conditional distributions, we argue that a world model implicitly defines a probability measure over future trajectories. In the local regime where latent dynamics admit an effective Markovian description, this path measure takes the Onsager-Machlup form. Within this framework, prediction (most probable trajectory), planning (constrained optimization), and uncertainty (fluctuations) emerge as operations on a single action functional. We decompose the latent dynamics into reversible and…

---

### [J-LAW: Joint Localization and Actionable World Modeling via Coupled Latent Factor Graphs](https://arxiv.org/abs/2606.28712v1)

- **arXiv**: `2606.28712v1`  |  **提交日期**: 2026-06-27
- **作者**: Guanqun Cao, Liang Chen

Classical SLAM estimates metric poses and a geometric map but produces no actionable predictive model for planning. Action-conditioned world models learn compact latent dynamics for planning but ignore global metric consistency and accumulate drift under open-loop rollout. We argue these are two views of the same estimation problem and propose J-LAW (Joint Localization and Actionable World Modeling) in this letter: a coupled factor graph that jointly optimizes metric object poses, latent world states, and latent landmark embeddings. The bridge is a pose-conditioned latent encoder and a…

---

## 📅 2026-06-29

### [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128v1)

- **arXiv**: `2606.28128v1`  |  **提交日期**: 2026-06-26
- **作者**: Peiwen Zhang, Yufan Deng, Shangkun Sun, Juncheng Ma, Duomin Wang, Jonas Du et al.

Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. Through extensive experiments, we find that such physical instability mainly arises from two factors: deformation of moving objects and implausible spatio-temporal correlations among interacting entities, particularly…

---

### [From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond](https://arxiv.org/abs/2606.28127v1)

- **arXiv**: `2606.28127v1`  |  **提交日期**: 2026-06-26
- **作者**: Paul Dubois

The AI community has framed the relationship between large language models (LLMs) and world models as a dichotomy: LLMs predict tokens; world models simulate reality. Yann LeCun argues in 2022 that reaching general intelligence requires abandoning autoregressive token prediction in favour of latent-space architectures. This framing is unnecessarily binary. Two claims will be defended. First, LLMs are a degenerate special case of world models: the state space is the set of all token sequences, the only action is appending one token, and world models are therefore a strict generalisation of…

---

### [Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control](https://arxiv.org/abs/2606.27964v1)

- **arXiv**: `2606.27964v1`  |  **提交日期**: 2026-06-26
- **作者**: Haoyuan Wang, Yabo Chen, Haibin Huang, Chi Zhang, Xuelong Li

Building interactive world models requires generating realistic videos while maintaining controllable dynamics over long horizons. Autoregressive video generation offers a scalable foundation, but suffers from error accumulation and temporal degradation during extended rollouts. This issue is further amplified under heterogeneous controls such as human motion and camera trajectories, which may interfere and destabilize a pretrained video prior, while existing methods often trade off controllability and visual quality. We propose "Directing the World", a fast autoregressive framework for…

---

### [Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents](https://arxiv.org/abs/2606.27806v1)

- **arXiv**: `2606.27806v1`  |  **提交日期**: 2026-06-26
- **作者**: Xinyuan Song, Zekun Cai

World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the…

---

### [Understanding Rollout Error in Graph World Models](https://arxiv.org/abs/2606.27780v1)

- **arXiv**: `2606.27780v1`  |  **提交日期**: 2026-06-26
- **作者**: Xinyuan Song, Zekun Cai

World models are often used for planning by rolling learned dynamics forward. Many planning environments, however, are not vectors or images; they are graphs of agents, tools, skills, routes, and dependencies. In these settings, a local prediction error may stay local or spread through the graph, and the failure mode changes again when edges are predicted rather than fixed. This paper studies long-horizon rollout error in Graph World Models (GWMs). We formulate a unified fixed-edge and dynamic-edge GWM framework with action nodes for node-, edge-, and graph-level decisions. We develop…

---

### [Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation](https://arxiv.org/abs/2606.27681v1)

- **arXiv**: `2606.27681v1`  |  **提交日期**: 2026-06-26
- **作者**: Xiang Gao, Kaiwen Dong, Yuguang Yao, Padmaja Jonnalagedda, Kamalika Das

World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and…

---

### [CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations](https://arxiv.org/abs/2606.27644v1)

- **arXiv**: `2606.27644v1`  |  **提交日期**: 2026-06-26
- **作者**: Kyumin Hwang, Wonhyeok Choi, Jaeyeul Kim, Jihun Park, Daehee Park, Sunghoon Im

This letter proposes CascadeOcc, a novel occupancy world model that prioritizes intrinsic structural hierarchy over extrinsic auxiliary modalities for autonomous driving. Occupancy world models -- forecasting the future driving environment and planning the driving trajectory -- effectively bridge perception and planning, but current approaches often heavily rely on external modalities or large language models, failing to fully exploit the inherent structural potential of occupancy representations themselves. To enhance representational capacity for complex 3D scenes, we integrate a cascaded…

---

## 📅 2026-06-27

### [PhysiFormer: Learning to Simulate Mechanics in World Space](https://arxiv.org/abs/2606.27364v1)

- **arXiv**: `2606.27364v1`  |  **提交日期**: 2026-06-25
- **作者**: Yiming Chen, Yushi Lan, Andrea Vedaldi

We present PhysiFormer, a diffusion transformer for physically-plausible 3D object motion. Unlike video world models that operate in view-dependent pixel space, PhysiFormer represents objects as 3D meshes expressed in world coordinates. Given the initial vertex positions and velocities, as well as object material type, rigid or elastic, the model samples future vertex trajectories. While related neural physics approaches build on ad-hoc latent spaces or explicitly enforce rigidity and causality, PhysiFormer shows that excellent results can be obtained without any such inductive biases, by…

---

### [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326v1)

- **arXiv**: `2606.27326v1`  |  **提交日期**: 2026-06-25
- **作者**: Nicklas Hansen, Xiaolong Wang

Modern generative world models render increasingly realistic action-controllable futures, yet they frequently hallucinate: rollouts remain visually fluent while drifting from the ground-truth dynamics. We hypothesize that hallucination concentrates in low-coverage regions of the state-action space, where lightweight data-centric signals can both detect it and guide mitigation. To test this, we introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, and train a 350M-parameter world model on it. We identify three…

---

### [Not All Actions Are Equal: Rethinking Conditioning for Dexterous World Model](https://arxiv.org/abs/2606.27325v1)

- **arXiv**: `2606.27325v1`  |  **提交日期**: 2026-06-25
- **作者**: Zizhao Yuan, Zhengtu Liang, Taowen Wang, Qiwei Liang, Yichi Wang, Yunheng Wang et al.

Recent advances in action-conditioned world models show promising progress in modeling complex interactions and forecasting future states under diverse action sequences. While these models are often driven by stronger visual representations and model capacity, action conditioning itself remains underexplored. Most existing approaches compress the entire action sequence into a single representation, which works well for low-DoF control but becomes less reliable in high-DoF scenarios. We observe that high-DoF dexterous actions are inherently heterogeneous, spanning multiple orders of magnitude,…

---

### [EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting](https://arxiv.org/abs/2606.27277v1)

- **arXiv**: `2606.27277v1`  |  **提交日期**: 2026-06-25
- **作者**: Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao

Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty into a single future prediction, while diffusion-based methods typically treat weather variables as…

---

### [A Generalization Theory for JEPA-Based World Models](https://arxiv.org/abs/2606.27014v1)

- **arXiv**: `2606.27014v1`  |  **提交日期**: 2026-06-25
- **作者**: Jingyi Cui, Qi Zhang, Hongwei Wen, Yisen Wang

Joint Embedding Predictive Architectures (JEPAs) have recently emerged as a promising paradigm for world modeling by learning predictive dynamics in a latent space rather than generating future observations at the input level. Despite their empirical success, the theoretical understanding of JEPA-based world models remains limited. In this paper, we develop the first generalization theory for JEPA-based world models. We formulate JEPA pretraining as a conditional spectral graph learning problem and show that the JEPA objective is equivalent to a low-rank factorization of an action-conditioned…

---

### [Einstein World Models](https://arxiv.org/abs/2606.26969v1)

- **arXiv**: `2606.26969v1`  |  **提交日期**: 2026-06-25
- **作者**: Munachiso Samuel Nwadike, Zangir Iklassov, Ali Mekky, Zayd M. Kawakibi Zuhri, Kentaro Inui

Does intelligence require the ability to reason about phenomena beyond direct experience? It is natural to suspect that some complex thought cannot be captured through language alone. However, of particular concern to this work, is whether visualising counterfactual events can complement language as a mechanism for complex thought. We ask whether LLMs can be trained to utilise such visualisation mechanisms, in a way that benefits their reasoning abilities. Motivated by this question, we propose Einstein World Models. EWMs are a blueprint for LLM-based reasoning systems that place…

---

### [Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds](https://arxiv.org/abs/2606.26964v1)

- **arXiv**: `2606.26964v1`  |  **提交日期**: 2026-06-25
- **作者**: Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang, Hailan Ma et al.

As embodied AI and world models increasingly operate in dynamic 3D environments, visual perception must move beyond passively interpreting given observations toward actively deciding what to observe. We study this problem through camera planning in dynamic 3D story worlds, where the camera must not only generate smooth motion, but also decide what visual evidence should be acquired before it moves. We formulate this capability as Narrative-Grounded World Visual Attention, where the camera acts as an embodied observer that determines what to observe, how to compose the observation, and how to…

---

### [Risk-Aware Selective Multimodal Driver Monitoring with Driver-State World Modeling](https://arxiv.org/abs/2606.26922v1)

- **arXiv**: `2606.26922v1`  |  **提交日期**: 2026-06-25
- **作者**: Daosheng Qiu, Haozhuang Chi, Hao Su, Shu Long, Xinyue Miao, Yongle Dong et al.

Continuous driver monitoring in automated vehicles requires low-latency inference while avoiding unsafe decisions under uncertain driver states. Large vision-language models provide broad multimodal priors, but their latency and limited reliability in this setting make them unsuitable as always-on in-cabin monitors. We propose a cost-aware selective inference framework for deployable multimodal driver monitoring. The core system is a lightweight RGB-physiological student that combines in-cabin visual observations with window-level HR/EDA signals, and a learned gate that decides when to accept…

---

### [LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography](https://arxiv.org/abs/2606.26713v1)

- **arXiv**: `2606.26713v1`  |  **提交日期**: 2026-06-25
- **作者**: Yuqi Jiang, Yumeng Liu, Zimu Li, Jinyuan Deng, Qian Jin, Yucheng Cui et al.

As semiconductor technology nodes scale, computational lithography is essential for ensuring yield and performance. However, lithography is a continuous physical process involving mask optimization, optical imaging, resist exposure, and development, which existing models fail to capture. To overcome this limitation, we present LithoDreamer, the first physics-informed World Model (WM) framework for computational lithography, which formulates the ``Layout-Mask-Resist Image-After Development Image (ADI)'' pipeline as a decision-driven multi-step evolution system. LithoDreamer captures feature…

---

### [PhysEditWorld: A Large-Scale Dataset Toward Physics-Editable World Models](https://arxiv.org/abs/2606.26694v1)

- **arXiv**: `2606.26694v1`  |  **提交日期**: 2026-06-25
- **作者**: Bin Hu, Yanwen Ma, Jiehui Huang, Ziliang Zhang, Haoning Wu, Ruicheng Zhang et al.

Recent game world models can synthesize visually plausible, action-conditioned rollouts. However, their interaction behaviors often remain limited to exploratory or wandering trajectories, and physical dynamics are typically learned as implicit correlations from data rather than as controllable variables. This limitation hinders their applicability to authored game environments, where physical rules are deliberately designed and require explicit manipulation. We introduce PhysEditWorld, a multimodal dataset with physical parameters, with a primary focus on gravity in this initial version. At…

---

### [Neural Voxel Dynamics: Learning Implicit 3D Physics via Volumetric Feature Advection](https://arxiv.org/abs/2606.26410v1)

- **arXiv**: `2606.26410v1`  |  **提交日期**: 2026-06-24
- **作者**: Zican Wang, Niloy Mitra

We present a self-supervised framework for learning implicit 3D physical dynamics directly from video-derived supervisory signals. While current generative video models achieve high visual fidelity, they lack a 3D geometric foundation, often resulting in physical inconsistencies and a failure to maintain object permanence. We address this by shifting the predictive bottleneck from 2D image space to a `lifted' 3D Volumetric Latent Space. Our method unprojects semantic features from a Video Joint-Embedding Predictive Architecture (V-JEPA) into a voxelized grid, grounded by monocular depth…

---

### [KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation](https://arxiv.org/abs/2606.26321v1)

- **arXiv**: `2606.26321v1`  |  **提交日期**: 2026-06-24
- **作者**: Runfeng Ling

Mobile manipulators need world models that are current, queryable, semantically meaningful, and usable under edge-compute constraints. This technical report presents KRVF, a source-aware semantic voxel world representation for edge mobile manipulation. Unlike reconstruction-centric mapping pipelines that primarily optimize global geometric fidelity, KRVF represents local world state as task-oriented voxels that encode occupancy, color, semantic evidence, temporal freshness, and evidence source. The representation separates measured occupancy from semantic-prior hypotheses, enabling…

---

### [Fast LeWorldModel](https://arxiv.org/abs/2606.26217v1)

- **arXiv**: `2606.26217v1`  |  **提交日期**: 2026-06-24
- **作者**: Yuntian Gao, Xiangyu Xu

Joint-Embedding Predictive Architectures (JEPAs), including recent LeWorldModel (LeWM), have become a promising foundation for reconstruction-free visual world models. For visual planning, however, LeWM evaluates candidate action sequences by repeatedly applying a local one-step latent transition model. This autoregressive rollout makes planning computationally expensive and exposes the predicted trajectory to accumulated latent errors as the horizon grows. We propose Fast LeWorldModel (Fast-LeWM), a fast latent world model that replaces repeated local rollout with action-prefix prediction.…

---

### [The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems](https://arxiv.org/abs/2606.26057v1)

- **arXiv**: `2606.26057v1`  |  **提交日期**: 2026-06-24
- **作者**: Seth Dobrin, Łukasz Chmiel

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process…

---

### [In-Context World Modeling for Robotic Control](https://arxiv.org/abs/2606.26025v2)

- **arXiv**: `2606.26025v2`  |  **提交日期**: 2026-06-24
- **作者**: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong et al.

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem.…

---

### [USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning](https://arxiv.org/abs/2606.25880v1)

- **arXiv**: `2606.25880v1`  |  **提交日期**: 2026-06-24
- **作者**: Yuchen Xie, Xinyu Zhou, Kuangji Zuo, Yanshuo Lu, Fengrui Huang, Boyu Ma et al.

Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only specification to unified spatial-semantic prompting. Based on this paradigm, we introduce Unified…

---

### [Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors](https://arxiv.org/abs/2606.25527v1)

- **arXiv**: `2606.25527v1`  |  **提交日期**: 2026-06-24
- **作者**: Guozheng Ma, Lu Li, Zilin Wang, Pierre-Luc Bacon, Dacheng Tao

Online reinforcement learning (RL) agents increasingly depend on knowledge acquired offline to achieve practical efficiency. Originally studied in offline-to-online RL, this paradigm now spans foundation model post-training and embodied intelligence, with prior types expanding from offline datasets and pre-trained policies to increasingly diverse knowledge sources such as multimodal foundation models and generative world models. Offline priors have become central to how deep RL is developed and deployed. However, this reliance introduces a challenge that the prevailing benchmark-driven…

---

### [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473v1)

- **arXiv**: `2606.25473v1`  |  **提交日期**: 2026-06-24
- **作者**: Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen, Jianfei Chen et al.

Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in diffusion distillation. This philosophy naturally carries over to the autoregressive setting, where…

---

### [Hypergraph Normal World Models for Logical Visual Anomaly Detection](https://arxiv.org/abs/2606.25368v1)

- **arXiv**: `2606.25368v1`  |  **提交日期**: 2026-06-24
- **作者**: Weizhi Nie, Zibo Xu, Weijie Wang, Yuting Su

Visual anomaly detection is often deployed with only normal training images. Most one-class detectors map test patches or features to a normal reference distribution. This works well for local structural defects. Logical anomalies are different. Each visible part may look normal, while the whole image violates a normal count, co-occurrence, or spatial relation. This paper studies whether a model can learn such a category-specific normal world from nominal images alone. We propose the Hypergraph Normal World Model, a normal-only detector that distills frozen DINOv2 patch tokens into patch,…

---

