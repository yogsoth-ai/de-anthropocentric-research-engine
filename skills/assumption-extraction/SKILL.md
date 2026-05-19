---
name: assumption-extraction
description: Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model.
execution: subagent
prompt: ./prompt.md
input: method_description
used-by: assumption-criticality
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete assumption extraction from a method/model description.
