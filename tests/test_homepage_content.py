import unittest
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


class HomepageTest(unittest.TestCase):
    def test_about_page_serves_root(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertIn('permalink: /', about)
        self.assertIn('author_profile: true', about)

    def test_config_has_empty_baseurl(self):
        config = (ROOT / '_config.yml').read_text()
        self.assertIn('baseurl                  : ""', config)

    def test_reference_style_sections_present(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertIn('id="about"', about)
        self.assertIn('id="news"', about)
        self.assertIn('id="research-notes"', about)
        self.assertIn('id="publications"', about)
        self.assertIn('id="contact"', about)
        self.assertIn('About Me', about)
        self.assertIn('News', about)
        self.assertIn('When a Better Clock Is Not a Better Sampler', about)

    def test_navigation_points_to_homepage_sections(self):
        nav = (ROOT / '_data' / 'navigation.yml').read_text()
        for anchor in ['#about', '#news', '#research-notes', '#publications', '#contact']:
            self.assertIn(anchor, nav)
        self.assertNotIn('Homepage', nav)
        self.assertNotRegex(nav, r'url:\s+"#research"\s*$')

    def test_news_dates_are_ordered_and_not_synthetic(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        news_dates = re.findall(r'<span class="news-date">([^<]+)</span>', about)
        self.assertGreaterEqual(len(news_dates), 3)
        self.assertEqual(news_dates, sorted(news_dates, reverse=True))
        self.assertNotIn('2025-12', news_dates)

    def test_news_uses_acceptance_timeline(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        news_items = re.findall(
            r'<span class="news-date">([^<]+)</span>\s*'
            r'<span class="news-text">([^<]+)</span>',
            about,
        )
        self.assertEqual(
            news_items,
            [
                ('2026-04-30', 'AutoQRA was accepted to ICML 2026.'),
                ('2026-04-04', 'Deputy, QR-Adaptor, and CoRE were accepted to ACL 2026.'),
                ('2026-01-25', 'Large Language Model Compression with Global Rank and Sparsity Optimization was accepted to ICLR 2026.'),
                ('2025-05-01', 'BSLoRA was accepted to ICML 2025.'),
                ('2025-03-14', 'Enhancing Object Coherence in Layout-to-Image Synthesis was accepted to ICME 2025.'),
                ('2025-01-22', 'RankAdaptor and QPruner were accepted to NAACL 2025.'),
                ('2024-12-09', 'Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving was accepted to AAAI 2025.'),
            ],
        )
        news_text = ' '.join(text for _, text in news_items)
        self.assertNotIn('available on arXiv', news_text)
        self.assertNotIn('studies million-scale', news_text)

    def test_previous_landing_page_patterns_removed(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertNotIn('profile-hero', about)
        self.assertNotIn('language-switch', about)
        self.assertNotIn('data-lang=', about)

    def test_research_note_has_visual_hero(self):
        note = (ROOT / 'notes' / 'damage-clock-negative-result' / 'index.md').read_text()
        self.assertIn('class="note-hero-visual"', note)
        self.assertIn('class="note-breadcrumb"', note)

    def test_damage_clock_note_exists(self):
        note = ROOT / 'notes' / 'damage-clock-negative-result' / 'index.md'
        self.assertTrue(note.is_file())
        note_text = note.read_text()
        self.assertIn('permalink: /notes/damage-clock-negative-result/', note_text)
        self.assertIn('When a Better Clock Is Not a Better Sampler', note_text)
        self.assertIn('figures/fig_result_delta_revised.svg', note_text)
        self.assertTrue((note.parent / 'figures' / 'fig_result_delta_revised.svg').is_file())
        self.assertTrue((note.parent / 'data' / 'r287_mean_fid.csv').is_file())

    def test_sidebar_does_not_duplicate_research_summary(self):
        author_profile = (ROOT / '_includes' / 'author-profile.html').read_text()
        self.assertNotIn('site.description', author_profile)

    def test_avatar_path_resolves_to_existing_image(self):
        config = (ROOT / '_config.yml').read_text()
        include = (ROOT / '_includes' / 'author-profile.html').read_text()
        avatar_match = re.search(r'avatar\s+:\s+"?([^"\n]+)"?', config)
        self.assertIsNotNone(avatar_match)
        avatar_path = avatar_match.group(1).lstrip('/')
        self.assertTrue((ROOT / avatar_path).exists(), avatar_path)
        self.assertIn('author.avatar | relative_url', include)

    def test_arxiv_publications_use_real_images(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        for image_name in [
            'llm-compression-global-rank-sparsity-main.png',
            'qr-adaptor-mixed-precision-main.png',
            'autoqra-main.png',
            'qpruner-main.png',
        ]:
            self.assertIn(image_name, about)
            self.assertTrue((ROOT / 'images' / 'papers' / image_name).exists())

    def test_complete_publication_groups_and_titles_present(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        for group in [
            'Post-training、模型发布与训练服务',
            'LLM Serving 与推理加速',
            '模型压缩与参数高效适配',
            '多模态生成模型',
            '评测与代码推理',
        ]:
            self.assertIn(group, about)

        for title in [
            'On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters',
            'Macaron-V1-Preview: A 749B Personal Agent Model with Mixture of LoRA',
            'MinT: Managed Infrastructure for Training and Serving Millions of LLMs',
            'Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving',
            'Making Activation Sparsity Executable in Grouped Low-Bit LLMs',
            'Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution',
            'Large Language Model Compression with Global Rank and Sparsity Optimization',
            'Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies',
            'AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning',
            'RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs',
            'QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models',
            'BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing',
            'LaRA: Layer-wise Rank Allocation for Efficient Fine-Tuning of Pruned Large Language Models',
            'SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads',
            'Enhancing Object Coherence in Layout-to-Image Synthesis',
            'CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction',
        ]:
            self.assertIn(title, about)

    def test_publications_include_authors_and_highlight_me(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertEqual(about.count('class="publication-authors"'), 16)
        self.assertGreaterEqual(about.count('<strong>Changhai Zhou</strong>'), 13)

    def test_mindlab_publications_use_lab_author(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertEqual(about.count('<p class="publication-authors">MindLab</p>'), 3)
        post_training = about.split('LLM Serving 与推理加速', 1)[0]
        self.assertNotIn('<strong>Changhai Zhou</strong> et al.', post_training)

    def test_deputy_is_not_listed_as_first_author(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        match = re.search(
            r'Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution.*?'
            r'<p class="pub-meta">([^<]+)</p>',
            about,
            re.S,
        )
        self.assertIsNotNone(match)
        self.assertNotIn('一作', match.group(1))
        self.assertNotIn('共一', match.group(1))

    def test_deputy_authors_are_complete(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        match = re.search(
            r'Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution.*?'
            r'<p class="publication-authors">([^<]*(?:<strong>[^<]+</strong>[^<]*)*)</p>',
            about,
            re.S,
        )
        self.assertIsNotNone(match)
        authors = re.sub(r'<[^>]+>', '', match.group(1))
        self.assertEqual(
            authors,
            'Yuhua Zhou*, Shichao Weng*, Changhai Zhou*, Yuhan Wu, Qian Qiao, Jun Gao, Fei Yang†, Aimin Pan†',
        )

    def test_publication_images_are_main_figures_not_cover_pages(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        for image_name in [
            'llm-compression-global-rank-sparsity-main.png',
            'qr-adaptor-mixed-precision-main.png',
            'autoqra-main.png',
            'qpruner-main.png',
            'dynamic-operator-optimization-main.png',
            'scaling-peft-main.png',
            'mint-main.png',
            'macaron-v1-preview-main.png',
            'rankadaptor-main.png',
            'bslora-main.png',
            'soulx-flashhead-main.png',
            'object-coherence-main.png',
            'core-benchmark-main.png',
        ]:
            self.assertIn(image_name, about)
            self.assertTrue((ROOT / 'images' / 'papers' / image_name).exists())

    def test_placeholder_publication_thumbnails_removed(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        styles = (ROOT / 'assets' / 'css' / 'main.scss').read_text()
        self.assertNotIn('publication-thumb--', about)
        self.assertNotIn('publication-thumb--', styles)


if __name__ == '__main__':
    unittest.main()
