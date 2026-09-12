---
name: collect-independent-judgments
description: "Collect judgments/rankings from multiple genuinely independent evaluators or perspectives before exposing any peer outputs, preserving ballots and rationale for later social-choice aggregation."
---

# collect-independent-judgments
## Purpose
Collect blinded judgments from genuinely independent evaluators or perspectives before exposing peer outputs.
## Input contract
```yaml
required: [judgment_prompt, evaluator_roster, candidate_set, independence_rules]
optional: [rubric, response_deadline, abstention_policy]
constraints: [evaluators receive no peer judgments; each ballot preserves rationale and provenance]
```
## Procedure
1. Freeze the candidate set, rubric, prompt, and independence rules before collection.
2. Obtain one sealed judgment and rationale per evaluator, recording abstentions and unavailable evidence.
3. Check for shared data, model, prompt, or deliberation leakage before unblinding.
4. Unblind only after collection, then return ballots, independence flags, and an aggregation-ready dataset.
## Output contract
```yaml
produces: [sealed_ballots, independence_audit, rationale_set, aggregation_dataset]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class gate: declared universe = all commissioned evaluator ballots; numerator = ballots complete, provenance-linked, and leakage-free; batch increment = one sealed ballot; stopping reason = roster exhausted or a declared quorum reached with all exclusions documented; source references = evaluator, prompt, data, and ballot IDs; direction/threshold reason = independence confidence decreases with shared inputs or peer exposure.
- No aggregation before the leakage check is complete.
## Failure and counterexamples
Do not count multiple roles using the same evidence as independent judgments. An abstention is a recorded outcome, not a missing pass.
## Provenance map
- resolved: collective-adjudication
