# compare-pair
## Purpose
Execute one pairwise comparison under a declared criterion and return a winner, confidence, tie status, and reasons.
## Input contract
```yaml
required: [item_a, item_b, comparison_criterion, comparison_model, evidence_register]
optional: [tie_rule, prior_ratings]
constraints: [criterion direction and evidence scope are fixed before comparison]
```
## Procedure
1. Verify that both items are comparable under the same criterion and evidence scope.
2. Assess item A and item B symmetrically, recording criterion-level evidence and limitations.
3. Select A, B, or tie; assign confidence on the declared scale and explain the decisive contrast.
4. Return the comparison record without updating global ratings.
## Output contract
```yaml
produces: [pairwise_result, confidence, rationale, evidence_gaps]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- The result includes exactly one winner or an explicit tie, confidence, criterion, and symmetric evidence notes.
- Confidence cannot exceed the support of the weaker side of the comparison.
## Failure and counterexamples
Do not compare items with different scopes or criteria. If evidence is asymmetric or incomparable, return unresolved rather than forcing a winner.
## Provenance map
- resolved: comparison-executor
- resolved: gap-pairwise-judgment
