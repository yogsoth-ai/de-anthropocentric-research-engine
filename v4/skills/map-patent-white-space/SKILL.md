---
name: map-patent-white-space
description: "Map protected feature combinations and identify technically meaningful, plausibly unprotected white space."
---

# map-patent-white-space

## Purpose

Map protected feature combinations and identify technically meaningful, plausibly unprotected white space.

## Input contract

```yaml
required: [patent_records, feature_schema, jurisdiction_scope]
optional: [claim_element_maps, family_map, technical_constraints]
constraints: [feature provenance and claim scope must be retained, unprotected means not evidenced as protected within the declared scope]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `parse-patent-claim` to parse claims into comparable elements.
2. You MUST load skill `trace-patent-family` to align family and jurisdiction evidence.
3. You MUST load skill `detect-coverage-gap` to identify absent, thin, or disconnected feature combinations.

Deviation: If claim records are already normalized, reuse them and skip reparsing. If family evidence is incomplete, label the white-space candidate provisional rather than treating absence as freedom to operate.

## Output contract

```yaml
produces: [feature_cross_matrix, protected_combinations, white_space_candidates, coverage_uncertainties]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Every candidate cell must cite the records and jurisdictions checked.
- Coverage is reported as a ratio over the declared feature universe; the denominator and missing cells must be visible.
- A gap is a candidate for investigation, not a legal conclusion.

## Failure and counterexamples

Do not infer unprotected status from an empty search result, a single family, or an unmatched synonym. Preserve alternative feature decompositions when the claim language is ambiguous.

## Provenance map

- `resolved: white-space-analysis`
- `resolved: knowledge-acquisition-white-space-mapping`
- `resolved: knowledge-acquisition-claim-decomposition`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| none retained | - | - | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append feature cells, cited claims, family/jurisdiction coverage, candidate gaps, and unresolved interpretation questions.
