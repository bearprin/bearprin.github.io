# bearprin.github.io

Personal homepage of Zixiong Wang ([bearprin.com](https://www.bearprin.com)),
built on the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

This repository was migrated from a Minimal Mistakes Jekyll site. The original
scaffold is preserved verbatim under `archive_minimal_mistakes/` for reference,
and hand-written content (bio, news, publications, profile photo, PDFs, the
Google Analytics ID) is mirrored under `personal_assets/` as a build-excluded
canonical archive. Both directories are listed in the `exclude:` block of
`_config.yml` so Jekyll never touches them.

## Local development

The site requires Ruby 3.x. From the repository root:

```bash
bundle config set --local path 'vendor/bundle'
bundle install
bundle exec jekyll serve
```

The build is also fine without ImageMagick (`imagemagick.enabled: false` in
`_config.yml`); enable it if you want responsive WebP variants generated for
images under `assets/img/`.

## Where things live

| Path                              | Purpose                                            |
| --------------------------------- | -------------------------------------------------- |
| `_pages/about.md`                 | Homepage bio + Services subsection.                |
| `_news/*.md`                      | News bullets shown on the about page.              |
| `_bibliography/papers.bib`        | Publications, with `selected={true}` highlights.   |
| `_pages/publications.md`          | Publications page (auto-renders the bib file).     |
| `_data/socials.yml`               | Email + GitHub handle for the social block.        |
| `assets/img/prof_pic.jpeg`        | Profile photo.                                     |
| `assets/img/publication_preview/` | Per-paper thumbnails referenced from the bib.      |
| `_sass/_variables.scss`           | Theme palette (defines `$teal-color`).             |
| `_sass/_themes.scss`              | Light/dark `--global-theme-color` bindings.        |
| `_sass/_typography.scss`          | Site font stack (Inter body / Newsreader heads).   |

## Snapshots

- `archive_minimal_mistakes/` — full untouched copy of the previous Minimal
  Mistakes site (layouts, includes, sass, assets, config). Useful for diffing
  during the migration; safe to delete once everything has been verified live.
- `personal_assets/` — extracted bio, news, publications metadata, profile
  photo, paper figures, and the original `_config.yml` (with the GA ID).
  See `personal_assets/README.md` for the provenance map.

## License

The al-folio theme is MIT-licensed (see the upstream repository). Site content
(bio, publications, images) is © Zixiong Wang.
