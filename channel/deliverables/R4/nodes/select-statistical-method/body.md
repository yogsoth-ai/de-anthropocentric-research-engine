# select-statistical-method

## Purpose

Perform select statistical method as a bounded experimental transformation.

## Input contract

```yaml
required: [design, outcome_type, sample_structure]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to select statistical method: Method choice must match pairing, distribution, multiplicity, and objective; retain alpha 0.05.
3. Emit analysis_method with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [analysis_method]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Method choice must match pairing, distribution, multiplicity, and objective; retain alpha 0.05.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: select-statistical-method <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/select-statistical-method <- architecture semantic consolidation
