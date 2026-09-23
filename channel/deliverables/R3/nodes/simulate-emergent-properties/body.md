# simulate-emergent-properties
## Purpose
Project selected structures into a blend and identify properties, affordances, contradictions, or mechanisms absent from either source alone.
## Input contract
```yaml
required: [selected_structures, blend_projection]
optional: [source_properties, compatibility_constraints, simulation_assumptions]
constraints: [emergence claim must specify the source properties it combines]
```
## Procedure
1. Project selected relations into the blended configuration.
2. Derive candidate interactions and properties of the blend.
3. Compare each property with the source spaces and flag genuinely emergent effects.
## Output contract
```yaml
produces: [blend_model, emergent_properties, interaction_mechanisms, contradiction_flags]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Each emergent property has a projection trace and is absent from each source alone under the stated comparison.
## Failure and counterexamples
Reject emergence claims caused by changed measurement, untracked assumptions, or simple source duplication.
## Provenance map
- `conceptual-blending/emergent-property-hunting`: resolved.
