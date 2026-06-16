---
name: rapid-triage
description: 'Strategy: rapid coarse screening — two filtering rounds compress a large set of gaps into a fine-rankable candidate set'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
- scoring-matrix-construction
sops:
- gap-normalization
- importance-scoring
- feasibility-scoring
- priority-synthesis
dependencies:
  tactics:
  - hypothesis-formation-scoring-matrix-construction
  sops:
  - gap-normalization
  - priority-synthesis
---

# Rapid Triage

Rapid coarse screening: when the number of gaps is very large (50+), first use binary filtering to quickly eliminate obviously unqualified gaps, then lightly score the survivors, compressing the candidate set down to a fine-rankable size.

## When to Use

- The number of gaps is very large (50+), making full multi-dimensional scoring of each gap infeasible
- Time or compute resources are limited and a quick preliminary ranking is needed
- As a precursor step to multi-criteria-ranking or portfolio-optimization
- You need to quickly show a team "which gaps are not worth considering"

## Thinking Framework

**Core principle**: don't finely rank garbage. Eliminate first, then fine-rank.

Two filtering rounds:

**Round 1: binary filtering (Keep / Drop)**
Ask three yes/no questions about each gap:
- Is this gap within our research scope? (scope filter)
- Is this gap technically solvable (not a philosophical problem, not an unbounded problem)? (solvability filter)
- Is this gap already being adequately addressed by sufficient recent work? (novelty filter)

Any answer of "no" → Drop. Passing all three → advance to round 2.

**Round 2: light scoring (1–3 points, two dimensions)**
Score surviving gaps on only two dimensions:
- Importance (1–3): a rough estimate of field impact
- Feasibility (1–3): whether progress can be made within 6 months with existing resources

Score = importance × feasibility (max 9 points). Take top-K (K = target fine-ranking count) into the next stage.

**Key insight**: the three round-1 questions must be answered quickly (no more than 30 seconds per gap); no deep analysis allowed. Speed is the core value of this strategy.

## Budget Gate

| Tier | Input gap count | Round-1 retention rate | Round-2 output | Final output |
|------|------------|------------|---------|---------|
| S | 50–80 | ≤60% | top-15 | Candidate set + elimination-rationale summary |
| M | 81–150 | ≤50% | top-20 | Candidate set + elimination-rationale summary |
| L | 150+ | ≤40% | top-30 | Candidate set + elimination-rationale summary + category statistics |

## Default Reference Flow

1. Call the `gap-normalization` SOP: normalize gap format, generate a one-sentence summary for each gap
2. Run round-1 binary filtering: answer the three yes/no questions for each gap, mark Keep / Drop
3. Record Drop rationale (out of scope / unsolvable / already adequately researched)
4. Call the `importance-scoring` SOP on the Keep set (1–3 coarse score)
5. Call the `feasibility-scoring` SOP on the Keep set (1–3 coarse score)
6. Call the `scoring-matrix-construction` tactic: build a light scoring matrix
7. Sort by importance × feasibility, take top-K
8. Call the `priority-synthesis` SOP: output the candidate set + elimination statistics

## context-checkpoint

After each round, record:
- Round-1 filtering result (Keep/Drop counts + Drop-reason distribution)
- Round-2 scoring matrix (surviving gaps × 2 dimensions)
- Final candidate set (top-K gap list)
- Suggested next strategy (multi-criteria-ranking or portfolio-optimization)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| hypothesis-formation-scoring-matrix-construction | Tactic: 编排多维度评分 SOP，为所有 gaps 构建综合评估矩阵 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| gap-normalization | SOP: 统一不同来源的 gap 格式为标准 GapRecord |
| priority-synthesis | SOP: 综合所有评分数据产出最终 gap 优先级列表及攻击路径建议 |

<!-- END available-tables (generated) -->
