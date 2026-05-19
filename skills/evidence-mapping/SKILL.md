---
name: evidence-mapping
description: Systematic evidence map construction — search, classify, locate gaps, visualize. Combines concept-matrix-construction, gap-keyword-extraction, evidence-grading, and egm-construction SOPs.
execution: tactic
used-by: gap-identification, gap-synthesis-strategy
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
