# personal_assets/

Snapshot of personal content extracted from the original Minimal Mistakes site
before the migration to al-folio. This directory is **excluded** from the Jekyll
build (`exclude` in `_config.yml`) and is kept purely as the canonical archive of
hand-written content. The original Minimal Mistakes scaffold lives in
`../archive_minimal_mistakes/`.

## Provenance map

| Path                       | Source                                | Purpose                                                     |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| `bio/home.md`              | `_pages/home.md`                      | Three news bullets driving the homepage News section.       |
| `bio/home.html`            | `_layouts/home.html`                  | Hand-written About / News / Publications / Services markup. |
| `bio/profile.jpeg`         | `assets/images/profile.jpeg`          | Headshot used as profile picture.                           |
| `publications-md/`         | `_publications/*.md`                  | Per-paper Jekyll collection entries (frontmatter + body).   |
| `publication-images/`      | `assets/images/`                      | All paper teasers and figures (kept as a single tree).      |
| `files/`                   | `assets/files/`                       | PDFs and slides referenced from the old site.               |
| `config-snapshot/_config.yml` | `_config.yml`                      | Snapshot of the Minimal Mistakes site configuration. The Google Analytics ID `G-L3V3YFHY81` was migrated from here into the new al-folio config. |

No `assets/videos/` directory existed on the source site; nothing to copy.

## Reuse notes

- `bio/profile.jpeg` is also copied to `assets/img/prof_pic.jpeg` for al-folio.
- Selected paper teasers (one per paper) are copied to
  `assets/img/publication_preview/<slug>.png` for the bibliography preview.
- The hand-written abstracts/figures from `publications-md/` were used as
  authoritative content; placeholder BibTeX in those files (the `xu2022lightweight`
  block accidentally pasted into several entries) was rewritten using the actual
  paper metadata (title, authors, venue, DOI/arXiv).
