---
name: dependency-sequencing
description: Determine task dependencies and execution order
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: list of implementation activities
output: dependency graph with predecessor/successor relationships
dependencies:
  sops:
  - spawn-agent
---

# SOP: Dependency Sequencing

Determine predecessor/successor relationships between activities and produce a valid execution order.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
