---
name: map-ablation-components
description: "Map system structure into ablatable units, dependencies, legal removal/replacement operations, and expected contribution hypotheses."
---

# map-ablation-components

## Purpose

Map system structure into ablatable units, dependencies, legal removal/replacement operations, and expected contribution hypotheses.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Partition the system into removable or replaceable units and record interfaces, shared state, and legal ablation boundaries.
2. For each unit, state the expected contribution, dependency risks, and the comparison needed to isolate its effect.
3. Check that the proposed ablations preserve the target claim and return a matrix of units, operations, and hypotheses.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The map ablation components decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject map ablation components when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: ablation-component-mapping
