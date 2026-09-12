# select-experimental-baseline

## Purpose

Perform select experimental baseline as a bounded experimental transformation.

## Input contract

```yaml
required: [claim, candidate_baselines, comparability_fields]
optional: [provenance, assumptions, uncertainty_register]
constraints: [inputs are typed, units and conditions are explicit, provenance is retained]
```

## Procedure

1. Validate the required fields and normalize units without changing their meaning.
2. Apply the operation specific to select experimental baseline: Selection rationale matches the claim and records provenance.
3. Emit baseline_selection with each decision tied to evidence, assumptions, or uncertainty.

## Output contract

```yaml
produces: [baseline_selection]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Selection rationale matches the claim and records provenance.
- Preserve nulls, contradictions, and boundary cases instead of smoothing them away.
- Record the stopping condition and unresolved questions when the operation cannot conclude.

## Failure and counterexamples

Mark the artifact unresolved when required fields conflict, provenance is absent, or the result exceeds scope. Retain counterexamples and failed checks.

## Provenance map

- resolved: select-experimental-baseline <- v3 refactory_source.json nodes[].name (normalized lookup)
- concept: experiment-execution/select-experimental-baseline <- architecture semantic consolidation
