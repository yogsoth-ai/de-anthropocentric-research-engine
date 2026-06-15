---
name: worst-case-construction
description: Construct extreme but plausible worst-case scenarios for stress testing
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: vulnerability drivers, failure dimensions, compound combination guidance
output: extreme scenario with breaking points, failure cascades, and recovery assessment
dependencies:
  sops:
  - spawn-agent
---

# SOP: Worst-Case Construction

Construct extreme but plausible worst-case scenarios that maximally stress the research approach. Identify breaking points, failure cascades, and recovery possibilities.

Subagent — spawned via subagent-spawning/spawn-agent skill.
