---
name: direct-analogy-generation
description: Find direct analogies from nature/tech/society that share structural properties with the problem. Produces analogy list with structural mappings.
execution: subagent
prompt: ./prompt.md
input: problem (string)
used-by: synectics, direct-analogy, excursion-method
---

# Direct Analogy Generation

Find direct analogies from nature, technology, and society.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Direct analogy generation requires broad cross-domain knowledge search and careful structural mapping. Benefits from dedicated focus on finding non-obvious parallels without premature solution generation.
