---
name: trace-assumption-cascade
description: "Trace downstream claims, methods, and conclusions that fail when a selected assumption is invalidated; distinguish local from cascading failure."
---

# trace-assumption-cascade
## Purpose
Trace downstream claims, methods, and conclusions that fail when a selected assumption is invalidated.
## Input contract
```yaml
required: [assumption, dependency_graph, downstream_claims]
optional: [failure_evidence, intervention]
constraints: [each cascade edge must identify dependency and failure mechanism]
```
## Procedure
1. Identify the assumption and immediate dependents.
2. Propagate invalidation through claims, methods, and conclusions.
3. Distinguish local from cascading failure and record recovery points.
## Output contract
```yaml
produces: [assumption_cascade, affected_claims, local_failures, cascading_failures, recovery_points]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class cascade coverage: declared universe = all downstream nodes reachable from the selected assumption; numerator = nodes with an assessed dependency and failure status; batch increment = one dependency layer; stopping reason = no new reachable nodes or marginal new impact is below a justified threshold; source references = dependency edges, assumption IDs, evidence IDs; direction/threshold reason = continue while newly reached nodes materially change decision or risk.
## Failure and counterexamples
Do not infer cascade from naming or proximity; require a dependency edge.
## Provenance map
- resolved: assumption-cascade
