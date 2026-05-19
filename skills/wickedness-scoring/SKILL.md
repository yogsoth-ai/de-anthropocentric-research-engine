---
name: wickedness-scoring
description: Score a problem against Rittel's 10 criteria to determine if it is tame, complex, or wicked.
execution: subagent
prompt: ./prompt.md
input: problem_description, context
used-by: wickedness-assessment
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete wickedness assessment (10-criterion scoring + classification).
