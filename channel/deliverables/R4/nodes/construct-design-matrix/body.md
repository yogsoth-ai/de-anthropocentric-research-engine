# construct-design-matrix

## Purpose

Perform construct design matrix as a bounded experimental transformation.

## Input contract

```yaml
required: [factor_schema, randomization_unit, blocking_plan]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to construct design matrix: Balanced allocation covers every declared factor combination; randomization is reproducible.
3. Emit design_matrix, allocation_record with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [design_matrix, allocation_record]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Balanced allocation covers every declared factor combination; randomization is reproducible.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: construct-design-matrix <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/construct-design-matrix <- architecture semantic consolidation
