# 四足机器人 (Quadruped Robots)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-07-01

### [Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing](https://arxiv.org/abs/2606.31912v1)

- **arXiv**: `2606.31912v1`  |  **提交日期**: 2026-06-30
- **作者**: Jiale Fan, Connor Flynn, Tianao Xu, Junzhe He, Andrei Cramariuc, Marco Hutter et al.

Learning-based control has revolutionized dynamic locomotion, yet navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost, high-frequency infrared…

---

### [LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music](https://arxiv.org/abs/2606.31158v1)

- **arXiv**: `2606.31158v1`  |  **提交日期**: 2026-06-30
- **作者**: Snehasis Banerjee, Ranjan Dasgupta

The quest for intuitive and natural human-robot interaction (HRI) remains a significant challenge in robotics. Traditional methods often rely on rigid, pre-programmed commands that limit the robot's expressiveness and adaptability. This paper introduces a novel framework that leverages the reasoning capabilities of Large Language Models (LLMs) to synthesize complex robotic actions from a rich tapestry of multimodal human inputs: natural speech, hand gestures, and music/sound beats. Our system architecture integrates a speech transcription model, a gesture recognition module, and a signal…

---

### [The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments](https://arxiv.org/abs/2606.30900v1)

- **arXiv**: `2606.30900v1`  |  **提交日期**: 2026-06-29
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen, Jan Tommy Gravdahl, Mario di Castro

Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone and a tendon-actuated soft gripper that enables the robot to pick up sampling tissues, swab contaminated surfaces, and release the tissues at designated collection locations for subsequent beryllium analysis. To enable intuitive…

---

## 📅 2026-06-30

### [KYON: Semi-Modular Wheel-Legged Quadruped With Agile Bimanual Capability](https://arxiv.org/abs/2606.30243v1)

- **arXiv**: `2606.30243v1`  |  **提交日期**: 2026-06-29
- **作者**: Luca Rossini, Arturo Laurenzi, Francesco Ruscelli, Yifang Zhang, Giovanbattista Gravina, Lorenzo Baccelliere et al.

This paper presents KYON, a hybrid wheel-legged quadruped robot equipped with a bimanual upper body for loco-manipulation tasks. The platform features a semi-modular design with a reconfigurable lower legs, enabling both wheeled and legged locomotion depending on the environment. A design approach that places actuators in the base and uses transmission mechanisms reduces distal inertia, improving agility and dynamic performance. The robot integrates a whole-body control framework together with a reinforcement learning based policy to handle nonlinear dynamics and enhance robustness to…

---

## 📅 2026-06-29

### [CacheMPC: Certified Cached Model Predictive Control for Quadruped Locomotion](https://arxiv.org/abs/2606.28300v1)

- **arXiv**: `2606.28300v1`  |  **提交日期**: 2026-06-26
- **作者**: Nimesh Khandelwal, Mehul Anand, Shakti S. Gupta, Mangal Kothari

Model Predictive Control (MPC) is the standard predictive layer in hierarchical quadruped controllers, but the per-cycle QP solve limits the update rate achievable on embedded processors. Because legged gaits revisit a bounded region of state space, MPC solutions admit caching and reuse. This paper proposes \emph{Certified CacheMPC}: a Locality-Sensitive-Hashed cache of horizon contact-force trajectories, partitioned by contact mode, retrieved at query time and accepted only when an a-posteriori per-query certificate confirms primal feasibility and a Lagrangian dual-gap upper bound on cost…

---

### [Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors](https://arxiv.org/abs/2606.28237v1)

- **arXiv**: `2606.28237v1`  |  **提交日期**: 2026-06-26
- **作者**: Youzhi Liu, Li Gao, Yifei Qian, Liu Liu, Yang Cai, Ziqiao Li

Quadruped robots have achieved remarkable locomotion, yet their behavioral repertoire remains confined to a few gaits--far from the expressive, companion-like presence long envisioned for them. Attempts to import the humanoid recipe of large-scale motion data have inherited one tacit assumption: that robot motion must first pass through an animal body, making data collection dependent on cooperative animals, reconstruction fragile across species, and retargeting ill-posed across incompatible morphologies. We propose Uni-Mo, a fully automated pipeline that removes the animal from the loop by…

---

### [PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control](https://arxiv.org/abs/2606.27861v1)

- **arXiv**: `2606.27861v1`  |  **提交日期**: 2026-06-26
- **作者**: Jiatao Ding, Songqun Gao, Andrea Del Prete, Matteo Saveriano

Reinforcement learning (RL) has emerged as a promising solution to accomplish complex robotic control tasks; however, most of the current work ignores the safety requirements. Safe RL seeks to maximize task performance while satisfying explicit physical constraints, but current algorithms struggle to learn the policy efficiently with precise constraint satisfaction. This work proposes PPO-EAL, a novel first-order constrained policy optimization framework that integrates exact augmented Lagrangian optimization into proximal policy optimization for safe robotic control. By combining clipped…

---

## 📅 2026-06-27

### [OctoSense: Self-Supervised Learning for Multimodal Robot Perception](https://arxiv.org/abs/2606.27317v1)

- **arXiv**: `2606.27317v1`  |  **提交日期**: 2026-06-25
- **作者**: Anthony Bisulco, Jeremy Wang, Kostas Daniilidis, Randall Balestriero, Pratik Chaudhari

We present OctoSense, an open-source sensor platform with stereo RGB and event cameras, LiDAR, a thermal camera, an inertial measurement unit, RTK-corrected global positioning system, and proprioception (CAN bus data from a car, and joint angles for a quadruped robot). The eponymous OctoSense dataset contains 59 hours of time-synchronized driving data across different types of environments at different times of the day, including situations with highly degraded sensors. We demonstrate multi-modal self-supervised learning using such real-world robotics data, where sensors have different…

---

### [MPC-Injection: Biasing Off-Policy Locomotion RL Toward Controller-Induced Behavior Basins](https://arxiv.org/abs/2606.26392v1)

- **arXiv**: `2606.26392v1`  |  **提交日期**: 2026-06-24
- **作者**: Roy Xing, Seyoung Ree, Brian Plancher

Reinforcement learning (RL) for locomotion frequently converges to locally optimal but undeployable behaviors, such as vibrating limbs or scooting on the torso, that maximize return without producing a usable gait. We present MPC-Injection, a low-overhead method that steers RL toward a designer-preferred gait by inserting transitions into the replay buffer from a model predictive controller solving the same Markov decision process. Unlike reward shaping, MPC-Injection does not require redesigning the task reward, and unlike adversarial imitation learning, it adds no discriminator, no…

---

### [Racing a Wheeled Quadruped: Active Load Transfer Mitigation via Model Predictive Control](https://arxiv.org/abs/2606.26313v1)

- **arXiv**: `2606.26313v1`  |  **提交日期**: 2026-06-24
- **作者**: Marla Eisman, Brian Lam, Samuel Sonnino, Francesco Borrelli

This paper presents a hierarchical control framework using model predictive control (MPC) and reinforcement learning (RL) for active roll control to manage lateral load transfer during autonomous racing of a wheeled quadruped. The framework integrates offline time-optimal raceline generation, an online MPC planner that actively minimizes the lateral Load Transfer Ratio (LTR), and a low-level, whole-body RL policy deployed directly onto the robot's 16 actuators. The MPC is based on a vehicle dynamics bicycle model of the Unitree Go2-W platform. The robot's leg actuators act as active…

---

### [Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion](https://arxiv.org/abs/2606.25965v1)

- **arXiv**: `2606.25965v1`  |  **提交日期**: 2026-06-24
- **作者**: Giulio Turrisi, Ozan Pali, Luca Oneto, Claudio Semini

Legged robots deployed in planetary exploration and other remote environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized control experts associated with distinct actuator…

---

### [StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots](https://arxiv.org/abs/2606.25765v1)

- **arXiv**: `2606.25765v1`  |  **提交日期**: 2026-06-24
- **作者**: Xincheng Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu et al.

Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in…

---

### [MAPL: Multi-Objective Preference Learning for Robot Locomotion](https://arxiv.org/abs/2606.25398v1)

- **arXiv**: `2606.25398v1`  |  **提交日期**: 2026-06-24
- **作者**: Xiyue Chen, Muhan Lin, Shuyang Shi, Joseph Campbell

Reward design remains a major bottleneck in reinforcement learning for robot locomotion, where successful policies often depend on carefully tuned, task-specific reward functions. Preference-based reinforcement learning offers an alternative, but existing LLM-based methods typically ask for a single overall judgment between behaviors, making it difficult to capture the multiple competing objectives that underlie high-quality locomotion. We present Multi-Objective AI-Informed Preference Learning (MAPL), a framework that learns locomotion rewards from high-level natural language objectives…

---

### [WaveForward: An Omnidirectional Passive Wheeled Quadruped Robot with Casters](https://arxiv.org/abs/2606.25299v1)

- **arXiv**: `2606.25299v1`  |  **提交日期**: 2026-06-24
- **作者**: Chuanlin Zhao, Qifeng Zheng, Shuhan Wang, Tiancheng Ma, Weixian Lin, Xin Luo

Wheeled-legged robots possess both agile mobility for traversing complex terrains and high efficiency, making them suitable for long-distance transportation applications. Conventional actuated wheeled robots require specialized hardware and electrical design due to the incorporation of wheel components. We propose a novel and low-cost passive wheeled legged robot equipped with standard casters on each leg to obtain omnidirectional mobility. The control method employs an asymmetric actor-critic structure, enabling the utilization of the privileged information of the passive caster's angles and…

---

