---
name: explore-resume
description: Understand the user's background comprehensively — technical stack, project experience, research experience, publications, research directions. Allows user to express interest beyond their resume. Execute once only, never re-run.
execution: dialogue
---

# Explore Resume

Build a comprehensive picture of who the user is professionally and academically.

## Execution

Dialogue — inline, no subagent.

## What to Ask About (one at a time)

- Technical stack (languages, frameworks, tools they're proficient in)
- Project experience (what have they built or contributed to)
- Course/research experience (what have they studied formally)
- Publications (if any — papers, preprints, technical reports)
- Current research directions (what are they working on now)
- Areas of interest beyond current experience (what excites them that they haven't done yet)

## Key Behaviors

- Allow user to express interest in areas outside their resume — this is not a constraint-gathering exercise
- In cold-start: user may not know what they can do. That's fine — capture what they've done and what excites them
- Execute once only. Never re-run this SOP.

## Output

Background section of ActorProfile.
