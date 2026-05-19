---
name: comparative-formulation
description: "Strategy: 构建对比性研究问题 — A vs B 的系统化比较"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
  - framework-selection-and-application
sops:
  - framework-matching
  - pico-application
  - finer-criteria-check
  - success-criteria-definition
dependencies:
  skills:
    - context-management
    - subagent-spawning
---

# Comparative Formulation

构建对比性研究问题 — 当研究需要比较 A vs B 时，系统化地构建公平、有意义的比较。

## 适用场景

- 需要比较两种方法/条件/群体
- 假设涉及"X 比 Y 更好/不同"
- 需要确保比较的公平性和有效性

## 思维框架

核心逻辑: 好的比较研究问题需要明确四个要素 — 比较什么（对象）、在什么维度上比较（指标）、在什么条件下比较（控制）、什么算"不同"（阈值）。

### 比较设计原则

- **公平性**: 比较条件对双方公平（不是 strawman）
- **维度明确**: 在哪个/哪些维度上比较
- **控制变量**: 除了比较对象外，其他条件相同
- **效应量**: 不只是"有没有差异"，还要"差异多大才有意义"

### 比较类型

| 类型 | 示例 | 关键考虑 |
|------|------|---------|
| 方法对比 | Method A vs Method B | 实现公平性、数据集选择 |
| 条件对比 | With X vs Without X | 控制变量、混淆因素 |
| 群体对比 | Group A vs Group B | 匹配、选择偏差 |
| 时间对比 | Before vs After | 历史效应、成熟效应 |

## Budget Gate

| Tier | 比较设计 | 公平性论证 | 产出 |
|------|---------|-----------|------|
| S | 比较对象 + 维度明确 | 基本公平性声明 | ≥1 对比 RQ |
| M | + 控制变量 + 效应量 | 公平性论证 + 潜在偏差识别 | ≥2 对比 RQ |
| L | + 多维度 + 敏感性 | 完整公平性分析 + 偏差缓解策略 | ≥3 对比 RQ |

## 默认参考流

1. 确定比较对象（A 和 B 是什么）
2. 确定比较维度（在什么指标上比较）
3. 确定控制条件（保持什么不变）
4. 论证公平性（比较是否 fair）
5. 用 PICO 框架结构化（C 组件是核心）
6. FINER 检验
7. 定义 success criteria（什么算"有意义的差异"）

## context-checkpoint

Strategy 完成后必须调用 context-checkpoint，记录:
- 比较对象及选择理由
- 比较维度
- 公平性论证
- 最终对比性 RQ
