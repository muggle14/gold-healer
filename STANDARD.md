# The Cosmic Alchemy project standard

## Purpose

This repository contains the static website for The Cosmic Alchemy. The public site
is served from `main` through GitHub Pages at `https://thecosmicalchemy.com/`.

## Source of truth

- `index.html` is the production homepage.
- `staging.html` is the noindex review homepage used before promotion.
- `architecture/` records why the site is designed and released this way.
- `architecture/source/` contains read-only original design assets.
- `branding/` contains web-ready derivatives.
- `.goldie/` records project assumptions, questions, state, and build notes.

## Standard layout

| Folder | Purpose |
|---|---|
| `architecture/` | Design documents, decisions, and source artefacts |
| `docs/` | Maintenance and delivery documentation |
| `src/` | Future extracted application source; currently the site remains at repository root for GitHub Pages |
| `tests/` | Automated test assets and future test suites |
| `scripts/` | Validation and maintenance utilities |
| `data/` | Sample data and fixtures |
| `data-drivers/` | Source-of-truth driver tables or specifications |
| `archive/` | Superseded artefacts moved with history preserved |
| `.goldie/` | Project state |
| `configs/` | Runtime or tool configuration |
| `workspace/` | Read-only third-party references |

## Release rules

1. Create a checkpoint before a material owner-feedback pass.
2. Make homepage changes in `staging.html` first.
3. Keep staging `noindex,nofollow`.
4. Run `scripts/validate_site.py` and browser QA before promotion.
5. Promote the verified staging content to `index.html` and restore production robots metadata.
6. Push through a review branch and draft pull request; merging to `main` is the public release gate.

## Non-negotiables

- Never delete historical assets with `git rm`; move superseded material to `archive/`.
- Never modify files under `architecture/source/` in place.
- Never publish invented or unapproved testimonials.
- Keep visible services, metadata, structured data, policies, and external-profile copy aligned.
- Keep the custom domain as the canonical URL.
