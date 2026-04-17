import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HomepageContentTest(unittest.TestCase):
    def test_config_uses_updated_identity(self):
        config = (ROOT / "_config.yml").read_text()
        self.assertIn('repository               : "manlenzzz/manlenzzz.github.io"', config)
        self.assertIn('url                      : "https://manlenzzz.github.io"', config)
        self.assertIn('baseurl                  : ""', config)
        self.assertIn('name             : "Changhai Zhou"', config)
        self.assertIn('email            : "chzhou25@m.fudan.edu.cn"', config)
        self.assertIn('googlescholar    : "https://scholar.google.com/citations?user=mM3rnV4AAAAJ&hl=zh-CN"', config)
        self.assertNotIn('zhouch23@m.fudan.edu.cn', config)

    def test_navigation_uses_anchor_links(self):
        nav = (ROOT / "_data/navigation.yml").read_text()
        for anchor in [
            '#about',
            '#research',
            '#selected-publications',
            '#full-publications',
            '#cv',
            '#contact',
        ]:
            self.assertIn(anchor, nav)

    def test_homepage_contains_complete_publication_list(self):
        about = (ROOT / "_pages/about.md").read_text()
        self.assertIn('author_profile: false', about)
        self.assertIn('Changhai Zhou', about)
        self.assertIn('周昌海', about)
        self.assertIn('data-language-button="en"', about)
        self.assertIn('data-language-button="zh"', about)
        self.assertIn('Dynamic Operator Optimization for Efficient Multi-Tenant LoRA Model Serving', about)
        self.assertIn('RankAdaptor: Hierarchical Dynamic Low-Rank Adaptation for Structural Pruned LLMs', about)
        self.assertIn('QPruner: Probabilistic Decision Quantization for Structured Pruning in Large Language Models', about)
        self.assertIn('Large Language Model Compression with Global Rank and Sparsity Optimization', about)
        self.assertIn('BSLoRA: Enhancing the Parameter Efficiency of LoRA with Intra-Layer and Inter-Layer Sharing', about)
        self.assertIn('Enhancing Object Coherence in Layout-to-Image Synthesis', about)
        self.assertIn('Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies', about)
        self.assertIn('CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction', about)
        self.assertIn('Deputy: Accelerating Large Language Model Inference with Dynamic Low-Rank Substitution', about)
        self.assertIn('AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning', about)
        self.assertIn('BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Models Inference', about)
        self.assertIn('SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads', about)
        self.assertNotIn('A manually curated publication list.', about)
        self.assertNotIn('zhouch23@m.fudan.edu.cn', about)

    def test_readme_mentions_root_repo_url(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('Changhai Zhou Homepage', readme)
        self.assertIn('https://manlenzzz.github.io/', readme)
        self.assertIn('manually maintained', readme)


if __name__ == '__main__':
    unittest.main()
