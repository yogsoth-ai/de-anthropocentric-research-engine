# construct-counterfactual

## Purpose
Construct the minimally or explicitly intervened counterfactual world required by the parent analysis.

## Input contract
```yaml
required: [baseline_artifact, intervention_target, intervention_specification]
optional: [structural_model, invariants, outcome_query]
constraints: [alter only declared factors; preserve stated invariants]
```

## Procedure
1. Freeze the baseline artifact and enumerate the target factor's dependencies.
2. Apply the intervention specification while holding declared invariants fixed.
3. Propagate direct and cascading effects through the structural model.
4. Compare queried outcomes and classify hold, weaken, flip, or indeterminate.

## Output contract
```yaml
produces: [counterfactual_world, changed_factors, cascading_effects, conclusion_status, consistency_check]
delta_fields: [findings, hypothesis_updates, uncertainties, open_questions]
```

## Quality gates
- The intervention is minimal or explicitly justified as non-minimal.
- Every changed downstream variable has a propagation explanation.
- Internal consistency and conclusion status are separately reported.

## Parameterization
Caller supplies artifact schema, intervention grammar, invariants, propagation model, outcome query, and status vocabulary.

## Failure and counterexamples
Reject worlds that silently alter non-target factors or violate declared structural constraints.

## Provenance map
- resolved: counterfactual-scenario-construction

