---
name: assumption-enumeration
description: Systematically identify all assumptions in a method/model — structural, parametric, distributional, and scope assumptions.
execution: subagent
prompt: ./prompt.md
input: method_description (string), context (string)
used-by: robustness-testing
---

# Assumption Enumeration

Exhaustively list all assumptions in a method.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one assumption enumeration pass.
