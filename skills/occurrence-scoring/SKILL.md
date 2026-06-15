---
name: occurrence-scoring
description: Rate failure mode occurrence probability 1-10. Estimates how likely each
  failure mode is to manifest during research execution.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), chains (string)
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
