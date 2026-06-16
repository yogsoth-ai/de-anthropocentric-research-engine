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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
