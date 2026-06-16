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

    def test_homepage_sections_present(self):
        about = (ROOT / '_pages' / 'about.md').read_text()
        self.assertIn('id="research"', about)
        self.assertIn('id="research-notes"', about)
        self.assertIn('id="publications"', about)
        self.assertIn('When a Better Clock Is Not a Better Sampler', about)

    def test_navigation_points_to_homepage_sections(self):
        nav = (ROOT / '_data' / 'navigation.yml').read_text()
        for anchor in ['#research', '#research-notes', '#publications', '#contact']:
            self.assertIn(anchor, nav)
        self.assertNotIn('Homepage', nav)
        self.assertNotIn('#about', nav)

    def test_seo_title_is_not_hardcoded_to_homepage(self):
        seo = (ROOT / '_includes' / 'seo.html').read_text()
        self.assertNotIn('<title>{{ site.title }} - Homepage</title>', seo)
        self.assertIn('seo_title', seo)

    def test_damage_clock_note_exists(self):
        note = ROOT / 'notes' / 'damage-clock-negative-result' / 'index.md'
        self.assertTrue(note.is_file())
        note_text = note.read_text()
        self.assertIn('permalink: /notes/damage-clock-negative-result/', note_text)
        self.assertIn('When a Better Clock Is Not a Better Sampler', note_text)
        self.assertIn('figures/fig_result_delta_revised.svg', note_text)
        self.assertTrue((note.parent / 'figures' / 'fig_result_delta_revised.svg').is_file())
        self.assertTrue((note.parent / 'data' / 'r287_mean_fid.csv').is_file())


if __name__ == '__main__':
    unittest.main()
