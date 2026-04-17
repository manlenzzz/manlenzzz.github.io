# Changhai Zhou Homepage

This repository contains the source for the personal academic homepage of Changhai Zhou.

## Site URL

Once GitHub Pages is enabled for this repository, the site is served at:

- `https://manlenzzz.github.io/`

## Main files

- `_pages/about.md`: single-page bilingual homepage content
- `_config.yml`: site metadata and root GitHub Pages settings
- `_data/navigation.yml`: homepage section anchors
- `_includes/head/custom.html`: language toggle behavior and favicon setup
- `assets/css/main.scss`: homepage-specific styling

## Publications

The publication list is manually maintained in `_pages/about.md`.
For the most up-to-date list, please refer to the linked Google Scholar profile on the homepage.

## Local preview

If Ruby, Bundler, and Jekyll are available locally, you can preview the site with:

```bash
bundle exec jekyll serve
```

A lightweight content sanity check is available with:

```bash
python -m unittest tests.test_homepage_content -v
```
