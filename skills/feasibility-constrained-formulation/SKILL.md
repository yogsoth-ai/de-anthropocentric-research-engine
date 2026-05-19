---
name: feasibility-constrained-formulation
description: "Strategy: 在资源约束下重塑研究问题 — pragmatic 调整保持核心价值"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
  - question-refinement-loop
sops:
  - scope-assessment
  - finer-criteria-check
  - success-criteria-definition
dependencies:
  skills:
    - context-management
    - subagent-spawning
---

# Feasibility-Constrained Formulation

在约束下重塑研究问题 — 当理想问题超出可用资源时，pragmatic 地调整问题使其可行，同时保持核心研究价值。

## 适用场景

- 理想的研究问题超出可用资源（时间/数据/计算/人力）
- 需要在 ambition 和 feasibility 之间做 trade-off
- 有明确的约束条件（deadline、budget、数据可得性）

## 思维框架

核心逻辑: 约束不是敌人，是设计参数。好的约束下重塑 = 找到"在这些约束内能回答的最有价值的问题"。

### 约束类型

| 约束 | 调整策略 | 示例 |
|------|---------|------|
| 时间不足 | 缩小范围 / 用 proxy 指标 | 3 个月 → 只做 pilot study |
| 数据不可得 | 换数据源 / 换研究对象 | 无法获取 X → 用公开数据集 Y |
| 计算资源不足 | 简化方法 / 缩小规模 | 无法训练大模型 → 用 fine-tuning |
| 专业知识不足 | 缩小领域 / 合作 | 不懂生物 → 聚焦计算部分 |

### 调整原则

- **保核心**: 调整范围和方法，但保持核心研究问题的本质
- **用 proxy**: 如果直接测量不可行，找合理的 proxy 指标
- **分阶段**: 大问题拆成 pilot → full study
- **明确 trade-off**: 显式说明因约束放弃了什么

## Budget Gate

| Tier | 约束分析 | 调整方案 | 产出 |
|------|---------|---------|------|
| S | 列出主要约束 | 1 个调整方案 | 可行的 RQ |
| M | 约束分类 + 影响评估 | 2-3 个调整方案 + 比较 | 最优可行 RQ + trade-off 声明 |
| L | 完整约束图 + 优先级 | 多方案 + Pareto 分析 | 约束下最优 RQ + 分阶段计划 |

## 默认参考流

1. 列出所有约束条件（资源、时间、数据、能力）
2. 评估每个约束对理想 RQ 的影响
3. 设计调整方案（缩小/proxy/分阶段）
4. 评估调整后 RQ 是否仍有价值
5. FINER 检验（特别关注 F = Feasible）
6. 定义 success criteria
7. 显式声明 trade-off

## context-checkpoint

Strategy 完成后必须调用 context-checkpoint，记录:
- 约束条件列表
- 理想 RQ vs 调整后 RQ
- 调整策略及理由
- Trade-off 声明
- 最终可行 RQ
