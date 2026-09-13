---
name: conceptual-blending
description: "Construct multiple input spaces, extract a shared generic space, selectively project structure into a blend, and simulate emergent properties that are not present in either source alone."
---

# conceptual-blending
## Purpose
Blend multiple input spaces through a generic space and selective projection to generate emergent research ideas.
## Input contract
```yaml
mode_contracts:
  two-space-blend: &blending_input
    required: [input_spaces]
    optional: [compatibility_constraints]
    constraints: [each_input_space_must_have_explicit_entities_and_relations]
  multi-space-blend: *blending_input
  emergent-property-search: *blending_input
```
## Execution protocol
1. Construct input spaces (`construct-input-spaces`).
2. Extract the generic space (`extract-generic-space`).
3. Simulate emergent properties (`simulate-emergent-properties`).
4. Check compatibility (`evaluate-compatibility`).
5. Synthesize an idea (`synthesize-idea`).
Deviation: two-space and multi-space modes change only the number of inputs; generic-space extraction is mandatory.
## Mode branches
- `two-space-blend`: blend two explicit input spaces.
- `multi-space-blend`: blend three or more spaces while preserving each projection trace.
- `emergent-property-search`: prioritize properties absent from every source space alone.
## Output contract
```yaml
mode_contracts:
  two-space-blend: &space_blend_output
    produces: [input_space_set, generic_space, blend_candidates, idea_set]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
  multi-space-blend: *space_blend_output
  emergent-property-search:
    produces: [input_space_set, blend_candidates, emergent_property_report, idea_set]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- B: all source spaces and projected relations are recorded; emergent properties must be absent from each source alone and compatible with target constraints.
## Failure and counterexamples
Reject mere juxtaposition, unsupported emergence claims, and blends with unresolved relation conflicts.
## Provenance map
- `creative-ideation/combinatorial-creativity`, `conceptual-blending`, `emergent-property-hunting`: resolved/concept per exact v3 lookup.
- Status: `creative-ideation/combinatorial-creativity`, `emergent-property-hunting` resolved; `conceptual-blending` concept (no exact v3 node).
## Preserved source criteria ledger
- Preserve generic-space construction, selective projection, and emergent-property semantics.
## Context checkpoint / Delta notes
Append source-space changes, projected relations, emergence claims, compatibility findings, and selected ideas.
