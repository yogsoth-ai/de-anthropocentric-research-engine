---
name: falsification-first-audit
description: "Convert a sharp scientific claim into the cheapest decisive falsification program. Steelman the claim into a precise testable form, specify observations/computations that could break it, execute the most informative probes first, and return only BROKEN, CORROBORATED, or UNFALSIFIABLE rather than a resilience score."
---

# falsification-first-audit
## Purpose
Convert a sharp claim into the cheapest decisive falsification program and return BROKEN, CORROBORATED, or UNFALSIFIABLE.
## Input contract
```yaml
required: [claim, scope, available_evidence]
optional: [mechanism, candidate_tests, mode]
constraints: [claim must expose observable consequences and boundary conditions]
```
## Execution protocol
1. Sharpen the claim and expose assumptions (`sharpen-falsifiable-claim`, `surface-assumptions`).
2. Design the cheapest decisive falsification test (`design-falsification-test`).
3. Execute the most informative probe (`execute-probe`).
4. Classify only the permitted truth-seeking verdict (`classify-falsification-verdict`).
Deviation: if no legitimate falsifier can be specified or reached, stop with UNFALSIFIABLE; do not substitute a resilience score.
## Output contract
```yaml
produces: [sharp_claim, falsification_program, probe_record, falsification_verdict]
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
