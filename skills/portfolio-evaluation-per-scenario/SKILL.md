---
name: portfolio-evaluation-per-scenario
description: Evaluate a specific portfolio's performance metrics and vulnerabilities
  under a given scenario.
execution: subagent
prompt: ./prompt.md
input: portfolio, scenario
dependencies:
  sops:
  - spawn-agent
---

# Portfolio Evaluation Per Scenario

Assess how a specific portfolio performs under a given future scenario, identifying performance metrics and vulnerabilities.

## Execution

Spawns a subagent that evaluates each portfolio member's performance under scenario conditions and aggregates into portfolio-level metrics.

## Why Subagent

Per-scenario evaluation requires careful reasoning about how each scenario's conditions affect each portfolio member differently. This analytical work is repeated per scenario and benefits from consistent, focused execution.

## HARD-GATE

Output must include quantified performance metrics for the portfolio under the scenario and identification of any members that become vulnerable or fail under scenario conditions.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
