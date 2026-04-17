---
permalink: /
title: ""
excerpt: ""
author_profile: false
classes: wide
redirect_from:
  - /about/
  - /about.html
---

<div class="homepage">
  <section class="profile-hero" id="about">
    <div class="hero-copy">
      <div class="hero-header-row">
        <div>
          <p class="section-kicker" data-lang="en">Academic Homepage</p>
          <p class="section-kicker" data-lang="zh">学术主页</p>
        </div>
        <div class="language-switch" role="group" aria-label="Language switch">
          <button type="button" class="language-button" data-language-button="en">EN</button>
          <button type="button" class="language-button" data-language-button="zh">中文</button>
        </div>
      </div>

      <h1 data-lang="en">Changhai Zhou</h1>
      <h1 data-lang="zh">周昌海</h1>

      <p class="hero-lead" data-lang="en">
        I am a PhD candidate at Fudan University working on efficient and deployable large language models,
        with current interests in model compression, parameter-efficient adaptation, model serving, and adaptive inference.
      </p>
      <p class="hero-lead" data-lang="zh">
        我是复旦大学博士生，主要研究高效且可部署的大语言模型，当前关注模型压缩、参数高效适配、模型服务，以及自适应推理。
      </p>

      <p class="hero-note" data-lang="en">
        My recent work focuses on making large models cheaper to train, tune, serve, and deploy under real memory and latency constraints.
      </p>
      <p class="hero-note" data-lang="zh">
        我近期的工作主要围绕如何在真实显存和时延约束下，让大模型的训练、微调、服务和部署都更高效。
      </p>

      <div class="hero-actions">
        <a class="home-button home-button--primary" href="#selected-publications">
          <span data-lang="en">Selected Publications</span>
          <span data-lang="zh">代表性论文</span>
        </a>
        <a class="home-button" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a>
        <a class="home-button" href="https://github.com/manlenzzz" target="_blank" rel="noopener">GitHub</a>
        <a class="home-button" href="mailto:{{ site.author.email }}">Email</a>
      </div>

      <div class="hero-meta">
        <div class="meta-card">
          <span data-lang="en">Focus</span>
          <span data-lang="zh">方向</span>
          <strong data-lang="en">LLM compression, PEFT, model serving, adaptive inference</strong>
          <strong data-lang="zh">大模型压缩、参数高效微调、模型服务、自适应推理</strong>
        </div>
        <div class="meta-card">
          <span data-lang="en">Affiliation</span>
          <span data-lang="zh">机构</span>
          <strong>Fudan University</strong>
        </div>
        <div class="meta-card">
          <span data-lang="en">Location</span>
          <span data-lang="zh">地点</span>
          <strong>Shanghai, China</strong>
        </div>
      </div>
    </div>

    <div class="hero-photo-shell">
      <div class="hero-photo-ring"></div>
      <img class="hero-photo" src="{{ '/images/me.png' | relative_url }}" alt="Portrait of Changhai Zhou">
    </div>
  </section>

  <section class="homepage-section" id="research">
    <div class="section-heading">
      <p class="section-kicker" data-lang="en">Research</p>
      <p class="section-kicker" data-lang="zh">研究方向</p>
      <h2 data-lang="en">Efficient large models for training, serving, and deployment.</h2>
      <h2 data-lang="zh">面向训练、服务与部署的大模型高效化。</h2>
      <p data-lang="en">
        My recent work lies at the intersection of compression, efficient adaptation, serving systems, and budget-aware inference for large language models.
        I am particularly interested in methods that optimize the full deployment pipeline rather than a single isolated module.
      </p>
      <p data-lang="zh">
        我近期的工作位于大语言模型压缩、高效适配、服务系统和预算感知推理的交叉点，尤其关注从整体部署链路出发，而不是只优化某个孤立模块的方法设计。
      </p>
    </div>

    <div class="research-grid">
      <article class="research-card">
        <h3 data-lang="en">Compression With Real Memory Gains</h3>
        <h3 data-lang="zh">真正带来内存收益的压缩</h3>
        <p data-lang="en">
          I study structured pruning and quantization strategies that reduce actual memory cost while preserving model quality as much as possible.
        </p>
        <p data-lang="zh">
          我关注能够真正降低内存开销的结构化剪枝与量化方法，同时尽可能保持模型性能稳定。
        </p>
      </article>

      <article class="research-card">
        <h3 data-lang="en">Efficient Adaptation After Compression</h3>
        <h3 data-lang="zh">压缩后的高效适配</h3>
        <p data-lang="en">
          A second line of work explores low-rank adaptation, mixed precision, and hierarchical allocation so compressed models can still be tuned efficiently.
        </p>
        <p data-lang="zh">
          第二条主线聚焦低秩适配、混合精度和分层分配，使压缩后的模型依然能够被高效而稳定地微调。
        </p>
      </article>

      <article class="research-card">
        <h3 data-lang="en">Serving and Adaptive Inference</h3>
        <h3 data-lang="zh">服务与自适应推理</h3>
        <p data-lang="en">
          I am also interested in multi-tenant serving, dynamic operator selection, and adaptive routing under practical latency and budget constraints.
        </p>
        <p data-lang="zh">
          我也关注多租户服务、动态算子选择，以及在实际时延和预算约束下的自适应路由与推理。
        </p>
      </article>
    </div>
  </section>

  <section class="homepage-section" id="selected-publications">
    <div class="section-heading">
      <p class="section-kicker" data-lang="en">Selected Publications</p>
      <p class="section-kicker" data-lang="zh">代表性论文</p>
      <h2 data-lang="en">Representative work on efficient LLMs, model serving, and adaptive inference.</h2>
      <h2 data-lang="zh">围绕高效大模型、模型服务与自适应推理的代表性工作。</h2>
    </div>

    <div class="publication-grid">
      <article class="pub-card pub-card--featured">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">AAAI / CCF-A</span>
          <span class="pub-venue" data-lang="zh">AAAI / CCF-A</span>
          <span class="pub-year" data-lang="en">First author + independent corresponding author</span>
          <span class="pub-year" data-lang="zh">一作+独立通讯</span>
        </div>
        <h3>Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving</h3>
        <p data-lang="en">Dynamic operator selection and scheduling for multi-tenant LoRA serving, improving online throughput while reducing service latency.</p>
        <p data-lang="zh">面向多租户 LoRA 服务，提出动态算子选择与调度方法，提升在线推理吞吐并降低服务时延。</p>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">ICLR / CCF-A</span>
          <span class="pub-venue" data-lang="zh">ICLR / CCF-A</span>
          <span class="pub-year" data-lang="en">First author</span>
          <span class="pub-year" data-lang="zh">一作</span>
        </div>
        <h3>Large Language Model Compression with Global Rank and Sparsity Optimization</h3>
        <p data-lang="en">A two-stage compression framework that jointly optimizes low-rank and sparse components across layers to better preserve performance under stronger compression.</p>
        <p data-lang="zh">提出两阶段的 LLM 压缩方法，在全局范围联合优化各层的低秩组件和稀疏组件，更好处理低秩与稀疏的相互作用，从而在更强压缩下尽量保住模型性能。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">NAACL / CCF-B</span>
          <span class="pub-venue" data-lang="zh">NAACL / CCF-B</span>
          <span class="pub-year" data-lang="en">First author</span>
          <span class="pub-year" data-lang="zh">一作</span>
        </div>
        <h3>RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs</h3>
        <p data-lang="en">Hierarchical rank allocation and performance modeling for structurally pruned LLMs, enabling more efficient low-rank fine-tuning.</p>
        <p data-lang="zh">针对结构化剪枝 LLM，提出分层 rank 分配与性能建模方法，实现更高效的低秩微调。</p>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">NAACL / CCF-B</span>
          <span class="pub-venue" data-lang="zh">NAACL / CCF-B</span>
          <span class="pub-year" data-lang="en">First author</span>
          <span class="pub-year" data-lang="zh">一作</span>
        </div>
        <h3>QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</h3>
        <p data-lang="en">A probabilistic decision quantization strategy for structured pruning that improves the balance between compression ratio and model accuracy.</p>
        <p data-lang="zh">提出面向结构化剪枝模型的概率决策量化策略，在压缩率与模型精度之间取得更优平衡。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">ACL 2026 / CCF-A</span>
          <span class="pub-venue" data-lang="zh">ACL2026 / CCF-A</span>
          <span class="pub-year" data-lang="en">First author</span>
          <span class="pub-year" data-lang="zh">一作</span>
        </div>
        <h3>Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</h3>
        <p data-lang="en">Introduces QR-Adaptor, which jointly allocates quantization bitwidths and LoRA ranks by linguistic hierarchy to approach 16-bit fine-tuning under a 4-bit budget.</p>
        <p data-lang="zh">提出 QR-Adaptor，从语言层级出发联合分配各层量化比特宽度与 LoRA 秩，在有限显存下协调冻结权重保真度与任务适应性，使 4-bit 预算下的微调效果接近 16-bit 基线。</p>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue" data-lang="en">ACL 2026 / CCF-A</span>
          <span class="pub-venue" data-lang="zh">ACL2026 / CCF-A</span>
          <span class="pub-year" data-lang="en">Co-first author</span>
          <span class="pub-year" data-lang="zh">共一</span>
        </div>
        <h3>Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution</h3>
        <p data-lang="en">A dynamic low-rank substitution framework that adaptively switches among full-parameter, low-rank, and skip branches to reduce FLOPs and cache cost.</p>
        <p data-lang="zh">提出动态低秩替代推理框架 Deputy，在注意力层与 FFN 层按 token 自适应选择全参数、低秩近似或跳过分支，并结合基于 LoRA 的最小二乘低秩构造与混合 KV Cache 设计，在尽量保持性能的同时显著降低推理 FLOPs 与缓存开销。</p>
      </article>
    </div>
  </section>

  <section class="homepage-section" id="full-publications">
    <div class="section-heading compact-heading">
      <p class="section-kicker" data-lang="en">Publications</p>
      <p class="section-kicker" data-lang="zh">论文列表</p>
    </div>

    <div class="year-blocks year-blocks--single">
      <div class="year-block">
        <ul class="publication-list publication-list--detailed">
          <li>
            <span class="pub-title">Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving</span>
            <span class="pub-meta" data-lang="en">AAAI / CCF-A / First author + independent corresponding author</span>
            <span class="pub-meta" data-lang="zh">AAAI / CCF-A / 一作+独立通讯</span>
            <p class="pub-summary" data-lang="en">Proposes dynamic operator selection and scheduling for multi-tenant LoRA serving, improving online throughput and reducing service latency.</p>
            <p class="pub-summary" data-lang="zh">面向多租户 LoRA 服务，提出动态算子选择与调度方法，提升在线推理吞吐并降低服务时延。</p>
          </li>
          <li>
            <span class="pub-title">RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs</span>
            <span class="pub-meta" data-lang="en">NAACL / CCF-B / First author</span>
            <span class="pub-meta" data-lang="zh">NAACL / CCF-B / 一作</span>
            <p class="pub-summary" data-lang="en">Proposes hierarchical rank allocation and performance modeling for structurally pruned LLMs, enabling more efficient low-rank fine-tuning.</p>
            <p class="pub-summary" data-lang="zh">针对结构化剪枝 LLM，提出分层 rank 分配与性能建模方法，实现更高效的低秩微调。</p>
          </li>
          <li>
            <span class="pub-title">QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</span>
            <span class="pub-meta" data-lang="en">NAACL / CCF-B / First author</span>
            <span class="pub-meta" data-lang="zh">NAACL / CCF-B / 一作</span>
            <p class="pub-summary" data-lang="en">Introduces a probabilistic decision quantization strategy that better balances compression ratio and model accuracy for structured pruning.</p>
            <p class="pub-summary" data-lang="zh">提出面向结构化剪枝模型的概率决策量化策略，在压缩率与模型精度之间取得更优平衡。</p>
          </li>
          <li>
            <span class="pub-title">Large Language Model Compression with Global Rank and Sparsity Optimization</span>
            <span class="pub-meta" data-lang="en">ICLR / CCF-A / First author</span>
            <span class="pub-meta" data-lang="zh">ICLR / CCF-A / 一作</span>
            <p class="pub-summary" data-lang="en">Presents a two-stage LLM compression method that jointly optimizes low-rank and sparse components across layers to better preserve performance under stronger compression.</p>
            <p class="pub-summary" data-lang="zh">提出两阶段的 LLM 压缩方法，在全局范围联合优化各层的低秩组件和稀疏组件，更好处理低秩与稀疏的相互作用，从而在更强压缩下尽量保住模型性能。</p>
          </li>
          <li>
            <span class="pub-title">BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</span>
            <span class="pub-meta" data-lang="en">ICML / CCF-A / Second author</span>
            <span class="pub-meta" data-lang="zh">ICML / CCF-A / 二作</span>
            <p class="pub-summary" data-lang="en">Improves LoRA with intra-layer and inter-layer sharing, further reducing fine-tuning parameters while maintaining performance.</p>
            <p class="pub-summary" data-lang="zh">通过层内与层间参数共享改进 LoRA 结构，在保持性能的同时进一步减少微调参数量。</p>
          </li>
          <li>
            <span class="pub-title">Enhancing Object Coherence in Layout-to-Image Synthesis</span>
            <span class="pub-meta" data-lang="en">ICME 2025 / CCF-B / Second author</span>
            <span class="pub-meta" data-lang="zh">ICME 2025 / CCF-B / 二作</span>
            <p class="pub-summary" data-lang="en">Combines global semantic fusion and self-similarity consistency attention in a diffusion framework to improve semantic relations and local physical consistency in layout-to-image synthesis.</p>
            <p class="pub-summary" data-lang="zh">提出结合全局语义融合（GSF）与自相似一致性注意力（SCA）的扩散式布局生成框架，同时增强对象间语义关系与局部物理一致性，提升 layout-to-image 合成的生成质量与可控性。</p>
          </li>
          <li>
            <span class="pub-title">Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</span>
            <span class="pub-meta" data-lang="en">ACL 2026 / CCF-A / First author</span>
            <span class="pub-meta" data-lang="zh">ACL2026 / CCF-A / 一作</span>
            <p class="pub-summary" data-lang="en">Introduces QR-Adaptor, which jointly allocates quantization bitwidths and LoRA ranks from linguistic hierarchies to balance frozen-weight fidelity and task adaptability under limited memory.</p>
            <p class="pub-summary" data-lang="zh">提出 QR-Adaptor，从语言层级出发联合分配各层量化比特宽度与 LoRA 秩，在有限显存下协调冻结权重保真度与任务适应性，使 4-bit 预算下的微调效果接近 16-bit 基线。</p>
          </li>
          <li>
            <span class="pub-title">CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction</span>
            <span class="pub-meta" data-lang="en">ACL 2026 / CCF-A</span>
            <span class="pub-meta" data-lang="zh">ACL2026 / CCF-A</span>
            <p class="pub-summary" data-lang="en">Introduces CoRE, a fine-grained code reasoning benchmark that evaluates whether LLMs truly understand execution via implementation invariance and process transparency.</p>
            <p class="pub-summary" data-lang="zh">提出细粒度代码推理评测基准 CoRE，从实现不变性与过程透明性两个维度评估大语言模型是否真正理解代码执行过程，并揭示当前模型在等价实现上的鲁棒性不足以及仅答对最终输出却无法正确追踪中间状态的“表面执行”问题。</p>
          </li>
          <li>
            <span class="pub-title">Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution</span>
            <span class="pub-meta" data-lang="en">ACL 2026 / CCF-A / Co-first author</span>
            <span class="pub-meta" data-lang="zh">ACL2026 / CCF-A / 共一</span>
            <p class="pub-summary" data-lang="en">Proposes a dynamic low-rank substitution framework that adaptively chooses full-parameter, low-rank, or skip branches per token and significantly reduces FLOPs and cache cost.</p>
            <p class="pub-summary" data-lang="zh">提出动态低秩替代推理框架 Deputy，在注意力层与 FFN 层按 token 自适应选择全参数、低秩近似或跳过分支，并结合基于 LoRA 的最小二乘低秩构造与混合 KV Cache 设计，在尽量保持性能的同时显著降低推理 FLOPs 与缓存开销。</p>
          </li>
          <li>
            <span class="pub-title">AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</span>
            <span class="pub-meta" data-lang="en">Under review at ICML 2026 / CCF-A</span>
            <span class="pub-meta" data-lang="zh">ICML2026在投 / CCF-A</span>
            <p class="pub-summary" data-lang="en">Jointly optimizes per-layer quantization bitwidths and LoRA ranks for mixed-precision fine-tuning using multi-fidelity evolutionary search and trust-region Bayesian optimization.</p>
            <p class="pub-summary" data-lang="zh">提出 AutoQRA，在混合量化微调中联合优化每层量化位宽与 LoRA 秩，并结合多保真进化搜索与信赖域贝叶斯优化，在给定内存预算下逼近全精度微调性能。</p>
          </li>
          <li>
            <span class="pub-title">BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Models Inference</span>
            <span class="pub-meta" data-lang="en">Under review at ICML 2026 / CCF-A</span>
            <span class="pub-meta" data-lang="zh">ICML2026在投 / CCF-A</span>
            <p class="pub-summary" data-lang="en">Proposes budget-driven dynamic depth routing with input- and budget-adaptive layer execution, plus first-layer KV cache reuse and budget prediction.</p>
            <p class="pub-summary" data-lang="zh">提出预算驱动的动态深度路由框架，通过决策模块按输入与预算自适应选择执行层，并结合首层 KV Cache 复用与预算预测器，在不同剪枝配置下兼顾推理性能与计算开销。</p>
          </li>
          <li>
            <span class="pub-title">SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads</span>
            <span class="pub-meta" data-lang="en">Technical Report</span>
            <span class="pub-meta" data-lang="zh">Technical Report</span>
            <p class="pub-summary" data-lang="en">Presents a unified 1.3B real-time streaming talking-head framework with streaming-aware spatiotemporal pretraining, temporal audio context caching, and oracle-guided bidirectional distillation.</p>
            <p class="pub-summary" data-lang="zh">提出统一的 1.3B 实时流式数字人生成框架，通过流式感知时空预训练、时序音频上下文缓存与 Oracle-guided 双向蒸馏缓解长序列漂移，在 HDTF/VFHQ 上取得领先结果，Lite 版本单张 RTX 4090 可达 96 FPS。</p>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="homepage-section" id="cv">
    <div class="section-heading compact-heading">
      <p class="section-kicker" data-lang="en">CV</p>
      <p class="section-kicker" data-lang="zh">简历</p>
      <h2 data-lang="en">Please email me for the latest CV.</h2>
      <h2 data-lang="zh">最新简历请通过邮件联系我获取。</h2>
      <p data-lang="en">I am organizing a clean downloadable version for this site.</p>
      <p data-lang="zh">我正在整理适合挂在主页上的简历版本，当前可通过邮件索取最新版。</p>
    </div>
    <div class="hero-actions hero-actions--compact">
      <a class="home-button home-button--primary" href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
      <a class="home-button" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a>
    </div>
  </section>

  <section class="homepage-section" id="contact">
    <div class="section-heading compact-heading">
      <p class="section-kicker" data-lang="en">Contact</p>
      <p class="section-kicker" data-lang="zh">联系</p>
      <h2 data-lang="en">I am happy to discuss research collaborations and related opportunities.</h2>
      <h2 data-lang="zh">欢迎交流研究合作以及相关学术机会。</h2>
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
</div>
