---
name: synthesize-literature-evidence
description: "Build a reproducible literature evidence base. Scoping, systematic, deep, narrative, and snowball are execution modes selected from intent and budget, not separate strategy nodes."
---

# synthesize-literature-evidence

## Purpose

Build a reproducible literature evidence base across scoping, systematic, deep, narrative, and snowball modes.

## Input contract

```yaml
required: [research_question, evidence_scope, inclusion_rules]
optional: [mode, seed_sources, query_set, time_window, quality_rubric]
constraints: [mode, eligible universe, provenance requirements, and stopping evidence must be explicit]
```

## Execution protocol

1. Define scope, queries, inclusion/exclusion rules, provenance, and stopping evidence (`define-evidence-protocol`).
2. Select high-information seeds and categorize the corpus (`select-seed-evidence`, `categorize-evidence`).
3. Extract structured records and audit study validity (`extract-evidence-record`, `audit-study-validity`).
4. Canonicalize entities, build the evidence hierarchy, and screen in stages (`canonicalize-entity`, `construct-hierarchy`, `screen-evidence-multistage`).
5. Expand citations and assess evidence saturation (`trace-citation-neighborhood`, `assess-evidence-saturation`).

Deviation: Mode determines which steps are needed. Scoping may stop after broad coverage and screening; systematic mode requires staged screening and validity audit; deep mode prioritizes full-text extraction; narrative mode may omit formal meta-analysis; snowball mode requires citation tracing. Omitted calls remain optional vocabulary, not phantom dependencies.

## Output contract

```yaml
produces: [evidence_corpus, structured_evidence_records, screening_flow, quality_assessment, synthesis_map, saturation_state]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
```

## Thresholds and quality gates

- A-class acquisition gates use six fields: declared universe, numerator, batch increment, stopping reason, source references, and direction/threshold rationale.
- C3 landscape acquisition: assess-evidence-saturation compares marginal information gain of the current batch with the comparable prior batch; set-threshold supplies a justified relative coverage floor instead of 150 sources.
- C4 direction narrowing: use candidate-pool/evidence-hit and full-text coverage ratios with a justified threshold; do not retain fixed 80-paper/30-page counts.
- C19 survey modes: use marginal topic coverage and evidence gain for saturation; set-threshold supplies scale-relative full-text, independent-source, and screening-coverage floors.
- C20 snowball: use relative coverage of high-information/critical nodes and new independent-evidence rate; stop when added citation batches are saturated under the declared threshold.

## Failure and counterexamples

Do not call a synthesis systematic without an auditable screening flow, deep without explicit full-text fields, or saturated when the current and prior comparable batches have not been compared. Abstract-only conclusions must be marked limited.

## Provenance map

- `resolved: literature-survey`
- `resolved: knowledge-acquisition-scoping-survey`
- `resolved: knowledge-acquisition-systematic-survey`
- `resolved: knowledge-acquisition-deep-survey`
- `concept: narrative-survey`
- `concept: snowball-survey`
- `resolved: knowledge-acquisition-survey-synthesis`

## Preserved source criteria ledger

| source | source line | kind | source criterion |
|---|---:|---|---|
| scoping-survey | 4239 | numeric/textual | breadth/depth: 100 paper-overview / 20 paper-search / 0 paper-research; HARD-GATE each SOP row ≥90%. |
| systematic-survey | 4246 | numeric/textual | 30 paper-research; HARD-GATE ≥90%. |
| deep-survey | 4253 | numeric | 50% deep-read rate (20/40). |
| snowball-survey | 4330 | numeric/textual | backward/forward lineage, 67% deep-read, minimal web-search budget. |

## Context checkpoint / Delta notes

Append protocol, seed rationale, screening counts, extracted records, quality judgments, citation expansion, saturation calculation, and unresolved evidence questions.
