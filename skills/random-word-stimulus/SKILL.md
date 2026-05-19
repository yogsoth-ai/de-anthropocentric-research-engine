---
name: random-word-stimulus
description: Use random word/concept injection as creative stimulus. Selects random concepts and forces connection to the problem space, generating unexpected solution paths.
execution: subagent
prompt: ./prompt.md
input: problem_description (string), stimulus_count (string)
used-by: cross-domain-discovery, lateral-thinking, synectics
---

# Random Word Stimulus

Use random word/concept injection as creative stimulus.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Random stimulus requires genuine randomness in word selection followed by forced-connection reasoning. Benefits from a dedicated context that commits fully to the association process without premature filtering.
