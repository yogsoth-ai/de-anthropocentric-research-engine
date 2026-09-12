---
name: instantiate-transfer
description: "Turn an abstract transferred principle into a concrete target-domain design/mechanism."
---

# instantiate-transfer
## Purpose
Turn an abstract transferred principle into a concrete target-domain design or mechanism.
## Input contract
```yaml
required: [abstract_principle, target_domain, target_constraints]
optional: [source_mapping, implementation_components]
constraints: [retain the source principle's causal role while adapting implementation]
```
## Procedure
1. Map each abstract relation to a target component or operation.
2. Specify the concrete mechanism, interfaces, and operating conditions.
3. Check whether the instantiated design preserves the intended function.
## Output contract
```yaml
produces: [target_mechanism, component_mapping, operating_conditions]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions]
```
## Quality gates
- Every target element has a source-principle trace and a constraint check.
## Failure and counterexamples
Reject literal copying that violates target conditions or omits the mechanism being transferred.
## Provenance map
- `creative-ideation/abstraction-to-design`: resolved.
- `creative-ideation/emulation-generation`: resolved.
- `creative-ideation/springboard-launch`: resolved.
