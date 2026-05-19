---
name: alternatives-generation
description: Generate alternatives for every known approach — ensure no approach goes unchallenged.
execution: subagent
prompt: ./prompt.md
input: known_approaches (string)
used-by: lateral-thinking, provocation-and-movement, random-entry, concept-fan, challenge-operation, six-hats-ideation, movement-extraction
---

# Alternatives Generation

Generate alternatives for every known approach.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Alternatives generation requires systematically considering each known approach and producing genuinely different alternatives (not variations). Benefits from dedicated context that can maintain the "different, not better" mindset.
