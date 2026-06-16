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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| and-or-decompose | KAOS-style recursive goal decomposition. AND decomposition for sub-goals that must ALL be satisfied. OR decomposition for alternative paths where any one suffices. Produces a GoalTree (DAG structure). |
| ask-decomposition-validation | Present the GoalTree to the user for confirmation. Ask about reasonableness, missing elements, and priority ordering among sub-goals. |
| feasibility-check | Cross-reference the GoalTree against ActorProfile (capabilities), ObstacleReport (known barriers), and timeline (deadline feasibility). Identify infeasible paths and suggest OR alternatives. |
| formulate-top-goal | Express the user's chosen research direction as a formal goal statement in the format: 'Achieve [what], such that [effect], under [constraints]'. Confirm with user before proceeding to decomposition. |
| validate-leaves | Quality check on leaf nodes of the GoalTree. Verify each leaf is specific enough, actionable, and that the set of leaves fully covers the top goal. Flag issues for further decomposition. |

<!-- END available-tables (generated) -->
