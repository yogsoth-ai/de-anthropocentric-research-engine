---
name: goal-decomposition
description: Structure the user's chosen direction into a formal goal tree using KAOS-style
  AND/OR decomposition. Validate feasibility against ActorProfile and ObstacleReport.
  Use after obstacle-analysis confirms the direction is viable.
dependencies:
  sops:
  - and-or-decompose
  - ask-decomposition-validation
  - feasibility-check
  - formulate-top-goal
  - validate-leaves
---

# Goal Decomposition

KAOS-style recursive goal decomposition into a validated GoalTree.

## Available SOPs

| SOP | Purpose | Execution |
|-----|---------|-----------|
| formulate-top-goal | Formulate the top-level goal statement with user | dialogue |
| and-or-decompose | Recursively decompose goal into AND/OR sub-goals | subagent |
| validate-leaves | Validate leaf goals are actionable and measurable | subagent |
| feasibility-check | Check leaf feasibility against ActorProfile + ObstacleReport | subagent |
| ask-decomposition-validation | Present GoalTree to user, get confirmation + priorities | dialogue |

## Methodology Guidance

- Small-scale OR situations can iterate within this tactic (try alternative decomposition)
- Infeasible paths: select OR alternative within tactic
- Fundamentally infeasible: return to earlier tactics (direction-narrowing or obstacle-analysis)
- You decide iteration depth

## Output (Tactic-Level Aggregation)

`GoalTree + user-confirmed priorities`
