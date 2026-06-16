---
name: plausibility-ranking
description: 'SOP: rank candidate explanations by plausibility using multi-dimensional weighted scoring'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Candidate explanation list + relevant evidence (from explanation-generation output)'
output: 'Plausibility-ranked list + per-dimension scores + ranking rationale'
dependencies:
  skills:
  - subagent-spawning
---

# Plausibility Ranking
Score candidate explanations on three dimensions — evidence consistency, parsimony, and explanatory scope — then weight and rank them to produce a priority list.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. ≥2 candidate explanations exist (from explanation-generation)
2. Each explanation has mechanism and predictions fields

Not satisfied → stop, return error: at least 2 candidate explanations are needed to rank.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the candidate explanation list
2. Evidence-consistency score (0-10): degree of agreement with known evidence
3. Parsimony score (0-10): number of assumptions the explanation requires (fewer = higher score)
4. Explanatory-scope score (0-10): how many related phenomena it can explain (not just the current anomaly)
5. Weighted ranking: default weights 0.5/0.3/0.2 (evidence/parsimony/scope), adjustable
6. Output ranked list + rationale

## Output Format
```json
{
  "weights": {"evidence": 0.5, "parsimony": 0.3, "scope": 0.2},
  "rankings": [
    {
      "rank": 1,
      "explanation_id": "E1",
      "statement": "...",
      "scores": {
        "evidence_consistency": 8,
        "parsimony": 7,
        "explanatory_scope": 6
      },
      "weighted_score": 7.4,
      "rationale": "Why this ranks here",
      "key_weakness": "Main reason it might be wrong"
    }
  ]
}
```
