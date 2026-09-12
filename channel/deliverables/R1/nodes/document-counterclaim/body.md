# document-counterclaim

## Purpose

Document a credible counterclaim, its supporting basis, scope, and implications for the focal claim.

## Input contract

```yaml
required: [focal_claim, counterclaim, evidence_records]
optional: [argument_context, boundary_conditions, response_options]
constraints: [counterclaim must be stated in its strongest evidence-supported form]
```

## Procedure

1. State the counterclaim and the proposition it challenges.
2. Attach supporting evidence, assumptions, and boundary conditions.
3. Compare explanatory coverage, conflicts, and unresolved evidence.
4. Record implications, possible rebuttals, and residual uncertainty.

## Output contract

```yaml
produces: [counterclaim_record, support_map, assumption_register, implication_set, rebuttal_questions]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Counterclaim is not a caricature of the opposing position.
- Evidence and scope are explicit.

## Failure and counterexamples

Do not dismiss a counterclaim because it is inconvenient or confuse disagreement with refutation.

## Provenance map

- `resolved: document-counterclaim`

