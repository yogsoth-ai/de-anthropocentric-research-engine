---
name: validate-leaves
description: Quality check on leaf nodes of the GoalTree. Verify each leaf is specific
  enough, actionable, and that the set of leaves fully covers the top goal. Flag issues
  for further decomposition.
execution: subagent
prompt: ./prompt.md
input: goal_tree (string), top_goal (string)
dependencies:
  sops:
  - spawn-agent
---

# Validate Leaves

Ensure GoalTree leaf nodes are high quality.

## Execution

Subagent — spawned via `subagent-spawning/spawn-agent` skill.

## Input

- GoalTree (full structure)
- Top goal statement

## Checks

- Is each leaf specific enough to act on?
- Is each leaf verifiable (can you tell when it's done)?
- Does the complete set of leaves cover the top goal?

## Output

Validation report — which leaves pass, which need further decomposition, coverage gaps.
