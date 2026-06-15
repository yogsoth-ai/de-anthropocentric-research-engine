---
name: generic-space-extraction
description: Extract shared abstract structure from two input spaces
execution: subagent
prompt: ./prompt.md
input: two_input_spaces (object)
dependencies:
  sops:
  - spawn-agent
---

# Generic Space Extraction

Extract shared abstract structure from two input spaces — the generic space captures what both inputs have in common at the highest level of abstraction.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Generic space extraction requires careful abstraction to find the deepest shared structure without over-generalizing. Benefits from dedicated analytical attention.
