---
name: pairwise-comparison
description: 'Tactic: rank gaps through relative comparison rather than absolute scoring, suited to hard-to-quantify situations'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
- gap-pairwise-judgment
- consistency-check
- priority-synthesis
dependencies:
  sops:
  - consistency-check
  - gap-pairwise-judgment
  - priority-synthesis
  tactics:
  - hypothesis-formation-scoring-matrix-construction
---

# Pairwise Comparison

When absolute scoring is hard to perform reliably (vague gap descriptions, incomparable dimensions, large rater bias), establish a gap ranking through pairwise relative comparison, then ensure the judgments are contradiction-free via a consistency check.

## Orchestration Intent

Absolute scoring requires raters to assign a value to each gap independently, which is easily affected by anchoring effects. Relative comparison ("A is more worth prioritizing than B") has a lower cognitive load and yields more stable judgments. This tactic implements an AHP (Analytic Hierarchy Process) style pairwise-comparison flow: first collect relative judgments for all gap pairs, then check judgment consistency, and finally synthesize the final ranking.

Inconsistent judgments (such as a cycle of A>B, B>C, C>A) are detected by the consistency-check SOP and trigger a correction round, until the consistency ratio CR < 0.1.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| gap-pairwise-judgment | Make a relative-importance judgment for each gap pair (1-9 Saaty scale) | Mandatory, first step |
| consistency-check | Compute the consistency ratio (CR), identify contradictory judgment pairs | Mandatory, after each comparison round |
| priority-synthesis | Synthesize final priority weights and ranking from the pairwise-comparison matrix | Mandatory, after CR passes |

## Orchestration Pattern

**Default (standard flow)**
1. gap-pairwise-judgment: perform comparisons for all N×(N-1)/2 gap pairs, producing a comparison matrix
2. consistency-check: compute CR; if CR ≥ 0.1, flag contradictory judgment pairs and return correction suggestions
3. (If correction needed) re-call gap-pairwise-judgment for the contradictory pairs only, up to 3 rounds
4. priority-synthesis: synthesize the final ranking once CR < 0.1

**Simplified (gap count ≤ 5)**
- Same as Default, but with fewer comparison pairs (≤10 pairs), usually passing the consistency check in a single round

**Deep (gap count > 15)**
- First use scoring-matrix-construction for preliminary screening, reducing gaps to ≤15
- Then run the standard pairwise flow
- priority-synthesis additionally outputs a sensitivity analysis (which gaps' rankings are most sensitive to a single judgment change)

## Minimum Yield

- A complete N×N pairwise comparison matrix (all gap pairs judged, no gaps missing)
- A final consistency ratio CR < 0.1 (hard constraint, cannot be skipped)
- A final priority ranking (including each gap's normalized weight)
- A correction history (if contradiction correction occurred, record which judgments were modified and why)

## Yield Report

After execution, report to the calling strategy:
- Gap count / number of comparison pairs / correction rounds
- The final CR value
- The top 3 gaps and their weights
- The least stable gaps (cases where the weight gap with an adjacent gap < 0.05)

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
| consistency-check | SOP: 检验 pairwise 判断矩阵的传递一致性，识别不一致项并建议修正 |
| gap-pairwise-judgment | SOP: 对两个 gap 进行逐标准相对优先级判断，输出偏好结果 |
| priority-synthesis | SOP: 综合所有评分数据产出最终 gap 优先级列表及攻击路径建议 |

<!-- END available-tables (generated) -->
