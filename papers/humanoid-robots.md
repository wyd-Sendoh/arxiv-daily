# 人形机器人 (Humanoid Robots)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-06-29

### [Booster Lab: A Data-Centric Pipeline for Learning Deployable Humanoid Locomotion Policies](https://arxiv.org/abs/2606.27813v1)

- **arXiv**: `2606.27813v1`  |  **提交日期**: 2026-06-26
- **作者**: Penghui Chen, Tinglong Zheng, Yufeng Zhang, Mingguo Zhao

Humanoid robot motion learning requires not only task-oriented control policies but also physically feasible and natural behaviors that can be transferred to real robots. However, robot-feasible motion data are often scarce: raw human demonstrations may be incompatible with the robot morphology, open-source clips vary in quality, and simulation-collected robot trajectories still require feasibility checking. To address these challenges, we propose a data-centric training and deployment pipeline that integrates motion data curation, real-to-sim model adaptation, AMP-based reinforcement…

---

### [CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation](https://arxiv.org/abs/2606.27676v1)

- **arXiv**: `2606.27676v1`  |  **提交日期**: 2026-06-26
- **作者**: Wenqi Ge, Junde Guo, Zhen Fu, Shunpeng Yang, Jiayu Chen, Hua Chen

Achieving everyday tasks with humanoid robots requires coordinating stable locomotion with versatile manipulation. However, existing whole-body controllers still face significant challenges. Methods trained solely via command sampling, without motion-capture (MoCap) data, often struggle with sparse rewards and require carefully tuned curricula to converge. This is especially problematic for upper-body control, where the resulting motions deviate from human-like statistics and degrade whole-body coordination. Conversely, approaches that imitate full-body MoCap data suffer from dataset…

---

## 📅 2026-06-27

### [HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation](https://arxiv.org/abs/2606.27239v1)

- **arXiv**: `2606.27239v1`  |  **提交日期**: 2026-06-25
- **作者**: Hongwu Wang, Chenhao Yu, Youhao Hu, Jiachen Zhang, Yuanyuan Li, Shaqi Luo

High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors that require coordinated perception, locomotion, and manipulation. Existing data-collection methods largely rely on robot teleoperation, which is constrained by hardware accessibility, operator expertise, and limited efficiency. Inspired by the Universal Manipulation Interface (UMI), we propose HumanoidUMI, a portable and robot-free framework for humanoid whole-body data collection. HumanoidUMI uses lightweight VR devices and UMI-inspired grippers to collect sparse human…

---

### [Identifying the Unknown: Prompt-Free Open Vocabulary Anomaly Recognition for Robot-Object Interaction](https://arxiv.org/abs/2606.26829v1)

- **arXiv**: `2606.26829v1`  |  **提交日期**: 2026-06-25
- **作者**: Philipp Allgeuer, Jan-Gerrit Habekost, Stefan Wermter

Robots operating in real-world environments must in general be able to recognize previously unseen objects. As robotic systems move toward open-world autonomy, there is a growing, yet largely unmet, need for open vocabulary object detectors that are prompt-free and efficient enough for continuous deployment. We present AnomNOVIC, a two-stage known-workspace framework that combines a masked autoencoder (MAE) trained for anomaly detection, with NOVIC, a powerful real-time prompt-free open vocabulary image classifier. The MAE produces generic object-agnostic bounding boxes, allowing NOVIC to…

---

### [PressMimic: Pressure-Guided Motion Capture and Control for Humanoid Robot Imitation](https://arxiv.org/abs/2606.26741v1)

- **arXiv**: `2606.26741v1`  |  **提交日期**: 2026-06-25
- **作者**: Yi Lu, Shenghao Ren, Tianyu Xiong, Zhaoxiang Li, Jiaqi Li, He Zhang et al.

Humanoid motion imitation requires not only accurate perception of human kinematics but also faithful reproduction of physical interactions with the environment. However, existing pipelines rely primarily on vision-based motion capture and kinematic imitation, largely ignoring contact dynamics, leading to artifacts such as foot sliding, floor penetration, and unstable behaviors. In this work, we revisit humanoid motion imitation from the perspective of physical grounding and leverage pressure as a unified modality across perception and control. We present PressMimic, a framework that…

---

### [A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots](https://arxiv.org/abs/2606.26425v1)

- **arXiv**: `2606.26425v1`  |  **提交日期**: 2026-06-24
- **作者**: Duncan William Calvert

Humanoid robots could take on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole body motion, perception, contact, and operator supervision. This thesis presents a robot-local, runtime-editable behavior authoring and runtime system. Our system strives to be maximally observable, predictable, and directable following Coactive Design principles developed during the DARPA Robotics Challenge. Our operator interface remains continuously synchronized to the robot for runtime authoring,…

---

### [TaskNPoint: How to Teach Your Humanoid to Hit a Backhand in Minutes](https://arxiv.org/abs/2606.26215v1)

- **arXiv**: `2606.26215v1`  |  **提交日期**: 2026-06-24
- **作者**: Blake Werner, Ilona Demler, Pietro Perona, Aaron D. Ames

How do we learn to hit a tennis backhand? Not from a thousand hours of tennis tournaments on TV - we work with a coach and practice. We argue this is also the right recipe for teaching dynamic skills to humanoid robots. This follows from a structural property of dynamic skills: the outcome is decided by a short, crucial portion of the trajectory - for a backhand, the ~20cm of racket travel around ball contact. Getting this interaction window right requires coordinating the whole motion, so that control, physics, and morphology act in concert. Learning thus reduces to mastering a handful of…

---

### [Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots](https://arxiv.org/abs/2606.25706v1)

- **arXiv**: `2606.25706v1`  |  **提交日期**: 2026-06-24
- **作者**: Yumeng Liu, Dongqi Wang, Jiyu Yu, Yijun Fan, Rong Xiong, Yue Wang

High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For…

---

### [WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning](https://arxiv.org/abs/2606.25591v1)

- **arXiv**: `2606.25591v1`  |  **提交日期**: 2026-06-24
- **作者**: Melya Boukheddimi, Omar Adjali, Daniel Sontag, Frank Kirchner

Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based pipelines. This work introduces a unified framework WOLF-VLA that integrates whole-body optimal-control (OC) motion synthesis with large-scale multi-modal dataset to train VLAs capable of generating humanoid locomotion policies directly…

---

### [Self Capacitive Tactile Sensor System designed for Companion Robots](https://arxiv.org/abs/2606.25348v1)

- **arXiv**: `2606.25348v1`  |  **提交日期**: 2026-06-24
- **作者**: Mohsin Ali, Hidenobu Sumioka, Shuhei Ikemoto

Tactile sensing is essential for humanoid robots to achieve safe physical interaction, dexterous manipulation, and truly human-like responsiveness. However, the design of such systems remains challenging. Conventional approaches often suffer from complex multilayer structures, intricate wiring, high cost, and poor scalability, making it difficult to realize full-body tactile sensing with real-time, low-latency detection while maintaining minimal computational load on the robot's main processor. In this work, we present a simple, scalable and hardware friendly tactile sensing system for a…

---

