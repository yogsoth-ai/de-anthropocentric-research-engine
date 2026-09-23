---
name: audit-data-contamination
description: "Audit train/test leakage, memorization artifacts, temporal leakage, and disclosure pathways that can invalidate evaluation."
---

# audit-data-contamination

## Purpose

Audit train/test leakage, memorization artifacts, temporal leakage, and disclosure pathways that can invalidate evaluation.

## Input contract

```yaml
required: [dataset_partitions, training_sources, evaluation_records]
optional: [release_history, deduplication_keys, access_logs]
constraints: [each contamination claim requires a matched record, pathway, and comparison basis]
```

## Procedure

1. Define partition, temporal, entity, and disclosure boundaries.
2. Match evaluation items against training and public-source records using declared keys.
3. Test suspected leakage pathways and compare affected with unaffected cases.
4. Classify confirmed, plausible, and unassessed contamination with impact notes.

## Output contract

```yaml
produces: [contamination_matches, pathway_map, affected_case_set, impact_assessment, audit_uncertainties]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Matching keys and time boundaries are recorded.
- False-positive matches are sampled and documented.

## Failure and counterexamples

Do not call lexical overlap contamination without a disclosure pathway, and do not infer clean separation from missing metadata.

## Provenance map

- `resolved: knowledge-acquisition-contamination-audit`

