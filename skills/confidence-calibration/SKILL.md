---
name: confidence-calibration
description: Calibrates confidence scores based on debate progression. Determines
  whether to escalate, continue, or terminate based on cumulative evidence.
execution: subagent
prompt: ./prompt.md
input: round_verdicts (string), confidence_history (string), budget_remaining (string)
dependencies:
  sops:
  - spawn-agent
---

# Confidence Calibration

Calibrates confidence based on debate progression.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Calibration requires meta-analysis of debate trajectory without being anchored to any single round's outcome. Isolated context enables objective trend assessment.

## Input

- **round_verdicts**: All judge verdicts so far
- **confidence_history**: Confidence scores from each round
- **budget_remaining**: Rounds/searches remaining in budget

## Output

- **calibrated_confidence**: Updated confidence in artifact viability (0.0–1.0)
- **decision**: escalate / continue / terminate
- **reasoning**: Why this decision given the trajectory
- **saturation_flag**: Whether debate is producing diminishing returns

## Budget

One unit = one calibration assessment per round.
