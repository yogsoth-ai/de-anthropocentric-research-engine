---
name: test-structure-preservation
description: "Test whether the proposed mapping preserves the required relations/operations/invariants and actively search for a minimal counterexample to preservation."
---

# test-structure-preservation
## Purpose
Test whether a proposed mapping preserves required relations, operations, and invariants, while searching a minimal counterexample.
## Input contract
```yaml
required: [mapping, preservation_obligations, source_and_target]
optional: [counterexample_search_space]
constraints: [obligations must be enumerated before testing]
```
## Procedure
1. Evaluate each relation, operation, and invariant.
2. Search for the smallest preservation failure.
3. Record pass, fail, unknown, and counterexample evidence.
## Output contract
```yaml
produces: [preservation_matrix, counterexample, failed_obligations, uncertainty]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A preserved invariant needs a tested mapping and evidence.
## Failure and counterexamples
Unknown preservation is not a pass.
## Provenance map
- resolved: isomorphism-falsification
