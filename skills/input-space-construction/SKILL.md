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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
