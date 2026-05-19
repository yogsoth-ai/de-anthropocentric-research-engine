---
name: surgery-operation
description: Execute component surgery operations (subtract/multiply/divide/unify/redirect) from Systematic Inventive Thinking.
execution: subagent
prompt: ./prompt.md
input: component_analysis (string)
used-by: structural-deconstruction, component-surgery
---

# Surgery Operation

Apply SIT surgical operators to system components for structural innovation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Component surgery requires careful reasoning about system integrity during each operation. Benefits from dedicated context that can track component states and verify function preservation after each cut.
