---
name: generate-attack-vector
description: "Generate a concrete executable attack/probe against a chosen threat surface."
---

# generate-attack-vector
## Purpose
Generate a concrete executable attack or probe against a chosen threat surface.
## Input contract
```yaml
required: [threat_surface, target, attack_constraints]
optional: [access_level, prior_findings]
constraints: [attack must identify trigger, observable, and failure condition]
```
## Procedure
1. Select an exposed surface and attack objective.
2. Specify trigger, steps, observables, and failure interpretation.
3. Rank priority by information value and severity.
## Output contract
```yaml
produces: [attack_vector, trigger, observable, failure_condition, priority]
delta_fields: [findings, uncertainties, decisions]
```
## Quality gates
- Vector must be executable within declared authority and scope.
## Failure and counterexamples
Do not call a hypothetical weakness an attack result until executed.
## Provenance map
- resolved: attack-vector-generation
