# verify-evidence-independence
## Purpose
Determine whether a finding is supported by independent evidence channels rather than one source lineage.
## Input contract
```yaml
required: [finding, evidence_records, independence_definition]
optional: [source_lineage, search_scope, stopping_rule]
constraints: [independence claims require explicit lineage and channel distinctions]
```
## Procedure
1. Group records by source, method, dataset, and citation lineage.
2. Identify channels that are independent under the supplied definition.
3. Compare direction, effect, and contradiction across channels.
4. Return support status, dependence risks, and remaining search needs.
## Output contract
```yaml
produces: [independence_assessment, independent_evidence_set, dependence_risks, open_questions]
delta_fields: [evidence_updates, uncertainties, open_questions]
```
## Quality gates
- No record is counted as independent without a documented lineage break.
- Agreement and disagreement are reported separately.
- Search stops only under caller-supplied stopping rule or explicit saturation rationale.
## Parameterization
Caller supplies evidence schema, independence tests, lineage fields, channel taxonomy, and stopping rule.
## Failure and counterexamples
Reject unsupported independence claims, duplicate lineages, or evidence pooled without provenance.
## Provenance map
- concept: deep-insight/cross-database-verification
## Preserved source criteria ledger
| source | criterion |
|---|---|
| deep-insight/cross-database-verification | Seek independent evidence channels sufficient to test source-specificity. |
