---
name: saturation-detection
description: Determines whether validation has reached saturation — no new weaknesses
  or failure modes being discovered. Used by all 5 campaigns as termination signal.
execution: subagent
prompt: ./prompt.md
input: findings_accumulated (string), latest_iteration_findings (string)
dependencies:
  sops:
  - spawn-agent
---

# Saturation Detection

Determines whether validation has reached saturation — no new weaknesses being discovered.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Requires comparing accumulated findings against latest iteration to compute novelty ratio — dedicated context prevents contamination from ongoing analysis.

## Input

- **findings_accumulated**: Running list of all findings from current campaign
- **latest_iteration_findings**: Findings from the most recent iteration

## Output

- **verdict**: `saturated` | `not-saturated`
- **confidence**: 0.0–1.0
- **novelty_ratio**: percentage of latest findings that are genuinely new
- **reasoning**: explanation of verdict

## Hard Constraint

≥3 consecutive iterations with <10% novel findings → `saturated`

## Budget

One unit = one saturation check. Called after each tactic iteration.
