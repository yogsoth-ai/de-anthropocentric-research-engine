---
name: atomize-concept
description: "Decompose compound concepts into atomic, non-overlapping concepts while preserving parent/part relationships."
---

# atomize-concept

## Purpose

Split a broad concept into definitional facets and distinguishable subconstructs.

## Input contract

```yaml
required: [concept_definition, domain_context]
optional: [theory, neighboring_concepts, examples]
constraints: [facets must be non-duplicate and retain the parent concept boundary]
```

## Procedure

1. Extract the concept's necessary, typical, and optional properties.
2. Separate facets by mechanism, function, level, or context.
3. Compare neighboring concepts and mark overlaps or gaps.
4. Emit a facet hierarchy with definitions and boundary examples.

## Output contract

```yaml
produces: [concept_facets, facet_definitions, overlap_map, boundary_examples]
delta_fields: [findings, uncertainties, open_questions]
```

## Quality gates

- Facets are distinguishable in principle.
- Parent and child scopes are explicit.

## Failure and counterexamples

Do not treat synonyms as distinct facets or split a concept solely by examples.

## Provenance map

- `resolved: atomize-concept`

