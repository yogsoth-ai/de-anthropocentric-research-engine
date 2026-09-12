# formulate-meta-analysis-scope

## Purpose

Instantiate a typed PICO/PECO-style evidence question for quantitative synthesis.

## Input contract

```yaml
required: [research_problem, population_or_exposure, comparator, outcome]
optional: [time_horizon, study_design, effect_measure]
constraints: [estimand, comparator, and outcome units must be explicit]
```

## Procedure

1. Specify population, intervention or exposure, comparator, outcome, and time horizon.
2. Define eligible designs and the estimand for quantitative synthesis.
3. Record effect-measure compatibility and planned conversions.
4. Mark scope boundaries and unresolved heterogeneity.

## Output contract

```yaml
produces: [typed_meta_analysis_question, eligibility_scope, estimand, compatibility_constraints]
delta_fields: [decisions, assumption_updates, uncertainties, open_questions]
```

## Quality gates

- The estimand is computable from eligible studies.
- Outcome and comparator definitions are not interchangeable aliases.

## Failure and counterexamples

Do not broaden the scope until unlike outcomes appear comparable or define a meta-analysis from a vague topic alone.

## Provenance map

- `concept: knowledge-acquisition-pico-formulation`
- `concept: hypothesis-formation/pico-application`
