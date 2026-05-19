---
name: detection-scoring
description: "Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact."
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), chains (string)
used-by: [failure-anticipation]
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
