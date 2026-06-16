---
name: creative-ideation
description: Creative Generation Engine — transforms research hypotheses into diverse
  solution spaces via 10 parallel creativity campaigns spanning structural, analogical,
  destructive, and combinatorial methods.
execution: entry
pre-conditions:
- north-star-crystallization (research intent crystallized)
- hypothesis-formation (at least 1 testable hypothesis or precise research question)
dependencies:
  campaigns:
  - assumption-destruction
  - biomimicry
  - combinatorial-creativity
  - cross-domain-discovery
  - lateral-thinking
  - morphological-exploration
  - perspective-forcing
  - structural-deconstruction
  - synectics
  - systematic-enumeration
  sops:
  - creative-ideation-paper-overview
  - creative-ideation-paper-research
  - creative-ideation-paper-search
  - creative-ideation-web-research
  - creative-ideation-web-search
---

# Creative Ideation

## Campaign Routing

| Signal Keywords | Route To |
|----------------|----------|
| SCAMPER, TRIZ, component surgery, structural transformation, function trimming | → structural-deconstruction |
| Cross-domain, analogical transfer, bisociation, random stimulus, forced connection | → cross-domain-discovery |
| Assumption negation, reverse brainstorming, worst method, anti-benchmark | → assumption-destruction |
| Biomimicry, biological analogy, natural strategies, BioTRIZ, ecosystem patterns | → biomimicry |
| Analogy, metaphor, excursion method, personal analogy, symbolic compression | → synectics |
| Morphological analysis, Zwicky box, CCA, dimension combination, design space | → morphological-exploration |
| PO, lateral thinking, concept fan, random entry, challenge operation | → lateral-thinking |
| Concept blending, blending, emergence, multi-level combination, function redistribution | → combinatorial-creativity |
| Perspective switching, six hats, role play, constraint injection, temporal projection | → perspective-forcing |
| Enumeration, coverage analysis, method matrix, ablation, failure taxonomy | → systematic-enumeration |

## Multi-Campaign Orchestration

When the research problem warrants broad creative exploration, CC may invoke multiple campaigns in parallel. Four natural cluster families:

| Cluster | Campaigns | When |
|---------|-----------|------|
| Analogy family (Analogy) | cross-domain-discovery + biomimicry + synectics | Problem benefits from external domain transfer |
| Combinatorial family (Combinatorial) | structural-deconstruction + morphological-exploration + combinatorial-creativity | Problem has decomposable structure |
| Disruptive family (Disruptive) | assumption-destruction + lateral-thinking + perspective-forcing | Problem is stuck in dominant paradigm |
| Coverage family (Coverage) | systematic-enumeration + morphological-exploration | Need exhaustive space mapping |

**Comprehensive divergence**: Invoke 3-5 campaigns based on problem characteristics. Each campaign executes independently with its own context file. Results aggregated at ENTRY level.

CC decides:
- Which campaigns to invoke (1 or many)
- Execution order (parallel or sequential)
- When to cross-pollinate between campaign outputs
- When to stop (saturation-detection signals)

## Four-Level Hierarchy

```
ENTRY.md (this file)
  └── Campaign (10) — self-contained creative activity domain
        └── Strategy (5 per campaign) — iterative framework with budget + state ledger
              └── Tactic (2-3 per campaign) — SOP combination principle
                    └── SOP — single operation (subagent or import)
```

## MCP Tools

| Server | Tools |
|--------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries |
| semantic-scholar | paper, paperBatch, references, citations, recommendations, relevanceSearch |

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research SOPs |
| literature-engine | paper-overview + paper-search + paper-research SOPs |
| subagent-spawning | Subagent dispatch conventions (spawn-agent skill) |
| context-management | Checkpoint protocol (context-init, context-checkpoint) |

## Context Management

- **Campaign start**: `context-init` — load or create campaign context file
- **After each strategy**: `context-checkpoint` — append strategy output to campaign file
- **CC discretion**: Additional checkpoints when information density warrants it

Context file naming: `context/creative-ideation-[campaign]-[topic].md`

## Execution Boundary

This engine STOPS at idea generation. Its output is a structured set of diverse ideas with:
- Description (what the idea is)
- Source method (which campaign/strategy/SOP produced it)
- Novelty assessment (BREAKTHROUGH / HIGH / MODERATE / INCREMENTAL)
- Feasibility initial judgment (not deep validation)

It does NOT:
- Converge or select (→ convergence repo)
- Validate or debate (→ validation repo)
- Design experiments (→ experiment-design repo)
- Implement or prototype

## Shared Components

### Import SOPs (5, all campaigns)

| SOP | Source | Quality Gate |
|-----|--------|-------------|
| web-search | web-browsing | Snippets only — no conclusions from snippets |
| web-research | web-browsing | Must fetch full page via apify |
| paper-overview | literature-engine | Abstract only — no methodology conclusions |
| paper-search | literature-engine | AI summary — sufficient for methodology understanding |
| paper-research | literature-engine | Full text — required for quoting results |

### Shared Subagent SOPs (9)

| SOP | Used By |
|-----|---------|
| saturation-detection | All 10 campaigns |
| novelty-scoring | All 10 campaigns |
| idea-synthesis | All 10 campaigns |
| domain-scanning | cross-domain, biomimicry, synectics, combinatorial |
| assumption-surfacing | assumption-destruction, lateral-thinking, perspective-forcing, structural-deconstruction |
| constraint-injection | perspective-forcing, lateral-thinking, structural-deconstruction, morphological-exploration |
| parameter-identification | structural-deconstruction, morphological-exploration, combinatorial-creativity, systematic-enumeration |
| po-provocation | assumption-destruction, lateral-thinking, perspective-forcing |
| random-word-stimulus | cross-domain-discovery, lateral-thinking, synectics |

### Shared Tactics (4)

| Tactic | Used By |
|--------|---------|
| analogy-extraction | cross-domain-discovery, synectics, biomimicry |
| combination-mapping | morphological-exploration, combinatorial-creativity, structural-deconstruction, systematic-enumeration |
| provocation-generation | lateral-thinking, assumption-destruction, perspective-forcing |
| evaluation-filtering | All 10 campaigns |

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| creative-ideation-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| creative-ideation-paper-research | Deep paper analysis with full text reading. Import of literature-engine/literature-research skill. Full text access — required for quoting results, verifying claims, extracting detailed methodology. |
| creative-ideation-paper-search | Mid-depth paper analysis via AI-generated summaries. Import of literature-engine/literature-search skill. Reads AI summary — sufficient for methodology understanding but not for quoting specific results. |
| creative-ideation-web-research | Deep web page analysis with full content extraction. Import of web-browsing/web-research skill. Must fetch full page via apify — no shortcuts. |
| creative-ideation-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |

## Available Campaigns

可选,无固定顺序;最终叶子终为 sop。

| Campaign | 何时用 |
| --- | --- |
| assumption-destruction | Assumption Destruction Campaign — open new solution spaces by negating, reversing, and challenging fundamental assumptions. |
| biomimicry | Biomimicry Campaign — discover transferable solutions from biological systems via Design Spiral, BioTRIZ, functional analogy, ecosystem patterns, and evolution strategies. |
| combinatorial-creativity | Combinatorial Creativity Campaign — produce emergent concepts via concept blending, multi-level bisociation, and function combination (Fauconnier-Turner) |
| cross-domain-discovery | Cross-Domain Discovery Campaign — find transferable mechanisms from unrelated fields via bisociation, analogical transfer, random stimulus, and forced bridging |
| lateral-thinking | Lateral Thinking Campaign — escape logical thinking tracks via PO/movement, random entry, concept fan, challenge, and six hats (de Bono) |
| morphological-exploration | Morphological Exploration Campaign — systematic dimension-combination enumeration to discover unexplored solution spaces via Zwicky box, CCA, and GMA |
| perspective-forcing | Perspective Forcing Campaign — discover hidden solutions by systematically switching viewpoints via roles, six hats, temporal projection, and constraint injection |
| structural-deconstruction | Decompose systems into components and reassemble via SCAMPER, SIT, TRIZ, and recombination. Campaign orchestrating 5 strategies for systematic structural transformation. |
| synectics | Synectics Campaign — systematic use of analogy and metaphor for breakthrough associations via Gordon's 4 analogy types and excursion method. |
| systematic-enumeration | Systematic Enumeration Campaign — exhaustive coverage analysis to discover overlooked solution spaces via benchmark sweep, method-problem matrix, ablation, and failure taxonomy |

<!-- END available-tables (generated) -->
