---
name: action-priority-matrix
description: Compute Risk Priority Number (RPN = S x O x D), classify failure modes
  into H/M/L action priority per AIAG-VDA tables.
execution: subagent
prompt: ./prompt.md
input: severity_scores (string), occurrence_scores (string), detection_scores (string)
dependencies:
  sops:
  - spawn-agent
---

# Action Priority Matrix

Computes RPN and classifies failure modes into High/Medium/Low action priority.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Priority classification requires mechanical computation followed by judgment on borderline cases. Isolated context ensures consistent application of thresholds.

## Input

- **severity_scores**: S scores for all failure modes
- **occurrence_scores**: O scores for all failure modes
- **detection_scores**: D scores for all failure modes

## Output

- **priority_matrix**: Full table with S, O, D, RPN, and H/M/L classification
- **action_required**: H-priority items requiring mandatory mitigation
- **borderline_cases**: Items near threshold boundaries
