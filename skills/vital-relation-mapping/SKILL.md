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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
