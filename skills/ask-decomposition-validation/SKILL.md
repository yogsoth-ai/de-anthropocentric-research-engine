---
name: ask-decomposition-validation
description: Present the GoalTree to the user for confirmation. Ask about reasonableness, missing elements, and priority ordering among sub-goals.
execution: dialogue
---

# Ask Decomposition Validation

Get user confirmation of the goal decomposition.

## Execution

Dialogue — inline, no subagent.

## What to Present

- GoalTree (simplified visual)
- Validation results (from validate-leaves)
- Feasibility assessment (from feasibility-check)

## What to Ask (one at a time)

- Does this decomposition look reasonable to you?
- Is there anything missing — a sub-goal I haven't captured?
- Among these sub-goals, what's your priority order? What would you tackle first?

## Output

User-confirmed GoalTree + priority ordering.
