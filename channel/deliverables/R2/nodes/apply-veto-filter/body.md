# apply-veto-filter
## Purpose
Eliminate alternatives that violate any declared hard threshold and expose the exact veto condition for each removal.
## Input contract
```yaml
required: [alternatives, hard_constraints, measured_values]
optional: [constraint_priorities, missing_value_policy]
constraints: [each alternative is tested against every hard constraint; missing measurements cannot silently pass]
```
## Procedure
1. Bind each hard constraint to its direction, threshold, unit, and evidence source.
2. Check every alternative against every constraint and record pass, fail, or unknown per cell.
3. Veto an alternative when any hard constraint fails; keep unknowns separate from passes.
4. Return survivors, vetoed alternatives, violated constraints, and unresolved checks.
## Output contract
```yaml
produces: [survivor_set, veto_log, unresolved_checks]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Every veto names one alternative, one hard constraint, the observed value, threshold, direction, and source.
- A survivor has no failed or silently unresolved hard constraint.
## Failure and counterexamples
Do not replace a hard veto with a weighted average. If a value is missing, report unknown rather than treating it as compliant.
## Provenance map
- resolved: conjunctive-filter
