---
name: strength-scoring
description: SOP for assigning calibrated strength scores to claims — evaluate evidence
  weight, count independent sources, check defeaters, produce scored assessment.
execution: sop
---

# Strength Scoring

Assign a calibrated strength score (0-10) to a claim based on its evidential support.

## Tool

`vault_query_graph` + CC reasoning

## Protocol

1. Query graph for all edges connected to the target claim
2. Count and classify:
   - Supporting evidence (by quality: strong/moderate/weak)
   - Contradicting evidence (by quality)
   - Independent source count
3. Apply scoring rubric:
   - 0-2: No evidence or only weak indirect support
   - 3-4: Some moderate evidence, significant contradictions
   - 5-6: Multiple moderate sources, few contradictions
   - 7-8: Strong direct evidence from independent sources
   - 9-10: Overwhelming convergent evidence, no undefeated contradictions
4. Update claim page frontmatter with `strength: <score>` and `strength-reasoning: <one-line>`

## HARD-GATE

<HARD-GATE>
Must provide explicit reasoning for the score. A number without justification is not valid.
</HARD-GATE>

## Yield

Returns: `{ claim: string, score: number, supporting: number, contradicting: number, reasoning: string }`
