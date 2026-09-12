# assess-patent-legal-status

## Purpose

Classify observed patent status by jurisdiction and observation date while preserving uncertainty and source dependence.

## Input contract

```yaml
required: [patent_record, jurisdiction, observation_date, status_sources]
optional: [family_events, prosecution_events]
constraints: [status is an observation tied to dated sources, not an undated legal inference]
```

## Procedure

1. Normalize application, publication, grant, lapse, expiration, and abandonment events.
2. Align events to jurisdiction and observation date.
3. Reconcile conflicting source observations and preserve the disagreement.
4. Emit status, confidence, and unresolved legal-status questions.

## Output contract

```yaml
produces: [status_timeline, jurisdiction_status, source_reconciliation, status_uncertainties]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Every status is dated and jurisdiction-scoped.
- Conflicts retain both source records and a reconciliation note.

## Failure and counterexamples

Do not infer current validity from a filing event alone or transfer one jurisdiction's status to another.

## Provenance map

- `resolved: knowledge-acquisition-legal-status-assessment`

