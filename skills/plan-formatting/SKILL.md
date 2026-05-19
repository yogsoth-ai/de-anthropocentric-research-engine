---
name: plan-formatting
description: "Format task plan as bite-sized executable tasks following superpowers:writing-plans conventions"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: plan-writing
input: estimated and sequenced activity list with IOs
output: executable plan document with no TBD/TODO (HARD-GATE)
---

# SOP: Plan Formatting

Format the complete task information into a bite-sized executable plan. HARD-GATE: output must contain zero TBD/TODO/placeholder text.

Subagent — spawned via subagent-spawning/spawn-agent skill.
