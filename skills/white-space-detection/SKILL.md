---
name: white-space-detection
description: Identify matrix regions not covered by existing methods
execution: subagent
prompt: ./prompt.md
input: matrix (object), known_methods_mapping (object)
dependencies:
  sops:
  - spawn-agent
---

# White Space Detection

Identify regions of the morphological matrix not covered by any existing method or solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

White space detection requires mapping known solutions onto the matrix, identifying gaps, and reasoning about why those gaps exist (overlooked vs infeasible vs unexplored).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
