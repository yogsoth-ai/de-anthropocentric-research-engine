# select-next-pair
## Purpose
Select the next comparison pair to maximize expected information gain while respecting unresolved uncertainty and coverage.
## Input contract
```yaml
required: [candidate_set, current_ratings, uncertainty_matrix, comparison_budget]
optional: [pair_history, exploration_policy, exclusion_constraints]
constraints: [candidate IDs are stable; expected information gain uses the declared model and available evidence]
```
## Procedure
1. Enumerate eligible unjudged pairs and compute their current uncertainty and decision relevance.
2. Estimate expected information gain under the declared comparison model, including the value of resolving a tie or cycle.
3. Exclude pairs blocked by scope or data constraints, then select the highest-value eligible pair.
4. Return the selected pair, rationale, alternatives considered, and the budget impact.
## Output contract
```yaml
produces: [selected_pair, information_gain_estimate, candidate_pair_table, selection_rationale]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- The selected pair is eligible, not already resolved under the same model, and has a stated information-gain rationale.
- If all pairs are exhausted or blocked, return an explicit stop reason.
## Failure and counterexamples
Do not select a pair solely because it is adjacent in a list. Expected information gain cannot be claimed when uncertainty inputs are absent.
## Provenance map
- resolved: pair-selector
