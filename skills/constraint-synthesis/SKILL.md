---
name: constraint-synthesis
description: Synthesize constraint analysis into actionable report with priorities
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: outputs from constraint-tree-building, sensitivity-ranking, constraint-breaking
output: integrated constraint report with prioritized actions and risk assessment
dependencies:
  sops:
  - spawn-agent
---

# SOP: Constraint Synthesis

Synthesize all constraint analysis outputs into a single actionable report. Integrates findings from tree-building, sensitivity ranking, and constraint-breaking into prioritized recommendations.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
