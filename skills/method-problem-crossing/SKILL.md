---
name: method-problem-crossing
description: Build method×problem cross-reference matrix showing which methods have been applied to which problems.
execution: subagent
prompt: ./prompt.md
input: method_list (array), problem_list (array)
used-by: coverage-analysis, benchmark-sweep, method-problem-matrix
---

# Method-Problem Crossing

Build a cross-reference matrix of methods × problems, documenting which combinations have been explored.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Matrix construction requires systematic cross-referencing of many method-problem pairs. Benefits from dedicated context to track all cells without losing state.
