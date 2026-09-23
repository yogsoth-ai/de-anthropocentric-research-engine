# map-research-landscape

## Purpose

Map candidate research fields or subfields, maturity, competition, entry barriers, tractability, and opportunity structure.

## Input contract

```yaml
required: [research_intent, scope_anchor]
optional: [actor_profile, seed_evidence, constraints]
constraints: [candidate fields require evidence references and declared comparison dimensions]
```

## Execution protocol

1. Generate diverse candidate fields and deliberate boundary crossings (`generate-candidate-directions`).
2. Synthesize maturity, competition, entry-barrier, tractability, and opportunity evidence (`synthesize-field-panorama`).

Deviation: Evidence acquisition is host-selected; do not invoke removed tool wrappers. Re-run candidate generation only when intent or scope changes materially.

## Output contract

```yaml
produces: [candidate_field_set, field_panorama, maturity_map, competition_map, opportunity_structure]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Each candidate must have evidence for the declared dimensions or an explicit missing marker.
- The panorama must include at least one direct opportunity and one barrier per candidate.
- Acquisition sufficiency is relative to the declared eligible evidence universe; saturation is assessed by marginal information gain rather than a fixed source count.

## Failure and counterexamples

Reject niche lists with no evidence, maturity claims based on publication volume alone, and opportunity claims that omit competition or entry barriers.

## Provenance map

- `resolved: landscape-reconnaissance`
- `resolved: north-star-crystallization-generate-candidate-fields`
- `resolved: north-star-crystallization-landscape-synthesis`
- `resolved: broad-web-search`
- `resolved: broad-paper-search`
- `resolved: north-star-crystallization-deep-web-search`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| none retained | — | — | No source numeric/textual criterion retained after normalization. |

## Context checkpoint / Delta notes

Append candidate fields, evidence references, dimension assessments, boundary-crossing rationale, and unresolved acquisition questions.
