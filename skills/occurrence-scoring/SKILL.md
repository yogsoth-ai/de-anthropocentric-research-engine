---
name: occurrence-scoring
description: Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), chains (string)
used-by: [failure-anticipation]
---

# Occurrence Scoring

Rates each failure mode's occurrence probability on a 1-10 scale.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Occurrence estimation requires probabilistic reasoning isolated from severity and detection considerations. Prevents halo effects.

## Input

- **failure_modes**: Failure mode catalog
- **chains**: Cause chains (for root cause probability assessment)

## Output

- **scores**: List of (failure_mode_id, occurrence_score, justification)
- **uncertainty_flags**: Modes where occurrence is highly uncertain
