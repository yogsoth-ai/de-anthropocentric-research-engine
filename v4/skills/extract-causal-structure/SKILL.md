---
name: extract-causal-structure
description: "Extract causal structure from source material at requested granularity: individual causal claims, ordered mechanism chains, mediators, assumptions, and stated boundary conditions."
---

# extract-causal-structure

## Purpose

Extract causal claims, mechanism chains, mediators, assumptions, and boundary conditions at caller-specified granularity.

## Input contract

```yaml
required: [source_material, extraction_granularity, causal_schema]
optional: [theory_description, domain_ontology, evidence_links]
constraints: [preserve direction and scope; distinguish observed association from asserted causation; attach evidence]
```

## Procedure

1. Identify candidate cause, mediator, effect, conditions, and temporal order.
2. Extract X→mediator→Y chains and direct X→Y claims at the requested granularity.
3. Record assumptions, boundary conditions, and evidence for each edge.
4. Assemble the causal graph and flag unsupported or ambiguous links.

## Output contract

```yaml
produces: [causal_claims, mechanism_chains, causal_graph, boundary_conditions, evidence_links]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties]
```

## Quality gates

- Mechanism-extraction mode produces at least 1 chain per supplied theory and at least 2 chains in total where that source protocol applies.
- Every edge has direction, scope, and evidence status; association is not upgraded to causation.
- Biological strategy extraction preserves mechanism-level details of how function is achieved.

## Parameterization

The caller must provide source material, theory or artifact schema, extraction granularity, causal edge vocabulary, boundary-condition fields, and evidence-link format.

## Failure and counterexamples

Reject chains with missing direction, no stated mechanism, or evidence that supports only correlation while the output claims causation.

## Provenance map

- resolved: hypothesis-formation/mechanism-extraction
- resolved: creative-ideation/biological-strategy-extraction
- resolved: stress-test/causal-claim-extraction
- intermediate: Pass3/extract-mechanism
- intermediate: Pass3/extract-causal-claims

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| hypothesis-formation/mechanism-extraction | 22 | numeric | Produce X→mediator→Y mechanism chains, at least 1 per theory and at least 2 total where applicable. |

