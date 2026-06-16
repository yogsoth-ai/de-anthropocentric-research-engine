---
name: explanation-generation
description: 'SOP: generate a list of candidate explanations for an anomalous phenomenon'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Structured anomaly description (from anomaly-characterization output)'
output: 'Candidate explanation list + observable predictions for each'
dependencies:
  skills:
  - subagent-spawning
---

# Explanation Generation
Generate multiple candidate explanations for an anomalous phenomenon through divergent thinking, and derive observable predictions for each explanation.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. A structured anomaly description exists (with phenomenon + deviation + excluded_explanations)
2. The anomaly has been confirmed as non-trivial (severity ≠ trivial)

Not satisfied → stop and return an error: anomaly-characterization must be completed first.
</HARD-GATE>

## Pipeline
1. Pre-check: verify the completeness of the anomaly description
2. Divergent thinking: generate ≥3 mechanistically distinct candidate explanations (not variants of the same explanation)
3. Prediction derivation: for each explanation, derive 1-2 observable predictions (what should be observed if the explanation is correct)
4. Evidence-consistency check: check each explanation against known evidence (consistent/inconsistent/neutral)
5. Deduplication: merge explanations with the same mechanism
6. Output the candidate explanation list

## Output Format
```json
[
  {
    "explanation_id": "E1",
    "statement": "Candidate explanation in one sentence",
    "mechanism": "How this explanation accounts for the anomaly",
    "predictions": [
      "Observable prediction 1 if this explanation is correct",
      "Observable prediction 2"
    ],
    "evidence_consistency": "consistent | inconsistent | neutral",
    "evidence_notes": "What existing evidence supports or contradicts this",
    "novelty": "known | extension | novel"
  }
]
```
At least 3 mechanistically distinct candidate explanations.
