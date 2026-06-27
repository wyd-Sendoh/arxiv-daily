# Diffusion Models

_自动追踪 arXiv 最新论文，最新更新在最上方。_

## 📅 2026-06-27

### [DanceOPD: On-Policy Generative Field Distillation](https://arxiv.org/abs/2606.27377v1)

- **arXiv**: `2606.27377v1`  |  **提交日期**: 2026-06-25
- **作者**: Wei Zhou, Xiongwei Zhu, Zelin Xu, Bo Dong, Lixue Gong, Yongyuan Liang et al.

Modern image generation demands a single model that unifies diverse capabilities, including text-to-image (T2I), local editing, and global editing. However, these capabilities are rarely naturally aligned and often conflict. For instance, editing tends to degrade T2I performance, while global and local editing interfere with each other. Consequently, effectively composing these capabilities has become a central challenge for image generation model training. To tackle this, we introduce DanceOPD, an on-policy generative field distillation framework for flow-matching models that routes each…

---

### [Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)](https://arxiv.org/abs/2606.27163v1)

- **arXiv**: `2606.27163v1`  |  **提交日期**: 2026-06-25
- **作者**: Ilia Larchenko

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding. The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final. It improves a vision-language-action (VLA) policy with a reinforcement-learning loop. The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection. The work mostly recombines existing RL ideas with…

---

### [Bridging Vision and Language Concepts through Optimal Transport Semantic Flow](https://arxiv.org/abs/2606.26891v1)

- **arXiv**: `2606.26891v1`  |  **提交日期**: 2026-06-25
- **作者**: Chenyang Zhang, Anqi Dong, Guangming Zhu, Nuoye Xiong, Siyuan Wang, Lin Mei et al.

Concept Bottleneck Models (CBMs) promise transparent reasoning by predicting through human-interpretable concepts, yet their effectiveness fundamentally depends on how well visual and textual representations are aligned or matched. Existing vision-language CBMs often rely on pre-aligned encoders or global cosine similarity, which obscures fine-grained concept localization and fails to reflect true semantic geometry. In this work, we rethink concept alignment as a dynamic cross-modal transport process instead of static projection and propose the Optimal Transport Flow Concept Bottleneck Model…

---

### [NaviCache: Test-Time Self-Calibration Caching for Video Generation](https://arxiv.org/abs/2606.26795v1)

- **arXiv**: `2606.26795v1`  |  **提交日期**: 2026-06-25
- **作者**: Zheqi Lv, Zhibo Zhu, Jinke Wang, Qi Tian, Shengyu Zhang, Zhengyu Chen et al.

Video Diffusion Models (VDMs) is constrained by immense computational costs. While offline calibration-based acceleration suffers from calibration data dependency, prohibitive calibration duration, and susceptibility to distribution shifts, offline calibration-free methods eliminate these hurdles. However, since they rely on instantaneous zero-order approximations where the mapping between input and output differences varies in real-time, they are susceptible to observational noise and ignore the intrinsic momentum within the diffusion trajectory. In this paper, we propose NaviCache, a…

---

### [LearniBridge: Learnable Calibration of Feature Caching for Diffusion Models Acceleration](https://arxiv.org/abs/2606.26778v1)

- **arXiv**: `2606.26778v1`  |  **提交日期**: 2026-06-25
- **作者**: Xuyue Huang, Zhe Chen, Wang Shen, Xiao-Ping Zhang

Diffusion Transformers (DiTs) have driven substantial progress in image and video generation but suffer from prohibitive computational costs. Feature caching accelerates inference by reusing intermediate representations. Existing methods rely on historical features for implementation simplicity, yet suffer from severe error accumulation at high acceleration ratios. To address this limitation, we investigate the nature of the requisite feature correction. We demonstrate that the optimal calibration update is characterized by a shared low-rank subspace across diverse prompts. Guided by this…

---

### [Escaping Iterative Parameter-Space Noise: Differentially Private Learning with a Hypernetwork](https://arxiv.org/abs/2606.26772v1)

- **arXiv**: `2606.26772v1`  |  **提交日期**: 2026-06-25
- **作者**: Naoki Nishikawa, Shokichi Takakura, Satoshi Hasegawa

Differentially private (DP) training of neural networks is often hindered by the large amount of noise required by gradient-based methods such as DP-SGD, which repeatedly inject high-dimensional noise in parameter space throughout training. In this paper, we propose a new framework for DP learning that avoids iterative optimization in parameter space. Instead of updating the target model using privatized gradients, we employ a hypernetwork trained on public datasets to map a private dataset to the parameters of the target model. Specifically, each example is embedded into a low-dimensional…

---

### [ResilPhase: Plug-and-Play Phase Mapping and Noise-Resilient Macro-Trajectory Extrapolation for Diffusion Acceleration](https://arxiv.org/abs/2606.26769v1)

- **arXiv**: `2606.26769v1`  |  **提交日期**: 2026-06-25
- **作者**: Qicheng Zhao, Yu Li, Qi Sun, Zheyu Yan

The adoption of powerful diffusion models is hindered by their significant inference latency. Recent ``cache-then-forecast'' schemes alleviate this issue by accelerating DiTs using derivative-based polynomials, but they suffer from severe quality degradation at high acceleration ratios. Our analysis reveals its root cause: the discrete extrapolation performed on representations that are misaligned with the continuous diffusion trajectory and are numerically unstable. Thus, accelerated DiTs suffer from accumulated spatial errors, noisy derivative amplification, and high-order instability. We…

---

### [Anatomy-Guided Residual Motion Diffusion for Controllable 4D Cardiac MRI Synthesis](https://arxiv.org/abs/2606.26764v1)

- **arXiv**: `2606.26764v1`  |  **提交日期**: 2026-06-25
- **作者**: Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang, Lingxiao Zhao, Xin Gao

Developing robust artificial intelligence models for 4D (3D + time) medical imaging is constrained by limited annotated data, inter-device domain shifts, and privacy restrictions. To address this, we propose a 4D controllable generative framework for anatomically consistent data augmentation. A semi-supervised variational autoencoder learns a compact latent representation of anatomical volumes while jointly predicting aligned segmentation masks in a unified framework. Anatomical structure is then disentangled from temporal dynamics through a cascaded latent diffusion model (LDM). A static LDM…

---

### [MLFFM-SegDiff: A Multi-Level Feature Fusion Diffusion Model for Skin Lesion Segmentation](https://arxiv.org/abs/2606.26712v1)

- **arXiv**: `2606.26712v1`  |  **提交日期**: 2026-06-25
- **作者**: Jingjun Gu, Chaojie Shen, Yifeng Cao, Wei Zhang, Yiliu Li, Aobo Fan

Skin lesion segmentation is a key task in computer-aided dermatological diagnosis, where accuracy directly impacts downstream analysis and disease classification. However, dermoscopic images are challenging due to blurred boundaries, low contrast, large shape variations, and artifacts such as hair and shadows. Recently, diffusion models have shown strong performance in medical image segmentation thanks to their progressive denoising and distribution modeling capabilities. Nevertheless, existing diffusion-based methods still suffer from limited cross-level feature interaction and insufficient…

---

### [Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean](https://arxiv.org/abs/2606.26618v1)

- **arXiv**: `2606.26618v1`  |  **提交日期**: 2026-06-25
- **作者**: Phannet Pov, Sovandara Chhoun, Hyun Woo Park, Wan-Sup Cho, Saksonita Khoeurn

Large pretrained text-to-speech (TTS) models sound almost human for well-resourced languages, but much worse for languages that are rare in their training data. We study this quality gap for Khmer and Korean using VoxCPM2, a 2.4B-parameter, tokenizer-free TTS model that joins a MiniCPM-4 language-model backbone with a flow-matching diffusion decoder. We build one shared, language-tagged corpus of about 26 hours and adapt VoxCPM2 with a single Low-Rank Adaptation (LoRA) adapter, trained on both languages at once and added to both the language model and the decoder. The adapter is…

---

### [Latent Diffusion Posterior Sampling with Surrogate Likelihood Guidance for PDE Inverse Problems](https://arxiv.org/abs/2606.26592v1)

- **arXiv**: `2606.26592v1`  |  **提交日期**: 2026-06-25
- **作者**: Yuanzhe Wang, Alexandre M. Tartakovsky

We propose latent-space diffusion posterior sampling (L-DPS), an approximate Bayesian framework for high-dimensional inverse problems governed by partial differential equations (PDEs). The method addresses three challenges in PDE-constrained inversion: implicit sample-based priors without tractable densities, high-dimensional spatially distributed parameters, and the high cost of repeated forward-model evaluations during posterior sampling. L-DPS combines a variational autoencoder, an unconditional latent diffusion model, diffusion posterior sampling, and a differentiable neural surrogate.…

---

### [Adversarial Diffusion Across Modalities: A Fusion Survey of Attacks, Defenses, and Evaluation for Text, Vision, and Vision-Language Models](https://arxiv.org/abs/2606.26566v1)

- **arXiv**: `2606.26566v1`  |  **提交日期**: 2026-06-25
- **作者**: Abrar Alotaibi, Moataz Ahmed

Adversarial evaluation of AI systems has matured along four largely disconnected tracks: diffusion-based attacks on text and large language models (LLMs), diffusion-based attacks on image classifiers, jailbreak pipelines against vision-language models, and diffusion-based input purification defenses. Each has developed its own vocabulary, threat models, and benchmarks, with denoising diffusion models emerging as a shared generative mechanism whose recipes are now actively ported between communities. This survey performs an information-fusion exercise at the meta-research level: we integrate…

---

### [VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation](https://arxiv.org/abs/2606.26534v1)

- **arXiv**: `2606.26534v1`  |  **提交日期**: 2026-06-25
- **作者**: Tianxin Xie, Chenxing Li, Dong Yu, Li Liu

Recently, zero-shot text-to-speech (TTS) has enabled high-fidelity and expressive speech synthesis, but it often fails to imitate unseen speaking styles from uncommon scenarios (e.g., crosstalk, dialects). Moreover, fine-tuning pretrained models requires large, high-quality datasets, limiting rapid personalization. We propose VoiceTTA, a reinforcement learning-based test-time adaptation (TTA) method that improves voice imitation of pretrained zero-shot TTS models. VoiceTTA introduces two style rewards based on coefficient-of-variation differences of F0 and energy, combined with speaker…

---

### [Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context](https://arxiv.org/abs/2606.26493v1)

- **arXiv**: `2606.26493v1`  |  **提交日期**: 2026-06-25
- **作者**: Fitsum Reda, John Kamalu, Roger Waleffe, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro

Diffusion language models offer a promising alternative to autoregressive models due to their potential for parallel and iterative generation. However, existing approaches use a single network for both context representation and iterative denoising, forcing one model to serve both roles and limiting its capacity for either role. We propose TwoTower, a block-wise autoregressive diffusion model that decouples these roles into two towers: a frozen AR context tower that causally processes clean tokens, and a trainable diffusion denoiser tower with bidirectional block attention that refines noisy…

---

