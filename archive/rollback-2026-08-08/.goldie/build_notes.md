# Build notes

The site has no compilation step. Release validation consists of the repository
validator, local HTTP checks, responsive browser review, keyboard interaction checks,
and review through the draft pull request.

Phase 5 automated validation passed on 2026-08-07. The responsive visual and keyboard
pass is still a release gate because no compatible browser connection was available.
Phase 6 is implemented in `staging.html`; production promotion must wait for that gate.
