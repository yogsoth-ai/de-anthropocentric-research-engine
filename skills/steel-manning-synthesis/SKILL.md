---
name: steel-manning-synthesis
description: Synthesize all attacks and verdicts into a final unified assessment with surviving concerns and recommended modifications.
execution: subagent
prompt: ./prompt.md
input: all_attacks, all_verdicts
used-by: [steel-manning]
---

# Steel-Manning Synthesis

The final integration step — synthesizes all perspective attacks, debate verdicts, and challenge results into a unified assessment. Produces the campaign's final verdict with surviving concerns and recommended modifications.

## Execution

Spawns a subagent that receives all attack and verdict data from the campaign and produces the final synthesis.

## Why Subagent

- Synthesis requires impartial integration across all prior work
- Must weigh competing perspectives without favoring any
- Isolation from individual attack/verdict roles ensures balanced final assessment

## HARD-GATE

Output must include:
- Final verdict: ACCEPT / REJECT / REVISE
- Every attack addressed (not ignored)
- Surviving concerns with severity ratings
- Recommended modifications (if REVISE)
- Confidence level in the verdict
