---
name: specify-relationship
description: "Specify direction, functional form, and theoretical basis of relationships among variables."
---

# specify-relationship

## Purpose

Specify the direction, type, and conditions of a relationship among constructs or variables.

## Input contract

```yaml
required: [variables, relationship_claim, observation_context]
optional: [theory, candidate_moderators, causal_assumptions]
constraints: [relationship type and direction must be distinguished from association strength]
```

## Procedure

1. Define variables, units, temporal order, and relation type.
2. State expected direction, nonlinearities, moderators, and boundary conditions.
3. Separate descriptive association from causal interpretation and list assumptions.
4. Emit a testable relationship specification.

## Output contract

```yaml
produces: [relationship_specification, direction_rule, moderator_set, causal_assumptions]
delta_fields: [hypothesis_updates, decisions, uncertainties, open_questions]
```

## Quality gates

- Direction and relation type are explicit.
- Causal claims include temporal and confounding assumptions.

## Failure and counterexamples

Do not infer causality from a directional correlation or hide moderators in an average effect.

## Provenance map

- `resolved: specify-relationship`

