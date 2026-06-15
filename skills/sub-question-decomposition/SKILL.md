---
name: sub-question-decomposition
description: 'Tactic: 将主问题分解为可独立回答的子问题层级'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- sub-question-generation
- dependency-mapping
- answering-sequence-design
dependencies:
  sops:
  - answering-sequence-design
  - dependency-mapping
  - sub-question-generation
---

# Sub-Question Decomposition

将主问题分解为可独立回答的子问题层级 — 当问题太复杂无法一次回答时。

## 编排意图

将"分解复杂问题"结构化为：生成子问题 → 映射依赖 → 设计回答顺序。三步依次执行，每步产出是下步输入。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| sub-question-generation | 将主问题分解为子问题 | 第一步，必调 |
| dependency-mapping | 映射子问题间的依赖关系 | 子问题生成后 |
| answering-sequence-design | 设计最优回答顺序 | 依赖图完成后 |

## 编排模式

**串行模式（唯一模式）**:
1. sub-question-generation → 子问题列表 + 独立性论证
2. dependency-mapping → 依赖图 + 关键路径
3. answering-sequence-design → 执行序列 + 并行机会

每一步严格依赖前一步的输出，不可并行。

## Minimum Yield

- ≥3 个子问题（M tier）
- 每个子问题有独立性论证
- 依赖图（无循环依赖）
- 建议回答序列 + 并行机会识别

## Yield Report

执行完成后报告:
- 生成的子问题数量
- 依赖关系数量
- 关键路径长度
- 可并行的子问题组
