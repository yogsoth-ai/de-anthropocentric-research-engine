---
name: gap-typology-classification
description: Classify gaps using Miles 7-type taxonomy (theoretical, methodological, empirical, population, practical, knowledge void, evidence gap).
execution: subagent
prompt: ./prompt.md
input: gap_description (string), evidence (string)
used-by: gap-classification
---

# Gap Typology Classification

Classify research gaps by type using established taxonomies.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one gap classification pass.
