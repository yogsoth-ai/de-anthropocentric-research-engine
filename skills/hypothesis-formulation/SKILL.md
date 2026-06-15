---
name: hypothesis-formulation
description: 'Campaign: 将 insight 和 gap 转化为结构化的可测试假设'
version: 1.0.0
category: hypothesis-formation
type: campaign
input: 排序后的 gaps + insights + tensions（来自 gap-prioritization 或上游 repo）
output: 结构化假设集 + falsifiability criteria + boundary conditions
strategies:
- deductive-hypothesis-generation
- inductive-hypothesis-generation
- abductive-hypothesis-generation
- competing-hypothesis-construction
- hypothesis-operationalization
tactics:
- theory-mechanism-extraction
- anomaly-driven-abduction
- falsifiability-audit
- competing-hypothesis-matrix
dependencies:
  campaigns:
  - research-question
  strategies:
  - abductive-hypothesis-generation
  - competing-hypothesis-construction
  - deductive-hypothesis-generation
  - hypothesis-operationalization
  - inductive-hypothesis-generation
  sops:
  - context-checkpoint
  - context-init
  - hypothesis-formation-quality-gate-check
  - hypothesis-formation-saturation-detection
  - hypothesis-synthesis
---

# Hypothesis Formulation

将 insight 和 gap 转化为结构化的可测试假设 — 回答"如何将 insight 转化为可测试假设？"

## HARD-GATE

<HARD-GATE>
前置条件（全部满足才能开始）:
1. 至少 1 个明确的研究 gap 或 insight 已被识别
2. gap/insight 有足够上下文（领域、现有理论、观察到的现象）
3. 研究意图已明确（知道要解释什么或预测什么）

不满足 → 停止，建议先完成 gap-prioritization 或上游工作。
</HARD-GATE>

## Campaign Goal

将模糊的"这里有个 gap"或"这个现象很有趣"转化为精确的、可证伪的、有边界条件的假设。产出不是"解决方案"，而是"可测试的命题"。

## Strategy Selection

| Strategy | 适用场景 | 推理方向 |
|----------|---------|---------|
| deductive-hypothesis-generation | 领域有成熟理论，gap 是理论预测与现实的偏差 | 理论 → 预测 |
| inductive-hypothesis-generation | 领域缺乏理论，但有大量经验观察或数据模式 | 数据 → 规律 |
| abductive-hypothesis-generation | 观察到无法被现有理论解释的异常现象 | 异常 → 最佳解释 |
| competing-hypothesis-construction | 需要保持开放性，避免 confirmation bias | 多解释并行 |
| hypothesis-operationalization | 已有方向性假设，需要 formalize 为可测试形式 | 模糊 → 精确 |

CC 根据输入特征（有无理论支撑、有无异常数据、假设成熟度）自主选择。可串行组合。

## Budget Gate

| Tier | 假设产出 | 理论/机制 | 可证伪性 | 竞争假设 |
|------|---------|----------|---------|---------|
| S | ≥2 个结构化假设 | ≥2 个相关理论 | 每个假设 1 个 falsification scenario | 可选 |
| M | ≥3 个结构化假设 | ≥3 个理论 + ≥5 个机制 | 每个假设 ≥1 scenario + boundary conditions | ≥2 个竞争假设 |
| L | ≥5 个结构化假设 | ≥5 个理论 + ≥8 个机制 | 完整 falsifiability audit | ≥3 个竞争假设 + 区分性预测 |

## Hypothesis Structure (标准产出格式)

每个假设必须包含:
- **Statement**: If X then Y（条件-结果形式）
- **Variables**: 自变量、因变量、控制变量、调节变量
- **Mechanism**: 为什么 X 会导致 Y（因果链）
- **Boundary conditions**: 假设成立的前提条件
- **Falsification**: 什么观察结果会推翻此假设
- **Measurability**: 如何测量（操作定义）

## Context Management

- Campaign 开始时调用 context-init
- 每个 strategy 完成后调用 context-checkpoint（硬性约束）
- 所有产出累积在单个 campaign-scoped context file

## Minimum Yield

每次 campaign 执行必须产出:
1. ≥2 个完整结构化假设（含全部 6 个组件）
2. 每个假设的可证伪性论证
3. 假设间的关系说明（互补/竞争/独立）
4. 推荐的后续方向（哪个假设最值得进一步发展为研究问题）
