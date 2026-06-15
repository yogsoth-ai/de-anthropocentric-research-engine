---
name: evidence-based-prioritization
description: 'Strategy: 基于证据强度的 AHRQ PiCMe 评估——用文献证据质量驱动 gap 优先级'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: gap-prioritization
tactics:
- scoring-matrix-construction
sops:
- ahrq-picme-assessment
- importance-scoring
- priority-synthesis
dependencies:
  tactics:
  - hypothesis-formation-scoring-matrix-construction
  sops:
  - gap-normalization
  - priority-synthesis
---

# Evidence-Based Prioritization

基于证据强度的优先级评估：用 AHRQ PiCMe 框架的六个维度系统评估每个 gap 背后的文献证据质量，让证据最薄弱、影响最大的 gap 浮出水面。

## 适用场景

- gap 来自严谨的文献调研（有明确的引用支撑）
- 需要向学术同行或资助机构解释优先级决策
- 研究领域有成熟的证据分级体系（医学、生物、部分 CS 子领域）
- 希望优先攻击"证据空白最大"而非"最热门"的 gap

## 思维框架

**核心原则**：gap 的优先级不仅取决于它有多重要，还取决于现有证据有多薄弱。证据越薄弱、重要性越高，优先级越高。

AHRQ PiCMe 六维度评估框架：

1. **Population（P）**：这个 gap 影响的群体/系统有多明确？覆盖多广？
2. **Intervention（I）**：现有干预/方法的证据质量如何？（RCT > 观察性 > 专家意见）
3. **Comparator（C）**：是否有合理的对照基线？缺乏对照是否本身就是 gap？
4. **Metrics（Me）**：结果指标是否标准化？指标缺失是否是 gap 的一部分？
5. **Evidence Strength（E）**：现有证据的一致性、样本量、方法论严谨度
6. **Evidence Gap（G）**：上述五维度中，哪些维度的证据最稀缺？

最终得分 = 重要性得分 × (1 − 证据充分度)。证据越充分的 gap，优先级反而降低（因为已有人在做）。

**关键洞察**：这个框架天然偏向"被忽视的重要问题"，而非"热门但已拥挤的问题"。

## Budget Gate

| Tier | Gap 数量 | PiCMe 维度 | 文献核查 | 最终产出 |
|------|---------|-----------|---------|---------|
| S | 3–8 | 全部 6 维度 | 每 gap ≥2 篇支撑文献 | 排序表 + 证据空白报告 |
| M | 9–15 | 全部 6 维度 | 每 gap ≥3 篇支撑文献 | 排序表 + 证据空白报告 + 前 3 gap 攻击建议 |
| L | 16–20 | 全部 6 维度 | 每 gap ≥5 篇支撑文献 | 排序表 + 详细证据图谱 + 前 5 gap 攻击建议 |

## 默认参考流

1. 调用 `gap-normalization` SOP：统一 gap 格式，提取每个 gap 的支撑文献列表
2. 调用 `ahrq-picme-assessment` SOP：对每个 gap 执行六维度评估
3. 调用 `importance-scoring` SOP：独立评估重要性（不受证据强度影响）
4. 调用 `scoring-matrix-construction` tactic：构建 gap × PiCMe维度 矩阵
5. 计算综合得分：重要性 × (1 − 证据充分度均值)
6. 调用 `priority-synthesis` SOP：生成最终排序 + 证据空白摘要

## context-checkpoint

每轮结束后记录：
- PiCMe 评估矩阵（gap × 6维度得分）
- 每个 gap 的支撑文献列表（含证据等级）
- 证据充分度综合得分
- 最终优先级排序（含得分公式）

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
