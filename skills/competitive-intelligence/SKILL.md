---
name: competitive-intelligence
description: 'Analyze competitor IP portfolios — comparative patent portfolio reports
  with strategy inference. Budget: 120 patent families, 15 claim parses, 40 web searches.'
execution: strategy
dependencies:
  tactics:
  - classification-navigation
  - knowledge-acquisition-claim-decomposition
  - patent-family-tracing
  sops:
  - assignee-normalization
  - citation-network-analysis
  - claim-parsing
  - knowledge-acquisition-saturation-detection
  - legal-status-assessment
  - patent-categorization
  - patent-query-formulation
  - patent-synthesis
  - quality-scoring
  - trend-analysis
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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| classification-navigation | IPC/CPC hierarchy drill-down and lateral expansion for patent discovery |
| knowledge-acquisition-claim-decomposition | Independent/dependent claim parsing, element extraction, and feature mapping to technical domains |
| patent-family-tracing | Forward/backward patent citation and priority tracing until saturation |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| assignee-normalization | Standardize assignee names and identify corporate group affiliations across patent offices |
| citation-network-analysis | Build and analyze patent citation networks — main path analysis, PageRank, cluster detection |
| claim-parsing | Patent claim syntax parsing — independent/dependent relationships and element extraction |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| legal-status-assessment | Determine patent legal status — active, expired, pending, lapsed, or revoked |
| patent-categorization | Classify patents by tech subdomain, application scenario, and value chain position |
| patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |
| patent-synthesis | Produce final structured patent intelligence report from all analysis results |
| quality-scoring | Multi-dimensional patent quality assessment — forward citations, family size, claim count, geographic breadth |
| trend-analysis | Patent filing volume time-series, technology lifecycle stage, and S-curve analysis |

<!-- END available-tables (generated) -->
