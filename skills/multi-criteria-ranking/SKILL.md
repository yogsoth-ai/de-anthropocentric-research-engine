---
name: multi-criteria-ranking
description: 'Strategy: multi-dimensional weighted scoring and ranking — decompose a gap into independent sub-questions, then recombine into a priority list'
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

# Multi-Criteria Ranking

Multi-dimensional weighted scoring and ranking: decompose the composite question "which gap is better" into several independent dimensions, score each separately, then recombine into a final ranking via weighted summation.

## When to Use

- The number of gaps is between 5 and 20
- A systematic, explainable basis for ranking is needed
- Decision-makers need to see each dimension's score (rather than a black-box ranking)
- You will later need to explain to others why a particular gap was chosen

## Thinking Framework

**Core principle**: the reliability of complex judgments comes from decomposition, not holistic intuition.

Break "which gap is most worth attacking" into four independent sub-questions:

1. **Importance**: once this gap is filled, how far will the field advance?
2. **Feasibility**: with existing resources and methods, can it be solved within a reasonable time?
3. **Novelty**: is this gap genuinely under-explored?
4. **Impact**: how broad are the downstream effects after solving it?

Each dimension is scored independently (1–5) to avoid cross-contamination between dimensions. Weights are set by AHP (Analytic Hierarchy Process) or specified by the user. Final score = Σ(dimension score × dimension weight).

**Sensitivity check**: perturb weights by ±20%; if the ranking is unchanged the conclusion is robust; if the ranking flips it must be flagged as "weight-sensitive".

## Budget Gate

| Tier | Gap count | Scoring dimensions | Sensitivity check | Final output |
|------|---------|---------|-----------|---------|
| S | 5–8 | ≥3 dimensions | Optional | Ranking table + attack suggestions for top 2 gaps |
| M | 9–15 | ≥4 dimensions | Required | Ranking table + attack suggestions for top 3 gaps |
| L | 16–20 | ≥5 dimensions | Required (multi-weight scenarios) | Ranking table + attack suggestions for top 5 gaps + weight-sensitivity report |

## Default Reference Flow

1. Call the `gap-normalization` SOP: normalize input gaps into a standard format (ID, title, one-sentence description)
2. Call the `ahp-weighting` SOP: determine each dimension's weight (default: importance 0.35, feasibility 0.25, novelty 0.20, impact 0.20)
3. Call the four scoring SOPs in parallel (`importance-scoring`, `feasibility-scoring`, `novelty-scoring`, `impact-scoring`)
4. Call the `scoring-matrix-construction` tactic: aggregate into a scoring matrix
5. Call the `priority-sensitivity-testing` tactic: perturb weights and check ranking robustness
6. Call the `priority-synthesis` SOP: produce the final ranking + attack suggestions

## context-checkpoint

After each round, record:
- The current scoring matrix (all gaps × all dimensions)
- The current weight vector
- The sensitivity-check result (robust / weight-sensitive, annotating any flipped gap pairs)
- The current top-N ranking

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| hypothesis-formation-scoring-matrix-construction | Tactic: 编排多维度评分 SOP，为所有 gaps 构建综合评估矩阵 |
| priority-sensitivity-testing | Tactic: 扰动评分权重，检验 gap 排序对权重选择的稳健性 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| gap-normalization | SOP: 统一不同来源的 gap 格式为标准 GapRecord |

<!-- END available-tables (generated) -->
