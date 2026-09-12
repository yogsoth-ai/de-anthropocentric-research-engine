# filter-false-gap
## Purpose
Distinguish a real knowledge gap from search failure, resolved questions, or unanswerable formulations.
## Input contract
```yaml
required: [gap_claim, search_record, evidence_scope]
optional: [prior_findings, answerability_constraints]
constraints: [absence claims must be tied to a declared search and scope]
```
## Procedure
1. Check whether the search covered the declared evidence scope.
2. Compare the claim with existing findings and resolved questions.
3. Test whether the formulation is answerable under stated constraints.
4. Label real gap, search failure, resolved, or unanswerable with rationale.
## Output contract
```yaml
produces: [gap_verdict, search_adequacy, answerability_note]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Verdict cites search adequacy and distinguishes unknown from absent.
## Failure and counterexamples
Do not confirm a gap from an under-scoped search or reject a gap merely because evidence is inconvenient.
## Provenance map
- `deep-insight/false-gap-filtering`: resolved.
