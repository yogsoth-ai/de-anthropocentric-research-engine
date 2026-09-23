# evaluate-optionality
## Purpose
Evaluate staging, deferral, reversible commitment, and information-gathering options under uncertainty.
## Input contract
```yaml
required: [decision_options, uncertainty_register, time_horizon, consequence_model]
optional: [irreversibility_costs, information_actions, trigger_conditions]
constraints: [each option states timing, reversibility, information gained, and consequence range]
```
## Procedure
1. Represent immediate, deferred, staged, and information-gathering actions on a common timeline.
2. Estimate each action's reversible value, delay cost, information gain, and downside exposure.
3. Identify trigger conditions that would justify advancing, pausing, or abandoning each staged option.
4. Emit an option-value comparison and the conditions under which deferral is preferable to commitment.
## Output contract
```yaml
produces: [option_value_table, timing_policy, trigger_conditions, uncertainty_notes]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- Each option includes at least one consequence of acting now and one consequence of waiting.
- Information value is not counted unless it can change a downstream decision.
## Failure and counterexamples
Do not call delay optionality when waiting only postpones an irreversible loss. If trigger conditions are unobservable, mark the option unresolved.
## Provenance map
- resolved: temporal-sequencing
