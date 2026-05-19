---
name: multi-criteria-scoring
description: Score gaps on multiple dimensions (importance, feasibility, novelty, urgency, impact) using weighted multi-criteria decision analysis.
execution: subagent
prompt: ./prompt.md
input: gap_list (string), scoring_criteria (string)
used-by: gap-prioritization
---

# Multi-Criteria Scoring

Score and rank gaps using weighted multi-criteria decision analysis.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one scoring pass over a set of gaps.
