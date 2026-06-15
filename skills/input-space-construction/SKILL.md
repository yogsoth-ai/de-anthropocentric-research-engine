---
name: input-space-construction
description: Build input spaces for two source concepts
execution: subagent
prompt: ./prompt.md
input: two_concepts (string)
dependencies:
  sops:
  - spawn-agent
---

# Input Space Construction

Build input spaces for two source concepts, elaborating each into its elements, relations, and attributes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Input space construction requires deep elaboration of each concept's internal structure, identifying non-obvious elements and relations. Benefits from dedicated focused attention on each concept independently.
