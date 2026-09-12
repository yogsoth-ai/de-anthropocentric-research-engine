---
name: resolve-inventive-contradiction
description: "Turn a design or research contradiction into targeted transformations using inventive-principle and separation reasoning, then evaluate whether the transformed configuration resolves the contradiction without creating a worse one."
---

# resolve-inventive-contradiction
## Purpose
Turn a technical or physical contradiction into targeted transformations and test whether the contradiction is resolved without creating a worse one.
## Input contract
```yaml
required: [contradiction_statement, conflicting_requirements, system_components]
optional: [operating_conditions, target_metrics, known_principles]
constraints: [improvement and worsening effects must be explicit]
```
## Execution protocol
1. Identify contradiction type and parameters (`identify-inventive-contradiction`).
2. Select applicable TRIZ principles (`select-inventive-principle`).
3. Apply separation options (`apply-separation-principle`).
4. Transform implicated components (`transform-component`).
5. Evaluate compatibility and residual conflict (`evaluate-compatibility`).
6. Synthesize the candidate resolution (`synthesize-idea`).
Deviation: use separation before inventive principles only when the contradiction is physical; retain both analyses and state why.
## Output contract
```yaml
produces: [contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: contradiction type, selected principles, transformations, and residual trade-offs are all traceable; resolution must improve the target without violating the other requirement.
## Failure and counterexamples
Reject a solution that merely accepts the trade-off, renames the contradiction, or shifts harm outside the declared boundary.
## Provenance map
- `creative-ideation/structural-deconstruction`: resolved.
- `triz`, `contradiction-matrix`, `separation-principles`: concept (no exact pool entries).
## Preserved source criteria ledger
- Preserve contradiction matrix reasoning, physical separation, and compatibility validation.
## Context checkpoint / Delta notes
Append contradiction parameters, selected principles, transformed components, residual conflicts, and decision rationale.
