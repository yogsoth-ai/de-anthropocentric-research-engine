---
name: level-specification
description: Determine appropriate levels for each experimental factor
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: factor list with types and ranges
output: specified levels for each factor with justification
dependencies:
  sops:
  - spawn-agent
---

# SOP: Level Specification

Determine the specific values (levels) at which each factor will be tested, including spacing strategy and justification.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
