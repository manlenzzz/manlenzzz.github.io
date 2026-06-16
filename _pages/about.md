---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
  - /homepage/
---

<div class="academic-home">
  <section id="about" class="home-section">
    <h1>About Me</h1>

    <p>
      I am a direct-track PhD student at <a href="https://www.fudan.edu.cn/" target="_blank" rel="noopener">Fudan University</a>,
      enrolled in 2023. My research focuses on efficient large language models, especially compression, PEFT, adaptive
      inference, and LLM serving systems.
    </p>

    <p>
      I work on the full path from model compression and parameter-efficient adaptation to post-training infrastructure,
      multi-tenant serving, evaluation, and multimodal generation.
    </p>
  </section>

  <section id="news" class="home-section">
    <h1>News</h1>

    <ul class="news-list">
      <li>
        <span class="news-date">2026-06</span>
        <span class="news-text">On the Scaling of PEFT studies million-scale personal adapters over trillion-parameter shared bases.</span>
      </li>
      <li>
        <span class="news-date">2026-05</span>
        <span class="news-text">MinT is available as a managed infrastructure report for training and serving millions of LoRA-backed LLMs.</span>
      </li>
      <li>
        <span class="news-date">2026-05</span>
        <span class="news-text">LLM compression with global rank and sparsity optimization, and QR-Adaptor, are available on arXiv.</span>
      </li>
      <li>
        <span class="news-date">2026-02</span>
        <span class="news-text">AutoQRA is available on arXiv, covering joint search over quantization bit-width and adapter rank.</span>
      </li>
      <li>
        <span class="news-date">2025-02</span>
        <span class="news-text">Dynamic Operator Optimization for multi-tenant LoRA serving appears at AAAI 2025.</span>
      </li>
    </ul>
  </section>

  <section id="research-notes" class="home-section">
    <h1>Notes</h1>

    <a class="note-index-row" href="{{ '/notes/damage-clock-negative-result/' | relative_url }}">
      <span class="note-index-date">2026-06-16</span>
      <span class="note-index-main">
        <strong>When a Better Clock Is Not a Better Sampler</strong>
        <span>A fixed-checkpoint consistency-model diagnostic where a post-hoc damage clock loses to the native skip rule.</span>
      </span>
      <span class="note-index-visual">
        <img src="{{ '/notes/damage-clock-negative-result/figures/fig_result_delta_revised.svg' | relative_url }}" alt="FID delta plot for the damage-clock diagnostic">
      </span>
    </a>
  </section>

  <section id="publications" class="home-section">
    <h1>Publications</h1>

    <div class="publication-group">
      <h2>Post-training、模型发布与训练服务</h2>

      <div class="publication-list">
        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/scaling-peft-main.png' | relative_url }}" alt="Main figure for PEFT scaling">
          <div class="publication-body">
            <h3>On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters</h3>
            <p class="publication-authors">MindLab</p>
            <p class="pub-meta">Thesis / Core Contributor</p>
            <p>
              面向 post-training 从单模型训练走向共享基座 + 海量个人 adapter 的趋势，提出 PEFT 的 Scale Up /
              Scale Down / Scale Out 视角；结合 1T base、百万 adapter 管理与 LoRA RL 实践，将 adapter 定位为个性化模型的持久状态与训练服务接口。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2606.02437" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/macaron-v1-preview-main.png' | relative_url }}" alt="Overview figure for Macaron-V1-Preview">
          <div class="publication-body">
            <h3>Macaron-V1-Preview: A 749B Personal Agent Model with Mixture of LoRA</h3>
            <p class="publication-authors">MindLab</p>
            <p class="pub-meta">Model Release / Core Contributor</p>
            <p>
              参与 Macaron-V1-Preview，面向 Agent 原生优化的 749B 开源模型；通过 MinT 与 Mix-of-LoRA 实现高效训推，引入
              R3 与 Harness Context Protocol 解决 RL、Agent 任务训练及 auto-research 中的训推/训服不一致，使模型在真实
              harness 上优化；在生活类 Agent 与 Openclaw 类 Agent 任务上超越 GPT-5.4 和 Claude Opus 4.7，并在 Coding
              Agent 类任务上取得开源模型 SOTA。
            </p>
            <p class="pub-buttons">
              <a href="https://macaron.im/mindlab/research/macaron-v1-preview" target="_blank" rel="noopener">Project</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/mint-main.png' | relative_url }}" alt="Main figure for MinT infrastructure">
          <div class="publication-body">
            <h3>MinT: Managed Infrastructure for Training and Serving Millions of LLMs</h3>
            <p class="publication-authors">MindLab</p>
            <p class="pub-meta">Technical Report / Core Contributor</p>
            <p>
              针对百万级 LoRA 从训练、版本、导出到上线的生命周期管理挑战，设计 shared-base + adapter revision 的托管基础设施；通过
              adapter-only handoff 与一致的训练/推理路径降低发版、回滚和服务成本。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2605.13779" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>
      </div>
    </div>

    <div class="publication-group">
      <h2>LLM Serving 与推理加速</h2>

      <div class="publication-list">
        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/dynamic-operator-optimization-main.png' | relative_url }}" alt="Main figure for Dynamic Operator Optimization">
          <div class="publication-body">
            <h3>Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Yuhua Zhou, Shiyang Zhang, Yibin Wang, Zekai Liu</p>
            <p class="pub-meta">AAAI 2025 / CCF-A / 一作</p>
            <p>
              针对多租户 LoRA serving 中 batch 形态、rank 组合和硬件特性动态变化导致 kernel 难以手工选择的问题，提出分层搜索空间与
              cost-model-guided evolutionary search，将 SGMV operator 从经验调参转化为可搜索、可迁移的系统优化问题。
            </p>
            <p class="pub-buttons">
              <a href="https://ojs.aaai.org/index.php/AAAI/article/view/34453" target="_blank" rel="noopener">Paper</a>
            </p>
          </div>
        </article>

        <article class="publication-item publication-item--text-only">
          <div class="publication-body">
            <h3>Making Activation Sparsity Executable in Grouped Low-Bit LLMs</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong> et al.</p>
            <p class="pub-meta">NeurIPS 2026 在投 / CCF-A / 一作</p>
            <p>
              针对分组低比特 LLM 中激活稀疏理论可省算、实际难加速的落差，提出 group-aligned sparse decoding，结合校准式稀疏规划、在线残差选择与融合低比特算子，把稀疏性落到端到端 decode 吞吐提升。
            </p>
          </div>
        </article>

        <article class="publication-item publication-item--text-only">
          <div class="publication-body">
            <h3>Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution</h3>
            <p class="publication-authors">Yuhua Zhou*, Shichao Weng*, <strong>Changhai Zhou</strong>*, Yuhan Wu, Qian Qiao, Jun Gao, Fei Yang†, Aimin Pan†</p>
            <p class="pub-meta">ACL 2026 / CCF-A</p>
            <p>
              面向 token 级计算冗余和固定近似策略难以兼顾质量/速度的问题，提出动态低秩替代推理框架，让 attention/FFN 在 full /
              low-rank / skip 路径间自适应切换，并以 hybrid KV cache 支撑低开销决策。
            </p>
          </div>
        </article>
      </div>
    </div>

    <div class="publication-group">
      <h2>模型压缩与参数高效适配</h2>

      <div class="publication-list">
        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/llm-compression-global-rank-sparsity-main.png' | relative_url }}" alt="Main figure for Large Language Model Compression with Global Rank and Sparsity Optimization">
          <div class="publication-body">
            <h3>Large Language Model Compression with Global Rank and Sparsity Optimization</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Qian Qiao, Yuhua Zhou, Yuxin Wu, Shichao Weng, Weizhong Zhang, Cheng Jin</p>
            <p class="pub-meta">ICLR 2026 / CCF-A / 一作</p>
            <p>
              针对 LLM 压缩中低秩与稀疏常被独立分配、忽略跨层冗余与二者交互的问题，提出 RPCA + Bernoulli global allocation
              两阶段框架；在全局预算下联合分配 rank 与 sparsity，兼顾可解释性与可落地性，为训练无关压缩提供更系统的层级分配范式。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/qr-adaptor-mixed-precision-main.png' | relative_url }}" alt="Main figure for QR-Adaptor">
          <div class="publication-body">
            <h3>Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Shiyang Zhang, Yuhua Zhou, Qian Qiao, Jun Gao, Shichao Weng, Weizhong Zhang, Cheng Jin</p>
            <p class="pub-meta">ACL 2026 / CCF-A / 一作</p>
            <p>
              针对 4-bit 微调中量化 fidelity 与 LoRA plasticity 相互耦合但常被分开调参的问题，提出 QR-Adaptor；从语言层级出发联合分配
              frozen weight bit-width 与 adapter rank，在固定显存预算下逼近 16-bit LoRA 基线，为低精度 PEFT 提供结构化分配依据。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2505.03802" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/autoqra-main.png' | relative_url }}" alt="Main figure for AutoQRA">
          <div class="publication-body">
            <h3>AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Shiyang Zhang, Yuhua Zhou, Qian Qiao, Jun Gao, Cheng Jin, Kaizhou Qin, Weizhong Zhang</p>
            <p class="pub-meta">ICML 2026 / CCF-A / 一作</p>
            <p>
              面对混合精度量化和 LoRA rank 组合空间巨大、人工规则难覆盖模型/任务差异的挑战，将每层 bit-width 与 rank 建模为联合离散搜索；用多保真进化搜索和信赖域贝叶斯优化降低搜索成本，给出自动化高效微调方案，减少从经验调参到部署可用之间的试错成本。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2602.22268" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/rankadaptor-main.png' | relative_url }}" alt="Main figure for RankAdaptor">
          <div class="publication-body">
            <h3>RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Shijie Han, Lining Yang, Yuhua Zhou, Xu Cheng, Yibin Wang, Hongguang Li</p>
            <p class="pub-meta">NAACL 2025 / CCF-B / 一作</p>
            <p>
              针对结构化剪枝后 LLM 各层容量受损不均、统一 rank 难以恢复性能的问题，提出分层动态 rank 分配和性能建模；在离线元学习与在线增量更新之间折中，把剪枝后的恢复微调从均匀补偿推进到按层诊断和按需适配。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2406.15734" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/qpruner-main.png' | relative_url }}" alt="Main figure for QPruner">
          <div class="publication-body">
            <h3>QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</h3>
            <p class="publication-authors"><strong>Changhai Zhou</strong>, Yuhua Zhou, Shijie Han, Qian Qiao, Hongguang Li</p>
            <p class="pub-meta">NAACL 2025 / CCF-B / 一作</p>
            <p>
              针对结构化剪枝进一步叠加量化时精度损失难预测的问题，将 layer-wise mixed precision 与 Bayesian refinement
              结合；把剪枝后模型的位宽分配从启发式选择转化为概率决策，使压缩率、显存和精度之间的取舍更可控，也更适合跨模型迁移。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/bslora-main.png' | relative_url }}" alt="Main figure for BSLoRA">
          <div class="publication-body">
            <h3>BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</h3>
            <p class="publication-authors">Yuhua Zhou, Ruifeng Li, <strong>Changhai Zhou</strong>, Fei Yang, Aimin Pan</p>
            <p class="pub-meta">ICML 2025 / CCF-A / 二作</p>
            <p>
              针对 LoRA 参数效率仍受层内/层间重复表达限制的问题，引入 intra-layer 与 inter-layer sharing 机制；在尽量保持适配能力的同时复用低秩参数，说明 adapter 本身也存在可压缩结构，为 LoRA 结构设计提供轻量改造方向。
            </p>
            <p class="pub-buttons">
              <a href="https://proceedings.mlr.press/v267/zhou25k.html" target="_blank" rel="noopener">PMLR</a>
            </p>
          </div>
        </article>

        <article class="publication-item publication-item--text-only">
          <div class="publication-body">
            <h3>LaRA: Layer-wise Rank Allocation for Efficient Fine-Tuning of Pruned Large Language Models</h3>
            <p class="publication-authors">Yuhua Zhou, <strong>Changhai Zhou</strong>, Shiyang Zhang, Fei Yang, Yi Zhang, Aimin Pan</p>
            <p class="pub-meta">IP&amp;M / 一区 top / 二作</p>
            <p>
              面向剪枝 LLM 微调预算有限、各层恢复需求差异大的问题，提出 layer-wise rank allocation；将有限 LoRA 参数投向更关键层，帮助剪枝模型在训练成本受限时更有效恢复能力，也为后续剪枝模型的 rank 分配研究提供早期实证依据。
            </p>
            <p class="pub-buttons">
              <a href="https://doi.org/10.1016/j.ipm.2025.104538" target="_blank" rel="noopener">DOI</a>
            </p>
          </div>
        </article>
      </div>
    </div>

    <div class="publication-group">
      <h2>多模态生成模型</h2>

      <div class="publication-list">
        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/soulx-flashhead-main.png' | relative_url }}" alt="Main figure for SoulX-FlashHead">
          <div class="publication-body">
            <h3>SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads</h3>
            <p class="publication-authors">Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, <strong>Changhai Zhou</strong>, Shunshun Yin, Siyuan Liu</p>
            <p class="pub-meta">Technical Report / Core Contributor</p>
            <p>
              面向长时实时数字人生成中音频驱动、身份一致性与长序列漂移难以兼顾的问题，参与 1.3B streaming talking-head
              模型；结合 streaming-aware spatiotemporal pre-training、audio context caching 与 oracle-guided distillation，把多模态生成从离线短片段推进到低延迟连续交互场景。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2602.07449" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>

        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/object-coherence-main.png' | relative_url }}" alt="Main figure for Enhancing Object Coherence in Layout-to-Image Synthesis">
          <div class="publication-body">
            <h3>Enhancing Object Coherence in Layout-to-Image Synthesis</h3>
            <p class="publication-authors">Yibin Wang, <strong>Changhai Zhou</strong>, Honghui Xu</p>
            <p class="pub-meta">ICME 2025 / CCF-B / 二作</p>
            <p>
              针对 layout-to-image 中对象语义错配、局部形变和物理关系不一致的问题，结合全局语义融合与自相似一致性注意力；让布局约束更稳定地传递到扩散生成过程，提升可控多模态生成的对象一致性，服务于更可编辑、更可靠的视觉内容生成。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2311.10522" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>
      </div>
    </div>

    <div class="publication-group">
      <h2>评测与代码推理</h2>

      <div class="publication-list">
        <article class="publication-item">
          <img class="publication-thumb" src="{{ '/images/papers/core-benchmark-main.png' | relative_url }}" alt="Main figure for CoRE code reasoning benchmark">
          <div class="publication-body">
            <h3>CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction</h3>
            <p class="publication-authors">Jun Gao, Yun Peng, Qian Qiao, <strong>Changhai Zhou</strong>, Yuhua Zhou, Shiyang Zhang, Shichao Weng, Zhenchang Xing, Xiaoxue Ren</p>
            <p class="pub-meta">ACL 2026 / CCF-A</p>
            <p>
              针对代码推理评测过度依赖最终输出、难以区分真实推理与表面执行的问题，构建细粒度 benchmark；从实现不变性和过程透明性刻画模型行为，把评测从答案正确性推进到推理过程诊断，为代码 LLM 的训练迭代提供更可解释的信号。
            </p>
            <p class="pub-buttons">
              <a href="https://arxiv.org/abs/2604.25399" target="_blank" rel="noopener">arXiv</a>
            </p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section id="contact" class="home-section">
    <h1>Contact</h1>

    <p>
      Feel free to reach out by <a href="mailto:{{ site.author.email }}">email</a>. You can also find my publication
      list on <a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a> and code on
      <a href="https://github.com/manlenzzz" target="_blank" rel="noopener">GitHub</a>.
    </p>
  </section>
</div>
