# assess-prior-art-and-claims

## Purpose

Assess novelty, prior art, claim scope, legal-status observations, and provenance without making unsupported legal conclusions.

## Input contract

```yaml
required: [claim_set, target_domain, jurisdiction_scope]
optional: [known_families, search_context, evidence_records]
constraints: [claim text and source provenance required, jurisdiction and observation date must be explicit]
```

## Execution protocol

1. Parse independent/dependent claims and map elements to technical functions (`parse-patent-claim`).
2. Trace priority, family, continuation, and citation relationships (`trace-patent-family`).
3. Assess breadth, limiting elements, overlap, and design-around vulnerability (`assess-patent-claim-scope`).
4. Classify observed status by jurisdiction and date (`assess-patent-legal-status`).
5. Check source independence before synthesizing novelty findings (`verify-evidence-independence`).

Deviation: Skip status or independence checks only when the corresponding input is absent; record the omission as an open question. Do not infer legal status from an undated or single-source record.

## Output contract

```yaml
produces: [claim_element_map, prior_art_family_map, scope_assessment, legal_status_observations, novelty_findings]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- Every claim element must map to a cited source or be marked unsupported.
- Any acquisition threshold must use a declared eligible family/source universe and relative coverage, not a fixed historical count.
- Status observations require jurisdiction, observation date, source, and uncertainty.

## Failure and counterexamples

Do not call a claim novel because no result was found; mark search coverage and unresolved elements. Do not collapse related family members into one record when claim scope or jurisdiction differs.

## Provenance map

- `resolved: prior-art-search`
- `resolved: knowledge-acquisition-claim-analysis`
- `resolved: knowledge-acquisition-claim-decomposition`
- `resolved: claim-parsing`
- `resolved: legal-status-assessment`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| claim-analysis | 4435 | numeric/textual | Budget 30 families / 30 claim / 20 web; HARD-GATE. |

## Context checkpoint / Delta notes

Append claim elements, family links, scope uncertainties, status observations, source-independence judgments, and unresolved search questions.
