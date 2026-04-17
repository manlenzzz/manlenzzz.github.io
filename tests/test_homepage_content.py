import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HomepageContentTest(unittest.TestCase):
    def test_config_uses_project_pages_settings(self):
        config = (ROOT / "_config.yml").read_text()
        self.assertIn('repository               : "manlenzzz/manlenzzz.github.io"', config)
        self.assertIn('url                      : "https://manlenzzz.github.io"', config)
        self.assertIn('baseurl                  : ""', config)
        self.assertIn('name             : "Changhai Zhou"', config)
        self.assertIn('googlescholar    : "https://scholar.google.com/citations?user=mM3rnV4AAAAJ&hl=zh-CN"', config)
        self.assertNotIn('Qian Qiao', config)

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
        masthead = (ROOT / '_includes/masthead.html').read_text()
        self.assertIn("{{ '/' | relative_url }}#about", masthead)
        self.assertIn("{{ '/' | relative_url }}{{ link.url }}", masthead)

    def test_homepage_contains_bilingual_sections(self):
        about = (ROOT / "_pages/about.md").read_text()
        self.assertIn('author_profile: false', about)
        self.assertIn('Changhai Zhou', about)
        self.assertIn('周昌海', about)
        self.assertIn('data-language-button="en"', about)
        self.assertIn('data-language-button="zh"', about)
        self.assertIn('Large Language Model Compression with Global Rank and Sparsity Optimization', about)
        self.assertIn('AutoQRA: Joint Optimization of Mixed-Precision Quantization and Low-rank Adapters for Efficient LLM Fine-Tuning', about)
        self.assertNotIn('My name is Qian Qiao', about)
        self.assertNotIn('Soul AILab', about)

    def test_readme_mentions_new_repo_url(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('Changhai Zhou Homepage', readme)
        self.assertIn('https://manlenzzz.github.io/', readme)
        self.assertIn('manually maintained', readme)


if __name__ == '__main__':
    unittest.main()
