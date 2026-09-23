# estimate-sample-size

## Purpose

Perform estimate sample size as a bounded experimental transformation.

## Input contract

```yaml
required: [detectable_effect, alpha, power, variance_model]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to estimate sample size: Use alpha 0.05 and power 0.8 as fixed design criteria; disclose effect and variance assumptions.
3. Emit sample_size_plan with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [sample_size_plan]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Use alpha 0.05 and power 0.8 as fixed design criteria; disclose effect and variance assumptions.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: estimate-sample-size <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/estimate-sample-size <- architecture semantic consolidation
