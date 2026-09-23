---
name: falsification-first-audit
description: "Convert a sharp scientific claim into the cheapest decisive falsification program. Steelman the claim into a precise testable form, specify observations/computations that could break it, execute the most informative probes first, and return only BROKEN, CORROBORATED, or UNFALSIFIABLE rather than a resilience score."
---

# falsification-first-audit
## Purpose
Convert a sharp claim into the cheapest decisive falsification program and return BROKEN, CORROBORATED, or UNFALSIFIABLE.
## Input contract
```yaml
mode_contracts:
  sharp-claim: &falsification_input
    required: [claim, scope, available_evidence]
    optional: [mechanism, candidate_tests]
    constraints: [claim_must_expose_observable_consequences_and_boundary_conditions]
  truthseeking-debate: *falsification_input
  truthseeking-red-team: *falsification_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `sharpen-falsifiable-claim` to sharpen the claim. You MUST load skill `surface-assumptions` to expose its assumptions.
2. You MUST load skill `design-falsification-test` to design the cheapest decisive falsification test.
3. You MUST load skill `execute-probe` to execute the most informative probe.
4. You MUST load skill `classify-falsification-verdict` to classify only the permitted truth-seeking verdict.
   If the claim depends on a structural mapping, consider `audit-structural-equivalence`. If the test or oracle may be circular, consider `audit-validator-independence`. If agreement among paths may not be independent, consider `audit-convergence-independence`. If simplicity is carrying the claim, consider `audit-explanatory-compression`. If survival is confined to an uncertain region, consider `map-validity-envelope`.
Deviation: if no legitimate falsifier can be specified or reached, stop with UNFALSIFIABLE; do not substitute a resilience score.
## Output contract
```yaml
mode_contracts:
  sharp-claim:
    produces: [claim_falsifiability, refutation_condition, attacks_attempted, outcome_bucket, refutation_or_surviving_forbidden_content, honest_residue]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions]
  truthseeking-debate:
    produces: [most_falsifiable_form, committed_refuter, cross_examination_findings, attack_severity, outcome_bucket, refutation_or_forbidden_content]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions]
  truthseeking-red-team:
    produces: [claim_load_rank, assumption_classification, refutation_condition, refutation_attempt, outcome_bucket, framing_risk_brief]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions]
```
## Thresholds and quality gates
- Verdict is BROKEN only when a legitimate falsifier succeeds; CORROBORATED only after an adequate test fails to falsify; otherwise UNFALSIFIABLE.
- Preserve scope, power/precision assumptions, and probe provenance.
## Failure and counterexamples
Post-hoc accommodation, unfalsifiable wording, or an unreachable test cannot support CORROBORATED.
## Provenance map
- resolved: falsification-first-stress-test
- resolved: adversarial-debate-truthseeking
- resolved: red-team-truthseeking
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Return only BROKEN, CORROBORATED, or UNFALSIFIABLE; no resilience score. |
## Context checkpoint / Delta notes
Append sharpened claim, test design, probe result, verdict, and unresolved falsifier questions.

## Mode branches
- `sharp-claim`: direct falsification program.
- `truthseeking-debate`: combine with adversarial exchange while preserving verdict semantics.
- `truthseeking-red-team`: use attack probes while preserving verdict semantics.
