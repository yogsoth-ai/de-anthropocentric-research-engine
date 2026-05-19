---
name: scoring-matrix-construction
description: "Tactic: 编排多维度评分 SOP，为所有 gaps 构建综合评估矩阵"
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
  - importance-scoring
  - feasibility-scoring
  - novelty-scoring
  - impact-scoring
  - ahrq-picme-assessment
dependencies:
  skills:
    - subagent-spawning
---

# Scoring Matrix Construction

编排多个评分维度 SOP，为每个 gap 构建多维度综合评估矩阵，作为排序决策的定量基础。

## 编排意图

单一维度评分容易产生偏差（例如纯按"重要性"排序会忽略可行性）。本 tactic 并行或串行调用各评分 SOP，在同一矩阵中对比所有 gaps 的多个维度得分，使优先级判断基于系统化证据而非直觉。

CC 根据 topic tier 选择覆盖维度数量；每个维度评分由专属 SOP 负责；评分完成后，CC 将各 SOP 产出汇总为单一矩阵格式。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| importance-scoring | 评估 gap 对领域的战略重要性（0-10） | 所有 tier 必选 |
| feasibility-scoring | 评估当前可用资源/方法下攻克 gap 的可行性（0-10） | 所有 tier 必选 |
| novelty-scoring | 评估 gap 的研究新颖性和原创贡献潜力（0-10） | 所有 tier 必选 |
| impact-scoring | 评估研究产出的潜在引用/应用影响（0-10） | M/L tier 增加 |
| ahrq-picme-assessment | 使用 AHRQ PiCMe 框架对临床/应用型 gap 做结构化评估 | L tier 或涉及 biomedical/health 领域时 |

## 编排模式

**Simplified（S tier，3 dims）**
- 调用：importance-scoring、feasibility-scoring、novelty-scoring
- 矩阵：gaps × 3 维度
- 并行执行所有 SOP，汇总结果

**Default（M tier，4 dims）**
- 调用：importance-scoring、feasibility-scoring、novelty-scoring、impact-scoring
- 矩阵：gaps × 4 维度
- 并行执行前 4 个 SOP，汇总结果

**Deep（L tier，5 dims + PiCMe）**
- 调用：全部 5 个 SOP
- 矩阵：gaps × 5 维度 + PiCMe 结构化评估附录
- 先并行执行前 4 个 SOP，PiCMe 串行在后（依赖领域确认）

## Minimum Yield

- 完整矩阵：所有 gaps × 所有维度均已填写得分（无空格）
- 每个评分单元均附有 1-2 句评分理由
- 矩阵包含加权合计列（默认等权重，除非上游提供权重）
- 产出格式：Markdown 表格 + 每个 gap 的评分摘要段落

## Yield Report

执行结束后向调用方 strategy 报告：
- 覆盖 gap 数量 / 评分维度数
- 得分分布（最高/最低/中位数）
- 评分差异最大的维度（供 sensitivity-testing 优先扰动）
- 评分置信度：哪些 gap 证据充分，哪些需要补充文献
