---
name: sobol-decomposition
description: Sobol variance decomposition — compute first-order and total-order sensitivity
  indices for precise variance attribution.
execution: subagent
prompt: ./prompt.md
input: model_description, input_distributions, sample_size
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete Sobol decomposition (sampling, index computation, interpretation).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
