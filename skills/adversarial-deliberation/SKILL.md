---
name: adversarial-deliberation
description: "Run structured attack/defense/adjudication over a claim, candidate, criterion set, or current winner. Perspective, target, escalation depth, loser-resurrection, and steelman/winner-stress modes are parameters; role execution is runtime-agnostic."
---

# adversarial-deliberation
## Purpose
Run structured attack, defense, cross-examination, and adjudication over a claim, candidate, criterion set, or current winner.
## Input contract
```yaml
mode_contracts:
  critic-defender-judge: &deliberation_input
    required: [target, claim_or_candidate, criteria]
    optional: [perspectives, escalation_depth]
    constraints: [target_scope_and_criteria_must_be_explicit, evidence_provenance_required]
  courtroom: *deliberation_input
  winner-stress: *deliberation_input
  resurrection-advocacy: *deliberation_input
  criteria-interrogation: *deliberation_input
  stakeholder-objection: *deliberation_input
  counter-thesis: *deliberation_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `construct-critique` to construct the strongest attack. You MUST load skill `construct-defense` to construct the strongest defensible case.
2. You MUST load skill `surface-assumptions` to expose load-bearing assumptions. You MUST load skill `construct-perspective-set` to construct alternate perspectives.
3. You MUST load skill `cross-examine` to cross-examine each exchange. You MUST load skill `assess-sensitivity` to perturb load-bearing choices.
4. You MUST load skill `adjudicate-exchange` to adjudicate against declared criteria. You MUST load skill `calibrate-adversarial-confidence` to update calibrated confidence.
   If the task shifts from balanced exchange to direct attack-surface probing, consider `structured-red-team`. If an exposed assumption requires focused perturbation, consider `assumption-stress-test`. If the surviving claim needs a decisive falsification program, `falsification-first-audit` may be the better next tactic.
Deviation: skip defense only when the target is explicitly exploratory; skip sensitivity only when no perturbable input is declared; otherwise retain all steps.
## Output contract
```yaml
mode_contracts:
  critic-defender-judge: &full_deliberation_output
    produces: [attack_record, defense_record, adjudication, confidence_trace]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  courtroom: *full_deliberation_output
  winner-stress:
    produces: [attack_record, adjudication, confidence_trace]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  resurrection-advocacy: &defense_deliberation_output
    produces: [defense_record, adjudication, confidence_trace]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  criteria-interrogation:
    produces: [attack_record, defense_record, adjudication]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  stakeholder-objection: *full_deliberation_output
  counter-thesis: *defense_deliberation_output
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
