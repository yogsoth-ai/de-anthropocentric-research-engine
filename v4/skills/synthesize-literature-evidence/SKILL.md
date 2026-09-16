---
name: synthesize-literature-evidence
description: "Build a reproducible literature evidence base. Scoping, systematic, deep, narrative, and snowball are execution modes selected from intent and budget, not separate strategy nodes."
---

# synthesize-literature-evidence

## Purpose

Build a reproducible literature evidence base across scoping, systematic, deep, narrative, and snowball modes.

## Input contract

```yaml
mode_contracts:
  scoping:
    required: [research_question, evidence_scope, inclusion_rules]
    optional: [seed_sources, query_set, time_window]
    constraints: [abstract_or_metadata_orientation_only, declared_universe_and_coverage_ratio]
  systematic:
    required: [research_question, evidence_scope, inclusion_rules]
    optional: [seed_sources, query_set, time_window, quality_rubric]
    constraints: [preregistered_search_and_staged_screening, validity_audit_required, declared_universe_and_coverage_ratio]
  deep:
    required: [research_question, evidence_scope, inclusion_rules]
    optional: [seed_sources, query_set, time_window, quality_rubric]
    constraints: [full_text_extraction_required, method_and_result_fields_must_be_traceable]
  narrative:
    required: [research_question, evidence_scope, inclusion_rules]
    optional: [seed_sources, query_set, time_window, quality_rubric]
    constraints: [heterogeneous_evidence_must_remain_explicit, no_formal_pooling_without_compatibility]
  snowball:
    required: [research_question, evidence_scope, inclusion_rules, seed_sources]
    optional: [query_set, time_window, quality_rubric]
    constraints: [backward_and_forward_citation_expansion, independent_evidence_saturation_required]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `define-evidence-protocol` to define scope, queries, inclusion and exclusion rules, provenance, and stopping evidence.
2. You MUST load skill `select-seed-evidence` to select high-information seeds. You MUST load skill `categorize-evidence` to categorize the corpus.
3. Apply the selected mode's extraction, appraisal, normalization, hierarchy, screening, or citation operations.
4. You MUST load skill `assess-evidence-saturation` to assess whether new independent evidence has saturated.
   If the synthesis needs a formal domain structure, consider `build-domain-ontology`. If an apparent absence needs validation as a research gap, consider `validate-research-gap`. If the evidence should define a quantitative comparison baseline, consider `establish-empirical-baseline`. If claims and counterclaims need explicit support relations, `construct-argument-map` may be the better next tactic.

Deviation: Mode determines which steps are needed. Scoping may stop after broad coverage and screening; systematic mode requires staged screening and validity audit; deep mode prioritizes full-text extraction; narrative mode may omit formal meta-analysis; snowball mode requires citation tracing. Omitted calls remain optional vocabulary, not phantom dependencies.

## Mode branches

- `scoping`: map the breadth of a field and its terminology to establish coverage, candidate sources, and a defensible follow-up scope. You MUST load skill `canonicalize-entity` to normalize entities and terminology. You MUST load skill `construct-hierarchy` to organize the mapped breadth. You MUST load skill `screen-evidence-multistage` to apply the declared broad screening stages.
- `systematic`: apply preregistered search, staged screening, and validity audit so inclusion decisions are reproducible and complete. You MUST load skill `screen-evidence-multistage` to perform staged screening. You MUST load skill `extract-evidence-record` to extract the included studies. You MUST load skill `audit-study-validity` to audit their validity.
- `deep`: prioritize full-text extraction and detailed study appraisal when the question requires mechanism-level evidence. You MUST load skill `extract-evidence-record` to extract full-text records. You MUST load skill `audit-study-validity` to perform detailed study appraisal.
- `narrative`: organize heterogeneous evidence into a transparent interpretive synthesis when formal pooling is not appropriate. You MUST load skill `extract-evidence-record` to retain structured source records. You MUST load skill `canonicalize-entity` to align recurring entities. You MUST load skill `construct-hierarchy` to organize the narrative evidence.
- `snowball`: expand backward and forward citation neighborhoods from high-information seeds, stopping when new independent evidence saturates. You MUST load skill `trace-citation-neighborhood` to expand the citation neighborhoods. You MUST load skill `extract-evidence-record` to preserve each retained source.

## Output contract

```yaml
mode_contracts:
  scoping:
    produces: [field_taxonomy, key_authors_and_groups, research_trends, open_questions, deep_investigation_entry_points]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  systematic:
    produces: [prisma_flow, structured_comparison_tables, per_paper_quality_assessment, evidence_backed_gaps, synthesis_narrative]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  deep:
    produces: [method_comparison, extracted_equations_algorithms, implementation_details, evidence_cited_conclusions, open_questions]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  narrative:
    produces: [central_thesis, thematic_supporting_evidence, addressed_counterarguments, gap_or_opportunity, narrative_arc]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
  snowball:
    produces: [seed_ancestor_map, seed_descendant_map, idea_evolution, branch_points, current_frontier, lineage_dag]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions, recommended_jumps]
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
| scoping-survey | 4239 | numeric/textual | breadth/depth: 100 paper-overview / 20 paper-search / 0 paper-research; HARD-GATE each SOP row >=90%. |
| systematic-survey | 4246 | numeric/textual | 30 paper-research; HARD-GATE >=90%. |
| deep-survey | 4253 | numeric | 50% deep-read rate (20/40). |
| snowball-survey | 4330 | numeric/textual | backward/forward lineage, 67% deep-read, minimal web-search budget. |

## Context checkpoint / Delta notes

Append protocol, seed rationale, screening counts, extracted records, quality judgments, citation expansion, saturation calculation, and unresolved evidence questions.
