---
name: prior-art-search
description: 'Evaluate novelty of specific invention — find relevant prior art across
  patents, publications, and products. Budget: 80 patent families, 20 claim parses,
  50 web searches.'
execution: strategy
dependencies:
  tactics:
  - classification-navigation
  - knowledge-acquisition-claim-decomposition
  - patent-family-tracing
  sops:
  - citation-network-analysis
  - claim-parsing
  - knowledge-acquisition-saturation-detection
  - legal-status-assessment
  - patent-query-formulation
  - patent-synthesis
  - quality-scoring
---

# Prior Art Search

Targeted prior art search to evaluate the novelty of a specific invention. Searches patents, academic publications, and commercial products for anticipating or obviating references.

## Purpose

Determine whether a specific invention is novel and non-obvious by systematically finding the closest prior art. Supports freedom-to-operate analysis and patentability assessments.

## Budget

| Metric | Target |
|--------|--------|
| Patent families analyzed | 80 |
| Claim parses | 20 |
| Web searches completed | 50 |

## State Ledger

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Patent families analyzed | 80 | 0 | 0% |
| Claim parses completed | 20 | 0 | 0% |
| Web searches completed | 50 | 0 | 0% |
| Relevant prior art refs | — | 0 | — |

**HARD-GATE**: Cannot exit iteration loop until 80% of patent families (64), claim parses (16), and web searches (40) budget met.

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| patent-family-tracing | Trace citation chains from closest prior art |
| classification-navigation | Find related patents via IPC/CPC neighborhood |
| claim-decomposition | Parse claims of closest references for element-by-element comparison |

## Available SOPs

| SOP | Role in This Strategy |
|-----|----------------------|
| patent-query-formulation | Generate targeted queries from invention disclosure |
| claim-parsing | Parse claims of found prior art for comparison |
| citation-network-analysis | Identify main citation paths leading to the invention |
| legal-status-assessment | Check if prior art references are still active |
| quality-scoring | Rank prior art by relevance and quality |
| saturation-detection | Check if prior art search has converged |
| patent-synthesis | Produce prior art search report |

## Execution Guidance

1. **Invention decomposition** — Break the target invention into key technical features
2. **Query formulation** — Use `patent-query-formulation` with invention features as input
3. **Broad search** — Execute web searches across patent and non-patent literature
4. **Citation tracing** — Use `patent-family-tracing` from closest hits
5. **Classification search** — Use `classification-navigation` in relevant IPC/CPC areas
6. **Claim parsing** — Parse claims of top 20 closest references with `claim-parsing`
7. **Element comparison** — Map invention features against prior art elements
8. **Saturation check** — Confirm search completeness with `saturation-detection`
9. **Synthesis** — Produce prior art report with relevance rankings

## Output Format

```markdown
# Prior Art Search Report: [Invention Title]

## Invention Summary
[Key technical features of the target invention]

## Search Strategy
[Queries used, databases searched, classification codes explored]

## Closest Prior Art (ranked by relevance)
| Rank | Reference | Type | Date | Relevance | Elements Anticipated |
|------|-----------|------|------|-----------|---------------------|

## Element-by-Element Comparison
[Feature matrix: invention elements vs. prior art coverage]

## Novelty Assessment
[Analysis of which elements are novel vs. anticipated]

## Non-Obviousness Analysis
[Combination analysis — would PHOSITA combine references?]

## Conclusion
[Overall patentability/FTO assessment]
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
| citation-network-analysis | Build and analyze patent citation networks — main path analysis, PageRank, cluster detection |
| claim-parsing | Patent claim syntax parsing — independent/dependent relationships and element extraction |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| legal-status-assessment | Determine patent legal status — active, expired, pending, lapsed, or revoked |
| patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |
| patent-synthesis | Produce final structured patent intelligence report from all analysis results |
| quality-scoring | Multi-dimensional patent quality assessment — forward citations, family size, claim count, geographic breadth |

<!-- END available-tables (generated) -->
