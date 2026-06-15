---
name: detection-scoring
description: 'Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates
  how likely current controls would catch the failure before impact.'
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), chains (string)
dependencies:
  sops:
  - spawn-agent
---

# Detection Scoring

Rates each failure mode's detectability on an inverted 1-10 scale (10 = hardest to detect).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Detection assessment requires reasoning about observability and monitoring independent of severity/occurrence. Isolated context ensures unbiased evaluation.

## Input

- **failure_modes**: Failure mode catalog
- **chains**: Effect chains (to assess where detection could occur)

## Output

- **scores**: List of (failure_mode_id, detection_score, justification)
- **detection_gaps**: Modes with no current detection mechanism

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
