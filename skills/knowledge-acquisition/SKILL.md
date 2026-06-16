---
name: knowledge-acquisition
description: 'Research Knowledge Acquisition Engine with 5 campaigns (literature-survey,
  patent-mining, benchmark-archaeology, meta-analysis, baseline-establishment). Use
  this skill whenever a user needs to systematically acquire research knowledge —
  academic literature, patent landscapes, benchmark evaluations, cross-study statistical
  synthesis, or SOTA performance baselines. Pre-condition: north-star-crystallization
  must be complete.'
dependencies:
  campaigns:
  - baseline-establishment
  - benchmark-archaeology
  - literature-survey
  - meta-analysis
  - patent-mining
---

# Knowledge Acquisition

Systematic research knowledge acquisition engine. Five campaigns, each a self-contained autonomous research activity domain. You provide a research intent — the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Pre-condition

North-star-crystallization must be complete before entering any campaign. Research intent must be fully crystallized.

## Four-Level Hierarchy

```
ENTRY.md (this file)
  → Campaign (5): self-contained research activity domain
    → Strategy: selected by analysis purpose/intent
      → Tactic: multi-step orchestration pattern (reusable across strategies)
        → SOP: single operation (import or subagent)
```

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| literature review, survey, paper search, PRISMA, snowball | → literature-survey |
| patent analysis, prior art, white space, claims, IPC | → patent-mining |
| benchmark analysis, evaluation methods, metric flaws, leaderboards, saturation | → benchmark-archaeology |
| cross-study statistical synthesis, effect size, heterogeneity, publication bias, GRADE | → meta-analysis |
| SOTA compilation, performance comparison, baseline reproduction, progress curves | → baseline-establishment |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **Serial**: literature-survey → baseline-establishment (survey first, then collect performance data)
- **Parallel**: patent-mining ∥ benchmark-archaeology (independent analyses on the same topic)
- **Conditional**: literature-survey → IF gaps found → meta-analysis (evidence synthesis on identified gaps)

The orchestrator decides composition based on the crystallized North Star statement.

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries, read_files_from_github_repository |
| semantic-scholar | ss_paper, ss_paper_batch, ss_references, ss_citations, ss_recommendations, ss_relevance_search, ss_author, ss_author_papers |

## Context Management Integration

- **Campaign start**: context-init (load/create campaign context file)
- **After each strategy completes**: context-checkpoint (append findings to campaign context file)
- **One context file per campaign**: all strategy outputs accumulate in a single campaign-scoped file

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research |
| literature-engine | literature-overview + literature-search + literature-research |
| subagent-spawning | Subagent dispatch conventions |
| context-management | Checkpoint protocol |

<!-- BEGIN available-tables (generated) -->

## Available Campaigns

Optional, no fixed order; the final leaf is always a sop.

| Campaign | When to use |
| --- | --- |
| baseline-establishment | SOTA Performance Baseline Campaign — 5 strategies for systematically collecting, standardizing, and analyzing performance data across methods. Produces standardized comparison tables, progress curves, and headroom analysis. |
| benchmark-archaeology | Evaluation Methodology Archaeology Campaign — 5 strategies for systematic analysis of AI/ML benchmarks, metrics, and leaderboards. Reveals construct validity issues, saturation, data contamination, and evaluation protocol inconsistencies. |
| literature-survey | Autonomous Literature Survey Campaign — 5 research paradigms (scoping, systematic, deep, narrative, snowball) with quantitative budget enforcement. Selects and executes the right survey paradigm based on research intent. |
| meta-analysis | Cross-Study Statistical Synthesis Campaign — 5 strategies for systematic collection and methodological planning of multi-study evidence synthesis. Covers pairwise, network, cumulative meta-analysis, heterogeneity investigation, and bias detection. Stops at protocol design (no computation). |
| patent-mining | Systematic Patent Analysis Campaign — 5 strategies for patent landscape analysis, prior art search, white space identification, competitive intelligence, and claim analysis. Produces structured patent intelligence reports. |

<!-- END available-tables (generated) -->
