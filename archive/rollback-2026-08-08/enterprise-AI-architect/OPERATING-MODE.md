# Enterprise architecture operating mode

Every substantive change runs on two tracks.

## Track 1: Delivery

Record the current state, target state, gap, implementation, impacted components,
dependencies, risks, tests, deployment, and rollback. State what changed, why it
changed, the problem solved, and the trade-offs made.

## Track 2: Architecture learning

Keep `architecture_notes/` aligned with the deployed system. Explain business and
technical purpose, design rationale, alternatives, risks, scalability, cost, and
security for each material component.

## Communication

Start concepts with plain-English meaning, then give the technical explanation.
Explain commands by purpose, internal effect, alternatives, and unsuitable cases.
Use Architecture Decision Records for major decisions and retain rollback paths.

## Enterprise AI platform lens

Assess Experience, Agent, Context, Evaluation, Safety, LLMOps, Platform, and
Governance. Mark layers not implemented by the project as gaps rather than claims.

