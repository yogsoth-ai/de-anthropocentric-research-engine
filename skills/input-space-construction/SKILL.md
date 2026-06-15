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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
