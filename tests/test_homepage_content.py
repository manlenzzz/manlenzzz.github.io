import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HomepageTest(unittest.TestCase):
    def test_about_page_serves_root(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertIn('permalink: /', about)

    def test_config_has_empty_baseurl(self):
        config = (ROOT / '_config.yml').read_text()
        self.assertIn('baseurl                  : ""', config)

    def test_publications_section_present(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertIn('id="publications"', about)


if __name__ == '__main__':
    unittest.main()
