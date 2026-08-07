# ADR 001: Recover the logo and stage before production

## Decision

Use the genuine transparent `brand_v2.png` from Git commit `4d5f824` as the brand
master. Preserve it under `architecture/source/branding/`, create deterministic web
derivatives under `branding/`, and review owner-feedback changes in `staging.html`
before promoting them to `index.html`.

## Context

The current hero is a framed poster, while the owner requested a simple plain logo.
The current 192 by 192 `brand_v3.png` contains a baked checkerboard and is not a
true transparent source. Historical Git objects contain a suitable transparent mark.

## Options

1. Request a new logo from the owner.
2. Continue using the framed poster.
3. Recover and preserve the historical transparent emblem.

## Trade-offs

The recovered mark avoids redrawing the brand and preserves the original symbols.
It is visually detailed, so small contexts use a tighter crop while the hero uses the
complete emblem.

## Why selected

The source is authentic, high resolution, transparent, already owned by the project,
and closest to the owner's plain-logo direction.

## Future implications

New brand exports should be derived from the preserved master. Production changes
should continue through a noindex staging surface and an explicit review gate.

