---
name: inversion-extraction
description: Extract constructive insights from worst solutions. Transform failure analysis into innovation directions.
execution: subagent
prompt: ./prompt.md
input: worst_solution (string), failure_analysis (string)
used-by: inversion-protocol, reverse-brainstorming, worst-method-inversion
---

# Inversion Extraction

Extract constructive insights from worst solutions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Inversion extraction requires careful analytical reasoning to transform "why this is bad" into "what the good version implies." Benefits from dedicated focus to avoid superficial inversions and find deep structural insights.
