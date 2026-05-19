---
name: re-scoring
description: Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), mitigations (string), original_scores (string)
used-by: [failure-anticipation]
---

# Re-Scoring

Re-evaluates Severity, Occurrence, and Detection scores after mitigations are applied.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Re-scoring requires fresh evaluation without anchoring to original scores. Isolated context prevents confirmation bias toward expected improvement.

## Input

- **failure_modes**: Original failure mode descriptions
- **mitigations**: Proposed mitigation measures
- **original_scores**: Pre-mitigation S/O/D scores for comparison

## Output

- **new_scores**: Post-mitigation S, O, D, and RPN for each mode
- **effectiveness**: Comparison with original scores
- **still_high**: Modes that remain H-priority after mitigation
