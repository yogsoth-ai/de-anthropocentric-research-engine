---
name: detect-feedback-loop
description: "Detect and characterize reinforcing/balancing feedback loops, participating variables, delays, and possible breakpoints."
---

# detect-feedback-loop

## Purpose

Detect reinforcing or balancing feedback loops in a causal or process structure and state the evidence for each loop.

## Input contract

```yaml
required: [causal_graph, node_semantics, edge_polarity]
optional: [time_delays, observed_series, intervention_records]
constraints: [loop classification requires directed edges and polarity or transition evidence]
```

## Procedure

1. Normalize directed relations, polarity, and delays.
2. Enumerate simple cycles and identify reinforcing or balancing sign patterns.
3. Compare loops with observations or intervention evidence where available.
4. Report loop boundaries, uncertain edges, and testable implications.

## Output contract

```yaml
produces: [feedback_loops, loop_classification, supporting_evidence, uncertain_edges, testable_implications]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates

- Every loop lists its ordered edges and polarity basis.
- Correlational cycles are not presented as causal loops without qualification.

## Failure and counterexamples

Do not infer feedback from a static co-occurrence or omit time direction where it determines loop meaning.

## Provenance map

- `resolved: detect-feedback-loop`

