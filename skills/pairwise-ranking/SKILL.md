---
name: pairwise-ranking
description: Pairwise Ranking Campaign — produce global rankings through pairwise
  comparisons and voting aggregation using Bradley-Terry, Elo, TrueSkill, Condorcet,
  Borda, Schulze methods.
execution: campaign
dependencies:
  strategies:
  - coherence-diagnosis
  - collective-adjudication
  - deliberative-calibration
  - dynamic-tracking
  - efficient-exploration
  sops:
  - context-checkpoint
  - context-init
  - convergence-saturation-detection
---

# Pairwise Ranking

Produce global rankings from pairwise comparisons. This campaign orchestrates comparison collection, rating computation, multi-judge aggregation, and consistency verification to yield robust ordinal rankings with confidence estimates.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| Small N precise comparison / 5-15 options / careful calibration | deliberative-calibration |
| Large N sparse / 100+ options / can only compare subset | efficient-exploration |
| Multi-judge / committee / multi-judge / LLM judge aggregation | collective-adjudication |
| Continuous update / Elo / live rating / A/B testing | dynamic-tracking |
| Consistency audit / cycle detection / transitivity check | coherence-diagnosis |

## Manifest

### Strategies

| Strategy | Methods | When |
|----------|---------|------|
| deliberative-calibration | Bradley-Terry, Thurstone, AHP pairwise, Borda | Small N complete comparison |
| efficient-exploration | BT incomplete, TrueSkill, Active learning, Rank Centrality | Large N sparse matrix |
| collective-adjudication | Condorcet/Schulze, Borda, Kemeny-Young, Copeland | Multi-judge aggregation |
| dynamic-tracking | Elo, Glicko-2, TrueSkill 2, Whole-History Rating | Continuous rating update |
| coherence-diagnosis | Consistency Ratio, cycle enumeration, mElo | Preference consistency check |

### Tactics

| Tactic | Purpose |
|--------|---------|
| adaptive-pair-selection | Iteratively select maximally informative pairs, compare, update ratings, check convergence |
| multi-judge-aggregation | Collect independent ballots from multiple judges, aggregate, identify disagreement |
| consistency-audit-loop | Detect cycles, localize inconsistencies, request corrections, recompute |

### SOPs

| SOP | Input | Output |
|-----|-------|--------|
| pair-selector | current_ratings, comparison_history | next_pairs[] |
| comparison-executor | pair, context | judgment(winner, confidence, reasoning) |
| rating-update | judgment, current_ratings, method | updated_ratings |
| convergence-check | rating_history | converged(bool), stability_score |
| ballot-collection | candidates[], perspectives[] | ballots[] |
| aggregation-method | ballots[], method | consensus_ranking |
| cycle-detection | comparison_matrix | cycles[], transitivity_score |
| inconsistency-localization | comparison_matrix, cycles[] | problematic_pairs[] |
| ranking-synthesis | ratings, consistency_report | final_ranking |

## Budget Table (M tier)

| Dimension | Threshold |
|-----------|-----------|
| Comparison pairs | >= N*log(N) pairs (N=candidate count) |
| Judge count (collective) | >=3 independent perspectives |
| Consistency check | CR < 0.1 or equivalent threshold |
| Convergence criterion | ranking stability >= 90% |

## MCP Tools

- `mcp__wiki-vault__vault_search` — retrieve candidate descriptions and prior rankings
- `mcp__wiki-vault__vault_add_edge` — record ranking relationships
- `mcp__wiki-vault__vault_query_graph` — check existing preference edges

## Context Management

- State is maintained in a `ranking_state` ledger passed between tactics
- Each SOP receives only its required inputs (no full state leakage)
- Convergence check gates iteration termination
- Final synthesis produces the deliverable ranking artifact
