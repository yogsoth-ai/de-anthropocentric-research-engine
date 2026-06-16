---
name: falsifiability-check
description: 'SOP: check whether a hypothesis meets the falsifiability criterion'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Hypothesis statement (with statement + variables + mechanism)'
output: 'Falsifiability verdict + falsification scenario + revision suggestions (if unfalsifiable)'
dependencies:
  skills:
  - subagent-spawning
---

# Falsifiability Check
Check hypotheses against Popper's falsifiability criterion, ensuring every hypothesis has an explicit refutation condition.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 hypothesis statement exists (with statement)
2. The hypothesis involves observable variables or phenomena

Not satisfied → stop and return an error: hypothesis statement is incomplete.
</HARD-GATE>

## Pipeline
1. Pre-check: verify the completeness of the hypothesis statement
2. Observable-prediction derivation: derive ≥2 specific observable predictions from the hypothesis
3. Refutation-prediction construction: construct "what should be observed if the hypothesis is wrong"
4. Feasibility assessment: is the refutation prediction testable technically and ethically?
5. Verdict: falsifiable / not falsifiable / needs revision
6. If not falsifiable: provide specific revision suggestions to make it falsifiable
7. Output the verdict

## Output Format
```json
{
  "hypothesis_id": "H1",
  "statement": "...",
  "positive_predictions": [
    "If H1 is true, we should observe X in condition Y"
  ],
  "falsification_scenario": "Specific observation that would conclusively refute H1",
  "testability": "high | medium | low",
  "verdict": "falsifiable | not_falsifiable | needs_revision",
  "revision_suggestion": "How to make it falsifiable (null if already falsifiable)",
  "notes": "Additional considerations"
}
```
