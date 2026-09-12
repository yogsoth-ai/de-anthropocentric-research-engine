# verify-reproducibility

## Purpose

Perform verify reproducibility as a bounded experimental transformation.

## Input contract

```yaml
required: [original_result, rerun_results, reproduction_protocol]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to verify reproducibility: Assess agreement against the declared target with fixed criteria, not relative coverage.
3. Emit reproducibility_assessment with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [reproducibility_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Assess agreement against the declared target with fixed criteria, not relative coverage.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: verify-reproducibility <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/verify-reproducibility <- architecture semantic consolidation
