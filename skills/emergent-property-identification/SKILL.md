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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
