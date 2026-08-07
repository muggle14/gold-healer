# Phase 5 — Validation and release readiness

## BEGINNING-OF-STAGE

- **Current state:** Phases 0–4 are present on `redesign/dark-luxe`, with the public
  GitHub Pages site still served from `main`.
- **Target state:** Validate the owner-approved staged page at phone, tablet, and desktop
  widths before promoting the same content to `index.html`.
- **Gap:** Automated validation can confirm structure, assets, metadata, links, and release
  markers. A connected browser is still required for visual overflow and keyboard checks.
- **Rollback point:** `db363da` (`chore: checkpoint before phase 5 and 6`).

## Validation matrix

| Check | Result | Evidence |
|---|---|---|
| Staging structure and content | PASS | `python3 scripts/validate_site.py` |
| Repository diff hygiene | PASS | `git diff --check` |
| Local homepage delivery | PASS | HTTP 200 for `staging.html` |
| Local icon runtime | PASS | HTTP 200 and pinned SHA-256 for Lucide 1.30.0 |
| Om/lotus favicon | PASS | PNG signature, alpha channel, and 32/48/180/480 dimensions |
| Public timing removal | PASS | No duration component or timing phrase in staging |
| Responsive browser widths | PENDING | Browser connection unavailable for 320–1440 px pass |
| Keyboard drawer and FAQ | PENDING | Requires the same browser pass |

## Testing strategy

The final interactive pass must cover 320, 360, 375, 390, 430, 768, 1024, and
1440 pixel widths. It must check horizontal overflow, header containment, mobile call to
action height, drawer focus trapping and Escape handling, FAQ expansion, footer icon
alignment, locally rendered icons, and browser console errors.

## Deployment and rollback

Promotion is a copy from `staging.html` to `index.html`, followed by restoring production
title, robots, and environment markers. The branch remains a draft pull request until the
interactive pass is complete. If a regression is found, return to `db363da` or revert the
individual Phase 5/6 commits; do not rewrite shared history.

## END-OF-STAGE

- **Status:** PENDING RELEASE GATE.
- **Completed:** automated staging, asset, metadata, policy, and HTTP validation.
- **Not completed:** responsive visual and keyboard-browser verification.
- **Release decision:** do not promote or merge while this gate remains open.
