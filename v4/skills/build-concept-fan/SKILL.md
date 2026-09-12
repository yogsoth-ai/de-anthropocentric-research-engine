---
name: build-concept-fan
description: "Expand a target goal into progressively broader concepts and alternative routes, then descend into new concrete approaches."
---

# build-concept-fan
## Purpose
Expand a goal into broader concepts and alternative routes, then descend into concrete approaches.
## Input contract
```yaml
required: [target_goal]
optional: [known_approaches, abstraction_levels, feasibility_constraints]
constraints: [each branch must state its abstraction level and relation to the goal]
```
## Procedure
1. State the current goal and its immediate concept.
2. Fan upward into broader purposes and downward into alternative implementations.
3. Compare branches and retain distinct routes for further investigation.
## Output contract
```yaml
produces: [concept_fan, abstraction_branches, concrete_routes]
delta_fields: [findings, hypothesis_updates, decisions, recommended_jumps]
```
## Quality gates
- Fan contains both broader and narrower branches; duplicate wording is not counted as a new route.
## Failure and counterexamples
Reject branches that merely rename the goal or violate declared feasibility constraints.
## Provenance map
- `lateral-thinking/concept-fan`: resolved.
