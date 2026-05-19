---
name: parameter-enumeration
description: "Enumerate possible values for each uncertainty driver using MECE principles"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - morphological-scenario
  - parameter-space-construction
input: validated driver list, value count guidance (2-4 per driver)
output: complete Zwicky Box (driver × value matrix) with value descriptions
---

# SOP: Parameter Enumeration

Enumerate the possible future states (values) for each identified uncertainty driver. Values must be mutually exclusive and collectively exhaustive (MECE) within each driver dimension.

Subagent — spawned via subagent-spawning/spawn-agent skill.
