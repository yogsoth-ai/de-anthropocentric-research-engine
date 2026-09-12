# decompose-evaluation-metric

## Purpose

Decompose an evaluation metric into rewarded signals, aggregation choices, polarity, ceiling effects, and Goodhart vulnerabilities.

## Input contract

```yaml
required: [metric_definition, scored_outputs]
optional: [reference_standard, aggregation_rule, known_failure_cases]
constraints: [each component must have a declared direction and interpretation]
```

## Procedure

1. Split the metric into primitive signals and aggregation operations.
2. Record polarity, scale, weighting, normalization, and ceiling/floor behavior.
3. Map rewarded shortcuts and construct-irrelevant incentives.
4. State interpretation limits and diagnostic needs.

## Output contract

```yaml
produces: [metric_components, aggregation_map, polarity_and_scale, ceiling_analysis, goodhart_risks]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Component contributions and aggregation are reconstructible.
- A high score is not treated as capability evidence without construct support.

## Failure and counterexamples

Do not infer metric meaning from its name or ignore nonlinear aggregation and clipping.

## Provenance map

- `concept: knowledge-acquisition-metric-decomposition`

