# Commands used

## Git history inspection

`git log`, `git rev-list`, `git ls-tree`, and `git archive` were used to locate earlier
branding objects and recover the selected binary without rewriting repository history.
These commands read the object database; `git archive` materialises a chosen historical
file. A manual download was an alternative, but it would lose provenance. Do not use
history-rewriting commands for this task.

## Image inspection and deterministic crops

`sips` inspected pixel dimensions and transparency, then cropped two exact derivatives
from the preserved source. It changes only the derivative files and does not redraw the
logo. A generative image editor was unsuitable because the sacred symbols and brand
geometry must remain source-faithful.

## Checkpoint commit

`git commit --allow-empty -m "chore: checkpoint before owner feedback implementation"`
recorded an explicit boundary while the tree was clean. Internally, Git created a new
commit pointing to the unchanged tree. A tag was an alternative, but the user requested
a commit. Do not use an empty commit when the history boundary has no project value.

The same mechanism created checkpoint `db363da` before Phase 5 verification and Phase 6
hardening, giving that pass an independent rollback boundary.

## Local preview

A local static HTTP server is used to exercise relative links and browser behaviour in
the same origin model as GitHub Pages. Opening files directly was an alternative, but it
can hide path and browser-security differences. Do not expose the local server publicly.

## Pinned icon runtime

`npm view` identified the current Lucide package version and `npm pack lucide@1.30.0`
retrieved the immutable registry archive without installing a project dependency tree.
The required UMD runtime and ISC licence were extracted under `vendor/lucide/`. A remote
pinned URL was an alternative, but it would retain a runtime network dependency. Do not
replace the vendored file without updating its version, licence, integrity record, and
browser regression checks.

## Small-icon export

`sips` cropped the approved Om-and-lotus area from the preserved logo master and exported
32, 48, and 180 pixel derivatives. This preserves the original geometry. Manual redrawing
was rejected because it could alter sacred symbols or brand proportions.
