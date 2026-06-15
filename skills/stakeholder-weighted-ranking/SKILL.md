---
name: stakeholder-weighted-ranking
description: 'Strategy: 按利益相关者视角加权——同一 gap 在不同视角下权重不同，最终取共识排序'
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

按利益相关者视角加权排序：识别所有相关方（研究者、工程师、政策制定者、终端用户等），为每类相关方构建独立的权重向量，分别排序后取共识。

## 适用场景

- 研究涉及多方利益相关者（如医疗 AI：临床医生 + 患者 + 监管机构）
- 不同相关方对"重要性"的定义存在根本分歧
- 需要在多方之间建立共识或展示不同视角的排序差异
- 资助机构或合作方需要看到自己视角下的优先级

## 思维框架

**核心原则**：没有客观的"最重要 gap"，只有"对谁最重要"。

流程分三层：

**第一层：相关方识别**
列出所有会受到研究结果影响的群体。每类相关方有不同的价值函数——工程师重视可行性，政策制定者重视影响力，学术研究者重视新颖性。

**第二层：视角内排序**
对每类相关方，使用与 multi-criteria-ranking 相同的四维度评分，但权重向量不同。例如：
- 学术研究者：新颖性 0.40、重要性 0.30、影响力 0.20、可行性 0.10
- 工程师：可行性 0.40、影响力 0.30、重要性 0.20、新颖性 0.10
- 政策制定者：影响力 0.45、重要性 0.35、可行性 0.15、新颖性 0.05

**第三层：共识合并**
Borda count 或加权平均各视角排序，识别"跨视角稳健的 top gap"（所有相关方都认为重要）和"视角分歧 gap"（某些相关方高度重视，其他人不在意）。

**关键洞察**：视角分歧本身是信息——分歧大的 gap 可能需要先做利益对齐，而非直接攻击。

## Budget Gate

| Tier | Gap 数量 | 相关方数量 | 共识方法 | 最终产出 |
|------|---------|-----------|---------|---------|
| S | 5–10 | 2–3 类 | 简单平均 | 各视角排序 + 共识 top-3 |
| M | 11–20 | 3–5 类 | Borda count | 各视角排序 + 共识 top-5 + 分歧分析 |
| L | 20+ | 5+ 类 | 加权 Borda + 敏感性 | 完整视角矩阵 + 共识排序 + 分歧热图 |

## 默认参考流

1. 调用 `gap-normalization` SOP：统一 gap 格式
2. 识别相关方类别（CC 自主判断或用户指定）
3. 为每类相关方调用 `ahp-weighting` SOP：生成该视角的权重向量
4. 对每类相关方并行执行四维度评分（`importance-scoring`、`feasibility-scoring`、`novelty-scoring`、`impact-scoring`）
5. 调用 `scoring-matrix-construction` tactic：构建 gap × 相关方 × 维度 三维矩阵
6. 调用 `priority-sensitivity-testing` tactic：检验相关方权重变化对共识排序的影响
7. 调用 `priority-synthesis` SOP：Borda count 合并 → 共识排序 + 分歧报告

## context-checkpoint

每轮结束后记录：
- 相关方列表及其权重向量
- 各相关方视角下的 gap 排序
- 共识排序（Borda 得分）
- 高分歧 gap 列表（标注分歧来源）

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
