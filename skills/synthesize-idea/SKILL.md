---
name: synthesize-idea
description: "Integrate generated fragments into a coherent candidate with mechanism, provenance, and next-test hooks."
---

# synthesize-idea
## Purpose
Integrate generated fragments into a coherent candidate with mechanism, provenance, and next-test hooks.
## Input contract
```yaml
required: [idea_fragments, target_problem]
optional: [mechanism_evidence, constraints, candidate_relations]
constraints: [candidate must state function, mechanism, assumptions, and unresolved risks]
```
## Procedure
1. Cluster compatible fragments around a target function.
2. Compose a candidate mechanism and identify required assumptions.
3. Attach provenance and define the next discriminating test or evidence request.
## Output contract
```yaml
produces: [coherent_idea, mechanism_summary, provenance_trace, next_test]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- Candidate is internally coherent, traceable to source fragments, and has a concrete next-test hook.
## Failure and counterexamples
Reject an idea that is only a slogan, lacks mechanism, or cannot be tested or challenged.
## Provenance map
- `creative-ideation/cross-domain-synthesis`: resolved.
- `creative-ideation/morphological-synthesis`: resolved.
- `creative-ideation/combinatorial-synthesis`: resolved.
- `creative-ideation/enumeration-synthesis`: resolved.
