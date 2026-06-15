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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
