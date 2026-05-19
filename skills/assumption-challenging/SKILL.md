---
name: assumption-challenging
description: "Challenge each assumption's validity — shared cross-repo SOP"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - assumption-constraint
  - conflict-resolution
  - constraint-breaking
shared: true
input: list of assumptions with context
output: validity assessment with confidence scores and evidence
---

# SOP: Assumption Challenging

Challenge each assumption's validity using systematic questioning. Determine which assumptions are well-founded, which are fragile, and which are likely false.

Subagent — spawned via subagent-spawning/spawn-agent skill.

Shared: This SOP is used across multiple strategies (assumption-constraint, conflict-resolution, constraint-breaking) and campaigns.
