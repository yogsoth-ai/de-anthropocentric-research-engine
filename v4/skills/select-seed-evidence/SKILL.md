---
name: select-seed-evidence
description: "Select and rank high-information seed sources for iterative evidence expansion using quality, recency, relevance, and network position."
---

# select-seed-evidence

## Purpose

Select and rank high-information seed sources for iterative evidence expansion using quality, recency, relevance, and network position.

## Input contract

```yaml
required: [candidate_sources, research_question, selection_criteria]
optional: [citation_graph, quality_assessments, recency_window]
constraints: [rank rationale and source independence must be explicit]
```

## Procedure

1. Score candidate sources against relevance, quality, recency, diversity, and network position.
2. Remove dependent duplicates and preserve complementary seeds.
3. Select seeds covering distinct mechanisms, populations, or evidence gaps.
4. Record expected expansion value and unresolved selection uncertainty.

## Output contract

```yaml
produces: [seed_set, ranking_rationale, diversity_coverage, expansion_questions]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```

## Quality gates

- Seed choice is not citation-count-only.
- Independent sources and complementary coverage are visible.

## Failure and counterexamples

Do not select only the most cited source or treat a review and its included primary study as independent seeds.

## Provenance map

- `resolved: knowledge-acquisition-seed-selection`

