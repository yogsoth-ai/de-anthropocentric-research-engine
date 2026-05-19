---
name: sensitivity-analysis
description: Sensitivity Analysis Campaign — identify which assumptions are most critical by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition, assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics, 11 subagent SOPs.
execution: campaign
used-by: deep-insight
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
