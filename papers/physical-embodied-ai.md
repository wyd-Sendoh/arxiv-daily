# 物理AI / 具身智能 (Physical & Embodied AI)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-07-02

### [EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards](https://arxiv.org/abs/2607.00218v1)

- **arXiv**: `2607.00218v1`  |  **提交日期**: 2026-06-30
- **作者**: Siddhant Panpatil, Arth Singh, Mijin Koo, Chaeyun Kim, Haon Park, Dasol Choi

Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric video benchmark of 1,200 robot-view scenarios annotated at half-second granularity, to evaluate VLMs as streaming guards across two tracks. The situational track (800 scenarios) spans four families, from routine and safe-but-suspicious…

---

## 📅 2026-07-01

### [MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments](https://arxiv.org/abs/2606.31966v1)

- **arXiv**: `2606.31966v1`  |  **提交日期**: 2026-06-30
- **作者**: Qingyun Liu, Jiwen Zhang, Jingyi Hu, Siyuan Wang, Zhongyu Wei

Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration generally improves embodied task completion, but its benefits depend on balancing collaborative gains…

---

### [MVP-Nav: Multi-layer Value Map Planner Navigator](https://arxiv.org/abs/2606.31919v1)

- **arXiv**: `2606.31919v1`  |  **提交日期**: 2026-06-30
- **作者**: Wenyuan Xie, Shaokai Wu, Yijin Zhou, Yanbiao Ji, Guodong Zhang, Bayram Bayramli et al.

Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose MVP-Nav, a physical-aware RGB-only navigation framework that aligns perception, planning, and…

---

### [Autonomous UAV Navigation for Individual Wildlife Re-Identification](https://arxiv.org/abs/2606.31772v1)

- **arXiv**: `2606.31772v1`  |  **提交日期**: 2026-06-30
- **作者**: Claire Sun, Tanya Berger-Wolf, Jenna Kline

Reliable individual re-identification (re-ID) of wildlife is essential for population monitoring, behavioral tracking, and conservation policy evaluation, yet large-scale data collection remains labor-intensive, relying on manual efforts by ecologists or citizen scientists. We propose an autonomous drone navigation system that actively optimizes image capture for downstream re-ID, moving beyond passive aerial sensing. The system combines YOLOv11 object detection with a DINOv2-based pose classifier to guide real-time flight decisions: detecting animals, orienting to expose the lateral flank…

---

### [AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience](https://arxiv.org/abs/2606.31467v1)

- **arXiv**: `2606.31467v1`  |  **提交日期**: 2026-06-30
- **作者**: Wenyi Zhang, Fanglong Yao, Youzhi Liu, Peng Hu, Zhengqiu Zhu, Chen Gao et al.

With the rapid advancement of aerospace embodied intelligence, enabling Unmanned Aerial Vehicles (UAVs) to autonomously understand and reason about complex environments has become increasingly important. However, existing UAV-based spatial reasoning approaches face critical limitations: single-view perception renders them vulnerable to occlusions and perspective distortions, while most VLMs lack explicit geometric modeling, relying on semantic cues and yielding inconsistent reasoning under viewpoint and scale variations. To address these challenges, we propose SatAgent, a UAV-Satellite…

---

### [Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning](https://arxiv.org/abs/2606.31157v1)

- **arXiv**: `2606.31157v1`  |  **提交日期**: 2026-06-30
- **作者**: Hongyi Lin, Yang Liu, Jinhua Zhao, Xiaobo Qu

Foundation models are increasingly integrated into embodied intelligence systems, but directly assigning them structured prediction tasks requires precise geometric and numerical estimation, where specialized models often remain stronger. This capability mismatch raises a key question: should foundation models replace task-specific predictors, or should they collaborate through tasks better aligned with their strengths? We propose FAT, a foundation-model-augmented task-specific reasoning framework that treats collaboration as task decomposition rather than model replacement. FAT decomposes…

---

### [CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction](https://arxiv.org/abs/2606.31086v1)

- **arXiv**: `2606.31086v1`  |  **提交日期**: 2026-06-30
- **作者**: Yuzhou Ji, Xiaotian Yang, Zhipeng Zhang

The rise of home-deployed embodied AI systems is driving a growing need for fast, metric 3D reconstruction of residential spaces to support navigation, interaction, and long-horizon task execution. However, the commonly used pinhole-camera 3D reconstruction pipelines struggle to model large indoor residences efficiently due to their limited field of view, to which achieving full coverage across multiple rooms often requires thousands of images and incurs drift from long chains of incremental alignment. In this work, we present CasaMaestro (Spanish words meaning ``house'' and ``master''), a…

---

### [Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation](https://arxiv.org/abs/2606.31071v1)

- **arXiv**: `2606.31071v1`  |  **提交日期**: 2026-06-30
- **作者**: Bing Wu, Zuyao Chen, Changwen Chen

Semantic navigation is a fundamental task for embodied agents operating in unseen environments, requiring both semantic understanding and long-term decision-making. Recent foundation models have empowered agents with rich semantic priors for this task. However, without structured global representations, decision-making often falls back on local observations and greedy strategies, resulting in inefficient exploration and myopic behaviors, especially in long-distance navigation. To address these challenges, we propose a zero-shot semantic navigation framework. Our method incrementally maintains…

---

### [LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents](https://arxiv.org/abs/2606.31045v1)

- **arXiv**: `2606.31045v1`  |  **提交日期**: 2026-06-30
- **作者**: Jingpu Yang, Fengxian Ji, Zhengzhao Lai, Zhexuan Cui, Guangxian Ouyang, Qian Jiang et al.

Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating procedures, into machine-checkable runtime constraints. We introduce LabGuard (Laboratory Guard), a language-to-execution safety suite that grounds natural-language laboratory rules into executable specifications and deploys them as…

---

### [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](https://arxiv.org/abs/2606.30608v2)

- **arXiv**: `2606.30608v2`  |  **提交日期**: 2026-06-29
- **作者**: Mohamed el Amine Boudjoghra, Ivan Laptev, Angela Dai

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry…

---

## 📅 2026-06-30

### [Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638v1)

- **arXiv**: `2606.30638v1`  |  **提交日期**: 2026-06-29
- **作者**: Jameel Hassan, Yasiru Ranasinghe, Vishal Patel

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their…

---

### [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](https://arxiv.org/abs/2606.30608v1)

- **arXiv**: `2606.30608v1`  |  **提交日期**: 2026-06-29
- **作者**: Mohamed el amine boudjoghra, Ivan Laptev, Angela Dai

Articulated 3D objects are essential for interactive environments in embodied AI, robotics, and virtual reality, but reconstructing their structure and motion from sparse observations remains challenging. Existing approaches remain largely constrained by lack of supervised data or lack the priors needed to reliably recover articulation, hidden geometry, and internal object structure. We present the first debate-driven agentic approach to articulated 3D object reconstruction from text or image inputs that both grounds articulation reasoning in concrete motion and exposes the occluded geometry…

---

### [The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction](https://arxiv.org/abs/2606.30308v1)

- **arXiv**: `2606.30308v1`  |  **提交日期**: 2026-06-29
- **作者**: Yuxi Wang, Chengkai Jin, Yufei Liu, Wenqi Ouyang, Tianyi Wei, Zhiwei Zeng et al.

4D hand motion reconstruction from egocentric video is bottlenecked by clear limitations of existing methods: image-based pipelines depend on a detector that fails under heavy occlusion, while video-based methods rely on temporal modules learned only from scarce hand-pose annotations, a narrow signal insufficient to model motion dynamics, occlusion reasoning, and hand-object interaction. These capabilities, however, are exactly what video generative models must implicitly acquire when trained to synthesize coherent video at internet scale. Motivated by this, we present ViDiHand, which…

---

### [Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](https://arxiv.org/abs/2606.30014v1)

- **arXiv**: `2606.30014v1`  |  **提交日期**: 2026-06-29
- **作者**: Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang et al.

Real-to-sim reconstruction for embodied AI requires geometry that is useful for collision reasoning, navigation, and agent-environment interaction, not only photorealistic novel-view synthesis. However, close-range urban facades are difficult for video-to-3D reconstruction: glass, reflections, repeated windows, and weak texture can produce visually plausible renderings with unstable surface geometry. We introduce shell-supervised Gaussian Splatting, a reconstruction-stage framework that uses an external facade structural shell as lightweight geometric supervision for video-driven Gaussian…

---

### [Efficient Visual Pointing for Embodied AI:Agent-Driven Data Synthesis, Cross-Block Attention, and Iterative Correction](https://arxiv.org/abs/2606.29850v1)

- **arXiv**: `2606.29850v1`  |  **提交日期**: 2026-06-29
- **作者**: Zijian Hong, Qi Lv, Yuxiang Xie, Jianming Xing, Xiang Deng, Weili Guan et al.

Visual pointing maps a language instruction to pixel co ordinates, a core skill for embodied AI. We describe our PointArena 2026 solution, which achieves 77.2% overall accuracy and ranks second on the benchmark. The ap proach targets three failure modes. First, agent-driven syn thesis builds large semantic and anchor-relative candidate pools; the server inventory contains 55,372 processed out puts, 53,772 de-duplicated sample IDs, and 37,574 train able completed or accepted rows. Second, a determinis tic steerable-data pipeline creates a verified 10,000-sample main set, plus reserve samples,…

---

## 📅 2026-06-29

### [HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration](https://arxiv.org/abs/2606.28215v1)

- **arXiv**: `2606.28215v1`  |  **提交日期**: 2026-06-26
- **作者**: Jiaxin Li, Yuxiang Wu, Zhenkai Zhang, Xinrui Shi, Haoyuan Wang, Yichen Zhao et al.

Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a…

---

### [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](https://arxiv.org/abs/2606.28182v1)

- **arXiv**: `2606.28182v1`  |  **提交日期**: 2026-06-26
- **作者**: Qinhong Zhou, Chuang Gan, Anoop Cherian

Embodied agents operating in decentralized and partially observable environments have attracted growing attention in recent years. However, existing large language model (LLM)-based agents often exhibit behaviors that are misaligned with their partners or inconsistent with the environment state, leading to inefficient cooperation and poor task success. To address this challenge, we propose a novel framework, Learning Laws of Cooperation (LLawCo), that enables embodied agents to autonomously align with both their partners and task objectives. Our framework allows agents to reflect on past…

---

### [AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration](https://arxiv.org/abs/2606.28049v1)

- **arXiv**: `2606.28049v1`  |  **提交日期**: 2026-06-26
- **作者**: Haotian Li, Yida Wang, Leyuan Wang, Jinshan Lai, Keyang Wang, Zonghao Guo et al.

In recent years, multimodal large language models (MLLMs) have shown strong potential for embodied intelligence, yet their ability to maintain geometrically consistent spatial understanding across heterogeneous views remains under-evaluated. Existing benchmarks largely focus on single-agent, single-view perception, leaving a gap in the systematic assessment of collaborative air-ground settings, where multi-scale observations are complementary but introduce scale mismatch, asymmetric occlusion, and reference-frame inconsistencies. We present AirGroundBench, a diagnostic benchmark for…

---

### [Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection](https://arxiv.org/abs/2606.27962v1)

- **arXiv**: `2606.27962v1`  |  **提交日期**: 2026-06-26
- **作者**: Junwu Xiong, Yongjian Guo, Mingxi Luo, Ning Qiao, Lei Kang, Song Wang et al.

This paper presents a cloud-native simulation infrastructure framework for embodied intelligence that supports large-scale training, standardized evaluation, and simulation-based data collection. The framework unifies simulation environment generation, task execution, trajectory collection, model evaluation, data management, and cloud services into a scalable and reproducible platform. To address the high cost, limited scalability, and poor reproducibility of real-world robotic data collection, the framework adopts cloud-native technologies including elastic resource scheduling, containerized…

---

### [When Multi-Robot Systems Meet Agentic AI:Towards Embodied Collective Intelligence](https://arxiv.org/abs/2606.27929v1)

- **arXiv**: `2606.27929v1`  |  **提交日期**: 2026-06-26
- **作者**: Yuxuan Yan, Yuanyuan Jia, Qianqian Yang

Embodied AI is increasingly becoming agentic, shifting robots from perception--control pipelines towards closed-loop systems that can retrieve context, deliberate during execution, monitor feedback, and refine future behavior. In parallel, robotics research has also moved from single-robot autonomy towards multi-robot systems, driven by the need for wider sensing, distributed action, heterogeneous capabilities, and fault tolerance. As AI agents move from single-agent use towards multi-agent collaboration, robotics faces a parallel challenge: robot teams must move beyond sharing maps, task…

---

### [NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning](https://arxiv.org/abs/2606.27826v1)

- **arXiv**: `2606.27826v1`  |  **提交日期**: 2026-06-26
- **作者**: Shiyun Zhao, Xinwei Song, Tianyu Guo, Xiaomeng Gao, Mingyuan Liu, Xu Han et al.

Multimodal large language models (MLLMs) are increasingly deployed as embodied planners in egocentric environments, where task success requires not only achieving instructed goals but also acting in socially appropriate ways. While explicit goals may render certain actions optimal, implicit social norms often impose hidden constraints. Existing evaluations typically focus on explicit goal achievement or direct norm knowledge, seldom assessing whether planners can infer and apply these hidden constraints within action sequences. We introduce NormAct, a benchmark for embodied social-norm…

---

## 📅 2026-06-27

### [Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy](https://arxiv.org/abs/2606.27251v1)

- **arXiv**: `2606.27251v1`  |  **提交日期**: 2026-06-25
- **作者**: Junhao Shi, Zezheng Huai, Siyin Wang, Jia Chen, Yubang Wang, Zhaoye Fei et al.

Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. Existing systems treat these as separate problems: VLM-based planners lack a unified cyber-physical action space, agent frameworks accumulate unbounded context that degrades temporal coherence, and VLA policies execute open-loop without detecting their own failures. We argue that persistent…

---

### [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079v1)

- **arXiv**: `2606.27079v1`  |  **提交日期**: 2026-06-25
- **作者**: Mingyang Lyu, Yinqian Sun, Yiyang Jia, Sicheng Shen, Moquan Sha, Huangrui Li et al.

In embodied intelligence, safety is a prerequisite for reliable robot deployment in the physical world. Current vision-language-action (VLA) models continue to advance toward general-purpose task capability, yet their embodied safety limits remain poorly understood. To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), instruction-side safety (Safe-Lang), and perception-side safety (Safe-Vis), and evaluate policies…

---

### [SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation](https://arxiv.org/abs/2606.25497v1)

- **arXiv**: `2606.25497v1`  |  **提交日期**: 2026-06-24
- **作者**: Hao Su, Yuehao Huang, Yukai Ma, Yong Liu, Jiajun Lv

Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations. Existing monolithic methods struggle with long-horizon reasoning and generalize poorly to novel environments. To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reasoning capabilities of Large Language Models (LLMs) with dynamic scene graphs. Crucially, it decouples asynchronous global semantic planning from the high-frequency reactive control loop. The LLM serves as a global planner, decomposing…

---

### [AI Coaching for Accelerating Human Skill Development with Reinforcement Learning](https://arxiv.org/abs/2606.25337v1)

- **arXiv**: `2606.25337v1`  |  **提交日期**: 2026-06-24
- **作者**: Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam

AI copilots can substantially boost human performance through shared control, but excessive assistance can induce over-reliance and skill atrophy. This paper studies how an embodied AI agent can act as a coach that accelerates human motor-skill development. We argue that effective coaching requires strategic scaffolding and stepping back that are aligned with the learner's capability, allowing productive failures that drive learning. We formalize the interactive AI coaching process as a non-cooperative dynamic game in which the learner optimizes task performance while the coach targets the…

---

