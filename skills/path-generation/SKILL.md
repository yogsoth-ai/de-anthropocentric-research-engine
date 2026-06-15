---
name: path-generation
description: Generate combination paths through consistent space
execution: subagent
prompt: ./prompt.md
input: reduced_space (object)
dependencies:
  sops:
  - spawn-agent
---

# Path Generation

Generate combination paths through the consistent solution space, prioritizing unexplored and novel configurations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Path generation requires strategic traversal of the reduced solution space, selecting configurations that maximize coverage, novelty, and diversity rather than random sampling.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
