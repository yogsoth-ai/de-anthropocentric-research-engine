---
name: compare-hypotheses
description: "Build an explicit comparison matrix over hypotheses, predictions, and evidence."
---

# compare-hypotheses

## Purpose

Compare competing hypotheses against shared evidence, predictions, assumptions, and explanatory scope.

## Input contract

```yaml
required: [hypotheses, evidence_records, comparison_criteria]
optional: [priors, discriminating_predictions, model_constraints]
constraints: [criteria and evidence must be applied symmetrically]
```

## Procedure

1. Normalize hypotheses to comparable claims and assumptions.
2. Map each hypothesis to predictions and supporting or conflicting evidence.
3. Compare explanatory coverage, residual anomalies, and required assumptions.
4. Record relative support and evidence that would change the comparison.

## Output contract

```yaml
produces: [hypothesis_comparison, prediction_matrix, support_profile, discriminating_evidence]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Shared evidence is not counted repeatedly.
- A criterion omitted for one hypothesis is omitted for all.

## Failure and counterexamples

Do not choose the simplest-sounding hypothesis without comparing predictive adequacy and assumptions.

## Provenance map

- `resolved: compare-hypotheses`

