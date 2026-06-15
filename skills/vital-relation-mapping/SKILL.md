---
name: vital-relation-mapping
description: Map 15 vital relations between concepts
execution: subagent
prompt: ./prompt.md
input: concept_pair (string)
dependencies:
  sops:
  - spawn-agent
---

# Vital Relation Mapping

Map 15 vital relations between concepts — the fundamental cognitive relations that structure conceptual integration (Change, Identity, Time, Space, Cause-Effect, Part-Whole, Representation, Role, Analogy, Disanalogy, Property, Similarity, Category, Intentionality, Uniqueness).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Vital relation mapping requires systematic analysis of 15 distinct relation types between two concepts, each requiring careful judgment about presence, strength, and compression potential. Benefits from methodical dedicated attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
