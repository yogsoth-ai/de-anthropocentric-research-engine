---
name: boundary-analysis
description: Boundary Analysis Campaign — probe where methods fail, map validity envelopes,
  test robustness, catalog failure modes, detect scaling limits. 5 strategies, 3 tactics,
  11 subagent SOPs.
execution: campaign
dependencies:
  strategies:
  - boundary-critique
  - deep-insight-validity-envelope-mapping
  - failure-mode-analysis
  - robustness-testing
  - scaling-frontier
  sops:
  - boundary-synthesis
  - context-checkpoint
  - context-init
---

# Boundary Analysis

Probe where methods fail — validity envelopes, robustness, failure modes, scaling limits.

## Design Philosophy

This campaign is a strategy book — CC reads, internalizes, and autonomously constructs an approach. The SKILL.md files are textbooks, not scripts.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| 有效条件、适用范围、多轴变异、退化曲线 | → validity-envelope-mapping |
| 跨方法一致性、多模型收敛、Wimsatt 鲁棒性 | → robustness-testing |
| 系统边界、纳入/排除、CSH 批判 | → boundary-critique |
| 失效模式、边界输入、分布偏移、对抗性 | → failure-mode-analysis |
| 规模极限、scaling law、行为突变、容量 | → scaling-frontier |

## Available Tactics

- multi-model-convergence — Wimsatt-style cross-validation
- systematic-perturbation — multi-axis validity probing
- failure-mode-cataloging — systematic failure taxonomy

## Available SOPs

**Import (5):** web-search, web-research, paper-overview, paper-search, paper-research

**Subagent (11):** assumption-enumeration, alternative-model-generation, convergence-assessment, fragility-flagging, variation-axis-definition, controlled-perturbation, validity-envelope-construction, edge-case-generation, failure-clustering, scaling-regime-detection, boundary-synthesis

**Shared (1):** evidence-synthesis

## Context Management

context-checkpoint after each strategy completes.

<!-- BEGIN available-tables (generated) -->

## Available Strategies

可选,无固定顺序;最终叶子终为 sop。

| Strategy | 何时用 |
| --- | --- |
| boundary-critique | Apply CSH boundary critique — what is included/excluded, who benefits/is harmed, what expertise is privileged/marginalized. Identifies opportunities at the boundaries. |
| deep-insight-validity-envelope-mapping | Map multi-dimensional validity envelopes — define variation axes, perturb systematically, measure degradation, construct boundary surface. |
| failure-mode-analysis | Systematically catalog failure modes — generate edge cases, observe failures, cluster by mechanism, identify triggers and frequency. |
| robustness-testing | Test conclusion robustness via multi-model convergence — enumerate assumptions, generate alternatives, compare results, flag fragile conclusions. |
| scaling-frontier | Analyze behavior across scales — detect regime changes, identify capacity limits, fit scaling laws within regimes. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| boundary-synthesis | Compile all boundary analysis products into a coherent report — validity envelopes, robustness results, failure catalogs, scaling maps, safe operating conditions. |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |

<!-- END available-tables (generated) -->
