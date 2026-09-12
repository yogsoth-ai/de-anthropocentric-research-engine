---
name: extract-empirical-regularity
description: "Extract a repeatable empirical pattern from observations, state its support and exceptions, and generalize cautiously without importing an unsupported mechanism."
---

# extract-empirical-regularity

## Purpose

Extract a repeatable empirical pattern from records while preserving conditions, exceptions, and uncertainty.

## Input contract

```yaml
required: [observations, variable_schema, condition_schema]
optional: [replication_records, measurement_uncertainty]
constraints: [regularity claims require multiple comparable observations or an explicit single-case limitation]
```

## Procedure

1. Normalize observations, units, and conditions.
2. Identify repeated associations, trends, or invariants.
3. Test exceptions, alternative explanations, and measurement artifacts.
4. State the regularity with scope and uncertainty boundaries.

## Output contract

```yaml
produces: [regularity_statement, supporting_records, exception_set, scope_conditions]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Conditions and exceptions accompany every regularity.
- Correlation is not labeled mechanism without supporting evidence.

## Failure and counterexamples

Do not generalize a pattern across changed populations or protocols without a comparability check.

## Provenance map

- `resolved: extract-empirical-regularity`

