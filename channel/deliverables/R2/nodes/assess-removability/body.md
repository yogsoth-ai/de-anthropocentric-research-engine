# assess-removability
## Purpose
Estimate whether a constraint can be removed or relaxed, at what cost, and with which residual risks.
## Input contract
```yaml
required: [constraint_record, dependency_map, removal_options, cost_model]
optional: [time_horizon, safety_limits, stakeholder_requirements]
constraints: [each option states feasibility, cost units, dependencies, and residual risk]
```
## Procedure
1. Trace the constraint to dependent claims, processes, and safety conditions.
2. Generate removal or relaxation options and estimate direct cost, delay, dependency changes, and residual risk.
3. Test each option against non-negotiable boundaries and identify the cheapest feasible relaxation.
4. Emit removability class, cost/risk profile, and a reversible trial where one exists.
## Output contract
```yaml
produces: [removability_assessment, option_comparison, residual_risks, recommended_trial]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- A-class gate: declared universe = all identified constraints and removal options; numerator = options with dependency, cost, and residual-risk evidence; batch increment = one option assessed; stopping reason = all options assessed or a feasible dominant option is established; source references = dependency, cost, and risk IDs; direction/threshold reason = removability improves only when dependency burden and residual risk decrease without violating hard boundaries.
- A removal claim must include at least one dependency, one cost, and one residual risk.
## Failure and counterexamples
Do not label a constraint removable because it is inconvenient. If removal changes the target construct, report a scope change instead.
## Provenance map
- resolved: removability-assessment
