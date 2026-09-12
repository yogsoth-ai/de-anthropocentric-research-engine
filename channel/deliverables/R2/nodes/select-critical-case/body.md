# select-critical-case
## Purpose
Select most-likely, least-likely, or otherwise inference-maximizing cases that can decisively support or refute a claim.
## Input contract
```yaml
required: [claim, case_universe, selection_logic]
optional: [likelihood_model, boundary_conditions]
constraints: [case selection rule and inference purpose must be explicit]
```
## Procedure
1. Define the eligible case universe and selection objective.
2. Rank cases under the declared logic.
3. Select and justify the critical case, including excluded cases.
## Output contract
```yaml
produces: [critical_case, selection_rationale, excluded_cases, inference_role]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Selected case must be traceable to the stated selection logic.
## Failure and counterexamples
Do not call a convenient case critical without comparing it to the declared universe.
## Provenance map
- resolved: critical-case-design
- resolved: counterexample-heuristics
