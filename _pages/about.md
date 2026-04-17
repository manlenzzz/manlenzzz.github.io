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

  <section class="homepage-section" id="selected-publications">
    <div class="section-heading">
      <p class="section-kicker" data-lang="en">Selected Publications</p>
      <p class="section-kicker" data-lang="zh">代表性论文</p>
      <h2 data-lang="en">A recent research line from compression to efficient adaptation.</h2>
      <h2 data-lang="zh">从模型压缩延伸到高效适配的一条近期研究线索。</h2>
      <p data-lang="en">
        The papers below reflect my recent focus on large language model efficiency, especially the connection between structured compression,
        post-compression adaptation, and practical deployment constraints.
      </p>
      <p data-lang="zh">
        下面这些工作集中体现了我近期围绕大语言模型高效化的研究，尤其关注结构化压缩、压缩后适配与真实部署约束之间的联系。
      </p>
    </div>

    <div class="publication-grid">
      <article class="pub-card pub-card--featured">
        <div class="pub-card-top">
          <span class="pub-venue">ICLR 2026</span>
          <span class="pub-year">2026</span>
        </div>
        <h3>Large Language Model Compression with Global Rank and Sparsity Optimization</h3>
        <p data-lang="en">A unified view of rank allocation and sparsity budgeting for compressing large language models under practical resource constraints.</p>
        <p data-lang="zh">从统一视角联合考虑秩分配与稀疏预算，在实际资源约束下进行大语言模型压缩。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue">NAACL 2025</span>
          <span class="pub-year">2025</span>
        </div>
        <h3>QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</h3>
        <p data-lang="en">Explores structured pruning decisions through probabilistic quantization for deployment-oriented large language model compression.</p>
        <p data-lang="zh">通过概率量化建模结构化剪枝决策，面向实际部署场景探索大语言模型压缩方法。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue">Information Processing &amp; Management</span>
          <span class="pub-year">2026</span>
        </div>
        <h3>LaRA: Layer-wise rank allocation for efficient fine-tuning of pruned large language models</h3>
        <p data-lang="en">Shows how pruning and adaptation can be better co-designed through layer-wise rank allocation after compression.</p>
        <p data-lang="zh">通过层级秩分配把剪枝与后续适配更紧密地结合起来，提升压缩后模型的微调效率。</p>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue">arXiv</span>
          <span class="pub-year">2026</span>
        </div>
        <h3>AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</h3>
        <p data-lang="en">Unifies mixed-precision quantization and low-rank adapters in a single optimization framework for efficient fine-tuning.</p>
        <p data-lang="zh">将混合精度量化与低秩适配器纳入同一个优化框架，提升大模型高效微调能力。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2602.22268" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue">arXiv</span>
          <span class="pub-year">2026</span>
        </div>
        <h3>Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</h3>
        <p data-lang="en">Studies how mixed-precision fine-tuning can better preserve model fidelity while retaining adaptation flexibility.</p>
        <p data-lang="zh">研究混合精度微调如何在保持模型原有能力的同时维持足够的适配灵活性。</p>
        <div class="pub-links">
          <a href="https://arxiv.org/abs/2505.03802" target="_blank" rel="noopener">arXiv</a>
        </div>
      </article>

      <article class="pub-card">
        <div class="pub-card-top">
          <span class="pub-venue">ICML 2025</span>
          <span class="pub-year">2025</span>
        </div>
        <h3>BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</h3>
        <p data-lang="en">Further reduces LoRA overhead by introducing sharing mechanisms across and within layers.</p>
        <p data-lang="zh">通过层内与层间共享机制进一步降低 LoRA 的参数与计算开销。</p>
      </article>
    </div>
  </section>

  <section class="homepage-section" id="full-publications">
    <div class="section-heading">
      <p class="section-kicker" data-lang="en">Full Publications</p>
      <p class="section-kicker" data-lang="zh">论文列表</p>
      <h2 data-lang="en">A manually curated publication list.</h2>
      <h2 data-lang="zh">手动维护的论文列表。</h2>
      <p data-lang="en">
        This page currently foregrounds my recent work on efficient LLMs. For the broader and most up-to-date publication list,
        please also visit my Google Scholar profile.
      </p>
      <p data-lang="zh">
        当前页面重点展示我近期在大模型高效化方向上的论文；更完整、也更实时的论文列表请参考我的 Google Scholar 页面。
      </p>
    </div>

    <div class="year-blocks">
      <div class="year-block">
        <h3>2026</h3>
        <ul class="publication-list">
          <li>
            <span class="pub-title">Large Language Model Compression with Global Rank and Sparsity Optimization</span>
            <span class="pub-meta">ICLR 2026</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03801" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">LaRA: Layer-wise rank allocation for efficient fine-tuning of pruned large language models</span>
            <span class="pub-meta">Information Processing &amp; Management, 2026</span>
          </li>
          <li>
            <span class="pub-title">AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning</span>
            <span class="pub-meta">arXiv 2026</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2602.22268" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies</span>
            <span class="pub-meta">arXiv 2026</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2505.03802" target="_blank" rel="noopener">arXiv</a></span>
          </li>
        </ul>
      </div>

      <div class="year-block">
        <h3>2025</h3>
        <ul class="publication-list">
          <li>
            <span class="pub-title">QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models</span>
            <span class="pub-meta">NAACL 2025</span>
            <span class="pub-links-inline"><a href="https://arxiv.org/abs/2412.11629" target="_blank" rel="noopener">arXiv</a></span>
          </li>
          <li>
            <span class="pub-title">BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing</span>
            <span class="pub-meta">ICML 2025</span>
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
