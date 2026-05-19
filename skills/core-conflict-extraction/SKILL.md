---
name: core-conflict-extraction
description: "Extract core conflict in Evaporating Cloud format (A-B-C-D-D')"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - bottleneck-identification
  - conflict-resolution
  - constraint-breaking
input: causal tree root causes, identified dilemmas
output: Evaporating Cloud with assumptions on each arrow
---

# SOP: Core Conflict Extraction

Extract the core conflict from identified root causes and express it in Goldratt's Evaporating Cloud format (A-B-C-D-D') with explicit assumptions on each arrow.

Subagent — spawned via subagent-spawning/spawn-agent skill.
