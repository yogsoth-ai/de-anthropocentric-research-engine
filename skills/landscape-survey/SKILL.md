---
name: landscape-survey
description: Patent landscape full-scan — maps technology domain via assignee ranking, IPC/CPC classification, filing trends. Budget: 200 patent families, 0 claim parses, 80 web searches.
execution: strategy
used-by: patent-mining
---

# Landscape Survey

Full-scan patent landscape analysis. Maps the technology domain by identifying key assignees, classifying by IPC/CPC taxonomy, and analyzing filing trends over time.

## Purpose

Produce a comprehensive patent landscape map for a given technology domain, answering: Who are the key players? What are the main technology branches? How is filing activity trending?

## Budget

| Metric | Target |
|--------|--------|
| Patent families analyzed | 200 |
| Claim parses | 0 |
| Web searches completed | 80 |

## State Ledger

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Patent families analyzed | 200 | 0 | 0% |
| Web searches completed | 80 | 0 | 0% |
| Assignees identified | — | 0 | — |
| IPC/CPC classes mapped | — | 0 | — |

**HARD-GATE**: Cannot exit iteration loop until 80% of patent families (160) and web searches (64) budget met.

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| patent-family-tracing | Expand from seed patents to full family coverage |
| classification-navigation | Drill into IPC/CPC hierarchy to find all relevant subclasses |

## Available SOPs

| SOP | Role in This Strategy |
|-----|----------------------|
| patent-query-formulation | Generate initial search queries for the domain |
| patent-categorization | Classify discovered patents into technology sub-domains |
| assignee-normalization | Standardize assignee names across patent offices |
| trend-analysis | Analyze filing volume time-series and lifecycle curves |
| quality-scoring | Rank patent families by quality metrics |
| saturation-detection | Check if landscape scan has converged |
| patent-synthesis | Produce final landscape report |

## Execution Guidance

1. **Query formulation** — Use `patent-query-formulation` to generate keyword + IPC/CPC + assignee search strategies
2. **Broad search** — Execute web searches across patent databases (Google Patents, Espacenet, USPTO)
3. **Family tracing** — Use `patent-family-tracing` tactic to expand from top results
4. **Classification drill** — Use `classification-navigation` tactic to find related technology branches
5. **Categorization** — Classify all found patents using `patent-categorization`
6. **Assignee normalization** — Standardize names with `assignee-normalization`
7. **Trend analysis** — Run `trend-analysis` on the full dataset
8. **Saturation check** — Use `saturation-detection` to confirm convergence
9. **Synthesis** — Produce final report with `patent-synthesis`

## Output Format

```markdown
# Patent Landscape Report: [Technology Domain]

## Executive Summary
[Key findings in 3-5 bullets]

## Top Assignees (ranked by family count)
| Rank | Assignee | Families | Key IPC Classes |
|------|----------|----------|-----------------|

## Technology Classification Map
[IPC/CPC hierarchy with patent counts per node]

## Filing Trends
[Time-series data: year, total filings, top assignee filings]

## Technology Clusters
[Grouped by application domain / technology branch]

## Appendix: Full Patent Family List
[Structured table of all 200 families]
```
