# specify-boundaries

## Purpose

Specify the population, system, temporal, and conceptual boundaries within which a claim or study is intended to hold.

## Input contract

```yaml
required: [claim_or_question, target_context]
optional: [known_limits, adjacent_domains, time_window]
constraints: [each boundary must be observable or operationally enforceable]
```

## Procedure

1. Identify included and excluded populations, systems, conditions, and times.
2. Separate conceptual boundaries from practical sampling limits.
3. Record boundary rationale and expected failure outside scope.
4. Emit a boundary schema for downstream comparison.

## Output contract

```yaml
produces: [boundary_specification, inclusion_edges, exclusion_edges, extrapolation_limits]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- Boundaries do not depend on observed outcomes.
- Extrapolation limits are explicit.

## Failure and counterexamples

Do not define the boundary as whatever data happen to be available.

## Provenance map

- `resolved: specify-boundaries`

