---
name: strength-assessment
description: Tactic for assessing argument strength — evaluate evidence quality, count
  independent sources, check for defeaters, assign calibrated confidence scores.
execution: tactic
dependencies:
  sops:
  - evidence-attachment
  - strength-scoring
---

# Strength Assessment

Evaluate the strength of claims based on their evidential support.

## Minimum Yield

<HARD-GATE>
Must score ≥3 claims per invocation.
</HARD-GATE>

## Protocol

1. For each claim, gather all linked evidence (supporting and contradicting)
2. Evaluate evidence quality:
   - Source reliability (peer-reviewed > preprint > blog)
   - Directness (direct test > indirect inference > analogy)
   - Independence (multiple independent sources > single source chain)
3. Check for defeaters:
   - Undercutting defeaters (evidence that the support doesn't actually support)
   - Rebutting defeaters (evidence directly contradicting the claim)
   - Undermining defeaters (evidence that the evidence itself is unreliable)
4. Assign strength score (0-10) with explicit reasoning via `strength-scoring`
5. Flag claims with score < 3 as "weak" and claims with score > 7 as "strong"

## SOPs Used

- **strength-scoring** — assign and record strength scores
- **evidence-attachment** — create additional evidence links discovered during assessment

## Yield Report

Returns: `{ claims_scored: number, strong_claims: number, weak_claims: number, defeaters_found: number }`
