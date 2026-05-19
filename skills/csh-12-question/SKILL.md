---
name: csh-12-question
description: Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions (motivation, control, expertise, legitimacy) comparing is vs ought.
execution: subagent
prompt: ./prompt.md
input: system_description (string), context (string)
used-by: stakeholder-mapping
---

# CSH 12-Question

Critical Systems Heuristics boundary analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one CSH 12-question analysis pass.
