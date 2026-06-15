---
name: validity-envelope-construction
description: Combine multi-axis perturbation data into a multi-dimensional validity
  description with boundary conditions and interaction effects.
execution: subagent
prompt: ./prompt.md
input: perturbation_data (string), axes (string)
dependencies:
  sops:
  - spawn-agent
---

# Validity Envelope Construction

Construct the multi-dimensional validity boundary.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one envelope construction from perturbation data.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
