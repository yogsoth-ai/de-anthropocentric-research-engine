---
name: represent-mechanism-edge
description: "Represent a directed mechanism edge with pathway, sign/direction, assumptions, falsifier, strength, and evidence provenance."
---

# represent-mechanism-edge
## Purpose
Represent a directed mechanism edge with pathway, sign, assumptions, falsifier, strength, and evidence provenance.
## Input contract
```yaml
required: [source_entity, target_entity, mechanism_pathway, direction, evidence_register]
optional: [edge_type, strength_scale, assumptions, falsifier]
constraints: [source and target are typed; direction, pathway, evidence, and falsifier are explicit]
```
## Procedure
1. Type the source and target entities and select the relation/edge type.
2. State the mechanism pathway and direction, including enabling conditions and assumptions.
3. Attach supporting and contradicting evidence, assign strength on the declared scale, and define a falsifier.
4. Emit the edge record with provenance and unresolved mechanism questions.
## Output contract
```yaml
produces: [mechanism_edge, evidence_links, assumption_list, falsifier, unresolved_questions]
delta_fields: [findings, evidence_updates, hypothesis_updates, assumption_updates, uncertainties, open_questions]
```
## Quality gates
- Every edge states HOW the source can affect the target, not only that they co-occur.
- Strength is bounded by the evidence and includes both supporting and contradicting records when available.
## Failure and counterexamples
Do not encode correlation as a mechanism. If the pathway or direction is unknown, emit an unresolved edge rather than a causal claim.
## Provenance map
- resolved: mechanism-edge-creation
- resolved: mechanism-mapping
