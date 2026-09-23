# generate-competing-hypotheses

## Purpose

Generate distinct, testable hypotheses that explain a target observation or research problem.

## Input contract

```yaml
required: [problem_statement, observations, scope_constraints]
optional: [existing_theories, analogies, anomaly_records]
constraints: [each hypothesis must imply a differentiating prediction or assumption]
```

## Procedure

1. Extract the target phenomenon and unresolved explanatory gap.
2. Generate mechanismally distinct explanations, including a null or status-quo hypothesis.
3. Translate each explanation into predictions, assumptions, and disconfirming observations.
4. Deduplicate equivalent explanations and retain the comparison set.

## Output contract

```yaml
produces: [hypothesis_set, mechanism_descriptions, prediction_set, assumption_register]
delta_fields: [hypothesis_updates, uncertainties, open_questions, recommended_jumps]
```

## Quality gates

- Hypotheses differ in mechanism or prediction, not wording only.
- A null or baseline explanation is considered where applicable.

## Failure and counterexamples

Do not generate unfalsifiable narratives or discard inconvenient hypotheses before comparison.

## Provenance map

- `resolved: generate-competing-hypotheses`

