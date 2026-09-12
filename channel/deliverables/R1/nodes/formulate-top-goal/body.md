# formulate-top-goal

## Purpose

Formalize a research goal as an outcome, desired effect, and explicit constraints.

## Input contract

```yaml
required: [research_intent]
optional: [actor_profile, constraints, evidence_context]
constraints: [goal wording must identify an observable outcome and relevant boundary conditions]
```

## Procedure

1. State the outcome that should change and the desired direction of change.
2. Identify scope, actors, resources, time, and non-negotiable constraints.
3. Separate goal content from proposed methods and assumptions.
4. Emit a testable top-goal statement with unresolved choices.

## Output contract

```yaml
produces: [top_goal, desired_effect, constraint_set, goal_assumptions, open_goal_questions]
delta_fields: [findings, hypothesis_updates, assumption_updates, decisions, uncertainties, open_questions]
```

## Quality gates

- Outcome and desired direction are observable.
- Constraints are not hidden in method wording.

## Failure and counterexamples

Do not accept “understand the topic” as a top goal without an outcome or decision target.

## Provenance map

- `resolved: formulate-top-goal`
