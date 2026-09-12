---
name: mine-patent-landscape
description: "Map a patent landscape using families, classifications, assignees, filing dynamics, quality, and technical-domain coverage without prescribing a patent provider."
---

# mine-patent-landscape

## Purpose

Map a patent landscape using families, classifications, assignees, filing dynamics, quality, and technical-domain coverage without prescribing a provider.

## Input contract

```yaml
required: [technical_domain, jurisdiction_scope, patent_records]
optional: [seed_families, assignee_schema, time_window]
constraints: [family identity, classification, assignee, date, and source provenance must be retained]
```

## Execution protocol

1. Trace priority, family, and citation relationships (`trace-patent-family`).
2. Expand or delimit the technical neighborhood (`navigate-patent-classification`).
3. Canonicalize assignees and entities (`canonicalize-entity`).
4. Analyze filing dynamics and temporal regimes (`analyze-temporal-trajectory`).
5. Identify coverage gaps and citation structure (`detect-coverage-gap`, `analyze-patent-citation-network`).

Deviation: Skip entity canonicalization when records already carry a stable canonical key. Skip temporal analysis when no time field exists, and mark the missing dimension instead of imputing it.

## Output contract

```yaml
produces: [patent_family_map, classification_neighborhood, assignee_profile, filing_trajectory, coverage_gaps, citation_network]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Coverage ratios use declared family/classification universes and expose numerator, denominator, batch increment, stopping reason, and source references.
- Saturation is determined by marginal information gain from additional families or classifications.
- Filing trends must preserve jurisdiction and observation window.

## Failure and counterexamples

Do not count family members as independent inventions, equate assignee name variants without provenance, or treat an uncited classification gap as unprotected space.

## Provenance map

- `resolved: patent-mining`
- `resolved: knowledge-acquisition-landscape-survey`
- `resolved: knowledge-acquisition-competitive-intelligence`
- `resolved: knowledge-acquisition-patent-family-tracing`
- `resolved: knowledge-acquisition-classification-navigation`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| none retained | — | — | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append family deduplication, classification paths, canonical entities, trajectory observations, gap cells, citation links, and unresolved records.
