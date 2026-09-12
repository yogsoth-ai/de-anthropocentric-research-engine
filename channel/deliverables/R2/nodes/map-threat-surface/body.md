# map-threat-surface
## Purpose
Enumerate attackable dimensions of an artifact and rate exposure and accessibility.
## Input contract
```yaml
required: [artifact, threat_model, access_context]
optional: [asset_inventory, severity_scale]
constraints: [surface dimensions, access assumptions, and rating anchors must be explicit]
```
## Procedure
1. Inventory components, interfaces, assumptions, and exposed data.
2. Enumerate attackable dimensions and access paths.
3. Rate exposure/accessibility and record untested surfaces.
## Output contract
```yaml
produces: [threat_surface, access_map, exposure_ratings, untested_surfaces]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- Each surface has an artifact location, access assumption, exposure rating, and rationale.
## Failure and counterexamples
Do not infer low exposure from absence of an observed attack; mark untested instead.
## Provenance map
- resolved: threat-surface-mapping
