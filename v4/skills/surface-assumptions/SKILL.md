---
name: surface-assumptions
description: "Enumerate explicit and implicit assumptions in a claim, model, method, decision, or design."
---

# surface-assumptions

## Purpose

Enumerate explicit and implicit assumptions in a claim, model, method, decision, or design and expose their evidential status.

## Input contract

```yaml
required: [artifact, claim_or_decision, context]
optional: [causal_claims, evidence, stakeholder_views, assumption_taxonomy]
constraints: [separate explicit from implicit assumptions; preserve the artifact's wording; attach evidence strength and criticality to each assumption]
```

## Procedure

1. Parse the artifact into claims, dependencies, conditions, and unstated background requirements.
2. Enumerate assumptions and classify each as explicit or implicit and by type.
3. Attach supporting or contradicting evidence and rate assumption strength and criticality.
4. Mark assumptions whose failure would change the conclusion and return the assumption register.

## Output contract

```yaml
produces: [assumption_register, evidence_assessments, critical_assumptions, dependency_notes]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates

- Every assumption has a type, explicit/implicit status, evidence assessment, and criticality rating.
- The register distinguishes load-bearing assumptions from decorative assumptions and preserves interaction effects when supplied.
- Do not replace enumeration with a generic risk paragraph.

## Parameterization

The caller must provide the artifact or claim, the context and intended conclusion, any known causal claims, the assumption taxonomy, evidence sources, and the rating scale for strength and criticality.

## Failure and counterexamples

Reject when the artifact or conclusion is missing, assumptions are asserted without relation to the claim, or contradictory evidence is silently omitted.

## Provenance map

- concept: creative-ideation/assumption-surfacing
- concept: deep-insight/assumption-enumeration
- concept: convergence/assumption-extraction
- resolved: stress-test/key-assumptions-check

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| stress-test/key-assumptions-check | 11 | gate | Enumerate all assumptions, classify them, and assess evidence strength and criticality. |

