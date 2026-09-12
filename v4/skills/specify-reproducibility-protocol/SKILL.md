---
name: specify-reproducibility-protocol
description: "Define exact/statistical/conceptual reproduction target and the controls needed to test it."
---

# specify-reproducibility-protocol

## Purpose

Define exact/statistical/conceptual reproduction target and the controls needed to test it.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Choose the exact, statistical, or conceptual reproduction target and define what counts as agreement.
2. Map seeds, environment capture, data versioning, rerun count, and comparison metrics to that target.
3. Return acceptance criteria and known limits so a later verification can distinguish failure from target mismatch.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The specify reproducibility protocol decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject specify reproducibility protocol when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: reproducibility-protocol
