# analyze-intervention

## Purpose

Analyze an intervention's target, mechanism, implementation conditions, and observed effects.

## Input contract

```yaml
required: [intervention, target_system, outcome_records]
optional: [implementation_records, comparator, mechanism_hypotheses]
constraints: [effect interpretation must retain implementation and comparison conditions]
```

## Procedure

1. Define intervention components, dose, timing, and target mechanism.
2. Map implementation fidelity and deviations to observed conditions.
3. Compare outcomes with the declared comparator and plausible alternatives.
4. Summarize mechanism evidence, effect heterogeneity, and unresolved attribution.

## Output contract

```yaml
produces: [intervention_map, implementation_profile, outcome_comparison, mechanism_assessment, attribution_limits]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Intervention components and implementation are separated.
- Comparator and outcome conditions are explicit.

## Failure and counterexamples

Do not attribute an effect to the intervention when co-interventions or implementation changes are untracked.

## Provenance map

- `resolved: analyze-intervention`

