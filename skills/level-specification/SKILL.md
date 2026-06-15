---
name: level-specification
description: Determine appropriate levels for each experimental factor
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: factor list with types and ranges
output: specified levels for each factor with justification
dependencies:
  sops:
  - spawn-agent
---

# SOP: Level Specification

Determine the specific values (levels) at which each factor will be tested, including spacing strategy and justification.

Subagent — spawned via subagent-spawning/spawn-agent skill.
