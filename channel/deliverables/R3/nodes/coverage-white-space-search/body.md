# coverage-white-space-search
## Purpose
Map known methods against a problem space and generate candidates from uncovered intersections.
## Input contract
```yaml
required: [reference_items, coverage_dimensions]
optional: [performance_records, eligibility_rules]
constraints: [reference items and dimension values must be identifiable]
```
## Execution protocol
1. Inventory references (`inventory-reference-items`).
2. Map coverage (`map-coverage-space`).
3. Detect uncovered regions (`detect-coverage-gap`).
4. Synthesize candidates (`synthesize-idea`).
Deviation: acquisition is runtime-selected; do not infer coverage from missing records.
## Output contract
```yaml
produces: [reference_inventory, coverage_map, white_space_gaps, candidate_ideas]
delta_fields: [findings, evidence_updates, hypothesis_updates, decisions, open_questions]
```
## Thresholds and quality gates
- B: every reported gap is an explicit uncovered intersection over the declared dimensions; duplicate or ineligible regions are excluded.
## Failure and counterexamples
Do not label a region white space when it is merely unsearched, incomparable, or outside the declared universe.
## Provenance map
- `systematic-enumeration`, `benchmark-sweep`, `coverage-analysis`, `white-space-identification`, `benchmark-inventory`, `coverage-gap-detection`, `white-space-detection`: resolved/concept by exact lookup.
- Status: all except `benchmark-inventory` resolved; `benchmark-inventory` concept (only package-prefixed variant found).
## Preserved source criteria ledger
- Preserve inventory → coverage crossing → gap detection → candidate synthesis.
## Context checkpoint / Delta notes
Append inventory additions, occupied cells, gap definitions, exclusions, and generated candidates.
