---
permalink: /
title: ""
excerpt: ""
author_profile: false
classes: wide
redirect_from:
  - /about/
  - /about.html
  - /homepage/
---

<main class="homepage">
  <section class="profile-hero" id="about">
    <div class="hero-header-row">
      <a class="hero-nameplate" href="{{ '/' | relative_url }}#about">Changhai Zhou</a>
      <div class="language-switch" role="group" aria-label="Language switch">
        <button type="button" class="language-button" data-language-button="en">EN</button>
        <button type="button" class="language-button" data-language-button="zh">中文</button>
      </div>
    </div>

    <div class="hero-layout">
      <div class="hero-copy">
        <p class="hero-label" data-lang="en">PhD student, efficient large language models</p>
        <p class="hero-label" data-lang="zh">博士生，大语言模型高效化</p>

        <h1 data-lang="en">Changhai Zhou</h1>
        <h1 data-lang="zh">周昌海</h1>

        <p class="hero-lead" data-lang="en">
          I work on making large language models cheaper to train, adapt, and serve without losing the behavior that matters.
        </p>
        <p class="hero-lead" data-lang="zh">
          我的研究关注如何降低大语言模型训练、适配与服务成本，同时尽量保留真正重要的模型行为。
        </p>

        <div class="hero-actions">
          <a class="home-button home-button--primary" href="#publications">
            <span data-lang="en">Read papers</span>
            <span data-lang="zh">查看论文</span>
          </a>
          <a class="home-button" href="#research-notes">
            <span data-lang="en">Experiment notes</span>
            <span data-lang="zh">实验札记</span>
          </a>
          <a class="home-button" href="mailto:{{ site.author.email }}">Email</a>
        </div>
      </div>

      <aside class="hero-side" aria-label="Profile summary">
        <div class="hero-photo-shell">
          <img class="hero-photo" src="{{ '/images/me.png' | relative_url }}" alt="Portrait of Changhai Zhou">
        </div>
        <dl class="hero-meta">
          <div class="meta-card">
            <dt data-lang="en">Focus</dt>
            <dt data-lang="zh">方向</dt>
            <dd data-lang="en">Compression / PEFT / adaptive inference / serving</dd>
            <dd data-lang="zh">模型压缩 / 参数高效微调 / 自适应推理 / 服务系统</dd>
          </div>
          <div class="meta-card">
            <dt data-lang="en">Affiliation</dt>
            <dt data-lang="zh">机构</dt>
            <dd>Fudan University</dd>
          </div>
          <div class="meta-card">
            <dt data-lang="en">Links</dt>
            <dt data-lang="zh">链接</dt>
            <dd><a href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a> / <a href="https://github.com/manlenzzz" target="_blank" rel="noopener">GitHub</a></dd>
          </div>
        </dl>
      </aside>
    </div>
  </section>

  <section class="homepage-section research-section" id="research">
    <div class="section-heading">
      <h2 data-lang="en">Research interests</h2>
      <h2 data-lang="zh">研究兴趣</h2>
      <p data-lang="en">
        I care about the practical boundary where compression, adaptation, and deployment decisions change model behavior.
      </p>
      <p data-lang="zh">
        我关注压缩、适配与部署决策真正改变模型行为的边界，而不只是指标上的局部改进。
      </p>
    </div>

    <ul class="interest-list">
      <li>
        <span data-lang="en">Model compression and quantization</span>
        <span data-lang="zh">模型压缩与量化</span>
      </li>
      <li>
        <span data-lang="en">Parameter-efficient fine-tuning</span>
        <span data-lang="zh">参数高效微调</span>
      </li>
      <li>
        <span data-lang="en">Efficient and adaptive inference</span>
        <span data-lang="zh">高效与自适应推理</span>
      </li>
      <li>
        <span data-lang="en">LLM serving systems</span>
        <span data-lang="zh">大模型服务系统</span>
      </li>
      <li>
        <span data-lang="en">Evaluation and reasoning of LLMs</span>
        <span data-lang="zh">大模型评测与推理能力</span>
      </li>
      <li>
        <span data-lang="en">Multimodal and generative models</span>
        <span data-lang="zh">多模态与生成模型</span>
      </li>
    </ul>
  </section>

  <section class="homepage-section notes-section" id="research-notes">
    <div class="section-heading">
      <h2 data-lang="en">Experiment notes worth keeping</h2>
      <h2 data-lang="zh">值得留下来的实验记录</h2>
      <p data-lang="en">
        Negative results and diagnostic runs, written so the next paper does not repeat the same mistake.
      </p>
      <p data-lang="zh">
        这里记录负结果和诊断实验，目标是让下一篇论文不用重复同一个错误。
      </p>
    </div>

    <a class="note-index-row" href="{{ '/notes/damage-clock-negative-result/' | relative_url }}">
      <span class="note-index-date">16 Jun 2026</span>
      <span class="note-index-main">
        <strong>When a Better Clock Is Not a Better Sampler</strong>
        <span data-lang="en">A fixed-checkpoint consistency-model diagnostic where a post-hoc damage clock loses to the native skip rule.</span>
        <span data-lang="zh">一个固定 checkpoint 的 consistency model 诊断实验：后验 damage clock 输给了原生 skip 规则。</span>
      </span>
      <span class="note-index-visual">
        <img src="{{ '/notes/damage-clock-negative-result/figures/fig_result_delta_revised.svg' | relative_url }}" alt="FID delta plot for the damage-clock diagnostic">
      </span>
    </a>
  </section>

  <section class="homepage-section publications-section" id="publications">
    <div class="section-heading">
      <h2 data-lang="en">Publications</h2>
      <h2 data-lang="zh">论文</h2>
      <p data-lang="en">
        A manually curated list. Google Scholar has the broader citation view.
      </p>
      <p data-lang="zh">
        这里是手动维护的论文列表，更完整的引用信息见 Google Scholar。
      </p>
    </div>

    <div class="year-blocks">
      <div class="year-block">
        <h3>2026</h3>
        <ul class="publication-list">
          <li>
            <span class="pub-title">Large Language Model Compression with Global Rank and Sparsity Optimization</span>
            <span class="pub-meta">ICLR 2026 | CCF-A | First author</span>
            <span class="pub-desc" data-lang="en">A two-stage LLM compression method that jointly optimizes low-rank and sparse components across layers, better handling their interaction and preserving accuracy under stronger compression.</span>
            <span class="pub-desc" data-lang="zh">提出两阶段 LLM 压缩方法，全局联合优化各层低秩与稀疏组件，更好处理低秩与稀疏之间的交互，在更强压缩下保持模型精度。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</span>
            <span class="pub-meta">ACL 2026 | CCF-A | First author</span>
            <span class="pub-desc" data-lang="en">Proposes QR-Adaptor, which jointly allocates per-layer quantization bitwidth and LoRA rank guided by linguistic hierarchies, approaching the 16-bit baseline under a 4-bit budget.</span>
            <span class="pub-desc" data-lang="zh">提出 QR-Adaptor，从语言层级出发联合分配各层量化位宽与 LoRA 秩，在 4-bit 预算下接近 16-bit 基线。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03802" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution</span>
            <span class="pub-meta">ACL 2026 | CCF-A | Co-first author</span>
            <span class="pub-desc" data-lang="en">A dynamic low-rank substitution inference framework where attention and FFN adaptively choose full, low-rank, or skip paths per token, combined with a hybrid KV cache to cut FLOPs.</span>
            <span class="pub-desc" data-lang="zh">提出动态低秩替代推理框架，使 attention 和 FFN 按 token 自适应选择全参、低秩或跳过路径，并结合混合 KV Cache 降低 FLOPs。</span>
          </li>
          <li>
            <span class="pub-title">AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</span>
            <span class="pub-meta">ICML 2026 | CCF-A | First author</span>
            <span class="pub-desc" data-lang="en">Jointly optimizes per-layer bitwidth and LoRA rank for mixed-precision fine-tuning, combining multi-fidelity evolutionary search with trust-region Bayesian optimization to approach full-precision quality.</span>
            <span class="pub-desc" data-lang="zh">在混合量化微调中联合优化每层位宽与 LoRA 秩，结合多保真进化搜索与信赖域贝叶斯优化逼近全精度性能。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2602.22268" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction</span>
            <span class="pub-meta">ACL 2026 | CCF-A</span>
            <span class="pub-desc" data-lang="en">A fine-grained code reasoning benchmark that evaluates LLMs along implementation invariance and procedural transparency, exposing "surface execution" behaviors in code tasks.</span>
            <span class="pub-desc" data-lang="zh">提出细粒度代码推理评测基准，从实现不变性与过程透明性评估 LLM，揭示模型在代码任务中的“表面执行”问题。</span>
          </li>
          <li>
            <span class="pub-title">Making Activation Sparsity Executable in Grouped Low-Bit LLMs</span>
            <span class="pub-meta">NeurIPS 2026 under review | CCF-A | First author</span>
            <span class="pub-desc" data-lang="en">A group-aligned sparse decoding method combining calibration-based sparsity planning, online residual selection, and fused low-bit kernels, delivering up to 1.8× end-to-end decode throughput on Qwen3/Llama-3.1.</span>
            <span class="pub-desc" data-lang="zh">提出组对齐稀疏解码方法，结合校准式稀疏规划、在线残差选择与融合低比特算子，使激活稀疏在分组量化模型上可执行；在 Qwen3/Llama-3.1 上端到端 decode 吞吐最高提升 1.8×。</span>
          </li>
          <li>
            <span class="pub-title">LaRA: Layer-wise Rank Allocation for Efficient Fine-Tuning of Pruned Large Language Models</span>
            <span class="pub-meta">Information Processing &amp; Management | SCI Q1 (top) | Second author</span>
            <span class="pub-desc" data-lang="en">Allocates fine-tuning parameters across layers of pruned models, recovering performance more effectively while keeping training efficient.</span>
            <span class="pub-desc" data-lang="zh">合理调配剪枝模型各层的微调参数，在保证高效训练的同时更好地恢复模型性能。</span>
          </li>
          <li>
            <span class="pub-title">SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads</span>
            <span class="pub-meta">Technical Report | Core contributor</span>
            <span class="pub-desc" data-lang="en">A unified 1.3B real-time streaming talking-head framework that uses Oracle-guided bidirectional distillation to mitigate long-sequence drift; the Lite variant runs at 96 FPS on a 4090.</span>
            <span class="pub-desc" data-lang="zh">参与统一 1.3B 实时流式数字人生成框架，利用 Oracle-guided 双向蒸馏缓解长序列漂移，Lite 版在 4090 上达到 96 FPS。</span>
          </li>
          <li>
            <span class="pub-title">MinT: Managed Infrastructure for Training and Serving Millions of LLMs</span>
            <span class="pub-meta">Technical Report | Core contributor</span>
            <span class="pub-desc" data-lang="en">An LLM fine-tuning and deployment management system that supports training, serving, exporting, and rollback for large base models and LoRA adapters at scale.</span>
            <span class="pub-desc" data-lang="zh">参与大模型微调与部署管理系统设计，支持大规模 base model 与 LoRA adapter 的训练、服务、导出和回滚流程。</span>
          </li>
        </ul>
      </div>

      <div class="year-block">
        <h3>2025</h3>
        <ul class="publication-list">
          <li>
            <span class="pub-title">Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving</span>
            <span class="pub-meta">AAAI 2025 | CCF-A | First author</span>
            <span class="pub-desc" data-lang="en">A dynamic operator selection and scheduling method for multi-tenant LoRA serving, improving online inference throughput and reducing serving latency.</span>
            <span class="pub-desc" data-lang="zh">面向多租户 LoRA 服务，提出动态算子选择与调度方法，提升在线推理吞吐并降低服务时延。</span>
          </li>
          <li>
            <span class="pub-title">RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs</span>
            <span class="pub-meta">NAACL 2025 | CCF-B | First author</span>
            <span class="pub-desc" data-lang="en">Hierarchical rank allocation and performance modeling for structurally pruned LLMs, enabling more efficient low-rank fine-tuning.</span>
            <span class="pub-desc" data-lang="zh">针对结构化剪枝 LLM，提出分层 rank 分配与性能建模方法，实现更高效的低秩微调。</span>
          </li>
          <li>
            <span class="pub-title">QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</span>
            <span class="pub-meta">NAACL 2025 | CCF-B | First author</span>
            <span class="pub-desc" data-lang="en">A probabilistic decision quantization strategy for structurally pruned LLMs, achieving a better trade-off between compression ratio and accuracy.</span>
            <span class="pub-desc" data-lang="zh">提出面向结构化剪枝模型的概率决策量化策略，在压缩率与模型精度之间取得更优平衡。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</span>
            <span class="pub-meta">ICML 2025 | CCF-A | Second author</span>
            <span class="pub-desc" data-lang="en">Improves LoRA through intra-layer and inter-layer parameter sharing, further reducing fine-tuning parameters while preserving performance.</span>
            <span class="pub-desc" data-lang="zh">通过层内与层间参数共享改进 LoRA 结构，在保持性能的同时进一步减少微调参数量。</span>
          </li>
          <li>
            <span class="pub-title">Enhancing Object Coherence in Layout-to-Image Synthesis</span>
            <span class="pub-meta">ICME 2025 | CCF-B | Second author</span>
            <span class="pub-desc" data-lang="en">A diffusion-based layout-to-image framework combining global semantic fusion (GSF) and self-similarity coherence attention (SCA), improving object semantic and physical coherence.</span>
            <span class="pub-desc" data-lang="zh">结合全局语义融合（GSF）与自相似一致性注意力（SCA）的扩散式布局生成框架，提升对象语义与物理一致性。</span>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="homepage-section contact-section" id="contact">
    <div class="section-heading">
      <h2 data-lang="en">Contact</h2>
      <h2 data-lang="zh">联系</h2>
      <p data-lang="en">Email is the best path for research questions, collaborations, and paper discussions.</p>
      <p data-lang="zh">如果是研究问题、合作或论文讨论，邮件是最合适的联系方式。</p>
    </div>

    <div class="contact-grid">
      <a class="contact-card" href="mailto:{{ site.author.email }}">
        <span class="contact-label" data-lang="en">Email</span>
        <span class="contact-label" data-lang="zh">邮箱</span>
        <strong>{{ site.author.email }}</strong>
      </a>

      <a class="contact-card" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">
        <span class="contact-label">Google Scholar</span>
        <strong data-lang="en">Publication list and citation profile</strong>
        <strong data-lang="zh">论文列表与引用信息</strong>
      </a>

      <a class="contact-card" href="https://github.com/manlenzzz" target="_blank" rel="noopener">
        <span class="contact-label">GitHub</span>
        <strong>@manlenzzz</strong>
      </a>
    </div>
  </section>
</main>
