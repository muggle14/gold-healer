# Deployment guide

## In plain English

Changes are reviewed away from the public homepage first. The old public version is
recoverable, and the final page is promoted only after the staging copy passes review.

## Technically

1. Preserve the pre-change state with a checkpoint commit.
2. Implement the proposed homepage in `staging.html` with `noindex,nofollow`.
3. Validate HTML, local links, booking links, metadata, structured data, and target
   responsive widths.
4. Copy the approved staged markup to `index.html`, restore production title and robot
   directives, and remove staging-only markers.
5. Commit the intentional files, push the review branch, and use a draft pull request
   into `main`.
6. GitHub Pages deploys only from `main`; merging remains the production release gate.

Rollback uses checkpoint commit `2fb7393` or a revert of the production-promotion
commit. Never delete historical branding sources.

