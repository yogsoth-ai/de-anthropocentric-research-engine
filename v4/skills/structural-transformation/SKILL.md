---
name: structural-transformation
description: "Decompose a system and apply component/function transformations such as remove, substitute, combine, redistribute, divide, or reverse."
---

# structural-transformation
## Purpose
Decompose a system and apply explicit SCAMPER structural/function transformations to generate and test alternatives.
## Input contract
```yaml
required: [system_or_design, transformation_target]
optional: [component_inventory, constraints, operator_sequence]
constraints: [operator and affected component must be named for every variant]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `decompose-components` to decompose components and functions.
2. You MUST load skill `transform-component` to apply exactly named SCAMPER operators: Substitute, Combine, Adapt, Modify (including magnify/minify variants), Put to another use, Eliminate, Reverse (including rearrange variants).
3. You MUST load skill `evaluate-compatibility` to evaluate each variant's compatibility.
4. You MUST load skill `synthesize-idea` to synthesize viable transformations.
   If the variants expose systematic uncovered regions, consider `coverage-white-space-search`. If progress is blocked by a contradiction, consider `resolve-inventive-contradiction`.
Deviation: operators may be selected or sequenced by the design question, but the record must state which of the seven operators were considered, applied, rejected, and why; "appropriate operator" is invalid.
## Output contract
```yaml
produces: [component_decomposition, operator_variants, compatibility_report, transformed_designs]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
```
## Thresholds and quality gates
- B: all seven SCAMPER operators are explicitly considered; each applied operator names target, change, rationale, and compatibility result.
## Failure and counterexamples
Reject variants with unnamed operators, hidden multi-operator changes, or transformations that violate hard constraints without disclosure.
## Provenance map
- `structural-deconstruction`, `component-surgery`, `scamper-transformation`, `function-trimming`, `function-combination`, `component-decomposition`: resolved.
## Preserved source criteria ledger
- Preserve the seven SCAMPER operators individually: Substitute; Combine; Adapt; Modify; Put to another use; Eliminate; Reverse. Magnify/minify and rearrange are recorded as variants of Modify and Reverse, not extra operators.
## Context checkpoint / Delta notes
Append component changes, operator coverage, rejected variants, compatibility results, and selected design.
