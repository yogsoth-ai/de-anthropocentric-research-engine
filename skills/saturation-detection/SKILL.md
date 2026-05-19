---
name: saturation-detection
description: Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey.
execution: subagent
prompt: ./prompt.md
input: existing_corpus (string), latest_batch (string)
used-by: literature-survey, patent-mining, benchmark-archaeology
---

# Saturation Detection

Determine when to stop expanding — diminishing returns analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Saturation judgment requires comparing the entire existing corpus against the latest batch of new papers. The comparison is context-intensive and benefits from dedicated processing.
