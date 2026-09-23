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

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `trace-patent-family` to trace priority, family, and citation relationships.
2. You MUST load skill `navigate-patent-classification` to expand or delimit the technical neighborhood.
3. You MUST load skill `canonicalize-entity` to canonicalize assignees and entities.
4. You MUST load skill `analyze-temporal-trajectory` to analyze filing dynamics and temporal regimes.
5. You MUST load skill `detect-coverage-gap` to identify coverage gaps. You MUST load skill `analyze-patent-citation-network` to analyze the citation structure.
   If the landscape is ready for claim-level white-space analysis, consider `map-patent-white-space` as the next tactic.

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
| none retained | - | - | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append family deduplication, classification paths, canonical entities, trajectory observations, gap cells, citation links, and unresolved records.
