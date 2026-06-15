---
name: framework-guided-formulation
description: 'Strategy: 选择 RQ 框架（PICO/SPIDER/SPICE/ECLIPSE）并系统应用'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
- framework-selection-and-application
- question-refinement-loop
sops:
- framework-matching
- pico-application
- spider-application
- spice-application
- eclipse-application
- finer-criteria-check
dependencies:
  tactics:
  - framework-selection-and-application
  - question-refinement-loop
---

# Framework-Guided Formulation

选择最适合的 RQ 框架并系统应用 — 当研究类型明确时，用标准框架结构化问题。

## 适用场景

- 研究类型明确（量化/定性/混合/评估）
- 有对应的标准框架可用
- 需要确保问题的各组件完整

## 思维框架

核心逻辑: 不同研究类型有不同的"好问题"标准。框架是前人总结的"好问题应该包含哪些组件"的清单。选对框架 → 填充每个组件 → 自然得到结构化的问题。

### 框架选择指南

| 研究类型 | 推荐框架 | 核心组件 |
|----------|---------|---------|
| 量化/干预研究 | PICO/PICOTS | Population, Intervention, Comparison, Outcome (+Time, Setting) |
| 定性研究 | SPIDER | Sample, Phenomenon of Interest, Design, Evaluation, Research type |
| 评估研究 | SPICE | Setting, Perspective, Intervention, Comparison, Evaluation |
| 混合方法 | ECLIPSE | Expectation, Client group, Location, Impact, Professionals, Service |

### 框架应用原则

- 每个组件必须有明确填充（不留空）
- 填充内容必须具体（不是"相关人群"而是"18-65岁的2型糖尿病患者"）
- 如果某组件不适用，显式说明为什么不适用

## Budget Gate

| Tier | 框架候选 | 框架应用 | FINER 检验 | 产出 |
|------|---------|---------|-----------|------|
| S | ≥2 框架比较 | 选定框架全组件填充 | 5 项全通过 | ≥1 RQ |
| M | ≥3 框架比较 | 选定框架全组件 + 替代框架对比 | 5 项 + success criteria | ≥2 RQ |
| L | ≥4 框架比较 | 多框架并行应用 + 最优选择 | 5 项 + criteria + 敏感性 | ≥3 RQ |

## 默认参考流

1. 确定研究类型（量化/定性/混合/评估）
2. 匹配候选框架（framework-matching SOP）
3. 应用选定框架（pico/spider/spice/eclipse-application SOP）
4. FINER 检验（finer-criteria-check SOP）
5. 未通过项修正 → 重新检验
6. 产出最终 RQ

## context-checkpoint

Strategy 完成后必须调用 context-checkpoint，记录:
- 选定的框架及理由
- 框架各组件的填充内容
- FINER 检验结果
- 最终 RQ 表述

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| framework-selection-and-application | Tactic: 选择最适合的 RQ 框架并系统应用 |
| question-refinement-loop | Tactic: 迭代精化研究问题直到通过 FINER 5 项标准 |

<!-- END available-tables (generated) -->
