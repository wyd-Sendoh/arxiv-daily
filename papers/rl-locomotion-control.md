# 强化学习运动控制 (RL Locomotion & Control)

_自动追踪 arXiv 最新论文，最新更新在最上方。_

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

