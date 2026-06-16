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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
