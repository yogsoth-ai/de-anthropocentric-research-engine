---
name: and-or-decompose
description: KAOS-style recursive goal decomposition. AND decomposition for sub-goals that must ALL be satisfied. OR decomposition for alternative paths where any one suffices. Produces a GoalTree (DAG structure).
execution: subagent
prompt: ./prompt.md
input: top_goal (string), actor_profile (string), obstacle_report (string)
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
