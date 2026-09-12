# adversarial-deliberation
## Purpose
Run structured attack, defense, cross-examination, and adjudication over a claim, candidate, criterion set, or current winner.
## Input contract
```yaml
required: [target, claim_or_candidate, criteria]
optional: [perspectives, escalation_depth, mode]
constraints: [target scope and criteria must be explicit, evidence provenance required]
```
## Execution protocol
1. Construct the strongest attack and defensible case (`construct-critique`, `construct-defense`).
2. Expose assumptions and alternate perspectives (`surface-assumptions`, `construct-perspective-set`).
3. Cross-examine each exchange and perturb load-bearing choices (`cross-examine`, `assess-sensitivity`).
4. Adjudicate against declared criteria and update calibrated confidence (`adjudicate-exchange`, `calibrate-adversarial-confidence`).
Deviation: skip defense only when the target is explicitly exploratory; skip sensitivity only when no perturbable input is declared; otherwise retain all steps.
## Output contract
```yaml
produces: [attack_record, defense_record, adjudication, confidence_trace]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- A-class debate calibration: declared universe = all rounds and claims; numerator = rounds with evidence-linked confidence updates; batch increment = one completed exchange; stopping reason = confidence stabilizes or unresolved disagreement is explicitly reported; source references = evidence IDs and round IDs; direction/threshold reason = escalate when new evidence changes ranking, terminate only when criteria are adjudicated or a non-resolvable uncertainty is recorded.
- Every verdict must cite criteria and preserve dissent.
## Failure and counterexamples
Do not treat rhetorical fluency as evidence. Mark unresolved when attack and defense share an untested assumption or criteria are absent.
## Provenance map
- resolved: multiagent-debate
- resolved: critic-defender-judge
- resolved: courtroom-structured
- resolved: adversarial-escalation
- resolved: steel-manning
- resolved: resurrection-advocacy
- resolved: winner-stress-testing
- resolved: adversarial-debate-protocol
- resolved: assumption-excavation
- resolved: multi-perspective-attack
- intermediate: Pass5/adversarial-debate
- intermediate: Pass5/steelman-validation
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Structured attack/defense/adjudication; loser-resurrection and steelman/winner-stress are parameters. |
## Context checkpoint / Delta notes
Append claim, criteria, attack/defense records, dissent, confidence changes, and unresolved questions.

## Mode branches
- `critic-defender-judge`: attack, defense, adjudication.
- `courtroom`: add cross-examination and explicit evidentiary ruling.
- `winner-stress`: perturb the current winner and record failure triggers.
- `resurrection-advocacy`: re-open a rejected candidate with a steelman.
- `criteria-interrogation`: challenge the criteria before ranking.
- `stakeholder-objection`: add perspective-specific objections.
- `counter-thesis`: require a mechanism-distinct opposing thesis.
