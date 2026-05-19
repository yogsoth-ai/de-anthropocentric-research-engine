---
name: execution-synthesis
description: "Synthesize complete execution report from all results, tests, and reproducibility data"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - result-validation-loop
  - implementation-planning
input: structured results, statistical tests, ROPE judgment, reproducibility assessment
output: complete execution report with findings, judgment, and next steps
---

# SOP: Execution Synthesis

Synthesize all execution outputs into a final report covering findings, statistical conclusions, reproducibility, and actionable next steps.

Subagent — spawned via subagent-spawning/spawn-agent skill.
