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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
