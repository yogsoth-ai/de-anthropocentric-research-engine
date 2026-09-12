---
name: construct-design-matrix
description: "Construct a balanced/randomized/orthogonal experimental design matrix appropriate to the chosen design mode."
---

# construct-design-matrix

## Purpose

Construct a balanced/randomized/orthogonal experimental design matrix appropriate to the chosen design mode.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Enumerate factors, levels, blocking variables, and the chosen design mode; reject levels that are not measurable.
2. Allocate runs under balance, orthogonality, randomization, and the stated run budget; show the allocation table.
3. Audit aliasing, coverage, and run-order bias, then return the matrix with diagnostics and unresolved compromises.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The construct design matrix decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject construct design matrix when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: design-matrix-construction
