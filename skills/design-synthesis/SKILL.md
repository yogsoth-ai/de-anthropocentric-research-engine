---
name: design-synthesis
description: "SOP: synthesize complete experiment design report"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - experiment-design
input: "All upstream SOP outputs (variables, levels, matrix, metrics, sample size, seeds, environment, config)"
output: "Complete experiment design report + feasibility assessment + risk inventory"
---

# SOP: Design Synthesis

Synthesize all upstream design SOP outputs into a complete experiment design report, perform consistency checks, assess feasibility, and identify potential risks.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Design synthesis requires a global perspective to review all design decisions for consistency and completeness — serves as the final quality gate of the experiment design phase, requiring independent critical thinking space.
