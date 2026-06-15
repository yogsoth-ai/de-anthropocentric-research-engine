---
name: steel-manning-synthesis
description: Synthesize all attacks and verdicts into a final unified assessment with
  surviving concerns and recommended modifications.
execution: subagent
prompt: ./prompt.md
input: all_attacks, all_verdicts
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
