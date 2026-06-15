---
name: decomposition-formulation
description: 'Strategy: 将复杂研究问题分解为可独立回答的子问题层级'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- sub-question-decomposition
sops:
- sub-question-generation
- dependency-mapping
- answering-sequence-design
- finer-criteria-check
dependencies:
  tactics:
  - sub-question-decomposition
  sops:
  - finer-criteria-check
---

# Decomposition Formulation

将复杂研究问题分解为可独立回答的子问题 — 当单一实验无法回答整个问题时。

## 适用场景

- 问题复杂度高，涉及多个独立维度
- 单一实验/研究无法完整回答
- 需要分阶段推进的研究计划
- 问题包含多个因果链或多个变量组

## 思维框架

核心逻辑: 复杂问题 = 多个简单问题的组合。找到正确的分解方式，使每个子问题可以独立回答，且子问题的答案组合起来能回答主问题。

### 分解原则

- **MECE**: 子问题互斥且穷尽（Mutually Exclusive, Collectively Exhaustive）
- **独立性**: 每个子问题可以独立设计研究方案
- **覆盖性**: 所有子问题的答案组合 = 主问题的答案
- **可操作性**: 每个子问题都是可研究的（不是哲学问题）

### 分解维度

- 按因果链: 前因 → 机制 → 结果
- 按变量: 每个关键变量一个子问题
- 按条件: 不同边界条件下的表现
- 按层级: 宏观 → 中观 → 微观
- 按时序: 短期 → 中期 → 长期效应

## Budget Gate

| Tier | 子问题数 | 依赖分析 | 序列设计 |
|------|---------|---------|---------|
| S | ≥2 子问题 | 基本依赖识别 | 建议顺序 |
| M | ≥3 子问题 | 依赖图 + 关键路径 | 最优序列 + 并行机会 |
| L | ≥5 子问题 | 完整依赖图 + 循环检测 | 多路径方案 + 资源分配 |

## 默认参考流

1. 分析主 RQ 的复杂度维度
2. 选择分解策略（按因果/变量/条件/层级/时序）
3. 生成子问题（sub-question-generation SOP）
4. 验证 MECE 和覆盖性
5. 映射依赖关系（dependency-mapping SOP）
6. 设计回答顺序（answering-sequence-design SOP）
7. 对每个子问题进行 FINER 检验

## context-checkpoint

Strategy 完成后必须调用 context-checkpoint，记录:
- 主 RQ 及其复杂度分析
- 选择的分解策略
- 子问题列表 + 独立性论证
- 依赖图
- 建议回答序列

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| sub-question-decomposition | Tactic: 将主问题分解为可独立回答的子问题层级 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| finer-criteria-check | SOP: FINER 5 项标准逐项检验研究问题质量 |

<!-- END available-tables (generated) -->
