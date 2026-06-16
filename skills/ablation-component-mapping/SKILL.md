---
name: ablation-component-mapping
description: Map system architecture to ablatable units for ablation studies
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: system architecture description, component list
output: ablation map with dependencies and removal strategies
dependencies:
  sops:
  - spawn-agent
---

# SOP: Ablation Component Mapping

Map the system architecture to a set of ablatable units, identifying dependencies, removal strategies, and expected impact for each component.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
