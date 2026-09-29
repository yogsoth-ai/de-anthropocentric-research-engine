---
name: filter-false-gap
description: "Distinguish a real knowledge gap from search failure, questions that prior work closes, and intrinsically unanswerable formulations. Prior work that touches a question without closing it leaves the gap open."
---

# filter-false-gap
## Purpose
Distinguish a real knowledge gap from search failure, closed questions, or unanswerable formulations, judging prior work by whether it closes the question rather than by whether it exists.
## Input contract
```yaml
required: [gap_claim, search_record, evidence_scope]
optional: [prior_findings, answerability_constraints]
constraints: [absence claims must be tied to a declared search and scope; a closure verdict cites the work that closes the question]
```
## Procedure
1. Check whether the search covered the declared evidence scope.
2. Compare the claim with prior findings. Prior work closes the question only when it is independently replicated, measures the construct directly, holds across the scope the claim names, and faces no unresolved contrary result; name each condition that fails and the work it applies to.
3. For a region no prior work touches, state why it is empty: unsearched, incoherent as a combination, unmeasurable, infeasible to study, or open.
4. Test whether the formulation is answerable under stated constraints.
5. Label `open`, `touched_not_closed`, `search_failure`, `resolved`, or `unanswerable` with rationale.
## Output contract
```yaml
produces: [gap_verdict, search_adequacy, closure_assessment, answerability_note]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Verdict cites search adequacy and distinguishes unknown from absent.
- A `resolved` verdict cites the closing work and shows all four closure conditions hold; a `touched_not_closed` verdict names the failing condition.
- An `open` verdict states why the region is worth entering, not only that it is empty.
## Failure and counterexamples
Do not confirm a gap from an under-scoped search, reject a gap merely because evidence is inconvenient, or treat publication in a region as closure of its question.
## Provenance map
- `deep-insight/false-gap-filtering`: resolved.
