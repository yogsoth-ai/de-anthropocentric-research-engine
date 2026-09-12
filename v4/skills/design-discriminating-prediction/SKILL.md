---
name: design-discriminating-prediction
description: "Construct a prediction that yields different outcomes under competing hypotheses."
---

# design-discriminating-prediction

## Purpose

Design an observation or test whose outcomes distinguish among competing hypotheses.

## Input contract

```yaml
required: [hypotheses, current_evidence, target_comparison]
optional: [constraints, measurable_variables, candidate_interventions]
constraints: [predictions must differ on an observable outcome]
```

## Procedure

1. Identify the unresolved contrast between hypotheses.
2. Derive each hypothesis's prediction under candidate conditions.
3. Select the condition maximizing interpretable separation within constraints.
4. Specify outcome, measurement, and interpretation for each possible result.

## Output contract

```yaml
produces: [discriminating_test, prediction_table, measurement_plan, interpretation_rules]
delta_fields: [hypothesis_updates, decisions, uncertainties, recommended_jumps]
```

## Quality gates

- Predictions differ before the test is selected.
- Confounds and ambiguous outcomes are recorded.

## Failure and counterexamples

Do not call a test discriminating when all hypotheses predict the same result or when the measurement cannot separate them.

## Provenance map

- `resolved: design-discriminating-prediction`

