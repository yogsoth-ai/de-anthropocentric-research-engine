# plan-effect-size

## Purpose

Choose effect-size estimands and conversion rules appropriate to outcomes and study design.

## Input contract

```yaml
required: [outcome_schema, study_designs, comparison_target]
optional: [reported_statistics, variance_rules, transformation_options]
constraints: [estimand, direction, and conversion assumptions must be explicit]
```

## Procedure

1. Match each outcome and design to a valid estimand.
2. Define direction, scale, variance, and required conversions.
3. Record unavailable statistics and assumptions for any conversion.
4. Produce a harmonized effect-size plan with incompatibilities.

## Output contract

```yaml
produces: [estimand_plan, conversion_rules, variance_requirements, incompatibility_log]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- Effects are comparable only under declared assumptions.
- Conversions remain traceable to reported statistics.

## Failure and counterexamples

Do not convert incompatible constructs into a common effect size merely to increase sample size.

## Provenance map

- `resolved: effect-size-planning`
