---
name: present-and-ask
description: Present the field panorama to the user and gather their preferences —
  which fields interest them, which they reject, and why. A dialogue SOP that bridges
  landscape-synthesis output to user decision.
execution: dialogue
---

# Present and Ask

Show field panorama to user and gather preferences.

## Execution

Dialogue — inline, no subagent.

## What to Present

FieldPanorama summary — each field with its key metrics and recommendation.

## What to Ask (one at a time)

- Which of these fields interest you? Why?
- Are there any you instinctively reject? Why?
- Is there a direction not listed that you'd like me to explore?

## Output

User's selected 1-2 fields of interest + reasoning.
