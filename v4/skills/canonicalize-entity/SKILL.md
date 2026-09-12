---
name: canonicalize-entity
description: "Resolve aliases and near-duplicates into canonical entities while preserving provenance and rejecting false merges; entity schema is configurable."
---

# canonicalize-entity

## Purpose

Resolve aliases and near-duplicates into canonical entities while preserving provenance and rejecting false merges.

## Input contract

```yaml
required: [raw_entities, entity_schema, alias_evidence]
optional: [synonym_dictionary, organization_relationships, graph_edges, canonicalization_policy]
constraints: [the entity schema is explicit; merge requires semantic identity evidence; preserve provenance and redirect relationships]
```

## Procedure

1. Normalize names, identifiers, and aliases under the caller-supplied entity schema.
2. Search for near-duplicates and compare definitions, identifiers, and provenance.
3. Merge only semantically identical entities into a canonical record and redirect dependent edges.
4. Preserve rejected-merge pairs and rationale, then return the canonicalized register.

## Output contract

```yaml
produces: [canonical_entities, alias_map, merge_decisions, redirected_edges, rejected_merges]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Preserve the source merge-candidates gate: scan at least 10 concepts, or all concepts if fewer than 10 exist; a candidate score >7.0 is a merge flag, not proof.
- Before merging aliases, verify pages refer to the same concept rather than merely related concepts; retain inline links and edge redirects where applicable.
- Assignee normalization preserves parent, subsidiary, and acquired-entity relationships rather than collapsing organizations into one name.

## Parameterization

The caller must provide the entity type and schema, canonical naming policy, alias/synonym evidence, merge confidence rule, graph-edge policy, and whether the task concerns concepts, assignees, or another entity class.

## Failure and counterexamples

Reject merges without semantic identity evidence, threshold-only matches, or records that lose provenance or dependent edges.

## Provenance map

- resolved: knowledge-structuring/merge-candidates
- resolved: knowledge-structuring/alias-resolution
- resolved: knowledge-acquisition/assignee-normalization
- intermediate: Pass3/merge-near-duplicate-concepts
- intermediate: Pass3/normalize-assignee
- intermediate: Pass4/map-field-taxonomy

## Verbatim source criteria excerpts

- `merge-candidates` line 18: If search returns another concept with score > 7.0, flag as merge candidate.
- `merge-candidates` line 25: Must scan at least 10 concepts (or all concepts if fewer than 10 exist).
- `alias-resolution` line 29: Before merging, verify the pages truly refer to the same concept (not related but distinct concepts).

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| knowledge-structuring/merge-candidates | 22 | numeric | Scan at least 10 concepts, or all if fewer than 10; score >7.0 flags a merge candidate. |
| knowledge-structuring/alias-resolution | 28 | gate | Verify semantic identity before merging; related-but-distinct concepts must not merge. |
