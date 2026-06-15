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
