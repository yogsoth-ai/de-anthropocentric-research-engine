---
name: controlled-perturbation
description: Systematically vary parameters along defined axes, recording performance
  at each point to identify degradation thresholds.
execution: subagent
prompt: ./prompt.md
input: method (string), variation_axis (string), range (string)
dependencies:
  sops:
  - spawn-agent
---

# Controlled Perturbation

Systematically perturb to find degradation thresholds.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one perturbation curve along one axis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
