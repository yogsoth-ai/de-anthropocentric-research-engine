---
name: morphological-exploration
description: Morphological Exploration Campaign — systematic dimension-combination enumeration to discover unexplored solution spaces via Zwicky box, CCA, and GMA
execution: campaign
used-by: creative-ideation
---

# Morphological Exploration

Systematic dimension-combination enumeration to discover unexplored solution spaces via Zwicky box, CCA, and GMA.

## Strategy Routing

| Strategy | Signal Keywords |
|----------|----------------|
| zwicky-box-construction | Zwicky, morphological box, parameter matrix, value grid |
| cross-consistency-analysis | CCA, pairwise consistency, reduce combinations, filter inconsistent |
| general-morphological-analysis | GMA, Ritchey, iterative morphological, complete analysis |
| design-space-mapping | design space, coverage, explored regions, visualization |
| parameter-variation | one-factor, parameter sweep, sensitivity, variation |

## Manifest

### Strategies

| Strategy | Description |
|----------|-------------|
| zwicky-box-construction | Classic Zwicky box: parameter identification → value enumeration → matrix construction |
| cross-consistency-analysis | CCA: pairwise consistency checking to reduce solution space 90-99% |
| general-morphological-analysis | Ritchey GMA: complete iterative morphological process |
| design-space-mapping | Visualize explored/unexplored regions of solution space |
| parameter-variation | Systematic one-factor-at-a-time parameter sweep |

### Tactics

| Tactic | Description |
|--------|-------------|
| combination-mapping | Systematically enumerate parameter dimensions and generate viable combinations (shared) |
| consistency-checking | Pairwise consistency evaluation to reduce solution space |
| white-space-identification | Identify unexplored viable regions in the morphological matrix |

### SOPs

| SOP | Description |
|-----|-------------|
| value-enumeration | Enumerate 3-5 values per parameter including extremes |
| matrix-construction | Build n-dimensional morphological matrix |
| consistency-pair-evaluation | Evaluate pairwise value consistency (logical/empirical/normative) |
| solution-space-reduction | Apply CCA to remove inconsistent combinations |
| path-generation | Generate combination paths through consistent space |
| white-space-detection | Identify matrix regions not covered by existing methods |
| combination-evaluation | Evaluate new combinations for feasibility and novelty |
| design-space-visualization | Generate structured description of design space |
| morphological-synthesis | Synthesize all morphological exploration outputs |

## Budget Table

| Strategy | web-search | web-research | paper-overview | paper-search | paper-research |
|----------|-----------|-------------|---------------|-------------|---------------|
| zwicky-box-construction | 25 | 8 | 25 | 15 | 5 |
| cross-consistency-analysis | 15 | 5 | 15 | 10 | 3 |
| general-morphological-analysis | 30 | 10 | 30 | 20 | 8 |
| design-space-mapping | 25 | 8 | 20 | 12 | 5 |
| parameter-variation | 20 | 5 | 20 | 12 | 5 |

## MCP Tools

| Tool | Server | Purpose |
|------|--------|---------|
| brave_web_search | brave-search | General web search for morphological methods |
| brave_llm_context | brave-search | Deep content extraction from web pages |
| apify/rag-web-browser | apify | Full page scraping for detailed content |
| get_paper_content | alphaxiv | Read academic paper content |
| discover_papers | alphaxiv | Find relevant research papers |
| relevanceSearch | semantic-scholar | Search academic literature |
| paper | semantic-scholar | Get paper details |
| citations | semantic-scholar | Trace citation networks |

## Context Management

- Each strategy tracks its own budget via State Ledger
- Strategies MUST NOT exceed allocated budget
- Campaign monitors cumulative spend across all strategies
- If a strategy exhausts budget before meeting yield, escalate to campaign level for reallocation
- Prefer paper-overview over paper-research for initial exploration (lower cost)

## Available Tactics

| Tactic | Role |
|--------|------|
| combination-mapping | Enumerate parameter combinations (shared, from combinatorial-creativity) |
| consistency-checking | Pairwise consistency evaluation and space reduction |
| white-space-identification | Identify unexplored viable regions |

## Available SOPs

| SOP | Role |
|-----|------|
| value-enumeration | Enumerate parameter values with boundary extremes |
| matrix-construction | Build n-dimensional morphological matrix |
| consistency-pair-evaluation | Evaluate pairwise consistency |
| solution-space-reduction | Remove inconsistent combinations via CCA |
| path-generation | Generate paths through consistent space |
| white-space-detection | Detect uncovered matrix regions |
| combination-evaluation | Evaluate combinations for feasibility/novelty |
| design-space-visualization | Describe design space structure |
| morphological-synthesis | Final output synthesis |
