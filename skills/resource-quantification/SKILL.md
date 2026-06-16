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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
