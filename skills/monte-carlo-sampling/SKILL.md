---
name: monte-carlo-sampling
description: Design and execute Monte Carlo sampling strategy for uncertainty propagation
  through a model.
execution: subagent
prompt: ./prompt.md
input: input_distributions, model_structure
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Monte Carlo propagation (sampling design, execution, output characterization).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
