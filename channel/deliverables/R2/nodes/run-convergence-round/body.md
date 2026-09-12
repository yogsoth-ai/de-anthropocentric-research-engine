# run-convergence-round
## Purpose
Run one structured revision round that updates arguments and evidence rather than merely averaging opinions.
## Input contract
```yaml
required: [current_state, participant_judgments, revision_prompt, convergence_rule]
optional: [prior_rounds, dissent_policy, stopping_rule]
constraints: [each participant receives the same state snapshot; revisions cite changed evidence or reasoning]
```
## Procedure
1. Freeze the current claims, evidence, disagreements, and round objective.
2. Collect independent judgments or critiques before distributing peer summaries.
3. Distribute the structured feedback, request revisions, and record what changed or remained disputed.
4. Measure convergence, preserve dissent, and return the next state plus a continue/stop recommendation.
## Output contract
```yaml
produces: [round_record, revised_state, dissent_register, convergence_measure, next_round_decision]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class gate: declared universe = all participants and claims in the round; numerator = judgments with evidence-linked revision or explicit unchanged rationale; batch increment = one completed round; stopping reason = convergence criterion met or remaining dissent is irreducible and documented; source references = state, judgment, and evidence IDs; direction/threshold reason = convergence increases only when independent revisions reduce claim-level disagreement without deleting supported dissent.
- Averaging opinions without a revision trace is not a convergence round.
## Failure and counterexamples
Do not call repeated agreement convergence when participants saw the same unchallenged premise. A changed score without changed reasoning remains unresolved.
## Provenance map
- resolved: iterative-convergence-round
