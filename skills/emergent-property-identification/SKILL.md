---
name: emergent-property-identification
description: Identify non-additive properties from combinations
execution: subagent
prompt: ./prompt.md
input: combination_proposal (object)
dependencies:
  sops:
  - spawn-agent
---

# Emergent Property Identification

Identify non-additive properties from combinations — properties that exist in the combination but not in any individual component.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Emergent property identification requires careful comparison between predicted additive properties and actual combination properties, plus creative imagination to spot non-obvious emergence. Benefits from dedicated analytical-creative attention.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
