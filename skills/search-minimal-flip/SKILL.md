---
name: search-minimal-flip
description: "Search for the smallest change to variables/assumptions/conditions that flips a target conclusion, decision, or causal claim."
---

# search-minimal-flip
## Purpose
Search for the smallest change to variables, assumptions, or conditions that flips a target conclusion.
## Input contract
```yaml
required: [target_conclusion, variables_or_assumptions, baseline_state]
optional: [distance_metric, constraints]
constraints: [flip criterion and change metric must be explicit]
```
## Procedure
1. Define baseline conclusion and permitted changes.
2. Enumerate increasingly small candidate changes.
3. Test the first valid flip and verify minimality.
## Output contract
```yaml
produces: [minimal_flip, changed_variables, flip_evidence, minimality_check]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A flip must change the target conclusion under declared conditions.
- Minimality requires a documented comparison against smaller or simpler changes.
## Failure and counterexamples
Do not call a change minimal when the search space or distance metric is unspecified.
## Provenance map
- resolved: minimal-change-search
