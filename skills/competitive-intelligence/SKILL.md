---
name: competitive-intelligence
description: Analyze competitor IP portfolios — comparative patent portfolio reports with strategy inference. Budget: 120 patent families, 15 claim parses, 40 web searches.
execution: strategy
used-by: patent-mining
---

# Competitive Intelligence

Analyzes competitor patent portfolios to infer R&D strategy, identify strengths and weaknesses, and produce comparative intelligence reports.

## Purpose

Profile competitor IP portfolios to understand their technology focus, filing strategy, geographic coverage, and potential future directions. Enables strategic IP positioning.

## Budget

| Metric | Target |
|--------|--------|
| Patent families analyzed | 120 |
| Claim parses | 15 |
| Web searches completed | 40 |

## State Ledger

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Patent families analyzed | 120 | 0 | 0% |
| Claim parses completed | 15 | 0 | 0% |
| Web searches completed | 40 | 0 | 0% |
| Competitors profiled | — | 0 | — |
| Portfolio comparisons | — | 0 | — |

**HARD-GATE**: Cannot exit iteration loop until 80% of patent families (96), claim parses (12), and web searches (32) budget met.

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| patent-family-tracing | Build complete portfolio for each competitor |
| classification-navigation | Map competitor technology focus areas |
| claim-decomposition | Analyze claim scope of competitor key patents |

## Available SOPs

| SOP | Role in This Strategy |
|-----|----------------------|
| patent-query-formulation | Generate assignee-focused search queries |
| assignee-normalization | Resolve subsidiary/parent relationships |
| patent-categorization | Classify competitor patents by technology area |
| citation-network-analysis | Map inter-competitor citation relationships |
| trend-analysis | Analyze competitor filing velocity and direction |
| claim-parsing | Parse key competitor claims for scope analysis |
| quality-scoring | Assess competitor patent quality distribution |
| legal-status-assessment | Determine active vs. expired competitor IP |
| saturation-detection | Confirm portfolio coverage is complete |
| patent-synthesis | Produce competitive intelligence report |

## Execution Guidance

1. **Competitor identification** — Identify target competitors from user input or landscape data
2. **Assignee normalization** — Resolve all name variants and subsidiaries with `assignee-normalization`
3. **Portfolio collection** — Search for all patents per competitor using `patent-query-formulation`
4. **Family tracing** — Complete portfolio with `patent-family-tracing`
5. **Categorization** — Classify each competitor's patents by technology with `patent-categorization`
6. **Trend analysis** — Analyze filing patterns per competitor with `trend-analysis`
7. **Citation analysis** — Map cross-citation between competitors with `citation-network-analysis`
8. **Key claim analysis** — Parse top patents per competitor with `claim-parsing`
9. **Quality assessment** — Score portfolios with `quality-scoring`
10. **Synthesis** — Produce comparative report with `patent-synthesis`

## Output Format

```markdown
# Competitive Patent Intelligence: [Technology Domain]

## Competitor Profiles
### [Competitor A]
- Portfolio size: [N] families
- Technology focus: [top IPC classes]
- Filing trend: [increasing/stable/declining]
- Geographic coverage: [jurisdictions]
- Key patents: [top 3 by quality score]

## Comparative Analysis
| Metric | Comp A | Comp B | Comp C |
|--------|--------|--------|--------|
| Total families | | | |
| Filing velocity (last 3yr) | | | |
| Avg quality score | | | |
| Geographic breadth | | | |

## Citation Network
[Inter-competitor citation patterns and influence]

## Strategic Inferences
[R&D direction, potential acquisitions, licensing opportunities]

## Recommendations
[Positioning strategy relative to competitors]
```
