---
name: consensus-measurement
description: Compute consensus score from collected judgments using the appropriate statistical method.
execution: subagent
prompt: ./prompt.md
input: judgments[]
used-by: structured-consensus
---

# Consensus Measurement

Compute a quantitative consensus score from the collected judgments. Automatically selects the appropriate measurement method based on data type (IQR for continuous, percentage agreement for categorical, Kendall's W for rankings).

## Execution

Spawn a subagent that analyzes the judgments array, determines the appropriate consensus metric, computes the score, and reports whether the consensus threshold is met.

## Why Subagent

- Statistical computation is a pure function with clear input/output
- Method selection logic is self-contained
- Result feeds directly into round-decision

## HARD-GATE

Output MUST contain: `consensus_score` (numeric), `method_used` (string), `threshold_met` (boolean), and `interpretation` (string). Score must be computed, not estimated.
