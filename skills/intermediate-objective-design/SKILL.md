---
name: intermediate-objective-design
description: Design intermediate objectives to overcome each identified obstacle
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: categorized obstacle list
output: intermediate objectives with verification criteria and dependency sequence
dependencies:
  sops:
  - spawn-agent
---

# SOP: Intermediate Objective Design

Design concrete, verifiable intermediate objectives (IOs) that overcome each identified obstacle.

Subagent — spawned via subagent-spawning/spawn-agent skill.
