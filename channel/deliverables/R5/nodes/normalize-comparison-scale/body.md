# normalize-comparison-scale
## Purpose
Normalize heterogeneous values onto a declared comparison scale while preserving direction, units, uncertainty, and transformation rule.
## Input contract
```yaml
required: [value_set, criterion_definitions, normalization_rule]
optional: [bounds, missing_value_policy, uncertainty_model]
constraints: [direction and units are preserved; rule is declared before transformation]
```
## Procedure
1. Validate units, direction, bounds, and missingness.
2. Apply the caller-supplied transformation to each value.
3. Preserve uncertainty and retain original values for audit.
4. Return normalized values and out-of-bound diagnostics.
## Output contract
```yaml
produces: [normalized_values, transformation_record, uncertainty_preservation, diagnostics]
delta_fields: [evidence_updates, uncertainties, open_questions]
```
## Quality gates
- All normalized values lie in the caller-declared range, commonly [0, 1].
- Maximize/minimize directions are explicit and correctly oriented.
- Missing and extrapolated values are labeled, never silently imputed.
## Parameterization
Caller supplies value schema, units, direction labels, bounds, transformation formula, and missingness policy.
## Failure and counterexamples
Reject mixed units, hidden inversion, or normalization that discards uncertainty and source values.
## Provenance map
- concept: convergence/normalization
- intermediate: Pass4/normalize-scores
- concept: knowledge-acquisition/compute-normalization
- intermediate: Pass4/normalize-compute-budget
