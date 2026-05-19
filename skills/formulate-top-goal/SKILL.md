---
name: formulate-top-goal
description: "Express the user's chosen research direction as a formal goal statement in the format: 'Achieve [what], such that [effect], under [constraints]'. Confirm with user before proceeding to decomposition."
execution: dialogue
---

# Formulate Top Goal

Crystallize the user's direction into a formal, confirmable goal statement.

## Execution

Dialogue — inline, no subagent.

## Format

"Achieve [what], such that [effect], under [constraints]"

## Process

1. Draft the goal statement based on accumulated context (direction + ActorProfile + obstacles accepted)
2. Present to user
3. Ask: "Is this what you want to achieve? Should I adjust anything?"
4. Iterate until user confirms

## Output

Confirmed top-level goal statement.
