---
name: research-question
description: 'Campaign: 将假设细化为精确的、框架化的研究问题'
version: 1.0.0
category: hypothesis-formation
type: campaign
input: 假设 + 领域约束（来自 hypothesis-formulation 或用户提供）
output: 框架化的研究问题 + scope + success criteria + sub-questions
strategies:
- framework-guided-formulation
- scope-calibration
- decomposition-formulation
- comparative-formulation
- feasibility-constrained-formulation
tactics:
- framework-selection-and-application
- question-refinement-loop
- sub-question-decomposition
dependencies:
  campaigns:
  - hypothesis-formulation
  strategies:
  - comparative-formulation
  - decomposition-formulation
  - feasibility-constrained-formulation
  - framework-guided-formulation
  - scope-calibration
  sops:
  - context-checkpoint
  - context-init
  - hypothesis-formation-quality-gate-check
  - hypothesis-formation-saturation-detection
  - question-synthesis
---

# Research Question Formulation

将假设细化为精确的研究问题 — 回答"如何将假设细化为精确研究问题？"

## HARD-GATE

<HARD-GATE>
前置条件（全部满足才能开始）:
1. 至少 1 个明确的假设或研究方向已确定
2. 研究领域和约束条件已知
3. 目标受众明确（学术论文？项目报告？）

不满足 → 停止，建议先完成 hypothesis-formulation 或明确研究方向。
</HARD-GATE>

## Campaign Goal

将"可测试的假设"转化为"精确的研究问题" — 问题必须有明确的 scope、可衡量的 success criteria、可分解的 sub-questions。产出是可以直接指导实验设计或文献综述的研究问题。

## Strategy Selection

| Strategy | 适用场景 | 核心动作 |
|----------|---------|---------|
| framework-guided-formulation | 研究类型明确，有对应标准框架 | 选框架 → 填充 |
| scope-calibration | 问题太宽或太窄 | zoom in/out |
| decomposition-formulation | 问题复杂度高，单一实验无法回答 | 拆解 |
| comparative-formulation | 需要比较 A vs B | 构建对比 |
| feasibility-constrained-formulation | 理想问题超出可用资源 | pragmatic 调整 |

CC 根据假设特征和约束条件自主选择。常见组合: framework-guided → scope-calibration → decomposition。

## Budget Gate

| Tier | 框架评估 | RQ 产出 | FINER 检验 | Sub-questions |
|------|---------|---------|-----------|--------------|
| S | ≥2 框架比较 | ≥1 精确 RQ | 5 项全通过 | 可选 |
| M | ≥3 框架比较 | ≥2 精确 RQ | 5 项全通过 + success criteria | ≥3 sub-questions |
| L | ≥4 框架比较 | ≥3 精确 RQ | 5 项全通过 + criteria + 回答序列 | ≥5 sub-questions + 依赖图 |

## Research Question Structure (标准产出格式)

每个 RQ 必须包含:
- **Main question**: 一句话精确表述
- **Framework**: 使用的框架及各组件填充
- **Scope**: 明确的边界（什么在范围内，什么不在）
- **Success criteria**: 什么算"回答了这个问题"
- **Sub-questions**: 可独立回答的子问题（如有）
- **FINER assessment**: Feasible, Interesting, Novel, Ethical, Relevant

## Context Management

- Campaign 开始时调用 context-init
- 每个 strategy 完成后调用 context-checkpoint（硬性约束）
- 所有产出累积在单个 campaign-scoped context file

## Minimum Yield

每次 campaign 执行必须产出:
1. ≥1 个完整框架化的研究问题（含全部 6 个组件）
2. FINER 5 项标准全部通过
3. 明确的 success criteria（可衡量）
4. Scope 声明（in/out of scope）
