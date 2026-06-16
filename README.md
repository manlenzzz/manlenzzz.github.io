# Changhai Zhou — Academic Homepage

Source for [https://manlenzzz.github.io/](https://manlenzzz.github.io/).

Built with Jekyll. The main entry point is `_pages/about.md` (served at `/`).

## Main files

- `_pages/about.md`: single-page bilingual homepage content
- `_config.yml`: site metadata and author profile
- `_data/navigation.yml`: homepage section anchors
- `notes/`: research notes and public experiment writeups
- `assets/css/main.scss`: homepage-specific visual styling
- `_includes/head/custom.html`: language toggle behavior and head customizations

## Publications

The publication section is manually maintained in `_pages/about.md`.
For the broader and most up-to-date list, please refer to the linked Google Scholar profile on the homepage.

## Local preview

If Ruby, Bundler, and Jekyll are available locally, you can preview the site with:

```bash
bundle exec jekyll serve
```

A lightweight content sanity check is also available via:

```bash
python -m unittest tests.test_homepage_content -v
```
