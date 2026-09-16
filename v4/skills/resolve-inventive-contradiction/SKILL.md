---
name: resolve-inventive-contradiction
description: "Turn a design or research contradiction into targeted transformations using inventive-principle and separation reasoning, then evaluate whether the transformed configuration resolves the contradiction without creating a worse one."
---

# resolve-inventive-contradiction
## Purpose
Turn a technical or physical contradiction into targeted transformations and test whether the contradiction is resolved without creating a worse one.
## Input contract
```yaml
mode_contracts:
  technical-contradiction: &contradiction_input
    required: [contradiction_statement, conflicting_requirements, system_components]
    optional: [operating_conditions, target_metrics, known_principles]
    constraints: [improvement_and_worsening_parameters_must_be_explicit]
  physical-contradiction: *contradiction_input
  separation: *contradiction_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-inventive-contradiction` to identify the contradiction type and parameters.
2. Apply the principle-selection or separation operations required by the selected mode.
3. You MUST load skill `transform-component` to transform the implicated components.
4. You MUST load skill `evaluate-compatibility` to evaluate compatibility and residual conflict.
5. You MUST load skill `synthesize-idea` to synthesize the candidate resolution.
Deviation: use separation before inventive principles only when the contradiction is physical; retain both analyses and state why.

## Mode branches

- `technical-contradiction`: represent the improving and worsening engineering parameters, use the contradiction matrix to select principles, and test the resulting trade-off. You MUST load skill `select-inventive-principle` to select the applicable principles.
- `physical-contradiction`: split the conflicting requirement by condition, time, space, or scale so one component can satisfy both demands without averaging them. You MUST load skill `apply-separation-principle` to apply the separation options. You MUST load skill `select-inventive-principle` to retain the required principle analysis.
- `separation`: search explicitly for a separation condition, transform the implicated component under that condition, and verify that residual conflicts are reduced. You MUST load skill `apply-separation-principle` to search and apply that condition.

## Output contract
```yaml
mode_contracts:
  technical-contradiction: &contradiction_output
    produces: [contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
  physical-contradiction: *contradiction_output
  separation: *contradiction_output
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
