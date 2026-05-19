---
name: inductive-hypothesis-generation
description: "Strategy: 从数据/观察归纳提炼假设"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
  - anomaly-driven-abduction
  - falsifiability-audit
sops:
  - anomaly-characterization
  - explanation-generation
  - variable-identification
  - relationship-specification
  - falsifiability-check
dependencies:
  skills:
    - context-management
    - subagent-spawning
    - literature-engine
---

# Inductive Hypothesis Generation

从数据/观察归纳提炼假设：在理论空白或理论不足的领域，从经验模式中提炼规律，谨慎泛化为可测试命题。

## 适用场景

- 领域缺乏成熟理论，但积累了大量经验观察或数据模式
- 研究 gap 表现为"反复出现的现象尚无系统性解释"
- 目标是从数据中提炼规律，为后续理论建构奠基
- 探索性研究阶段，尚不清楚哪些变量重要

不适用：已有明确理论框架的领域 → 改用 deductive-hypothesis-generation。

## 思维框架

**Observe patterns → Extract regularity → Generalize cautiously → Formulate testable claim**

归纳的核心逻辑：

1. **Observe patterns**：系统整理已有观察、数据、案例中反复出现的模式（不是单次异常）
2. **Extract regularity**：识别模式背后的规律性——什么条件下出现，什么条件下不出现
3. **Generalize cautiously**：将规律从具体样本谨慎泛化——明确泛化的边界，不过度外推
4. **Formulate testable claim**：将泛化规律转化为可在新样本上检验的命题

**归纳的核心风险**：过度泛化（从有限样本跳到普遍规律）。每个归纳假设必须明确：
- 观察来自哪些样本（样本特征、来源、时间范围）
- 泛化到哪些群体（泛化范围的边界）
- 什么证据会限制或推翻泛化

## Budget Gate

| Tier | 模式覆盖 | 规律提取 | 假设产出 | 泛化边界 |
|------|---------|---------|---------|---------|
| S | ≥3 个独立观察模式 | ≥2 条规律 | ≥2 个结构化假设 | 每个假设明确样本来源 |
| M | ≥5 个独立观察模式 | ≥3 条规律 | ≥3 个结构化假设 | 泛化边界 + falsification scenario |
| L | ≥8 个独立观察模式 | ≥5 条规律 | ≥4 个结构化假设 | 完整泛化边界 + 竞争规律比较 |

## 默认参考流

1. 调用 `anomaly-characterization` SOP：系统整理已有观察/数据中的模式（含频率、条件、例外）
2. 调用 `explanation-generation` SOP（via `anomaly-driven-abduction` tactic）：为每个模式生成候选规律解释
3. 调用 `variable-identification` SOP：将规律中的构念转化为可操作变量
4. 调用 `relationship-specification` SOP：明确变量间方向性关系（含调节条件）
5. 调用 `falsifiability-check` SOP（via `falsifiability-audit` tactic）：为每个假设生成 falsification scenario + 泛化边界

## context-checkpoint

每轮结束后记录：
- 已整理的观察模式清单（模式描述、来源、出现频率）
- 提取的规律列表（规律陈述、支撑模式、例外情况）
- 当前假设草稿集（含泛化边界声明）
- 可证伪性状态 + 过度泛化风险评估
