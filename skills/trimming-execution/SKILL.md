---
name: trimming-execution
description: Progressively remove components from a system while verifying function preservation through redistribution.
execution: subagent
prompt: ./prompt.md
input: function_model (string)
used-by: structural-deconstruction, function-trimming, component-decomposition
---

# Trimming Execution

Progressively remove components and verify function preservation.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Trimming requires careful step-by-step reasoning about function redistribution after each removal. Benefits from dedicated context that can track system state changes through multiple trimming iterations.
