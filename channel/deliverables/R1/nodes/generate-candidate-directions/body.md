# generate-candidate-directions

## Purpose

Generate diverse candidate research fields or subfields consistent with context while permitting deliberate boundary crossing.

## Input contract

```yaml
required: [research_intent, scope_anchor]
optional: [seed_evidence, actor_profile, constraints, neighboring_domains]
constraints: [each candidate must state fit, boundary crossing, and evidence needs]
```

## Procedure

1. Extract the problem mechanism, outcome, and scope anchor.
2. Generate candidates within the anchor and from adjacent domains.
3. Record the transfer or boundary-crossing rationale for each candidate.
4. Remove duplicates while preserving materially different mechanisms.

## Output contract

```yaml
produces: [candidate_directions, fit_rationales, boundary_crossings, evidence_questions]
delta_fields: [findings, hypothesis_updates, uncertainties, open_questions, recommended_jumps]
```

## Quality gates

- Candidates are distinct by mechanism or evidence opportunity.
- Speculative candidates are labeled as such.

## Failure and counterexamples

Do not equate popularity with fit or generate a list of fields without a boundary rationale.

## Provenance map

- `resolved: generate-candidate-fields`
