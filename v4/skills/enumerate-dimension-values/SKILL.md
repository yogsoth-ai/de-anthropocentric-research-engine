---
name: enumerate-dimension-values
description: "Enumerate meaningful values/levels for a dimension or factor. Mode controls representative, experimental, boundary, pathological, or adversarial coverage."
---

# enumerate-dimension-values

## Purpose

Enumerate meaningful values or levels for a dimension or factor, including representative, experimental, boundary, pathological, or adversarial coverage.

## Input contract

```yaml
required: [dimensions, value_schema, mode]
optional: [ranges, spacing_strategy, domain_constraints, baseline_values]
constraints: [values are typed to the dimension; mode determines representative, experimental, boundary, pathological, or adversarial coverage]
```

## Procedure

1. Validate each dimension's type, range, units, and constraints.
2. Generate representative values and caller-requested boundary or extreme values.
3. For experimental mode, apply the supplied spacing strategy and preserve factor comparability.
4. Deduplicate and annotate rationale, provenance, and expected coverage.
5. Return the value set per dimension.

## Output contract

```yaml
produces: [dimension_value_sets, boundary_cases, spacing_annotations, coverage_rationale]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Preserve the source representative enumeration of 3–5 values per parameter when that mode is selected.
- Preserve experimental factor levels of 2–5 levels with an explicit spacing strategy.
- Boundary/extreme mode must include the caller-defined boundary, pathological, distribution-shift, rare-combination, or scale-extreme cases; do not invent a fixed case count.

## Parameterization

The caller must provide dimensions and types, valid ranges and units, enumeration mode, spacing strategy, baseline values, and domain constraints. If experimental mode is used, provide factor roles and the intended comparison design.

## Failure and counterexamples

Reject values outside declared domains, levels without units or semantics, or pathological cases presented as representative defaults.

## Provenance map

- resolved: creative-ideation/value-enumeration
- resolved: stress-test/extreme-value-generation
- resolved: deep-insight/edge-case-generation
- resolved: experiment-execution/level-specification
- intermediate: Pass3/enumerate-values
- intermediate: Pass3/generate-extreme-values
- intermediate: Pass3/specify-factor-levels

## Verbatim source criteria excerpts

- `value-enumeration` line 14: Enumerate 3-5 meaningful values per parameter, ensuring coverage of boundary and extreme values.

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| creative-ideation/value-enumeration | 11 | numeric | Enumerate 3–5 values per parameter, including extremes. |
| experiment-execution/level-specification | 12 | numeric | Experimental factor levels use 2–5 levels and an explicit spacing strategy. |
