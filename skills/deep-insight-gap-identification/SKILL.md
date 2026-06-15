---
name: gap-identification
description: Identify research gaps via PICOS frameworks, concept matrices, evidence
  gap maps, keyword extraction, citation analysis, and topic modeling. Systematic
  discovery of what is missing in the literature.
dependencies:
  tactics:
  - evidence-mapping
  sops:
  - concept-matrix-construction
  - egm-construction
  - gap-keyword-extraction
---

# Gap Identification

Discover where gaps exist in the research landscape.

## When to Use

User has a research area and needs to find what's missing — uncharted territory, under-explored intersections, or absent evidence.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 60 | 54–66 |
| web-research | 10 | 9–11 |
| paper-overview | 80 | 72–88 |
| paper-search | 30 | 27–33 |
| paper-research | 5 | 4–6 |

## State Ledger

Print before every iteration:

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 60 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 80 | ? |
| paper-search | ? | 30 | ? |
| paper-research | ? | 5 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- evidence-mapping

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** gap-keyword-extraction, concept-matrix-construction, egm-construction

## Execution Guidance

Start with broad web-search + paper-overview to map the landscape. Use gap-keyword-extraction to identify gap-indicating sentences. Build concept-matrix to visualize coverage. Construct EGM for structural view of where evidence is dense vs absent.

## Output Format

Gap Candidate List with evidence pointers — each candidate includes: gap description, evidence source, confidence level, and location in concept matrix.
