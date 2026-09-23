# score-fmea-risk
## Purpose
Score severity, occurrence, detectability, and derive action priority for a failure mode.
## Input contract
```yaml
required: [failure_mode, severity_scale, occurrence_scale, detectability_scale]
optional: [evidence, priority_rule]
constraints: [scale anchors and direction must be declared before scoring]
```
## Procedure
1. Score severity, occurrence, and detectability against anchored scales.
2. Derive action priority using the declared rule.
3. Record evidence, uncertainty, and rationale for each score.
## Output contract
```yaml
produces: [severity_score, occurrence_score, detectability_score, action_priority, rationale]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Fixed scale semantics and scoring formula are retained; no relative substitution for risk methodology.
- A-class evidence coverage: declared universe = all failure modes in the register; numerator = modes with complete three-score evidence; batch increment = one scored mode batch; stopping reason = all material modes scored or residual unscored modes explicitly accepted; source references = incident data, tests, expert rationale; direction/threshold reason = prioritize higher severity/occurrence and lower detectability according to the declared rule.
## Failure and counterexamples
Do not compare scores from incompatible scales. Mark unknown rather than inventing a score.
## Provenance map
- resolved: severity-scoring
- resolved: occurrence-scoring
- resolved: detection-scoring
- resolved: action-priority-matrix
