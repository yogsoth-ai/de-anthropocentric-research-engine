---
name: confidence-scoring
description: SOP for assigning calibrated confidence scores to causal claims based
  on evidence quality and quantity.
execution: sop
---

# Confidence Scoring

Assign calibrated confidence scores to causal claims.

## Tool

CC file edit

## Protocol

1. Count supporting evidence (weighted by evidence hierarchy)
2. Count contradicting evidence (weighted similarly)
3. Calculate net confidence: support_weight / (support_weight + contradict_weight)
4. Adjust for mechanism plausibility (+0.1 if strong mechanism, -0.1 if no mechanism)
5. Update claim page frontmatter confidence field

## HARD-GATE

<HARD-GATE>
Confidence must be between 0.0 and 1.0. Must cite the evidence used in calculation.
</HARD-GATE>

## Yield

Returns: `{ claim: string, confidence: number, evidence_count: number }`
