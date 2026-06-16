---
name: and-or-decompose
description: KAOS-style recursive goal decomposition. AND decomposition for sub-goals
  that must ALL be satisfied. OR decomposition for alternative paths where any one
  suffices. Produces a GoalTree (DAG structure).
execution: subagent
prompt: ./prompt.md
input: top_goal (string), actor_profile (string), obstacle_report (string)
dependencies:
  sops:
  - spawn-agent
---

# AND/OR Decompose

Recursively decompose the top goal into a structured GoalTree.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- Confirmed top goal
- ActorProfile
- ObstacleReport

## Output

GoalTree — DAG with AND/OR nodes, leaf nodes representing actionable sub-goals.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
