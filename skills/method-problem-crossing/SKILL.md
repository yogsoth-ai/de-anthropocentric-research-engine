---
name: method-problem-crossing
description: Build method×problem cross-reference matrix showing which methods have
  been applied to which problems.
execution: subagent
prompt: ./prompt.md
input: method_list (array), problem_list (array)
dependencies:
  sops:
  - spawn-agent
---

# Method-Problem Crossing

Build a cross-reference matrix of methods × problems, documenting which combinations have been explored.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Matrix construction requires systematic cross-referencing of many method-problem pairs. Benefits from dedicated context to track all cells without losing state.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
