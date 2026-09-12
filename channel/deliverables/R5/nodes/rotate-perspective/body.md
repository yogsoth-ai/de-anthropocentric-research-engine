# rotate-perspective
## Purpose
Apply one perspective at a time to reinterpret a fixed target while holding evidence constant.
## Input contract
```yaml
required: [target_object, perspective_sequence, fixed_evidence]
optional: [objective_map, risk_taxonomy, opportunity_taxonomy]
constraints: [only perspective assumptions/objectives may change between passes]
```
## Procedure
1. Freeze target and evidence references.
2. Apply the first perspective and record assumptions, risks, and opportunities.
3. Reset to the frozen target and repeat for each remaining perspective.
4. Compare changed interpretations and retain provenance.
## Output contract
```yaml
produces: [perspective_interpretations, changed_assumptions, risk_opportunity_matrix, comparison_notes]
delta_fields: [findings, assumptions_updates, uncertainties]
```
## Quality gates
- Every pass names exactly one active perspective.
- Evidence references remain unchanged across passes.
- Differences are attributed to perspective assumptions, not silent target changes.
## Parameterization
Caller supplies target schema, perspective definitions/order, immutable evidence fields, and comparison rubric.
## Failure and counterexamples
Reject perspective passes that import new evidence or conflate multiple lenses without attribution.
## Provenance map
- concept: perspective-rotation
- concept: six-thinking-hats
- concept: personal-analogy
