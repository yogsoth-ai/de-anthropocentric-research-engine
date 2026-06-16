---
name: present-candidates
description: 'Analyze sub-directions within the user''s chosen field and present ranked
  candidates. Combines sub-direction identification, skill-gap matching, and presentation
  into a single SOP. Depth scales by start mode: cold-start shows broad sub-directions,
  warm-start shows specific sub-problems, hot-start shows granular technical details.'
execution: dialogue
---

# Present Candidates

Analyze + present sub-directions as ranked candidates.

## Execution

Dialogue — inline, CC does the analysis and presents directly.

## What to Do

1. From broad-paper-search and deep-web-search results, identify distinct sub-directions within the chosen field
2. For each sub-direction, assess: current activity level, gap size, skill fit with ActorProfile
3. Rank and present to user

## Depth Scales by Start Mode

- **cold-start**: "Here are the broad sub-directions you could pursue in [field]"
- **warm-start**: "Within [direction], here are the specific sub-problems and research tracks"
- **hot-start**: "For [specific topic], here are the granular knowledge points and technical details to consider"

## What to Ask (one at a time)

- Which of these excites you most?
- Where do you think you could make a unique contribution?

## Output

RankedCandidates[] + user's selection.
