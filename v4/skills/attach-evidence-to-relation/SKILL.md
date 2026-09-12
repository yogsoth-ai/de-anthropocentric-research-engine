---
name: attach-evidence-to-relation
description: "Attach supporting or contradicting evidence to a specific claim/relation with quality, directness, and independence metadata."
---

# attach-evidence-to-relation

## Purpose

Attach source evidence to a typed relation between concepts, claims, or entities with directness and independence metadata.

## Input contract

```yaml
required: [relation, evidence_records, relation_schema]
optional: [quality_rubric, independence_keys, confidence_prior]
constraints: [evidence must support the relation type and direction claimed]
```

## Procedure

1. Identify the relation type, endpoints, direction, and boundary conditions.
2. Match each evidence record to the relation and classify directness.
3. Assess quality, independence, consistency, and alternative interpretations.
4. Emit an evidence-linked relation with confidence rationale.

## Output contract

```yaml
produces: [evidence_relation, support_records, directness_assessment, independence_assessment, confidence_rationale]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Evidence supports the typed relation rather than only its endpoints.
- Dependent sources are not counted as independent.

## Failure and counterexamples

Do not attach a citation merely because it mentions both entities.

## Provenance map

- `resolved: attach-evidence-to-relation`

