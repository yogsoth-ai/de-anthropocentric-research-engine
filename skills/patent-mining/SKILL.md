---
name: patent-mining
description: Systematic Patent Analysis Campaign — 5 strategies for patent landscape analysis, prior art search, white space identification, competitive intelligence, and claim analysis. Produces structured patent intelligence reports.
execution: campaign
used-by: knowledge-acquisition
---

# Patent Mining

Systematic patent intelligence campaign. Analyzes patent landscapes, traces prior art, identifies white spaces, profiles competitor portfolios, and decomposes claim scope.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| "map the patent landscape for X" / "who are the key players in X" / "filing trends" | landscape-survey |
| "is X novel" / "find prior art for X" / "freedom to operate" | prior-art-search |
| "where are the gaps" / "uncovered areas" / "opportunity mapping" | white-space-analysis |
| "what is competitor Y doing" / "portfolio comparison" / "IP strategy" | competitive-intelligence |
| "analyze these claims" / "claim scope" / "protection breadth" | claim-analysis |

## Manifest

### Strategies (5)

| Strategy | Budget Summary |
|----------|---------------|
| landscape-survey | 200 families, 0 claim parses, 80 web searches |
| prior-art-search | 80 families, 20 claim parses, 50 web searches |
| white-space-analysis | 150 families, 10 claim parses, 60 web searches |
| competitive-intelligence | 120 families, 15 claim parses, 40 web searches |
| claim-analysis | 30 families, 30 claim parses, 20 web searches |

### Tactics (3)

| Tactic | Purpose |
|--------|---------|
| patent-family-tracing | Forward/backward citation and priority chain tracing |
| classification-navigation | IPC/CPC hierarchy drill-down and lateral expansion |
| claim-decomposition | Independent/dependent claim parsing and feature mapping |

### Subagent SOPs (11)

| SOP | Purpose |
|-----|---------|
| patent-query-formulation | Construct multi-faceted patent search strategies |
| patent-categorization | Classify patents by subdomain and value chain |
| assignee-normalization | Standardize assignee names and corporate groups |
| citation-network-analysis | Build citation graphs, compute main path and PageRank |
| trend-analysis | Filing volume time-series and S-curve lifecycle |
| white-space-mapping | Feature cross-matrix and blank area identification |
| claim-parsing | Claim syntax parsing and element extraction |
| legal-status-assessment | Determine patent legal status (active/expired/pending) |
| quality-scoring | Multi-dimensional patent quality assessment |
| patent-synthesis | Produce final structured intelligence report |
| saturation-detection | (shared) Determine when search expansion has saturated |

## Budget Table

| Strategy | Patent Families | Claim Parses | Web Searches |
|----------|----------------|--------------|--------------|
| landscape-survey | 200 | 0 | 80 |
| prior-art-search | 80 | 20 | 50 |
| white-space-analysis | 150 | 10 | 60 |
| competitive-intelligence | 120 | 15 | 40 |
| claim-analysis | 30 | 30 | 20 |

## MCP Tools

| Server | Tools Used | Purpose |
|--------|-----------|---------|
| brave-search | brave_web_search, brave_llm_context | Patent database web search, patent office queries |
| apify | google_scholar_scraper | Academic patent literature discovery |
| alphaxiv | full_text_papers_search, get_paper_content | Patent-related academic papers |
| semantic-scholar | ss_relevance_search, ss_citations, ss_references | Citation network for patent-adjacent literature |

## Context Management

- **State file**: Each strategy maintains a state ledger tracking progress against budget
- **Deduplication**: Patent families are deduplicated by priority number across strategies
- **Saturation**: Uses shared `saturation-detection` SOP to determine when citation/classification expansion has converged
- **Output**: Final deliverable is a structured patent intelligence report produced by `patent-synthesis` SOP
