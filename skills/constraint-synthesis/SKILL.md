---
name: constraint-synthesis
description: "Synthesize constraint analysis into actionable report with priorities"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by: constraint-analysis
input: outputs from constraint-tree-building, sensitivity-ranking, constraint-breaking
output: integrated constraint report with prioritized actions and risk assessment
---

# SOP: Constraint Synthesis

Synthesize all constraint analysis outputs into a single actionable report. Integrates findings from tree-building, sensitivity ranking, and constraint-breaking into prioritized recommendations.

Subagent — spawned via subagent-spawning/spawn-agent skill.
