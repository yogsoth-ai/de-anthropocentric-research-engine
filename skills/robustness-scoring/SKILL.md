---
name: robustness-scoring
description: "Compute robustness index across scenarios with sensitivity analysis"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - strategy-robustness-testing
input: compiled impact assessment matrix, scenario probabilities, weighting preferences
output: robustness index (0-100), sensitivity analysis, pivot triggers
---

# SOP: Robustness Scoring

Compute an overall robustness index for the research approach across all evaluated scenarios. Perform sensitivity analysis and identify pivot triggers.

Subagent — spawned via subagent-spawning/spawn-agent skill.
