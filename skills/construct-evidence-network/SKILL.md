---
name: construct-evidence-network
description: "Construct a network-meta-analysis evidence graph and evaluate connectivity/transitivity prerequisites."
---

# construct-evidence-network

## Purpose

Construct an evidence graph for network synthesis and evaluate connectivity, transitivity, and comparison support.

## Input contract

```yaml
required: [evidence_records, intervention_nodes, outcome_schema]
optional: [study_designs, effect_sizes, covariate_schema]
constraints: [edges require a shared outcome definition and traceable comparison evidence]
```

## Procedure

1. Normalize interventions, comparators, outcomes, and study-level edges.
2. Build the direct and indirect comparison graph with effect-support provenance.
3. Check connectivity and transitivity assumptions across connected components.
4. Report usable components, unsupported links, and synthesis limitations.

## Output contract

```yaml
produces: [evidence_graph, connected_components, transitivity_assessment, unsupported_links, synthesis_readiness]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Every edge points to a study record and outcome definition.
- Disconnected components are not silently combined.
- Transitivity judgments list the effect modifiers examined.

## Failure and counterexamples

Do not create indirect evidence from incomparable populations or outcomes, and do not treat graph connectivity as proof of exchangeability.

## Provenance map

- `resolved: knowledge-acquisition-evidence-network-construction`

