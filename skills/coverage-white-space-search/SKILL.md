---
name: coverage-white-space-search
description: "Map known methods against problem/parameter space and generate candidates from uncovered and weakly covered intersections. Acquisition mechanism is runtime-selected."
---

# coverage-white-space-search
## Purpose
Map known methods against a problem space and generate candidates from intersections that are uncovered or covered without being closed.
## Input contract
```yaml
required: [reference_items, coverage_dimensions]
optional: [performance_records, eligibility_rules]
constraints: [reference items and dimension values must be identifiable]
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `inventory-reference-items` to inventory references.
2. You MUST load skill `map-coverage-space` to map coverage and grade its strength.
3. You MUST load skill `detect-coverage-gap` to detect uncovered and weakly covered regions.
4. You MUST load skill `synthesize-idea` to synthesize candidates.
   If a candidate gap is ready to become a testable explanation, consider `formulate-hypotheses`. If the gap itself still requires evidence validation, consider `validate-research-gap`.
Deviation: acquisition is runtime-selected; do not infer coverage from missing records.
## Output contract
```yaml
produces: [reference_inventory, coverage_map, white_space_gaps, candidate_ideas]
delta_fields: [findings, evidence_updates, hypothesis_updates, decisions, open_questions]
```
## Thresholds and quality gates
- B: every reported gap is either an explicit uncovered intersection over the declared dimensions or an occupied intersection graded below full support, with its covering items and specific shortfall named; duplicate or ineligible regions are excluded.
## Failure and counterexamples
Do not label a region white space when it is merely unsearched, incomparable, or outside the declared universe, and do not treat a region as closed because items occupy it.
## Provenance map
- `systematic-enumeration`, `benchmark-sweep`, `coverage-analysis`, `white-space-identification`, `benchmark-inventory`, `coverage-gap-detection`, `white-space-detection`: resolved/concept by exact lookup.
- Status: all except `benchmark-inventory` resolved; `benchmark-inventory` concept (only package-prefixed variant found).
## Preserved source criteria ledger
- Preserve inventory -> coverage crossing -> gap detection -> candidate synthesis.
## Context checkpoint / Delta notes
Append inventory additions, occupied cells with strength grades, gap definitions, exclusions, and generated candidates.
