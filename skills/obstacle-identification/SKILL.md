---
name: obstacle-identification
description: TOC Prerequisite Tree — list obstacles preventing direct achievement
  of the objective
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: experiment objective and critical path
output: categorized obstacle list with severity and blocking relationships
dependencies:
  sops:
  - spawn-agent
---

# SOP: Obstacle Identification

Identify all obstacles that prevent direct achievement of the experiment objective using TOC Prerequisite Tree methodology.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
