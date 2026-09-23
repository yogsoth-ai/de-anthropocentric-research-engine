# identify-theory

## Purpose

Identify the theory or theoretical family that best organizes a claim, mechanism, or observed regularity.

## Input contract

```yaml
required: [claim_or_mechanism, construct_definitions, evidence_context]
optional: [candidate_theories, domain_scope]
constraints: [theory identification requires construct and mechanism correspondence]
```

## Procedure

1. Extract constructs, relations, boundary conditions, and explanatory target.
2. Compare candidate theories by construct mapping and predicted relations.
3. Record supporting, conflicting, and missing evidence for each mapping.
4. State the selected theory or unresolved alternatives with scope limits.

## Output contract

```yaml
produces: [theory_candidates, construct_mapping, relation_mapping, theory_assessment, scope_limits]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Mapping is based on definitions and relations, not name similarity.
- Boundary conditions are retained.

## Failure and counterexamples

Do not infer theoretical identity from shared vocabulary or force a theory when only a local mechanism is supported.

## Provenance map

- `resolved: identify-theory`

