# statistical-testing

## Purpose

Perform statistical testing as a bounded experimental transformation.

## Input contract

```yaml
required: [analysis_method, observations, estimand]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to statistical testing: Apply predeclared procedure; report effect, uncertainty, diagnostics; alpha 0.05.
3. Emit test_result with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [test_result]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Apply predeclared procedure; report effect, uncertainty, diagnostics; alpha 0.05.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: statistical-testing <- experiment-execution/statistical-testing
