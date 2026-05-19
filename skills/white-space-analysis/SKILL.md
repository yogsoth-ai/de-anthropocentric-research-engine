---
name: white-space-analysis
description: Identify patent coverage gaps — feature cross-matrix blank areas revealing unprotected technology combinations. Budget: 150 patent families, 10 claim parses, 60 web searches.
execution: strategy
used-by: patent-mining
---

# White Space Analysis

Identifies gaps in patent coverage by constructing feature cross-matrices and finding blank areas where no patents exist. Reveals opportunities for new filings.

## Purpose

Map the patent coverage landscape as a multi-dimensional feature matrix and identify unprotected technology combinations — areas where innovation is possible without infringing existing IP.

## Budget

| Metric | Target |
|--------|--------|
| Patent families analyzed | 150 |
| Claim parses | 10 |
| Web searches completed | 60 |

## State Ledger

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Patent families analyzed | 150 | 0 | 0% |
| Claim parses completed | 10 | 0 | 0% |
| Web searches completed | 60 | 0 | 0% |
| Feature dimensions defined | — | 0 | — |
| White spaces identified | — | 0 | — |

**HARD-GATE**: Cannot exit iteration loop until 80% of patent families (120) and web searches (48) budget met.

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| patent-family-tracing | Fill coverage map by tracing families in each matrix cell |
| classification-navigation | Define feature dimensions from IPC/CPC hierarchy |
| claim-decomposition | Extract feature elements from key patents to define matrix axes |

## Available SOPs

| SOP | Role in This Strategy |
|-----|----------------------|
| patent-query-formulation | Generate queries for each feature combination |
| patent-categorization | Assign patents to matrix cells |
| white-space-mapping | Construct cross-matrix and identify blanks |
| claim-parsing | Extract features from key patents for axis definition |
| trend-analysis | Identify which white spaces are trending toward filling |
| saturation-detection | Confirm matrix coverage is complete |
| patent-synthesis | Produce white space opportunity report |

## Execution Guidance

1. **Domain scoping** — Define the technology domain boundaries
2. **Feature extraction** — Use `claim-decomposition` on key patents to identify feature dimensions
3. **Matrix construction** — Define 2-3 feature axes using `white-space-mapping`
4. **Systematic search** — Query each matrix cell using `patent-query-formulation`
5. **Family tracing** — Use `patent-family-tracing` to ensure complete cell coverage
6. **Categorization** — Assign all patents to cells with `patent-categorization`
7. **Gap identification** — Identify empty and sparse cells
8. **Trend overlay** — Use `trend-analysis` to assess which gaps are closing
9. **Synthesis** — Produce opportunity report ranking white spaces by attractiveness

## Output Format

```markdown
# White Space Analysis: [Technology Domain]

## Feature Dimensions
[Axis definitions with rationale]

## Coverage Matrix
[Cross-matrix with patent counts per cell, blanks highlighted]

## Identified White Spaces (ranked by opportunity)
| Rank | Feature Combination | Adjacent Patents | Trend | Opportunity Score |
|------|--------------------|--------------------|-------|-------------------|

## Opportunity Assessment
[For each top white space: technical feasibility, market potential, filing risk]

## Recommendations
[Prioritized list of filing opportunities]
```
