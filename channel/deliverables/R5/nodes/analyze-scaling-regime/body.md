# analyze-scaling-regime

## Purpose
Analyze how conclusions or performance change across scale and identify regime shifts, saturation, scaling-law behavior, or frontier transitions.

## Input contract
```yaml
required: [scale_variable, outcome_series, observation_context]
optional: [candidate_scaling_laws, uncertainty_model, suspected_breakpoints]
constraints: [scale units and outcome direction must be explicit; observations remain ordered]
```

## Procedure
1. Normalize scale and outcome definitions while retaining original units.
2. Plot or tabulate local behavior and fit only caller-authorized within-regime models.
3. Locate qualitative shifts, saturation, or frontier transitions and test their stability.
4. Report regime boundaries, mechanism hypotheses, and extrapolation limits.

## Output contract
```yaml
produces: [regime_map, breakpoint_candidates, scaling_diagnostics, extrapolation_limits]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates
- Each claimed regime has observations on both sides or is marked extrapolative.
- Breakpoints include uncertainty or sensitivity information.
- Power-law/log-law labels are supported by fit diagnostics, not visual slope alone.

## Parameterization
Caller supplies scale axis, outcome schema, candidate laws, breakpoint rule, fit diagnostics, and acceptable extrapolation distance.

## Failure and counterexamples
Reject a regime claim based on a single point or a scale change confounded with protocol change.

## Provenance map
- resolved: scaling-frontier
- intermediate: deep-insight/scaling-analysis

