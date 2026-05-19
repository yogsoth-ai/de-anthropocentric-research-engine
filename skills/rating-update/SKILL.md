---
name: rating-update
description: Incorporate a new judgment into the rating model and return updated ratings for all candidates.
execution: subagent
prompt: ./prompt.md
input: judgment(object), current_ratings(object), method(string)
used-by: pairwise-ranking
---

# Rating Update

Incorporates a new pairwise judgment into the current rating model. Applies the specified method's update rules (Bradley-Terry MLE, Elo K-factor, TrueSkill Gaussian update, etc.) and returns the full updated rating vector.

## Execution

Runs as a subagent. Receives judgment, current ratings, and method specification, returns updated ratings.

## Why Subagent

Rating updates involve mathematical computation specific to the chosen method. Isolating this ensures correct application of update formulas without mixing method-specific logic into orchestration.

## HARD-GATE

Output MUST contain updated ratings for ALL candidates (not just the compared pair). The winner's rating MUST increase or stay the same. The method field MUST match the input method.
