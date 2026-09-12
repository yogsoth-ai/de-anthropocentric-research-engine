# validate-axis-independence
## Purpose
Test candidate dimensions pairwise for redundancy or dependence, merging covarying axes and removing non-informative axes.
## Input contract
```yaml
required: [candidate_axes, observations_or_measurements, independence_rule]
optional: [domain_constraints, sample_plan, prior_axis_map]
constraints: [each pair has a declared test, dependence criterion, and evidence basis]
```
## Procedure
1. Normalize axis definitions, units, ranges, and observed cases before comparison.
2. Test each axis pair for dependence, redundancy, or deterministic derivation under the declared rule.
3. Merge or remove axes only when the evidence crosses the stated criterion; preserve the rationale and affected mappings.
4. Emit the validated axis set, pairwise test matrix, and unresolved dependence cases.
## Output contract
```yaml
produces: [validated_axes, pairwise_independence_matrix, merge_map, unresolved_axis_pairs]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- Every candidate pair receives a test outcome or an explicit insufficient-evidence status.
- Removing an axis preserves the ability to represent every declared decision-relevant variation.
## Failure and counterexamples
Do not call axes independent because their labels differ. Do not merge axes solely to reduce table size.
## Provenance map
- resolved: axis-validation
