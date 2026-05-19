---
name: negation-definition
description: Define strongest plausible alternatives (negations) for each assumption to enable perturbation analysis.
execution: subagent
prompt: ./prompt.md
input: assumption_list
used-by: assumption-criticality
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete negation definition pass over an assumption list.
