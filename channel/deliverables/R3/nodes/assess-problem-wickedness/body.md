# assess-problem-wickedness
## Purpose
Assess whether a problem is tame, complex, or wicked using disagreement, moving boundaries, feedback, value conflict, and stopping-rule evidence.
## Input contract
```yaml
required: [problem_statement, stakeholder_views]
optional: [boundary_history, feedback_observations, candidate_stopping_rule]
constraints: [classification must cite observed disagreement or stability indicators]
```
## Procedure
1. Compare stakeholder definitions and desired outcomes.
2. Check boundary movement, feedback loops, and value conflicts.
3. Assess whether a stable stopping rule and agreed solution test exist.
4. Assign tame, complex, or wicked with evidence and uncertainty.
## Output contract
```yaml
produces: [wickedness_assessment, evidence_basis, workflow_implications]
delta_fields: [findings, uncertainties, decisions, open_questions]
```
## Quality gates
- Classification covers all five dimensions; disagreement is distinguished from missing information.
## Failure and counterexamples
Do not label a problem wicked solely because it is difficult or interdisciplinary.
## Provenance map
- `deep-insight/wickedness-assessment`: resolved.
