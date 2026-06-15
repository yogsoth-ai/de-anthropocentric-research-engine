---
name: multi-criteria-ranking
description: 'Strategy: 多维度加权评分排序——将 gap 分解为独立子问题后重组为优先级列表'
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

多维度加权评分排序：将"哪个 gap 更好"这一复合问题分解为若干独立维度，分别评分后通过加权求和重组为最终排序。

## 适用场景

- gap 数量在 5–20 个之间
- 需要系统化、可解释的排序依据
- 决策者需要看到每个维度的得分（而非黑箱排序）
- 后续需要向他人解释为何选择某个 gap

## 思维框架

**核心原则**：复杂判断的可靠性来自分解，而非整体直觉。

将"哪个 gap 更值得攻击"拆解为四个独立子问题：

1. **重要性**（Importance）：这个 gap 填补后，领域会前进多少？
2. **可行性**（Feasibility）：以现有资源和方法，能在合理时间内解决吗？
3. **新颖性**（Novelty）：这个 gap 是否真正未被充分探索？
4. **影响力**（Impact）：解决后的下游效应有多广？

每个维度独立评分（1–5），避免维度间的相互污染。权重由 AHP（层次分析法）或用户指定。最终得分 = Σ(维度得分 × 维度权重)。

**敏感性检验**：权重扰动 ±20%，若排序不变则结论稳健；若排序翻转则需标记为"权重敏感"。

## Budget Gate

| Tier | Gap 数量 | 评分维度 | 敏感性检验 | 最终产出 |
|------|---------|---------|-----------|---------|
| S | 5–8 | ≥3 维度 | 可选 | 排序表 + 前 2 gap 攻击建议 |
| M | 9–15 | ≥4 维度 | 必须 | 排序表 + 前 3 gap 攻击建议 |
| L | 16–20 | ≥5 维度 | 必须（多权重场景） | 排序表 + 前 5 gap 攻击建议 + 权重敏感性报告 |

## 默认参考流

1. 调用 `gap-normalization` SOP：将输入 gaps 统一为标准格式（ID、标题、一句话描述）
2. 调用 `ahp-weighting` SOP：确定各维度权重（默认：重要性 0.35、可行性 0.25、新颖性 0.20、影响力 0.20）
3. 并行调用四个评分 SOP（`importance-scoring`、`feasibility-scoring`、`novelty-scoring`、`impact-scoring`）
4. 调用 `scoring-matrix-construction` tactic：汇总为评分矩阵
5. 调用 `priority-sensitivity-testing` tactic：扰动权重，检验排序稳健性
6. 调用 `priority-synthesis` SOP：生成最终排序 + 攻击建议

## context-checkpoint

每轮结束后记录：
- 当前评分矩阵（所有 gap × 所有维度）
- 当前权重向量
- 敏感性检验结果（稳健 / 权重敏感，标注翻转的 gap 对）
- 当前 top-N 排序

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
