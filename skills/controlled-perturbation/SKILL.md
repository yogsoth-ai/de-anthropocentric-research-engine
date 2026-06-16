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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
