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
        with current interests in structured compression, parameter-efficient adaptation, and adaptive inference.
      </p>
      <p class="hero-lead" data-lang="zh">
        我是复旦大学博士生，主要研究高效且可部署的大语言模型，当前关注结构化压缩、参数高效适配，以及自适应推理。
      </p>

      <p class="hero-note" data-lang="en">
        A recurring theme in my work is simple: efficiency methods should translate into real memory savings and real inference benefits,
        not only cleaner sparsity numbers in a figure.
      </p>
      <p class="hero-note" data-lang="zh">
        我的一条持续研究主线很直接：高效化方法应该真正带来显存节省和推理收益，而不只是停留在图表里好看的稀疏指标。
      </p>

      <div class="hero-actions">
        <a class="home-button home-button--primary" href="#publications">
          <span data-lang="en">Publications</span>
          <span data-lang="zh">论文列表</span>
        </a>
        <a class="home-button" href="{{ site.author.googlescholar }}" target="_blank" rel="noopener">Google Scholar</a>
        <a class="home-button" href="https://github.com/manlenzzz" target="_blank" rel="noopener">GitHub</a>
        <a class="home-button" href="mailto:{{ site.author.email }}">Email</a>
      </div>

      <div class="hero-meta">
        <div class="meta-card">
          <span data-lang="en">Focus</span>
          <span data-lang="zh">方向</span>
          <strong data-lang="en">LLM compression, PEFT, adaptive inference</strong>
          <strong data-lang="zh">大模型压缩、参数高效微调、自适应推理</strong>
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
      <h2 data-lang="en">Efficient large models for real systems.</h2>
      <h2 data-lang="zh">面向真实系统的大模型高效化。</h2>
      <p data-lang="en">
        My recent work lies at the intersection of compression, efficient adaptation, and budget-aware inference for large language models.
        I am particularly interested in methods that co-design these components instead of optimizing them in isolation.
      </p>
      <p data-lang="zh">
        我近期的工作位于大语言模型压缩、高效适配和预算感知推理的交叉点，尤其关注把这些模块联合起来设计，而不是彼此割裂地分别优化。
      </p>
    </div>

    <div class="research-grid">
      <article class="research-card">
        <h3 data-lang="en">Compression With Real Memory Gains</h3>
        <h3 data-lang="zh">真正带来内存收益的压缩</h3>
        <p data-lang="en">
          I study structured pruning and quantization strategies that can reduce actual memory cost while keeping downstream quality as stable as possible.
        </p>
        <p data-lang="zh">
          我关注能够真正降低内存开销的结构化剪枝与量化方法，同时尽可能保持下游任务性能稳定。
        </p>
      </article>

      <article class="research-card">
        <h3 data-lang="en">Efficient Adaptation After Compression</h3>
        <h3 data-lang="zh">压缩后的高效适配</h3>
        <p data-lang="en">
          A second line of work explores low-rank adaptation, mixed precision, and layer-wise allocation so compressed models can still be tuned effectively.
        </p>
        <p data-lang="zh">
          第二条主线聚焦低秩适配、混合精度和层级分配，使压缩后的模型依然能够被高效而稳定地微调。
        </p>
      </article>

      <article class="research-card">
        <h3 data-lang="en">Budget-Aware Inference</h3>
        <h3 data-lang="zh">预算感知推理</h3>
        <p data-lang="en">
          I am also interested in dynamic sparsity and adaptive computation methods that better trade off inference efficiency and model quality under practical budgets.
        </p>
        <p data-lang="zh">
          我也关注动态稀疏与自适应计算，希望在实际预算约束下更好地平衡推理效率与模型效果。
        </p>
      </article>
    </div>
  </section>

  <section class="homepage-section" id="publications">
    <div class="section-heading">
      <p class="section-kicker" data-lang="en">Publications</p>
      <p class="section-kicker" data-lang="zh">论文列表</p>
      <h2 data-lang="en">A manually curated publication list.</h2>
      <h2 data-lang="zh">手动维护的论文列表。</h2>
      <p data-lang="en">
        The list below covers my recent work around large language model compression, parameter-efficient adaptation, and adaptive inference.
        For the most up-to-date version, please also see my Google Scholar profile.
      </p>
      <p data-lang="zh">
        下面是我近期围绕大语言模型压缩、参数高效适配与自适应推理的论文。最新与最完整的版本也可参考我的 Google Scholar 页面。
      </p>
    </div>

    <div class="year-blocks">
      <div class="year-block">
        <h3>2026</h3>
        <ul class="publication-list">
          <li>
            <span class="pub-title">Large Language Model Compression with Global Rank and Sparsity Optimization</span>
            <span class="pub-meta">ICLR 2026 · CCF-A · First author</span>
            <span class="pub-desc" data-lang="en">A two-stage LLM compression method that jointly optimizes low-rank and sparse components across layers, better handling their interaction and preserving accuracy under stronger compression.</span>
            <span class="pub-desc" data-lang="zh">提出两阶段 LLM 压缩方法，全局联合优化各层低秩与稀疏组件，更好处理低秩与稀疏之间的交互，在更强压缩下保持模型精度。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</span>
            <span class="pub-meta">ACL 2026 · CCF-A · First author</span>
            <span class="pub-desc" data-lang="en">Proposes QR-Adaptor, which jointly allocates per-layer quantization bitwidth and LoRA rank guided by linguistic hierarchies, approaching the 16-bit baseline under a 4-bit budget.</span>
            <span class="pub-desc" data-lang="zh">提出 QR-Adaptor，从语言层级出发联合分配各层量化位宽与 LoRA 秩，在 4-bit 预算下接近 16-bit 基线。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03802" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution</span>
            <span class="pub-meta">ACL 2026 · CCF-A · Co-first author</span>
            <span class="pub-desc" data-lang="en">A dynamic low-rank substitution inference framework where attention and FFN adaptively choose full, low-rank, or skip paths per token, combined with a hybrid KV cache to cut FLOPs.</span>
            <span class="pub-desc" data-lang="zh">提出动态低秩替代推理框架，使 attention 和 FFN 按 token 自适应选择全参、低秩或跳过路径，并结合混合 KV Cache 降低 FLOPs。</span>
          </li>
          <li>
            <span class="pub-title">AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</span>
            <span class="pub-meta">ICML 2026 · CCF-A · First author</span>
            <span class="pub-desc" data-lang="en">Jointly optimizes per-layer bitwidth and LoRA rank for mixed-precision fine-tuning, combining multi-fidelity evolutionary search with trust-region Bayesian optimization to approach full-precision quality.</span>
            <span class="pub-desc" data-lang="zh">在混合量化微调中联合优化每层位宽与 LoRA 秩，结合多保真进化搜索与信赖域贝叶斯优化逼近全精度性能。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2602.22268" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction</span>
            <span class="pub-meta">ACL 2026 · CCF-A</span>
            <span class="pub-desc" data-lang="en">A fine-grained code reasoning benchmark that evaluates LLMs along implementation invariance and procedural transparency, exposing "surface execution" behaviors in code tasks.</span>
            <span class="pub-desc" data-lang="zh">提出细粒度代码推理评测基准，从实现不变性与过程透明性评估 LLM，揭示模型在代码任务中的“表面执行”问题。</span>
          </li>
          <li>
            <span class="pub-title">Making Activation Sparsity Executable in Grouped Low-Bit LLMs</span>
            <span class="pub-meta">NeurIPS 2026 (under review) · CCF-A · First author</span>
            <span class="pub-desc" data-lang="en">A group-aligned sparse decoding method combining calibration-based sparsity planning, online residual selection, and fused low-bit kernels, delivering up to 1.8× end-to-end decode throughput on Qwen3/Llama-3.1.</span>
            <span class="pub-desc" data-lang="zh">提出组对齐稀疏解码方法，结合校准式稀疏规划、在线残差选择与融合低比特算子，使激活稀疏在分组量化模型上可执行；在 Qwen3/Llama-3.1 上端到端 decode 吞吐最高提升 1.8×。</span>
          </li>
          <li>
            <span class="pub-title">LaRA: Layer-wise Rank Allocation for Efficient Fine-Tuning of Pruned Large Language Models</span>
            <span class="pub-meta">Information Processing &amp; Management · SCI Q1 (top) · Second author</span>
            <span class="pub-desc" data-lang="en">Allocates fine-tuning parameters across layers of pruned models, recovering performance more effectively while keeping training efficient.</span>
            <span class="pub-desc" data-lang="zh">合理调配剪枝模型各层的微调参数，在保证高效训练的同时更好地恢复模型性能。</span>
          </li>
          <li>
            <span class="pub-title">SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads</span>
            <span class="pub-meta">Technical Report · Core contributor</span>
            <span class="pub-desc" data-lang="en">A unified 1.3B real-time streaming talking-head framework that uses Oracle-guided bidirectional distillation to mitigate long-sequence drift; the Lite variant runs at 96 FPS on a 4090.</span>
            <span class="pub-desc" data-lang="zh">参与统一 1.3B 实时流式数字人生成框架，利用 Oracle-guided 双向蒸馏缓解长序列漂移，Lite 版在 4090 上达到 96 FPS。</span>
          </li>
          <li>
            <span class="pub-title">MinT: Managed Infrastructure for Training and Serving Millions of LLMs</span>
            <span class="pub-meta">Technical Report · Core contributor</span>
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
            <span class="pub-meta">AAAI 2025 · CCF-A · First author</span>
            <span class="pub-desc" data-lang="en">A dynamic operator selection and scheduling method for multi-tenant LoRA serving, improving online inference throughput and reducing serving latency.</span>
            <span class="pub-desc" data-lang="zh">面向多租户 LoRA 服务，提出动态算子选择与调度方法，提升在线推理吞吐并降低服务时延。</span>
          </li>
          <li>
            <span class="pub-title">RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs</span>
            <span class="pub-meta">NAACL 2025 · CCF-B · First author</span>
            <span class="pub-desc" data-lang="en">Hierarchical rank allocation and performance modeling for structurally pruned LLMs, enabling more efficient low-rank fine-tuning.</span>
            <span class="pub-desc" data-lang="zh">针对结构化剪枝 LLM，提出分层 rank 分配与性能建模方法，实现更高效的低秩微调。</span>
          </li>
          <li>
            <span class="pub-title">QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</span>
            <span class="pub-meta">NAACL 2025 · CCF-B · First author</span>
            <span class="pub-desc" data-lang="en">A probabilistic decision quantization strategy for structurally pruned LLMs, achieving a better trade-off between compression ratio and accuracy.</span>
            <span class="pub-desc" data-lang="zh">提出面向结构化剪枝模型的概率决策量化策略，在压缩率与模型精度之间取得更优平衡。</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</span>
            <span class="pub-meta">ICML 2025 · CCF-A · Second author</span>
            <span class="pub-desc" data-lang="en">Improves LoRA through intra-layer and inter-layer parameter sharing, further reducing fine-tuning parameters while preserving performance.</span>
            <span class="pub-desc" data-lang="zh">通过层内与层间参数共享改进 LoRA 结构，在保持性能的同时进一步减少微调参数量。</span>
          </li>
          <li>
            <span class="pub-title">Enhancing Object Coherence in Layout-to-Image Synthesis</span>
            <span class="pub-meta">ICME 2025 · CCF-B · Second author</span>
            <span class="pub-desc" data-lang="en">A diffusion-based layout-to-image framework combining global semantic fusion (GSF) and self-similarity coherence attention (SCA), improving object semantic and physical coherence.</span>
            <span class="pub-desc" data-lang="zh">结合全局语义融合（GSF）与自相似一致性注意力（SCA）的扩散式布局生成框架，提升对象语义与物理一致性。</span>
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
