# extract-biological-strategy
## Purpose
Extract the causal mechanism, boundary conditions, and trade-offs by which a biological analog achieves its function.
## Input contract
```yaml
required: [biological_analog, function_evidence]
optional: [mechanism_literature, environmental_conditions, tradeoffs]
constraints: [strategy claims must distinguish mechanism from observed outcome]
```
## Procedure
1. Trace the analog's structures, processes, and feedback that produce the function.
2. State boundary conditions, resources, and failure modes.
3. Separate transferable principles from organism-specific implementation details.
## Output contract
```yaml
produces: [biological_mechanism, boundary_conditions, tradeoff_register, transferable_principles]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties]
```
## Quality gates
- Mechanism is causally connected to function and includes conditions under which transfer would fail.
## Failure and counterexamples
Reject metaphorical descriptions without mechanism or principles that omit resource and trade-off constraints.
## Provenance map
- `biomimicry/abstract`: concept (no exact pool entry).
- `biotriz`: concept (no exact pool entry).
