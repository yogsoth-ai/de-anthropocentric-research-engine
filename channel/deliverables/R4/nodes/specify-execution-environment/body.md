# specify-execution-environment

## Purpose

Perform specify execution environment as a bounded experimental transformation.

## Input contract

```yaml
required: [hardware, software, data_versions, configuration]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to specify execution environment: All materially affecting variables are pinned or explicitly unknown.
3. Emit environment_spec with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [environment_spec]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- All materially affecting variables are pinned or explicitly unknown.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: specify-execution-environment <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/specify-execution-environment <- architecture semantic consolidation
