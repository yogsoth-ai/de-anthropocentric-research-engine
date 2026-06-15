---
name: resource-quantification
description: Quantify resource demand vs supply vs gap for each resource category
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: experiment plan, resource inventory, task estimates
output: demand/supply/gap table per resource category with severity ratings
dependencies:
  sops:
  - spawn-agent
---

# SOP: Resource Quantification

Quantify resource demand, supply, and gap for each resource category (compute, data, time, human, financial).

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
