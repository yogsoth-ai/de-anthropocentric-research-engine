---
name: structured-consensus
description: Structured Consensus Campaign — converge multiple perspectives into shared agreement through iterative structured dialogue using Delphi variants, NGT, RAND/UCLA, Consensus Conference methods.
execution: campaign
used-by: convergence
---

# Structured Consensus

Converge multiple independent perspectives into shared agreement through iterative structured dialogue. This campaign orchestrates Delphi variants, Nominal Group Technique, RAND/UCLA Appropriateness Method, and Consensus Conference protocols to systematically reduce disagreement while preserving legitimate dissent.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| Iterative convergence to single answer / establish guidelines / determine threshold | convergence-distillation |
| Map disagreement structure / wicked problems / value conflicts | disagreement-cartography |
| Aggregate probability judgments / technology timeline / market forecast | futures-calibration |
| Establish acceptability standards / medical guidelines / regulatory standards | appropriateness-bounding |
| Distill strongest arguments / policy deliberation / interdisciplinary dispute | argument-crystallization |

## Manifest

### Strategies

| Strategy | Method Family | Purpose |
|----------|--------------|---------|
| convergence-distillation | Classic Delphi, Modified Delphi, NGT | Iterative convergence to single answer |
| disagreement-cartography | Policy Delphi, Argument Delphi, SAST | Map disagreement structure |
| futures-calibration | Real-Time Delphi, Prediction Markets | Aggregate probability judgments |
| appropriateness-bounding | RAND/UCLA Appropriateness, Consensus Conference | Establish acceptability standards |
| argument-crystallization | Argument Delphi, Dialectical Delphi | Distill strongest arguments |

### Tactics

| Tactic | Purpose | SOPs |
|--------|---------|------|
| iterative-convergence-round | Collect → feedback → revise → check → decide | judgment-collection, feedback-distribution, consensus-measurement, round-decision |
| disagreement-mapping | Collect → cluster → extract arguments → visualize | judgment-collection, cluster-analysis, argument-extraction, disagreement-visualization |
| threshold-calibration | Adjust thresholds → observe consensus changes | threshold-sweep, consensus-classification, consensus-measurement |

### SOPs

| SOP | Input | Output |
|-----|-------|--------|
| judgment-collection | question, perspectives[] | judgments[] |
| feedback-distribution | judgments[], round_n | feedback_report |
| consensus-measurement | judgments[] | consensus_score, method_used |
| round-decision | consensus_score, round_n, stability | continue/stop |
| cluster-analysis | judgments[] | clusters[], cluster_characterization[] |
| argument-extraction | cluster, judgments[] | arguments[] |
| disagreement-visualization | clusters[], arguments[] | disagreement_map |
| threshold-sweep | judgments[], threshold_range | threshold_curve |
| consensus-classification | judgments[], threshold | consensus_items[], dissensus_items[] |
| consensus-synthesis | rounds_history, final_judgments | consensus_report |

## Budget Table (M Tier)

| Parameter | Constraint |
|-----------|-----------|
| Perspectives/experts | >=4 independent perspectives |
| Iteration rounds | 2-4 rounds (until consensus threshold or stability) |
| Consensus threshold | >=70% agreement or IQR <= 1 |
| Dissent documentation | All non-consensus items must document reasons |

## MCP Tools

- `mcp__semantic-scholar__relevanceSearch` — find methodological references
- `mcp__wiki-vault__vault_search` — retrieve prior consensus results from vault

## Context Management

- Each round's judgments are stored in state and passed forward
- Feedback reports summarize prior round without exposing individual identities
- Final synthesis aggregates all rounds into a single consensus report
- Non-consensus items are explicitly documented with dissent rationale
