---
name: severity-scoring
description: Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA
  severity scale calibrated for research artifacts.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), chains (string)
dependencies:
  sops:
  - spawn-agent
---

# Severity Scoring

Rates each failure mode's severity on a 1-10 scale based on end-effect impact.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Severity assessment requires consistent calibration across all modes. Isolated context prevents anchoring bias from occurrence or detection considerations.

## Input

- **failure_modes**: Failure mode catalog
- **chains**: Cause-mode-effect chains (for end-effect reference)

## Output

- **scores**: List of (failure_mode_id, severity_score, justification)
- **calibration_notes**: Any scoring edge cases or assumptions
