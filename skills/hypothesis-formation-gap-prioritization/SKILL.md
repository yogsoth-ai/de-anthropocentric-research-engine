---
name: gap-prioritization
description: 'Campaign: 系统化评估和排序研究 gaps，确定最值得攻击的目标'
version: 1.0.0
category: hypothesis-formation
type: campaign
input: 上游 repo 产出的 gaps（任意格式：knowledge-acquisition、deep-insight、或用户手动提供）
output: 排序后的 gap 优先级列表 + 前 N 个 gap 的攻击路径建议
strategies:
- multi-criteria-ranking
- evidence-based-prioritization
- stakeholder-weighted-ranking
- portfolio-optimization
- rapid-triage
tactics:
- scoring-matrix-construction
- pairwise-comparison
- priority-sensitivity-testing
dependencies:
  campaigns:
  - hypothesis-formulation
  strategies:
  - evidence-based-prioritization
  - hypothesis-formation-portfolio-optimization
  - multi-criteria-ranking
  - rapid-triage
  - stakeholder-weighted-ranking
  tactics:
  - pairwise-comparison
  sops:
  - context-checkpoint
  - context-init
  - hypothesis-formation-quality-gate-check
  - hypothesis-formation-saturation-detection
---

# Gap Prioritization

系统化评估和排序研究 gaps — 回答"哪些 gap 最值得攻击？"

## HARD-GATE

<HARD-GATE>
前置条件（全部满足才能开始）:
1. 至少 3 个明确的研究 gaps 已被识别（来自上游 repo 或用户提供）
2. 每个 gap 有足够描述（至少包含：gap 是什么、为什么存在、在哪个领域）
3. 研究意图已明确（north-star-crystallization 完成或用户明确表达）

不满足 → 停止，告知用户需要先完成上游工作。
</HARD-GATE>

## Campaign Goal

将一批未排序的研究 gaps 转化为带优先级的攻击列表。产出不是"发现新 gap"，而是"对已有 gap 做决策"。

## Strategy Selection

| Strategy | 适用场景 | 默认 |
|----------|---------|------|
| multi-criteria-ranking | gap 数量适中（5-20），需要系统化评估 | ✓ |
| evidence-based-prioritization | gap 来自严谨文献调研，有充足证据支撑 | |
| stakeholder-weighted-ranking | 研究涉及多方利益相关者 | |
| portfolio-optimization | gap 数量大（20+），需要组合层面决策 | |
| rapid-triage | gap 数量极大（50+），需要先快速粗筛 | |

CC 根据 gap 数量、证据充分度、利益相关者复杂度自主选择 strategy。可组合使用（如 rapid-triage 先筛 → multi-criteria-ranking 精排）。

## Budget Gate

| Tier | Gap 数量 | 评估维度 | 评分轮次 | 最终产出 |
|------|---------|---------|---------|---------|
| S | 3-5 | ≥3 | 1 | 排序 + 前 2 攻击建议 |
| M | 6-20 | ≥4 | ≥2（含敏感性检验） | 排序 + 前 3-5 攻击建议 |
| L | 20+ | ≥5 | ≥3（含组合优化） | 排序 + 前 5-8 攻击建议 + portfolio 分析 |

## Context Management

- Campaign 开始时调用 context-init
- 每个 strategy 完成后调用 context-checkpoint（硬性约束）
- 所有产出累积在单个 campaign-scoped context file

## Minimum Yield

每次 campaign 执行必须产出:
1. 标准化的 gap 列表（统一格式）
2. 多维度评分矩阵（或等价的排序依据）
3. 最终优先级排序
4. 前 N 个 gap 的攻击路径建议（含方法方向、预期难度、所需资源）

<!-- BEGIN available-tables (generated) -->

## Available Strategies

可选,无固定顺序;最终叶子终为 sop。

| Strategy | 何时用 |
| --- | --- |
| evidence-based-prioritization | Strategy: 基于证据强度的 AHRQ PiCMe 评估——用文献证据质量驱动 gap 优先级 |
| hypothesis-formation-portfolio-optimization | Strategy: gap 组合视为投资组合——用风险/收益/多样性优化选出最优 gap 组合 |
| multi-criteria-ranking | Strategy: 多维度加权评分排序——将 gap 分解为独立子问题后重组为优先级列表 |
| rapid-triage | Strategy: 快速粗筛——两轮过滤将大量 gaps 压缩为可精排的候选集 |
| stakeholder-weighted-ranking | Strategy: 按利益相关者视角加权——同一 gap 在不同视角下权重不同，最终取共识排序 |

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| pairwise-comparison | Tactic: 通过相对比较而非绝对评分对 gaps 进行排序，适用于难以量化的场景 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |
| hypothesis-formation-quality-gate-check | Shared SOP: 通用质量门检查（格式完整性、逻辑一致性） |
| hypothesis-formation-saturation-detection | Shared SOP: 判断当前活动是否已达信息饱和 |

## Available Campaigns

可选,无固定顺序;最终叶子终为 sop。

| Campaign | 何时用 |
| --- | --- |
| hypothesis-formulation | Campaign: 将 insight 和 gap 转化为结构化的可测试假设 |

<!-- END available-tables (generated) -->
