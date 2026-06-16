# Homepage Reference Redesign Design

## Goal

Redesign the personal academic homepage to closely match the structure and feel of `https://luoxyhappy.github.io/` while keeping this repository's Jekyll/Minimal Mistakes stack.

The target is a plain, readable academic homepage rather than a modern landing page. The page should feel familiar to academic visitors: author profile on the left, compact content on the right, visible news, and publication entries with clear links.

## Scope

- Replace the current large hero-card homepage with a reference-style academic layout.
- Use English only.
- Restore `author_profile: true` on the root page so the left sidebar shows the profile, avatar, location, affiliation, email, Google Scholar, and GitHub.
- Restructure the content area into these sections:
  - `About Me`
  - `News`
  - `Publications`
  - `Contact`
- Keep the existing research and publication content, but remove duplicated Chinese copy and language switching UI.
- Keep the existing Jekyll build system and Minimal Mistakes theme files.
- Avoid copying the reference site's source wholesale. Match its layout and visual language using local code.

## Page Content

### About Me

The first section introduces Changhai Zhou as a direct-track PhD student at Fudan University enrolled in 2023. It briefly states the research focus: efficient large language models, model compression, parameter-efficient fine-tuning, adaptive inference, and serving systems.

### News

Add a compact reverse-chronological news list. News should highlight major accepted papers and project updates already present in the current page content. The design should match the reference site's simple date-plus-text rows.

### Publications

Publications should appear as a vertical list, not as year cards. Each item contains:

- Optional thumbnail area using a neutral generated-style placeholder when no real project image is available.
- Title.
- Venue and author-role metadata.
- One-sentence description.
- Small rectangular action buttons such as `arXiv`, `Code`, or `Project` when a real URL exists.

The first implementation can keep all current 2026 and 2025 publications on the root page.

### Contact

Contact is a short text block with email, Google Scholar, and GitHub links. It should not use large cards.

## Visual Direction

- White background with Minimal Mistakes' two-column academic layout.
- Left sidebar profile visible on desktop and stacked above content on smaller screens.
- Compact typography similar to the reference site.
- Blue links and small blue publication buttons.
- Thin separators between publication entries.
- No large rounded cards, radial gradients, oversized hero headline, or language segmented control.

## Files To Change

- `_pages/about.md`: replace the hero-style homepage markup with simple academic sections and enable the author profile.
- `assets/css/main.scss`: remove or neutralize the current `.homepage` hero/card styles and add reference-style publication/news CSS.
- `_includes/head/custom.html`: remove the language toggle script if it becomes unused; keep favicon/meta tags.
- `_data/navigation.yml`: keep section links, likely `About`, `News`, `Publications`, and `Contact`.
- `_config.yml`: update author metadata only if needed for sidebar display.

## Behavior

- Anchor navigation should continue to work.
- External links open in a new tab as currently configured by the existing head template.
- The page should be usable without JavaScript.

## Testing

- Run the Jekyll build command available in the repository.
- If dependencies are available, serve locally and inspect desktop/mobile layout.
- Run existing tests if they still apply; update only if assertions describe the removed hero design rather than the intended content.

## Out Of Scope

- Adding new publications beyond the current content.
- Designing or generating real paper thumbnails.
- Migrating away from Minimal Mistakes.
- Rewriting the resume or PDF output.
