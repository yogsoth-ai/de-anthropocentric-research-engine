# classify-stakeholder-salience
## Purpose
Classify stakeholder salience using power, legitimacy, urgency, dependency, or a supplied schema.
## Input contract
```yaml
required: [stakeholder_set, salience_schema]
optional: [power_evidence, legitimacy_evidence, urgency_evidence, dependency_evidence]
constraints: [each classification dimension needs an evidence status]
```
## Procedure
1. Normalize stakeholders and their relevant claims or stakes.
2. Score or categorize each stakeholder on the supplied salience dimensions.
3. Record dependency and conflict effects, then produce a prioritized salience map.
## Output contract
```yaml
produces: [salience_map, dimension_scores, dependency_notes, priority_order]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Schema dimensions are explicit; missing evidence is marked unknown rather than treated as zero.
## Failure and counterexamples
Do not equate high power with high legitimacy, and do not collapse conflicting dimensions into one unexplained rank.
## Provenance map
- `stakeholder-salience-analysis`: concept (no exact pool entry).
- `salience-classification`: resolved.
