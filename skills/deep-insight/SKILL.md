---
name: deep-insight
description: 'Deep Insight Engine with 5 campaigns (gap-analysis, insight, boundary-analysis,
  sensitivity-analysis, problem-reformulation). Use this skill whenever a user needs
  to deeply analyze research gaps, understand root causes, probe method boundaries,
  assess assumption sensitivity, or reformulate research problems. Pre-condition:
  north-star-crystallization complete + knowledge-acquisition campaign has produced
  initial findings.'
dependencies:
  campaigns:
  - boundary-analysis
  - deep-insight-sensitivity-analysis
  - gap-analysis
  - insight
  - problem-reformulation
---

# Deep Insight

Deep insight engine — from surface phenomena to root causes, boundaries, assumptions, and the problem itself. Five campaigns, each a self-contained autonomous analysis domain. You provide a research gap or finding — the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Design Philosophy

Strategy Book mode. This file is a textbook, not a script. CC reads, internalizes principles, then autonomously constructs the analysis approach for the specific research situation.

Hard constraints only:
- **Budget Gate**: Meet the strategy's quantitative floor (±10%) before completing
- **Minimum Yield**: Per-tactic hard floors on output quality
- **HARD-GATE**: Pre-conditions must be satisfied before entry
- **Context-checkpoint**: Triggered after each strategy completes

Everything else — execution order, iteration count, tactic selection, SOP combination — is CC's autonomous decision.

## Pre-conditions

1. North-star-crystallization must be complete (research intent crystallized)
2. Knowledge-acquisition campaign must have produced initial findings (gaps, patterns, anomalies)

## Four-Level Hierarchy

```
ENTRY.md (this file)
  → Campaign (5): self-contained deep analysis domain
    → Strategy: selected by analysis purpose/intent
      → Tactic: multi-step orchestration pattern (reusable across strategies)
        → SOP: single operation (import or subagent)
```

CC can skip the tactic layer and use SOPs directly when the task is simple enough.

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| gap identification, gap classification, evidence mapping, prioritization, gap validation | → gap-analysis |
| root-cause analysis, stakeholders, tensions, HMW, assumption audit, 5 Whys | → insight |
| validity boundaries, method failure, robustness, distribution shift, scaling limits | → boundary-analysis |
| assumption ranking, sensitivity, variance decomposition, uncertainty propagation, critical path | → sensitivity-analysis |
| redefining the problem, dominant ideas, multiple perspectives, double-loop learning, wicked problems | → problem-reformulation |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **"Understand this gap deeply"**: gap-analysis → insight
- **"Is this method reliable"**: boundary-analysis → sensitivity-analysis
- **"Are we solving the wrong problem"**: problem-reformulation (may loop back to gap-analysis)
- **Full deep dive**: gap-analysis → insight → boundary-analysis → sensitivity-analysis → problem-reformulation

The orchestrator decides composition based on the research state and user intent.

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
- **CC discretion**: Additional checkpoints when information density warrants it
- **One context file per campaign**: format `context/deep-insight-[campaign]-[topic].md`

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research |
| literature-engine | literature-overview + literature-search + literature-research |
| subagent-spawning | Subagent dispatch conventions |
| context-management | Checkpoint protocol |
| north-star-crystallization | Pre-condition (research intent) |
| knowledge-acquisition | Pre-condition (initial findings) |

<!-- BEGIN available-tables (generated) -->

## Available Campaigns

Optional, no fixed order; the final leaf is always a sop.

| Campaign | When to use |
| --- | --- |
| boundary-analysis | Boundary Analysis Campaign — probe where methods fail, map validity envelopes, test robustness, catalog failure modes, detect scaling limits. 5 strategies, 3 tactics, 11 subagent SOPs. |
| deep-insight-sensitivity-analysis | Sensitivity Analysis Campaign — identify which assumptions are most critical by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition, assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics, 11 subagent SOPs. |
| gap-analysis | Gap Analysis Campaign — identify, classify, validate, and prioritize research gaps via systematic evidence mapping. 5 strategies (gap-identification, gap-classification, gap-validation, gap-prioritization, gap-synthesis), 3 tactics, 12 subagent SOPs. |
| insight | Insight Campaign — deep root-cause analysis of why research gaps persist. 5 strategies (root-cause-drilling, stakeholder-mapping, tension-mining, question-reformulation, assumption-audit), 4 tactics, 13 subagent SOPs. |
| problem-reformulation | Problem Reformulation Campaign — question the problem itself. Escape dominant ideas, reframe from multiple perspectives, apply dialectical inquiry, assess wickedness, discover appreciative alternatives. 5 strategies, 3 tactics, 10 subagent SOPs. |

<!-- END available-tables (generated) -->
