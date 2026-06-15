---
name: critical-path-identification
description: Identify which input uncertainties contribute most to output uncertainty
  and compute EVPI for research prioritization.
execution: subagent
prompt: ./prompt.md
input: propagation_results, input_output_relationships
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete critical path analysis (importance ranking, EVPI computation, recommendations).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
