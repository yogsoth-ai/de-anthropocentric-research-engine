# detect-contradiction

## Purpose

Detect and classify explicit contradictions in derivations, claims, or evidence relations.

## Input contract

```yaml
required: [claims_or_derivation, evidence_relations, scope_context]
optional: [logic_rules, causal_graph, contradiction_taxonomy]
constraints: [distinguish formal, empirical, scope-dependent, and unresolved contradiction; preserve both sides]
```

## Procedure

1. Normalize claims, predicates, scope, and evidence polarity.
2. Compare opposing claims or support/contradict relations under shared scope.
3. Classify the conflict and record the exact conflicting statements.
4. Create a contradiction record and identify the evidence needed for adjudication.

## Output contract

```yaml
produces: [contradiction_register, conflicting_relations, classification, adjudication_questions]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Support and contradict evidence are both recorded; contradiction cannot be hidden by selecting one polarity.
- Scope mismatch is labeled scope-dependent rather than formal contradiction.
- Each contradiction includes both endpoints and a reproducible comparison basis.

## Parameterization

The caller must provide claim schema, evidence polarity vocabulary, scope rules, logic/causal relation types, and the adjudication status vocabulary.

## Failure and counterexamples

Reject conflicts caused only by incomparable metrics, different scopes, or duplicate text; retain them as unresolved comparability issues.

## Provenance map

- resolved: stress-test/contradiction-detection
- resolved: knowledge-structuring/contradiction-flagging
- concept: stress-test/detect-contradiction
- intermediate: Pass3/detect-contradiction
- intermediate: Pass3/flag-contradictory-evidence

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| knowledge-structuring/contradiction-flagging | 18 | gate | Record simultaneous support and contradict evidence and do not ignore either. |

