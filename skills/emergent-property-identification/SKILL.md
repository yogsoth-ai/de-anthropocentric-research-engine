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
