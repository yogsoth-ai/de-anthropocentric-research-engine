---
name: design-randomness-protocol
description: "Identify randomness sources and define seed/repetition/propagation rules sufficient for the intended reproducibility level."
---

# design-randomness-protocol

## Purpose

Identify randomness sources and define seed/repetition/propagation rules sufficient for the intended reproducibility level.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Inventory every stochastic source, including sampling, initialization, augmentation, scheduling, and nondeterministic kernels.
2. Assign seed ownership, propagation rules, repetition counts, and logging points for the declared reproducibility target.
3. Walk one rerun through the protocol and flag any randomness that remains uncontrolled or only statistically reproducible.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The design randomness protocol decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject design randomness protocol when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: seed-protocol-design
