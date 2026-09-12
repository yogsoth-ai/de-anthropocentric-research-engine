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
1. Decompose components and functions (`decompose-components`).
2. Apply exactly named SCAMPER operators (`transform-component`): Substitute, Combine, Adapt, Modify/Magnify/Minify, Put to another use, Eliminate, Reverse/Rearrange.
3. Evaluate compatibility of each variant (`evaluate-compatibility`).
4. Synthesize viable transformations (`synthesize-idea`).
Deviation: operators may be selected or sequenced by the design question, but the record must state which of the seven operators were considered, applied, rejected, and why; “appropriate operator” is invalid.
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
- `structural-deconstruction`, `component-surgery`, `scamper-transformation`, `function-trimming`, `function-combination`, `component-decomposition`: resolved where exact names exist; otherwise concept.
## Preserved source criteria ledger
- Preserve the seven SCAMPER operators individually: Substitute; Combine; Adapt; Modify/Magnify/Minify; Put to another use; Eliminate; Reverse/Rearrange.
## Context checkpoint / Delta notes
Append component changes, operator coverage, rejected variants, compatibility results, and selected design.
