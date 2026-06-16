---
name: contradiction-matrix-lookup
description: Query the 39x39 TRIZ contradiction matrix to find recommended inventive
  principles for a given technical contradiction.
execution: subagent
prompt: ./prompt.md
input: improving_parameter (string), worsening_parameter (string)
dependencies:
  sops:
  - spawn-agent
---

# Contradiction Matrix Lookup

Query the TRIZ contradiction matrix for applicable inventive principles.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Matrix lookup requires knowledge of the 39 engineering parameters and their intersections, plus interpretation of which principles are most relevant to the specific context. Benefits from dedicated analytical focus.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
