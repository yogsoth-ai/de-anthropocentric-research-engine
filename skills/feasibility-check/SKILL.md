---
name: feasibility-check
description: Cross-reference the GoalTree against ActorProfile (capabilities), ObstacleReport (known barriers), and timeline (deadline feasibility). Identify infeasible paths and suggest OR alternatives.
execution: subagent
prompt: ./prompt.md
input: goal_tree (string), actor_profile (string), obstacle_report (string)
---

# Feasibility Check

Reality-check the GoalTree against the user's actual situation.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- GoalTree (full structure)
- ActorProfile
- ObstacleReport

## Checks Against

- ActorProfile: Can this user do each leaf?
- ObstacleReport: Are known barriers addressed?
- Timeline: Can it be done in time?

## Output

Feasibility assessment per branch — feasible / stretch / infeasible + reasoning. For infeasible paths: suggest OR alternatives.
