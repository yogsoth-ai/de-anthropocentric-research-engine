# evaluate-scenario-impact
## Purpose
Evaluate one fixed candidate, path, or portfolio under one explicit scenario.
## Input contract
```yaml
required: [candidate, scenario, evaluation_criteria]
optional: [baseline, metric_definitions, vulnerability_rules]
constraints: [criteria, units, and scenario assumptions remain fixed during evaluation]
```
## Procedure
1. Instantiate the candidate under scenario assumptions.
2. Compute or qualitatively assess each declared criterion.
3. Identify tradeoffs, vulnerabilities, and failure triggers.
4. Return impact evidence and unresolved uncertainties.
## Output contract
```yaml
produces: [impact_assessment, metric_results, tradeoffs, vulnerabilities, failure_triggers]
delta_fields: [findings, uncertainties, decisions]
```
## Quality gates
- All declared criteria are addressed with units or explicit qualitative scales.
- Vulnerable or failing members are named, not hidden in aggregate scores.
- Scenario assumptions and baseline are cited for every comparison.
## Parameterization
Caller supplies candidate schema, scenario schema, criteria, metric formulas, baseline, and vulnerability thresholds.
## Failure and counterexamples
Reject evaluations that change scenario assumptions midstream or report aggregate impact without member-level checks.
## Provenance map
- concept: convergence/portfolio-evaluation-per-scenario
- concept: experiment-execution/scenario-impact-assessment
- intermediate: Pass3/evaluate-scenario
- intermediate: Pass3/assess-scenario-impact
