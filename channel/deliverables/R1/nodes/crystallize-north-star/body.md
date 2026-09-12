# crystallize-north-star

## Purpose

Compress a validated goal structure into one specific, ambitious, achievable research North Star.

## Input contract

```yaml
required: [goal_tree, constraints, intended_effect]
optional: [feasibility_annotations, actor_profile, evidence_context]
constraints: [the statement must preserve the declared outcome and limiting constraints]
```

## Procedure

1. Identify the highest-value outcome and the mechanism or capability it should change.
2. Remove branch detail that does not distinguish the intended direction.
3. Draft one sentence with outcome, scope, and constraint boundaries.
4. Check traceability back to the goal tree and record unresolved tension.

## Output contract

```yaml
produces: [north_star_statement, research_brief, traceability_map, unresolved_tensions]
delta_fields: [findings, hypothesis_updates, decisions, uncertainties, open_questions]
```

## Quality gates

- The statement is testable and scoped.
- Every essential term traces to a goal or constraint.

## Failure and counterexamples

Do not turn a slogan into a North Star or omit constraints merely to make the sentence aspirational.

## Provenance map

- `resolved: north-star-crystallization-crystallize-north-star`

