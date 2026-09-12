---
name: identify-variables
description: "Identify relevant variables/factors and annotate functional roles."
---

# identify-variables

## Purpose

Identify relevant variables, factors, conditions, and assumptions and annotate their functional roles.

## Input contract

```yaml
required: [artifact_or_system, target_claim_or_outcome]
optional: [causal_claims, domain_schema, candidate_factors]
constraints: [include explicit and implicit factors; each variable has a role, provenance, and suspected importance]
```

## Procedure

1. Parse the target claim or outcome and list quantities that could support, alter, or confound it.
2. Enumerate explicit and implicit variables, factors, conditions, and assumptions.
3. Classify functional roles such as causal variable, factor, design dimension, mediator, moderator, or confounder.
4. Attach provenance and suspected importance and return the structured variable list.

## Output contract

```yaml
produces: [variable_register, role_annotations, provenance_links, importance_notes]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- The register is exhaustive relative to the supplied artifact and causal claims; explicit and implicit entries are distinguished.
- Every factor has a functional role and a suspected-importance annotation; do not collapse variables with different causal roles.

## Parameterization

The caller must provide the artifact/system description, target claim or outcome, optional causal claims, role ontology, domain vocabulary, and any candidate-factor list to reconcile.

## Failure and counterexamples

Reject when a variable has no relation to the target outcome, a role is assigned without evidence, or a confounder is silently treated as a cause.

## Provenance map

- concept: hypothesis-formation/variable-identification
- resolved: stress-test/factor-enumeration
- resolved: creative-ideation/parameter-identification

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| stress-test/factor-enumeration | 18 | structural | List all factors, conditions, and assumptions supporting the artifact conclusion, including explicit and implicit entries and suspected importance. |

