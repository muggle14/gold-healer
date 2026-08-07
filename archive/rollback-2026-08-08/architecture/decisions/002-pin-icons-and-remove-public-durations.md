# ADR 002: Pin icons and remove public session durations

## Decision

Serve Lucide 1.30.0 from `vendor/lucide/`, use a dedicated Om-and-lotus favicon crop,
and remove all session-duration labels from the public and staged homepages.

## Context

The website previously loaded the mutable `@latest` Lucide bundle from a third-party
content delivery network. The small icon reused a more complex mark, and session timing
scope remained ambiguous after the initial owner-feedback pass.

## Options

1. Continue using the mutable external icon URL and existing small mark.
2. Pin an external Lucide version but retain the network dependency.
3. Vendor the pinned runtime, preserve its licence, create a source-faithful small icon,
   and remove public timing content.

## Trade-offs

Vendoring adds approximately 407 KB to the repository but removes a mutable runtime
dependency and reduces third-party requests. Removing duration labels requires booking
conversations to establish timing individually.

## Why selected

The decision improves reliability, privacy transparency, brand clarity at small sizes,
and consistency with the owner's instruction to remove timing scope.

## Future implications

Lucide upgrades require an explicit version change, licence review, integrity refresh,
and regression test. Session duration must not be reintroduced without owner approval.
