---
name: weight-elicitation-sop
description: Compute criteria weights using a specified elicitation method (AHP, Swing, BWM, MACBETH, or Simos).
execution: subagent
prompt: ./prompt.md
input: criteria (string[]), method (string)
used-by: multi-criteria-scoring
---

# Weight Elicitation SOP

Compute criteria weight vector using a specified weighting method (AHP, Swing, BWM, MACBETH, or Simos).

## Execution

Subagent receives criteria list and method name, executes the standard procedure for that method, and outputs a normalized weight vector.

## Why Subagent

Weight computation involves pairwise comparison matrices or ranking logic, requiring independent reasoning space and consistency verification.

## HARD-GATE

Weights must sum to 1.0 (allowing ±0.001 rounding error), and must pass the method's consistency check (e.g., AHP CR < 0.1).
