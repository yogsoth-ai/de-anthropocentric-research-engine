---
name: atomize-claim
description: "Decompose a compound position into atomic, independently challengeable/falsifiable claims and expose implicit assumptions."
---

# atomize-claim

## Purpose

Split a compound claim into atomic propositions that can receive separate evidence and confidence judgments.

## Input contract

```yaml
required: [compound_claim]
optional: [argument_context, domain_terms, evidence_records]
constraints: [atomic claims retain logical connectors and scope qualifiers]
```

## Procedure

1. Identify subjects, predicates, qualifiers, conditions, and logical connectors.
2. Split independent propositions while preserving dependency and quantifier scope.
3. Mark implicit premises and ambiguous terms.
4. Emit an ordered atomic claim set with recomposition rules.

## Output contract

```yaml
produces: [atomic_claims, logical_connectors, implicit_premises, recomposition_map]
delta_fields: [findings, uncertainties, open_questions]
```

## Quality gates

- Recombining the atoms preserves the original meaning.
- Each atom is independently evidence-addressable.

## Failure and counterexamples

Do not split a definition or condition from the proposition it qualifies.

## Provenance map

- `resolved: atomize-claim`

