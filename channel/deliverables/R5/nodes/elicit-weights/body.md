# elicit-weights
## Purpose
Produce a normalized criterion-weight vector using a caller-selected elicitation method.
## Input contract
```yaml
required: [criteria, elicitation_method, preference_inputs]
optional: [consistency_threshold, pairwise_scale, missing_preference_policy]
constraints: [weights are nonnegative and sum to 1 within declared tolerance]
```
## Procedure
1. Validate criteria and method applicability.
2. Convert preference inputs to a weight vector using the declared method.
3. Compute consistency diagnostics where the method supports them.
4. Return weights, diagnostics, and unresolved preference gaps.
## Output contract
```yaml
produces: [weight_vector, consistency_diagnostics, preference_gaps, method_record]
delta_fields: [decisions, uncertainties, open_questions]
```
## Quality gates
- AHP-style elicitation accepts 2–9 dimensions only.
- Weight sum is 1.0 within caller-declared tolerance (default ±0.001).
- Consistency ratio is reported; CR > 0.1 is flagged when applicable.
## Parameterization
Caller supplies criterion schema, method, pairwise/preference scale, tolerance, and consistency policy.
## Failure and counterexamples
Reject inapplicable dimensionality, negative weights, missing comparisons, or unreported inconsistency.
## Provenance map
- concept: hypothesis-formation/ahp-weighting
- concept: convergence/weight-elicitation-sop
## Preserved source criteria ledger
| source | criterion |
|---|---|
| hypothesis-formation/ahp-weighting | AHP applicability range is 2–9 dimensions. |
| hypothesis-formation/ahp-weighting | Weight vector sums to 1.0 within ±0.001. |
| hypothesis-formation/ahp-weighting | CR > 0.1 is flagged. |
