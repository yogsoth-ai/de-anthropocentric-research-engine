---
name: evidence-mapping
description: Systematic evidence map construction — search, classify, locate gaps,
  visualize. Combines concept-matrix-construction, gap-keyword-extraction, evidence-grading,
  and egm-construction SOPs.
execution: tactic
dependencies:
  sops:
  - concept-matrix-construction
  - deep-insight-paper-overview
  - deep-insight-paper-search
  - egm-construction
  - evidence-grading
  - gap-keyword-extraction
---

# Evidence Mapping

Systematically build evidence maps to reveal structural gaps.

## Operations

- concept-matrix-construction — articles × concepts coverage visualization
- gap-keyword-extraction — gap-indicating sentence identification
- evidence-grading — quality assessment of available evidence
- egm-construction — structured evidence gap map output

## Available SOPs

**Subagent:** concept-matrix-construction, gap-keyword-extraction, evidence-grading, egm-construction
**Import:** paper-overview, paper-search

## Execution Guidance

Build concept matrix first (articles × concepts), identify empty cells as gap candidates, verify with keyword extraction from full texts, grade evidence quality in populated cells, construct final EGM for structural view.

## Minimum Yield

```
<HARD-GATE>
- concept-matrix: >= 1 constructed
- gap-keyword passes: >= 3
- evidence grading: >= 5 items graded
- EGM: >= 1 constructed
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| concept-matrix-construction | Build articles × concepts coverage matrix to visualize research landscape and identify empty cells as gap candidates. |
| deep-insight-paper-overview | Paper metadata and abstract-level overview. Import of literature-engine/literature-overview skill. Abstracts only — no substantive claims without deeper reading. |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| egm-construction | Build structured Evidence Gap Maps — define axes (intervention × outcome or method × domain), place gaps in cells, annotate with evidence density and quality. |
| evidence-grading | Assess evidence quality using GRADE/SOE framework. Rates certainty level and identifies downgrade reasons. |
| gap-keyword-extraction | Extract gap-indicating sentences and phrases from papers/reviews. Identifies linguistic markers of research gaps (e.g., "remains unclear", "has not been explored", "limited understanding"). |

<!-- END available-tables (generated) -->
