---
name: random-paper-entry
description: Select random paper facet as creative stimulus. Uses genuine randomness in paper selection to break domain fixation.
execution: subagent
prompt: ./prompt.md
input: none
used-by: cross-domain-discovery, random-stimulus-entry, domain-divergence
---

# Random Paper Entry

Select random paper facet as creative stimulus.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Random paper selection requires genuine exploration without goal-directed filtering. The subagent must resist the temptation to select "relevant" papers and instead embrace true randomness, then force associations from whatever is found.
