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

## Local preview

A local static HTTP server is used to exercise relative links and browser behaviour in
the same origin model as GitHub Pages. Opening files directly was an alternative, but it
can hide path and browser-security differences. Do not expose the local server publicly.

