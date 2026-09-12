# construct-validity-envelope
## Purpose
Synthesize multi-axis breakpoints into a multidimensional statement of where a claim or method remains valid.
## Input contract
```yaml
required: [claim_or_method, axis_results, validity_criteria]
optional: [boundary_interactions, uncertainty_model, extrapolation_policy]
constraints: [each boundary is tied to an axis result and evidence]
```
## Procedure
1. Align axis scales, directions, and validity labels.
2. Combine breakpoint regions and inspect interaction effects.
3. Mark supported, uncertain, and invalid regions.
4. Emit the envelope with extrapolation warnings and monitoring observables.
## Output contract
```yaml
produces: [validity_envelope, boundary_conditions, uncertain_regions, monitoring_observables]
delta_fields: [findings, uncertainties, open_questions]
```
## Quality gates
- No envelope boundary lacks an axis-level witness.
- Interactions are reported when independent-axis combination is unjustified.
- Extrapolated regions are labeled as such.
## Parameterization
Caller supplies axis schema, breakpoint format, validity criteria, interaction policy, and uncertainty representation.
## Failure and counterexamples
Reject envelopes inferred from one axis, unsupported extrapolation, or boundaries without observables.
## Provenance map
- concept: deep-insight/validity-envelope-construction
- concept: stress-test/validity-envelope-construction
