---
name: trace-patent-family
description: "Trace priority, family membership, forward/backward citations, and continuation relationships until relevant family structure stabilizes."
---

# trace-patent-family

## Purpose

Trace priority, family membership, forward/backward citations, and continuation relationships until relevant family structure stabilizes.

## Input contract

```yaml
required: [patent_records, priority_links, family_identifiers]
optional: [citation_edges, continuation_records, jurisdiction_scope]
constraints: [family relation, jurisdiction, date, and source provenance must be explicit]
```

## Procedure

1. Normalize priority claims, publication identifiers, and jurisdiction fields.
2. Link family members, continuations, divisionals, and citation relations.
3. Deduplicate records while preserving claim and jurisdiction differences.
4. Expand until the relevant family universe and stopping rationale are stable.

## Output contract

```yaml
produces: [family_graph, priority_map, continuation_map, citation_links, family_universe, unresolved_links]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Every family edge has a relation type and source.
- Family members are not counted as independent inventions.
- Coverage claims expose the declared family universe.

## Failure and counterexamples

Do not merge records on assignee or title similarity alone, and do not infer family membership from a shared keyword.

## Provenance map

- `resolved: knowledge-acquisition/patent-family-tracing`

