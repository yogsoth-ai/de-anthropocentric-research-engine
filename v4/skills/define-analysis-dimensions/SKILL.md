---
name: define-analysis-dimensions
description: "Identify approximately independent dimensions/axes that span the relevant problem, design, or validity space and define their semantics."
---

# define-analysis-dimensions

## Purpose

Define approximately independent, measurable axes that span a problem, design, or validity space.

## Input contract

```yaml
required: [problem_or_artifact, target_outcome, dimension_ontology]
optional: [candidate_axes, domain_constraints, measurement_plan]
constraints: [each axis has semantics, type, direction, and measurement rule; correlated axes are flagged]
```

## Procedure

1. Extract factors and conditions relevant to the target outcome.
2. Group candidates into dimensions and test approximate independence.
3. Define each dimension's domain, units, direction, and observability.
4. Return the dimension set with exclusions and unresolved dependencies.

## Output contract

```yaml
produces: [dimension_set, axis_definitions, independence_notes, coverage_scope]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Every retained axis is independent enough for the caller's analysis and is measurable under the supplied plan.
- Parameter-space mapping covers all dimensions relevant to assertion validity; omitted axes require a reason.
- Do not confuse a value/level with the dimension that contains it.

## Parameterization

The caller must provide the target problem, outcome, axis ontology, candidate factors, domain bounds, measurement units, and independence criterion.

## Failure and counterexamples

Reject duplicate axes, dimensions with no observable values, or an independence claim unsupported by a comparison.

## Provenance map

- resolved: deep-insight/variation-axis-definition
- resolved: stress-test/parameter-space-mapping
- resolved: creative-ideation/parameter-identification
- intermediate: Pass3/map-parameter-space
- intermediate: Pass3/identify-dimensions

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| deep-insight/variation-axis-definition | 14 | structural | Identify orthogonal axes, ensuring they are independent, measurable, and span the parameter space. |

