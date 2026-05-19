---
name: result-collection
description: "Collect experiment outputs — metrics, logs, artifacts — into structured result set"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - result-analysis
  - result-validation-loop
input: completed task outputs (files, logs, metrics)
output: structured result set with completeness assessment
---

# SOP: Result Collection

Collect and structure all experiment outputs into a unified result set for downstream analysis.

Subagent — spawned via subagent-spawning/spawn-agent skill.
