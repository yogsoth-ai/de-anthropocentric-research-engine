---
name: hypothesis-formation-saturation-detection
description: 'Shared SOP: judge whether the current activity has reached information saturation'
version: 1.0.0
category: hypothesis-formation
type: sop
shared: true
campaigns:
- gap-prioritization
- hypothesis-formulation
- research-question
input: Cumulative output of the current activity + the most recent round's increment
output: Saturated/not-saturated verdict + rationale
dependencies:
  skills:
  - subagent-spawning
---

# Saturation Detection

Judge whether the current activity has reached information saturation — decide whether to keep iterating.

## HARD-GATE

<HARD-GATE>
Input must contain: output from at least 2 iteration rounds (the increment needs to be compared).
</HARD-GATE>

## Pipeline

1. **Precondition check**: is there enough iteration data to compare
2. **Increment analysis**: what the most recent round added compared to the previous one
3. **Novelty judgment**: whether the added content provides genuinely new information
4. **Convergence detection**: whether the increment is decreasing
5. **Saturation verdict**: saturated / not saturated
6. **Output**: verdict + rationale + recommendation

## Saturation Criteria

**Saturated (should stop iterating)**:
- The most recent round produced no new substantive information
- The added content is mostly restatement or minor tweaks of what is already known
- The increment contributes < 5% to the final output

**Not saturated (should keep iterating)**:
- The most recent round produced a new dimension/perspective/information
- The increment makes a substantive contribution to the final output
- There are known but unexplored directions

## Output Format

```
Judgment: SATURATED / NOT_SATURATED
Confidence: HIGH / MEDIUM / LOW
Rationale: [one-sentence rationale]
Last round increment: [what the most recent round added]
Recommendation: STOP / CONTINUE (with direction)
```
