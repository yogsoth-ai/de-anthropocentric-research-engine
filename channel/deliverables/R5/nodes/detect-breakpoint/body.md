# detect-breakpoint
## Purpose
Locate the point or region where performance, validity, or a claim changes regime.
## Input contract
```yaml
required: [ordered_observations, target_metric, flip_or_regime_rule]
optional: [candidate_axis, smoothing_rule, uncertainty_bounds]
constraints: [ordering and metric direction are explicit]
```
## Procedure
1. Sort observations along the declared axis and validate comparability.
2. Detect abrupt flips, slope changes, saturation, or regime transitions.
3. Estimate boundary region and attach uncertainty.
4. Return witness observations and follow-up tests.
## Output contract
```yaml
produces: [breakpoint_region, regime_label, witness_observations, uncertainty, follow_up_tests]
delta_fields: [findings, uncertainties, open_questions]
```
## Quality gates
- A breakpoint requires observations on both sides or an explicit one-sided limitation.
- Metric direction and flip rule are declared before detection.
- Smoothing or interpolation never replaces raw witnesses.
## Parameterization
Caller supplies observation schema, axis ordering, metric, flip/regime rule, smoothing, and uncertainty policy.
## Failure and counterexamples
Reject boundaries inferred from unvalidated ordering, single noisy points, or hidden smoothing.
## Provenance map
- concept: stress-test/breakpoint-detection
- concept: deep-insight/controlled-perturbation
