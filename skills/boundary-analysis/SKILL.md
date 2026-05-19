---
name: boundary-analysis
description: Boundary Analysis Campaign — probe where methods fail, map validity envelopes, test robustness, catalog failure modes, detect scaling limits. 5 strategies, 3 tactics, 11 subagent SOPs.
execution: campaign
used-by: deep-insight
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
