---
name: gap-prioritization
description: 'Campaign: Systematically assess and rank research gaps, determining the targets most worth attacking'
version: 1.0.0
category: hypothesis-formation
type: campaign
input: 'Gaps produced by upstream repos (any format: knowledge-acquisition, deep-insight, or manually provided by the user)'
output: Ranked gap priority list + suggested attack paths for the top N gaps
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

Systematically assess and rank research gaps — answering "which gaps are most worth attacking?"

## HARD-GATE

<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 3 clearly identified research gaps already exist (from an upstream repo or provided by the user)
2. Each gap has sufficient description (at least: what the gap is, why it exists, in which domain)
3. The research intent is clear (north-star-crystallization completed or explicitly stated by the user)

Not met → stop, and inform the user that upstream work must be completed first.
</HARD-GATE>

## Campaign Goal

Turn a batch of unranked research gaps into a prioritized attack list. The output is not "discovering new gaps" but "making decisions about existing gaps."

## Strategy Selection

| Strategy | When to use | Default |
|----------|---------|------|
| multi-criteria-ranking | Moderate number of gaps (5-20), systematic assessment needed | ✓ |
| evidence-based-prioritization | Gaps from rigorous literature review, with ample supporting evidence | |
| stakeholder-weighted-ranking | Research involves multiple stakeholders | |
| portfolio-optimization | Large number of gaps (20+), portfolio-level decisions needed | |
| rapid-triage | Very large number of gaps (50+), rapid coarse screening needed first | |

CC autonomously selects a strategy based on gap count, evidence sufficiency, and stakeholder complexity. Strategies can be combined (e.g., rapid-triage to screen first → multi-criteria-ranking for fine ranking).

## Budget Gate

| Tier | Number of gaps | Assessment dimensions | Scoring rounds | Final output |
|------|---------|---------|---------|---------|
| S | 3-5 | ≥3 | 1 | Ranking + top 2 attack suggestions |
| M | 6-20 | ≥4 | ≥2 (incl. sensitivity testing) | Ranking + top 3-5 attack suggestions |
| L | 20+ | ≥5 | ≥3 (incl. portfolio optimization) | Ranking + top 5-8 attack suggestions + portfolio analysis |

## Context Management

- Call context-init at the start of the campaign
- Call context-checkpoint after each strategy completes (hard constraint)
- All outputs accumulate in a single campaign-scoped context file

## Minimum Yield

Each campaign execution must produce:
1. A standardized gap list (unified format)
2. A multi-dimensional scoring matrix (or an equivalent ranking basis)
3. A final priority ranking
4. Suggested attack paths for the top N gaps (incl. method direction, expected difficulty, required resources)

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
