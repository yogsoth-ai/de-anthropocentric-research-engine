---
name: specify-execution-environment
description: "Specify environment variables that materially affect interpretation or reproducibility: hardware, software, data, configuration, and versioning."
---

# specify-execution-environment

## Purpose

Specify environment variables that materially affect interpretation or reproducibility: hardware, software, data, configuration, and versioning.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Capture hardware, software, data, configuration, and version variables that can change the experiment's interpretation.
2. Mark which variables are fixed, sampled, or uncontrolled and connect each to a reproducibility or validity risk.
3. Return a minimal environment record with identifiers, capture timing, and the omissions that remain material.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The specify execution environment decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject specify execution environment when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: environment-specification
