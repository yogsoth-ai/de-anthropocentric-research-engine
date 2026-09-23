---
name: operationalize-construct
description: "Turn abstract variables/constructs into measurable operational definitions."
---

# operationalize-construct

## Purpose

Translate an abstract construct into observable indicators, measurement rules, and validity checks.

## Input contract

```yaml
required: [construct_definition, target_context]
optional: [theory, candidate_indicators, measurement_constraints]
constraints: [indicators must map to construct facets and declare direction]
```

## Procedure

1. Decompose the construct into facets and boundary conditions.
2. Map each facet to observable indicators and measurement procedures.
3. Specify aggregation, polarity, missingness, and confound handling.
4. Record convergent, discriminant, and construct-irrelevant validity checks.

## Output contract

```yaml
produces: [construct_operationalization, indicator_map, measurement_rules, validity_checks]
delta_fields: [findings, decisions, uncertainties, open_questions]
```

## Quality gates

- Indicators cover the declared construct facets.
- Operational rules are reproducible and distinguish proxy from direct measure.

## Failure and counterexamples

Do not substitute an easy-to-measure proxy without stating the construct loss.

## Provenance map

- `resolved: operationalize-construct`

