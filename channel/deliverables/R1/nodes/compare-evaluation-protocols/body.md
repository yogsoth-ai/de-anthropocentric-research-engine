# compare-evaluation-protocols

## Purpose

Build a protocol-difference matrix and estimate which differences can materially change measured performance.

## Input contract

```yaml
required: [protocol_records, metric_schema, comparison_target]
optional: [paired_results, sensitivity_assumptions]
constraints: [differences require explicit protocol fields and a comparable outcome]
```

## Procedure

1. Extract protocol elements into a normalized comparison schema.
2. Align datasets, populations, metrics, baselines, and evaluation conditions.
3. Mark differences and assess their plausible performance effect.
4. Separate observed effects from unresolved protocol confounding.

## Output contract

```yaml
produces: [protocol_difference_matrix, materiality_assessment, confounding_notes, comparability_judgment]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- The compared metric and target are held constant or explicitly qualified.
- Missing protocol fields remain visible.

## Failure and counterexamples

Do not attribute score differences to method quality when protocol differences are unmeasured.

## Provenance map

- `resolved: knowledge-acquisition-evaluation-protocol-comparison`

