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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
