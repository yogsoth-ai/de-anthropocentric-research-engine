# validate-causal-link

## Purpose

Audit a causal relation for clarity, existence, sufficiency, and logical completeness using CLR-style checks.

## Input contract

```yaml
required: [causal_relation, source_evidence, boundary_conditions]
optional: [causal_graph, alternative_explanations, clr_checklist]
constraints: [the relation has explicit cause and effect; distinguish clarity, existence, sufficiency, and logical completeness]
```

## Procedure

1. Parse the causal relation and define its scope and terms.
2. Check whether the stated cause exists and is connected to the effect.
3. Test sufficiency, omitted conditions, and alternative explanations.
4. Record each CLR result and return a validated, weakened, or unresolved link.

## Output contract

```yaml
produces: [causal_link_assessment, clr_results, missing_conditions, evidence_requests]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties]
```

## Quality gates

- All eight CLR categories are retained when the caller supplies the full checklist.
- Clarity, existence, sufficiency, and logical completeness are reported separately.
- A causal label is not accepted when evidence supports only association.

## Parameterization

The caller must provide the cause/effect schema, evidence and boundary conditions, CLR checklist, alternative-explanation fields, and verdict vocabulary.

## Failure and counterexamples

Reject links with undefined variables, missing scope, circular support, or causal language unsupported by the evidence.

## Provenance map

- resolved: deep-insight/clr-validation

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| deep-insight/clr-validation | 13 | structural | Retain eight CLR validation categories for causal claims: clarity, existence, sufficiency, and logical completeness are explicit checks. |

