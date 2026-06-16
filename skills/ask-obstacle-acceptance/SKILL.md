---
name: ask-obstacle-acceptance
description: Present obstacles with their severity assessments and proposed mitigations
  to the user. Ask whether they can accept these obstacles. If unacceptable after
  2 rounds, return to present-candidates.
execution: dialogue
---

# Ask Obstacle Acceptance

Get user's acceptance of the obstacle landscape.

## Execution

Dialogue — inline, no subagent.

## What to Present

Each obstacle with:
- Severity assessment
- Proposed mitigation
- Estimated effort

## What to Ask (one at a time)

- Given these obstacles and mitigations, can you accept this direction?
- Are there difficulties I missed that you're aware of?
- Is there any obstacle here that's a complete deal-breaker?

## Search

Optional — may use the 5 imported skills if user raises new concerns that need investigation.

## If Unacceptable

Signal to tactic that direction needs to change (return to present-candidates in direction-narrowing tactic).

## Output

User's acceptance decision + any new concerns raised.
