---
name: sensitivity-analysis
description: Sensitivity Analysis Campaign — identify which assumptions are most critical
  by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition,
  assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics,
  11 subagent SOPs.
execution: campaign
dependencies:
  strategies:
  - assumption-criticality
  - decision-sensitivity
  - parameter-screening
  - uncertainty-propagation
  - variance-decomposition
  sops:
  - context-checkpoint
  - context-init
---

# Sensitivity Analysis

Identify which assumptions are most critical — rank by impact on conclusions.

## Design Philosophy

This campaign is a strategy book — CC reads, internalizes, and autonomously constructs an approach.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| 快速筛选、Morris 方法、OAT、初步排除 | → parameter-screening |
| 方差分解、Sobol 指数、贡献度、交互效应 | → variance-decomposition |
| 假设致命性、扰动、否定、重新推导 | → assumption-criticality |
| 不确定性传播、Monte Carlo、分布、贝叶斯 | → uncertainty-propagation |
| 决策敏感性、EVPI、影响图、龙卷风图 | → decision-sensitivity |

## Available Tactics

- screening-then-decomposition — Morris quick screen then Sobol precise decomposition
- assumption-perturbation — one-at-a-time assumption negation and re-derivation
- uncertainty-cascade — Monte Carlo propagation through model

## Available SOPs

**Import (5):** web-search, web-research, paper-overview, paper-search, paper-research

**Subagent (11):** morris-screening, sobol-decomposition, interaction-detection, assumption-extraction, negation-definition, re-derivation, conclusion-sensitivity-measurement, distribution-assignment, monte-carlo-sampling, critical-path-identification, sensitivity-synthesis

**Shared (1):** assumption-surfacing

## Context Management

context-checkpoint after each strategy completes.

<!-- BEGIN available-tables (generated) -->

## Available Strategies

可选,无固定顺序;最终叶子终为 sop。

| Strategy | 何时用 |
| --- | --- |
| assumption-criticality | Measure how much conclusions change when each assumption is negated. Ranks assumptions by their impact on the final result. |
| decision-sensitivity | Identify which uncertainties would actually change the research direction decision. Compute EVPI to prioritize uncertainty reduction. |
| parameter-screening | Quick Morris method screening to identify which parameters have large effects and which can be safely ignored. |
| uncertainty-propagation | Propagate input uncertainties through the model via Monte Carlo sampling. Identifies which input uncertainties contribute most to output uncertainty. |
| variance-decomposition | Sobol variance decomposition — compute first-order and total-order sensitivity indices to quantify each parameter's contribution to output variance. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |

<!-- END available-tables (generated) -->
