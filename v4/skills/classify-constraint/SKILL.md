---
name: classify-constraint
description: "Classify constraints as hard, soft, or assumption-like after explicit identification."
---

# classify-constraint
## Purpose
Classify each identified constraint as hard, soft, or assumption-like and make the consequence of that class explicit.
## Input contract
```yaml
required: [constraint_candidates, evidence_register, decision_context]
optional: [stakeholder_requirements, prior_constraint_ledger]
constraints: [each candidate has a statement, scope, source, and consequence if violated]
```
## Procedure
1. Parse each candidate into condition, scope, source, and violation consequence.
2. Mark hard when violation is disqualifying and externally anchored; soft when tradeable; assumption-like when inferred and testable.
3. Record the evidence and counterevidence supporting the class.
4. Emit the classified ledger and tests or escalation required for uncertain classes.
## Output contract
```yaml
produces: [constraint_ledger, classification_rationale, validation_actions]
delta_fields: [findings, evidence_updates, assumption_updates, uncertainties, decisions]
```
## Quality gates
- Every class has a source, scope, and violation consequence.
- An assumption-like item cannot be enforced as a hard veto until independently validated.
## Failure and counterexamples
Do not classify a preference as hard merely because it is strongly stated. Keep ambiguous constraints unresolved.
## Provenance map
- resolved: constraint-classification
