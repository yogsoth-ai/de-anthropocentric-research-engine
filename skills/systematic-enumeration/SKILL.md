---
name: systematic-enumeration
description: Systematic Enumeration Campaign — exhaustive coverage analysis to discover overlooked solution spaces via benchmark sweep, method-problem matrix, ablation, and failure taxonomy
execution: campaign
used-by: creative-ideation
---

# Systematic Enumeration

Exhaustive coverage analysis to discover overlooked solution spaces via benchmark sweep, method-problem matrix, ablation, and failure taxonomy.

## Strategy Routing

| Strategy | Signal Keywords |
|----------|----------------|
| benchmark-sweep | benchmark, state-of-the-art, survey, catalog, inventory, known solutions |
| method-problem-matrix | matrix, crossing, intersection, method×problem, unexplored combinations |
| ablation-brainstorm | ablation, remove, component, dependency, what-if-removed |
| failure-taxonomy | failure, fault, error, breakdown, failure mode, robustness |
| factorial-ideation | factor, level, DOE, design of experiments, combination, factorial |

## Manifest

### Strategies

| Strategy | Description |
|----------|-------------|
| benchmark-sweep | Systematically scan all known solutions, identify gaps |
| method-problem-matrix | Cross method×problem matrix, find unexplored intersections |
| ablation-brainstorm | Remove components one by one, observe system changes |
| failure-taxonomy | Catalog all failure modes, generate targeted solutions |
| factorial-ideation | DOE thinking: identify factors, define levels, explore combinations |

### Tactics

| Tactic | Description |
|--------|-------------|
| evaluation-filtering | Multi-dimensional evaluation and tiered filtering (shared) |
| coverage-analysis | Benchmark inventory → method-problem crossing → intersection evaluation |
| gap-driven-generation | Coverage gap detection → failure-driven generation → factor-level design |

### SOPs

| SOP | Description |
|-----|-------------|
| benchmark-inventory | Catalog all known solutions/methods in domain |
| method-problem-crossing | Build method×problem cross-reference matrix |
| intersection-evaluation | Evaluate exploration status of each matrix cell |
| ablation-execution | Remove components one by one, record responses |
| dependency-identification | Identify critical dependencies from ablation results |
| failure-mode-cataloging | Systematically catalog failure modes |
| failure-driven-generation | Generate solutions targeting each failure mode |
| factor-level-design | Identify factors and levels, design experiment matrix |
| coverage-gap-detection | Detect uncovered regions in solution space |
| enumeration-synthesis | Synthesize all systematic enumeration outputs |

## Budget Table

| Strategy | web-search | web-research | paper-overview | paper-search | paper-research |
|----------|-----------|-------------|---------------|-------------|---------------|
| benchmark-sweep | 30 | 10 | 30 | 20 | 8 |
| method-problem-matrix | 25 | 8 | 25 | 15 | 5 |
| ablation-brainstorm | 20 | 5 | 20 | 12 | 5 |
| failure-taxonomy | 25 | 10 | 25 | 15 | 5 |
| factorial-ideation | 20 | 8 | 20 | 12 | 5 |

## MCP Tools

| Tool | Server | Purpose |
|------|--------|---------|
| brave_web_search | brave-search | General web search for methods and examples |
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
| evaluation-filtering | Multi-dimensional evaluation and tiered filtering (shared) |
| coverage-analysis | Benchmark inventory → crossing → intersection evaluation |
| gap-driven-generation | Gap detection → failure-driven generation → factor-level design |

## Available SOPs

| SOP | Role |
|-----|------|
| benchmark-inventory | Catalog all known solutions in domain |
| method-problem-crossing | Build method×problem cross-reference matrix |
| intersection-evaluation | Evaluate exploration status of matrix cells |
| ablation-execution | Component removal and response recording |
| dependency-identification | Critical dependency extraction |
| failure-mode-cataloging | Systematic failure mode classification |
| failure-driven-generation | Targeted solution generation per failure mode |
| factor-level-design | Factor/level identification and experiment matrix |
| coverage-gap-detection | Uncovered region detection and prioritization |
| enumeration-synthesis | Final synthesis of all enumeration outputs |
