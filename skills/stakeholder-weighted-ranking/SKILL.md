---
name: stakeholder-weighted-ranking
description: 'Strategy: Weight by stakeholder perspective — the same gap carries different
  weight under different perspectives; take the consensus ranking at the end'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
- scoring-matrix-construction
- priority-sensitivity-testing
sops:
- importance-scoring
- feasibility-scoring
- novelty-scoring
- impact-scoring
- ahp-weighting
- priority-synthesis
dependencies:
  tactics:
  - hypothesis-formation-scoring-matrix-construction
  - priority-sensitivity-testing
  sops:
  - gap-normalization
---

# Stakeholder-Weighted Ranking

Rank with weights by stakeholder perspective: identify all relevant parties (researchers, engineers, policymakers, end users, etc.), construct an independent weight vector for each class of party, rank separately, and then take the consensus.

## When to Use

- The research involves multiple stakeholders (e.g., medical AI: clinicians + patients + regulators)
- Different parties have fundamentally divergent definitions of "importance"
- A consensus must be built across parties, or the ranking differences across perspectives must be shown
- A funding agency or collaborator needs to see priorities from their own perspective

## Thinking Framework

**Core principle**: there is no objective "most important gap", only "most important to whom".

The process has three layers:

**Layer 1: Stakeholder identification**
List all groups that would be affected by the research results. Each class of party has a different value function — engineers value feasibility, policymakers value impact, academic researchers value novelty.

**Layer 2: Within-perspective ranking**
For each class of party, use the same four-dimensional scoring as multi-criteria-ranking, but with a different weight vector. For example:
- Academic researchers: novelty 0.40, importance 0.30, impact 0.20, feasibility 0.10
- Engineers: feasibility 0.40, impact 0.30, importance 0.20, novelty 0.10
- Policymakers: impact 0.45, importance 0.35, feasibility 0.15, novelty 0.05

**Layer 3: Consensus merging**
Borda count or weighted-average the per-perspective rankings, identifying the "cross-perspective robust top gaps" (deemed important by all parties) and the "perspective-divergent gaps" (highly valued by some parties, ignored by others).

**Key insight**: perspective divergence is itself information — a gap with large divergence may need interest-alignment first, rather than a direct attack.

## Budget Gate

| Tier | Gap count | Party count | Consensus method | Final output |
|------|---------|-----------|---------|---------|
| S | 5–10 | 2–3 classes | Simple average | Per-perspective rankings + consensus top-3 |
| M | 11–20 | 3–5 classes | Borda count | Per-perspective rankings + consensus top-5 + divergence analysis |
| L | 20+ | 5+ classes | Weighted Borda + sensitivity | Full perspective matrix + consensus ranking + divergence heatmap |

## Default Reference Flow

1. Call the `gap-normalization` SOP: unify gap format
2. Identify stakeholder classes (CC judges autonomously or the user specifies)
3. For each class of party, call the `ahp-weighting` SOP: generate that perspective's weight vector
4. Run the four-dimensional scoring in parallel for each class of party (`importance-scoring`, `feasibility-scoring`, `novelty-scoring`, `impact-scoring`)
5. Call the `scoring-matrix-construction` tactic: build the gap × party × dimension three-dimensional matrix
6. Call the `priority-sensitivity-testing` tactic: test the effect of stakeholder weight changes on the consensus ranking
7. Call the `priority-synthesis` SOP: Borda-count merge → consensus ranking + divergence report

## context-checkpoint

After each round, record:
- Stakeholder list and their weight vectors
- The gap ranking under each stakeholder perspective
- The consensus ranking (Borda scores)
- The list of high-divergence gaps (annotated with the source of divergence)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| hypothesis-formation-scoring-matrix-construction | Tactic: orchestrate multi-dimensional scoring SOPs to build a comprehensive assessment matrix for all gaps |
| priority-sensitivity-testing | Tactic: perturb scoring weights to test the robustness of the gap ranking against weight choice |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| gap-normalization | SOP: Unify gaps from different sources into the standard GapRecord format |

<!-- END available-tables (generated) -->
