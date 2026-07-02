# 强化学习运动控制 (RL Locomotion & Control)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-07-02

### [A Data-Enabled Primal-Dual Approach for Policy Learning with SDP Formulations](https://arxiv.org/abs/2607.00644v1)

- **arXiv**: `2607.00644v1`  |  **提交日期**: 2026-07-01
- **作者**: Han Wang, Feiran Zhao, Florian Dorfler

This paper develops a data-enabled primal-dual framework for learning optimal control policies for unknown linear discrete-time systems from online data. The proposed approach views the data-dependent control synthesis problem as a time-varying semidefinite program (SDP) whose coefficients are recursively updated from online closed-loop measurements. Instead of repeatedly solving a full SDP as new data arrive, the policy is updated online through lightweight primal-dual iterations, each consisting of a linear equation solve and a projection onto the positive semidefinite cone. The framework…

---

### [[Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator](https://arxiv.org/abs/2607.00569v1)

- **arXiv**: `2607.00569v1`  |  **提交日期**: 2026-07-01
- **作者**: Lina van Brügge, Shruti Kotpalliwar, Anton Koval, Akshit Saradagi, George Nikolakopoulos

In this article, we present dynamic modeling, gait synthesis, and feedback control design for a modular novel subsurface robot, designed for human-free subsurface exploration and excavation. The subsurface propagator design is based on two major aspects: 1) anchor and propel movement like an earthworm and 2) excavation similar to tunnel boring machines. This design is decoupled into five separate modules: one drill head to excavate and create cavity for propagation, two modules to anchor the robot, and two modules to enable propagation of the body. In order to design a controller for each of…

---

### [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272v1)

- **arXiv**: `2607.00272v1`  |  **提交日期**: 2026-06-30
- **作者**: Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar et al.

Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with…

---

### [3D Point World Models: Point Completion Enables More Accurate Dynamics Learning](https://arxiv.org/abs/2607.00148v1)

- **arXiv**: `2607.00148v1`  |  **提交日期**: 2026-06-30
- **作者**: Skand Peri, Hung Nguyen, Chanho Kim, Li Fuxin, Stefan Lee

Learning predictive models of the world enables robotic control through planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models lack explicit 3D spatial structure and suffer from geometrically inconsistent long-term rollouts with compounding errors. Emerging 3D dynamics models based on partial point clouds improve geometric consistency but remain sensitive to occlusions and accumulated prediction drift. To address these challenges, we present 3D Point World Models (3DPWM) - a task-agnostic world model that operates entirely in 3D…

---

### [A Synthetic-Driven Vision System for Assembly Step Recognition](https://arxiv.org/abs/2607.00129v1)

- **arXiv**: `2607.00129v1`  |  **提交日期**: 2026-06-30
- **作者**: Hui Zhang, Xuanang Lei, Rui Wang, Julian Ferchow, Mirko Meboldt

Quality control in industrial assembly is essential, and real-time monitoring of the assembly process is crucial for preventing costly defects and ensuring production reliability. Vision-based automated inspection offers a powerful solution for such real-time monitoring. However, due to the specialized industrial components and processes, training these models typically relies on task-specific real-world data, which is costly and labor-intensive to collect and annotate. In this paper, we propose a system that automatically generates realistic assembly sequences and further trains real-time…

---

### [Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation](https://arxiv.org/abs/2606.31043v2)

- **arXiv**: `2606.31043v2`  |  **提交日期**: 2026-06-30
- **作者**: Ethan Hirschowitz, Fabio Ramos

Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We…

---

## 📅 2026-07-01

### [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](https://arxiv.org/abs/2606.31993v1)

- **arXiv**: `2606.31993v1`  |  **提交日期**: 2026-06-30
- **作者**: Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín

While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit,…

---

### [SENSE-VAD: Sentient and Semantic Video Anomaly Detection for Autonomous Driving](https://arxiv.org/abs/2606.31875v1)

- **arXiv**: `2606.31875v1`  |  **提交日期**: 2026-06-30
- **作者**: Nghia T. Nguyen, Lokman Bekit, Yasin Yilmaz

Autonomous vehicles (AVs) must navigate not only motion-based hazards but also socially complex situations whose danger is constituted by inter-agent relationships rather than movement statistics alone. A child running away from a guardian, a person being carried by another, or a pursuer chasing a pedestrian across a sidewalk are all anomalous in social context, yet none produces an obvious motion signal that current anomaly detectors are equipped to flag. We introduce SENSE-VAD, the first synthetic video anomaly detection benchmark for autonomous driving explicitly designed around socially…

---

### [Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors](https://arxiv.org/abs/2606.31101v1)

- **arXiv**: `2606.31101v1`  |  **提交日期**: 2026-06-30
- **作者**: Zixing Wang, Kausik Sivakumar, Jinghuan Shang, Yafei Hu, Zhaoming Xie, Ran Gong et al.

Bridging the sim-to-real gap is a core challenge in deploying learned manipulation policies. Sim-to-real learning is attractive because it can replace expensive real robot demonstrations with scalable synthetic data, yet world-action models have not previously been shown to transfer from simulation to real robotic manipulation. We study whether a world-action model can be trained from synthetic priors and deployed zero-shot in the real world. To this end, we build upon Cosmos Policy, a video diffusion model adapted for visuomotor control. We construct simulation environments with extensive…

---

### [Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation](https://arxiv.org/abs/2606.31043v1)

- **arXiv**: `2606.31043v1`  |  **提交日期**: 2026-06-30
- **作者**: Ethan Hirschowitz, Fabio Ramos

Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We…

---

## 📅 2026-06-30

### [VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645v1)

- **arXiv**: `2606.30645v1`  |  **提交日期**: 2026-06-29
- **作者**: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel et al.

Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale. We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction…

---

### [OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning](https://arxiv.org/abs/2606.30378v1)

- **arXiv**: `2606.30378v1`  |  **提交日期**: 2026-06-29
- **作者**: Haocong He, Chenfei Liao, Zichen Wen, Zihao Dongfang, Xu Zheng, Bin Ren et al.

Multimodal Large Language Models (MLLMs) have demonstrated promising spatial reasoning capabilities, while these abilities remain underexplored in the emerging visual modality of panoramic imagery. The full 360°$\times$180° field of view of panoramas essentially supports complex global multi-step reasoning, which is also the fundamental advantage of panoramas in applications such as embodied intelligence. However, existing panoramic benchmarks largely focus on simplistic queries that rely on local cues or single-/few-step reasoning, thereby ignoring the fundamental advantage of panoramas and…

---

### [ReactiveBFM: Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control](https://arxiv.org/abs/2606.30362v1)

- **arXiv**: `2606.30362v1`  |  **提交日期**: 2026-06-29
- **作者**: Xiao Chen, Weishuai Zeng, Xiaojie Niu, Zirui Wang, Jianan Li, Huayi Wang et al.

While current Behavior Foundation Models (BFMs) provide robust control priors for humanoids, they only execute pre-defined reference motions. As a result, they are vulnerable to environmental shifts and incapable of reactive whole-body coordination. Naively cascading them with generative motion planners fails to achieve true reactivity, as inevitable tracking discrepancies induce fatal cumulative exposure bias. To bridge this gap, we propose ReactiveBFM, a real-time closed-loop planning-control framework. At its core, we effectively mitigate exposure bias via a scheduled prefix sampling…

---

### [ConCent: Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration](https://arxiv.org/abs/2606.30268v1)

- **arXiv**: `2606.30268v1`  |  **提交日期**: 2026-06-29
- **作者**: Heecheol Kim, Namiko Saito, Katsushi Ikeuchi, Yasuyuki Matsushita

Sim-to-real policy transfer -- deploying policies trained in simulation in the real world -- is a promising paradigm for scaling robot manipulation without large-scale real-world data. However, transferring simulation-trained policies remains challenging due to discrepancies in contact dynamics -- particularly in contact-rich tasks where subtle differences can alter task outcomes entirely. Because interaction between the manipulated object and the environment is mediated through contact, task success depends on accurately reproducing task-relevant contacts. Accordingly, in manipulation,…

---

### [Domain Adaptation with Adaptive Imagination for Visual Reinforcement Learning under Limited Target Data](https://arxiv.org/abs/2606.30192v1)

- **arXiv**: `2606.30192v1`  |  **提交日期**: 2026-06-29
- **作者**: Hyunwoo Park, Sang-Hyun Lee

Sim-to-real transfer remains a major obstacle for reinforcement learning (RL), especially for vision-based control where image observations exacerbate the state-distribution shift between simulation and the real world. Domain adaptation (DA) is a promising remedy for this challenge. Prior sim-to-real DA works have demonstrated encouraging results, yet these approaches typically assume substantially more target data, which is not available in practice. Indeed, their performance degrades significantly when the target data budget is reduced. To address this challenge, we propose AIDA (Adaptive…

---

### [SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance](https://arxiv.org/abs/2606.30113v1)

- **arXiv**: `2606.30113v1`  |  **提交日期**: 2026-06-29
- **作者**: Tengyue Jiang, Chunpu Xu, Jiayue Kang, Yao Mu

Discrete action tokenization provides a compact interface for autoregressive VLA policies, but accurately recovering continuous robot actions from discrete codes remains challenging. Existing tokenizers typically map each discrete code to a fixed continuous action prototype, ignoring the robot's current proprioceptive state. This limitation is particularly pronounced in manipulation, where the same action token may require different continuous controls under different joint configurations, object poses, and contact conditions. We therefore propose SA-VLA, a state-aware action tokenizer that…

---

### [FalconTrack: Photorealistic Auto-Labeled Perception and Physics-Aware Vision-Based Aerial Tracking](https://arxiv.org/abs/2606.29783v1)

- **arXiv**: `2606.29783v1`  |  **提交日期**: 2026-06-29
- **作者**: Yan Miao, Karteek Gandiboyina, Noah Giles, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos et al.

Vision-based aerial tracking is critical in GPS-denied environments. Reliable perception for tracking depends on large-scale labeled data, yet most photorealistic datasets rely on heavy manual annotation and are time-consuming to produce. We present FalconTrack, a unified perception-and-tracking framework that (i) leverages a photorealistic editable simulator for automated label generation and (ii) combines multi-head perception with physics-aware tracking for zero-shot sim-to-real transfer. FalconTrack provides an automated labeling pipeline in a Gaussian Splatting simulator that isolates…

---

### [CORE Planner: Contextual-memory Oriented Reinforcement-learning in Unknown Environments for Robot Navigation](https://arxiv.org/abs/2606.29222v1)

- **arXiv**: `2606.29222v1`  |  **提交日期**: 2026-06-28
- **作者**: Jintao Kong, Zhihao Zhang, Weihuang Chen, Liming Chen, Zhongyu Guo, Shuaiyu Liu et al.

Autonomous navigation in unknown environments requires a robot to efficiently reach a predefined goal while exploring without prior maps. Although progress has been made in this area, most existing works still rely on traditional planning methods with hand-crafted rules, while learning-based methods often suffer from limited environmental memory and challenges in simulation-to-real (sim-to-real) transfer. To overcome these limitations, we propose a Contextual-memory Oriented Reinforcement-learning (CORE) planner for robot navigation in unknown environments. The proposed CORE planner…

---

### [Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis](https://arxiv.org/abs/2606.28805v1)

- **arXiv**: `2606.28805v1`  |  **提交日期**: 2026-06-27
- **作者**: Christian Conti, Bilan Yang, Alexander Sigrist, Lorenzo Miele, Yamen Saraiji, Peter Dürr et al.

At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics--a requirement made even more stringent by the adversarial nature of the game, where any regime in which a model fails to…

---

## 📅 2026-06-27

### [VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity](https://arxiv.org/abs/2606.27344v1)

- **arXiv**: `2606.27344v1`  |  **提交日期**: 2026-06-25
- **作者**: Yuemin Mao, Uksang Yoo, Jean Oh, Jonathan Francis, Jeffrey Ichnowski

Dexterous manipulation depends on contact events that are fast, local, and often visually occluded. Piezoelectric microphones offer a compact and high-bandwidth way to sense these interactions, but the resulting vibro-acoustic signals are difficult to simulate faithfully enough for end-to-end sim-to-real policy learning on dexterous robot hands. We propose VibeAct, a framework that bridges real vibrotactile sensing and simulation-based reinforcement learning through a shared physical representation of contact and slip. In the real world, we embed piezoelectric microphones into a dexterous…

---

### [Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)](https://arxiv.org/abs/2606.27163v1)

- **arXiv**: `2606.27163v1`  |  **提交日期**: 2026-06-25
- **作者**: Ilia Larchenko

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection. The work mostly recombines existing RL ideas with…

---

### [RobOralScan: Learning Active Intraoral Scanning for Robotic Dental Reconstruction](https://arxiv.org/abs/2606.26955v1)

- **arXiv**: `2606.26955v1`  |  **提交日期**: 2026-06-25
- **作者**: Jinhyung Lee, Haeun Yun, Siwon Kim, Gihyun Baek, Sungho Moon, Sehyun Hwang et al.

Intraoral scanning is widely used for digital optical impressions in prosthodontic, implant, and orthodontic treatment, but full-arch and long-span scanning remain labor-intensive tasks with limited automation. In the confined oral cavity, operators must continuously adjust scanner motion while accumulating narrow field-of-view observations, making reconstruction quality sensitive to missing tooth surfaces and operator workload. We propose RobOralScan, which, to the best of our knowledge, is the first reinforcement learning (RL)-based pipeline for robotic automatic intraoral scanning.…

---

### [IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control](https://arxiv.org/abs/2606.26575v1)

- **arXiv**: `2606.26575v1`  |  **提交日期**: 2026-06-25
- **作者**: Chenlong Liu, Zhuohui Zhang, Xinyan Chen, Zhipeng Wang, Bin Cheng, Bin He

Complex multi-agent control tasks remain challenging for traditional rule-based and model-based approaches, motivating the adoption of learning-based methods. However, learning-based methods often struggle with sim-to-real transfer because they rely on accurate dynamics modeling or system identification and learn policies in low-level control spaces that are highly sensitive to dynamics mismatch, making them costly and fragile in complex environments. To address this issue, we propose a sim-to-real method for multi-agent control, which is insensitive to dynamics mismatch via effect alignment.…

---

### [Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?](https://arxiv.org/abs/2606.26428v1)

- **arXiv**: `2606.26428v1`  |  **提交日期**: 2026-06-24
- **作者**: Tyler Ga Wei Lum, Kushal Kedia, C. Karen Liu, Jeannette Bohg

Multi-fingered robots promise the speed and dexterity of human hands, yet challenging problems such as precise assembly have remained out of reach. These tasks are contact-rich, making data collection for imitation learning difficult, and sparse-reward, making direct exploration with reinforcement learning (RL) intractable. Consequently, prior work has made progress by structuring the problem with specialized grippers, tool attachments, and environment fixtures. In this work, we argue that before a robot can perfect precise assembly, it must first learn to play. We further ask the question:…

---

### [Cross-View Variance Correlation in Path-Traced Stereo:A Hidden Shortcut in Synthetic Training Data](https://arxiv.org/abs/2606.25483v1)

- **arXiv**: `2606.25483v1`  |  **提交日期**: 2026-06-24
- **作者**: Po-Ting Lin

Path-traced synthetic stereo data underlie a large fraction of modern disparity-estimation training pipelines. We report a previously unrecognised property of such data: while the Monte Carlo (MC) noise streams of the two cameras are statistically independent, the underlying \emph{variance fields} -- deterministic per-pixel functions of the rendering integrand -- are highly correlated once aligned by the ground-truth disparity warp. Across 20 scenes rendered with Mitsuba~3, the warped Pearson correlation reaches $ρ{=}0.754{\pm}0.016$ across 20 scenes at $\mathrm{SPP}{=}512$, and on a…

---

### [DynaMOMA: Instantaneous Prediction of Grasp Poses for Mobile Manipulation of Dynamic Objects](https://arxiv.org/abs/2606.25295v1)

- **arXiv**: `2606.25295v1`  |  **提交日期**: 2026-06-24
- **作者**: Zhinan Yu, Junyan Xu, Jiazhao Zhang, Zheng Qin, Yijie Tang, Yuhang Huang et al.

Mobile manipulation is a fundamental robotics task and has advanced rapidly in recent years, enabling robots to navigate, reach, and interact with objects in complex environments. However, mobile manipulation of dynamic objects remains highly challenging, as robots must coordinate the mobile base and arm while adapting to continuously evolving target poses. A key challenge lies in predicting temporally consistent short-horizon grasp trajectories from dynamic observations. In this work, we propose \ours{}, a dynamic mobile manipulation framework that couples instantaneous grasp trajectory…

---

