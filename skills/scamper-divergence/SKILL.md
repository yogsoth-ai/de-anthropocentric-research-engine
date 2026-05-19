---
name: scamper-divergence
description: Execute SCAMPER 7 operators on a target solution. Subagent self-selects best 2-3 operators for deepest exploration.
execution: subagent
prompt: ./prompt.md
input: existing_solution (string)
used-by: structural-deconstruction, scamper-transformation
---

# SCAMPER Divergence

Execute all 7 SCAMPER operators and self-select the most productive 2-3 for deep exploration.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

SCAMPER requires systematic application of 7 distinct mental operators, each demanding a different creative lens. Benefits from dedicated context that can fully commit to each operator without cross-contamination.
