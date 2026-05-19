---
name: force-fit
description: Force-fit excursion discoveries back to the original problem. Deliberately create connections between unrelated findings and the challenge.
execution: subagent
prompt: ./prompt.md
input: excursion_discoveries (string), original_problem (string)
used-by: synectics, excursion-method, excursion-orchestration
---

# Force-Fit

Force-fit excursion discoveries back to the original problem.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Force-fitting requires holding two unrelated domains in mind simultaneously and deliberately creating connections that don't naturally exist. Benefits from focused creative tension without premature judgment.
