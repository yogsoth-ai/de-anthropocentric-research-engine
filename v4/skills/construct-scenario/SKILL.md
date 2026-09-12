---
name: construct-scenario
description: "Construct a scenario across key uncertainties with explicit assumptions and plausibility. Modes include baseline/narrative, counterfactual, and extreme-but-plausible worst-case with breaking point, failure cascade, recovery assumptions, and distinguishing observables."
---

# construct-scenario

## Purpose
Construct scenarios across key uncertainties with explicit assumptions and plausibility, including baseline, counterfactual, and extreme-but-plausible modes.

## Input contract
```yaml
required: [context, uncertainty_set, scenario_mode]
optional: [drivers, dependency_model, probability_method, recovery_assumptions]
constraints: [scenario assumptions and distinguishing observables must be explicit]
```

## Procedure
1. Select uncertainty axes and record their state space.
2. Generate distinct combinations appropriate to the mode.
3. Propagate interactions, breaking points, failure cascades, and recovery assumptions where applicable.
4. Attach plausibility rationale, distinguishing observables, and outcome implications.

## Output contract
```yaml
produces: [scenario_set, assumptions, plausibility_rationales, observables, outcome_implications]
delta_fields: [findings, hypothesis_updates, uncertainties, open_questions]
```

## Quality gates
- At least 3 scenarios span different combinations of key uncertainties.
- Scenarios are internally consistent and materially distinct.
- Worst-case mode includes breaking point, cascade, recovery, and observables.

## Parameterization
Caller supplies context schema, uncertainty axes, mode, distinctness rule, plausibility/probability method, and worst-case fields.

## Failure and counterexamples
Reject decorative narratives that do not vary an uncertainty or expose a testable implication.

## Provenance map
- resolved: scenario-construction
- resolved: counterfactual-scenario-construction
- resolved: worst-case-construction
- resolved: stress-scenario

## Preserved source criteria ledger

| source | criterion |
|---|---|
| scenario-construction | Output contains at least 3 distinct scenarios spanning different combinations of key uncertainties. |
| scenario-construction | Each scenario includes a narrative, key assumptions, and probability estimate. |
| worst-case-construction | Extreme-but-plausible mode includes breaking points, failure cascades, and recovery assessment. |
