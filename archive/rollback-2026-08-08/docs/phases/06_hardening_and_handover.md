# Phase 6 — Hardening and handover

## BEGINNING-OF-STAGE

- **Current state:** The owner-feedback design is staged, but the small icon uses the
  full mark, the icon library is loaded from a mutable external URL, timing remains
  visible, and repository housekeeping is incomplete.
- **Target state:** Apply the two owner approvals, remove timing scope, reduce mutable
  browser dependencies, preserve legacy assets, and leave a maintainable release record.
- **Gap:** Brand, dependency, state, and folder conventions need explicit implementation.
- **Rollback point:** `db363da` (`chore: checkpoint before phase 5 and 6`).

## Delivered changes

- The approved transparent-gold emblem lineage from `4d5f824` remains the website mark.
- The favicon now uses only the Om-and-lotus portion in 32, 48, 180, and 480 pixel PNGs.
- All public session-duration labels and the booking duration card are removed from
  `staging.html`.
- Lucide 1.30.0 is served locally with its ISC licence and pinned integrity hash.
- `STANDARD.md`, project-state files, required folder READMEs, ADR 002, and a legacy
  asset catalogue document the operating model without deleting historical files.
- The validator now enforces timing removal, favicon integrity, vendored dependency
  integrity, stage-state validity, and the required repository skeleton.

## Architecture impact

- **Experience:** small-icon clarity and cleaner service/booking cards.
- **Safety and privacy:** one mutable third-party runtime request is removed; Google Fonts
  remains the documented external browser dependency.
- **Platform and governance:** deterministic dependency verification, a staged release
  gate, project state, ADR traceability, and retained design history.
- **Cost and scale:** no hosting service is added; the repository grows by the local icon
  bundle and favicon derivatives, which GitHub Pages can serve directly.

## Risks and follow-up

- The pinned icon runtime must be deliberately upgraded with a new licence and hash check.
- Google Fonts is still external and can be self-hosted in a future privacy-hardening pass.
- The responsive visual and keyboard gate in Phase 5 remains required before promotion.

## END-OF-STAGE

- **Status:** IMPLEMENTATION COMPLETE; RELEASE PENDING PHASE 5 VISUAL GATE.
- **Testing:** automated validator, diff hygiene, local HTTP, PNG and SHA-256 checks pass.
- **Deployment:** staged only on the review branch; `main` and the public site are unchanged.
- **Rollback:** revert the Phase 6 commit or return to checkpoint `db363da`.
