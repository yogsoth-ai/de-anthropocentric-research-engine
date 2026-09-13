# Mode-conditioned contract format

Status: normative proposal for N1/N2/R6, 2026-09-13. Scope: all 22 registry nodes whose `modes` array is non-empty (92 mode entries in the current registry).

## 1. Locked syntax

For a node with modes, `## Input contract` contains exactly one YAML block with exactly one top-level key, `mode_contracts`. The value is a mapping whose keys are exactly the registry `modes`, once each, in registry order. Each mode value contains exactly these keys:

```yaml
mode_contracts:
  <mode-id>:
    required: [field_a, field_b]
    optional: [field_c]
    constraints: [constraint text]
```

`required`, `optional`, and `constraints` are always present; an empty list is written as `[]`. Contract field identifiers use lower_snake_case. Mode keys preserve registry spelling exactly, including slash and capitalization. `constraints` is a YAML sequence of strings, not a comma-packed string. No node-level `required`, `optional`, or `constraints` keys are allowed beside `mode_contracts`.

`## Output contract` uses the same shape. Every mode value contains exactly `produces` and `delta_fields`:

```yaml
mode_contracts:
  <mode-id>:
    produces: [artifact_a, artifact_b]
    delta_fields: [findings, decisions]
```

`delta_fields` may contain only the fixed eight names: `findings`, `evidence_updates`, `hypothesis_updates`, `assumption_updates`, `uncertainties`, `decisions`, `open_questions`, `recommended_jumps`. No top-level `produces` or `delta_fields` is allowed in a mode-bearing node.

The parser MUST reject: a missing mode, an extra mode, duplicate mode keys, a node-level contract key, a missing per-mode key, a non-list value, or a delta name outside the eight-name whitelist. A mode-bearing node with no mode-specific difference still uses this syntax.

After the host selects a mode, that mode's `required` fields are mandatory inputs and every listed `produces` field is a mandatory successful result. `optional` fields may be absent. `delta_fields` lists state channels the node is permitted to update; it does not make every listed channel mandatory. The selected mode comes from the execution plan/registry and is not repeated as a synthetic `mode` input field.

Nodes without registry modes keep the existing flat contract syntax. There is no `default` mode and no wildcard mode contract.

## 2. Reuse rule for identical modes

YAML anchors are the only permitted de-duplication. They are standard YAML and resolve to independent mappings before validation. Do not use prose such as “same as above”, a custom `inherits` key, or an omitted block.

### 2.1 Different outputs: `synthesize-literature-evidence`

```yaml
# Input contract
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

```yaml
# Output contract
mode_contracts:
  scoping:
    produces: [evidence_corpus, synthesis_map, saturation_state]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  systematic:
    produces: [evidence_corpus, structured_evidence_records, screening_flow, quality_assessment, synthesis_map, saturation_state]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  deep:
    produces: [evidence_corpus, structured_evidence_records, quality_assessment, synthesis_map]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  narrative:
    produces: [evidence_corpus, structured_evidence_records, synthesis_map]
    delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
  snowball:
    produces: [evidence_corpus, structured_evidence_records, synthesis_map, saturation_state]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions, recommended_jumps]
```

The output names above are the union already used by the tactic, narrowed per mode. Their source obligations are `scoping-survey`, `systematic-survey`, `deep-survey`, `narrative-review`, and `snowball` in `scripts/refactory_source.json`; the mode-specific depth/screening/citation constraints are preserved rather than inferred from a mode label.

### 2.2 Same outputs: `resolve-inventive-contradiction`

```yaml
# Input contract
mode_contracts:
  technical-contradiction: &contradiction_input
    required: [contradiction_statement, conflicting_requirements, system_components]
    optional: [operating_conditions, target_metrics, known_principles]
    constraints: [improvement_and_worsening_parameters_must_be_explicit]
  physical-contradiction: *contradiction_input
  separation: *contradiction_input

```

```yaml
# Output contract
mode_contracts:
  technical-contradiction: &contradiction_output
    produces: [contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
  physical-contradiction: *contradiction_output
  separation: *contradiction_output
```

The anchor is deliberate: the three v3 sources (`triz-contradiction-resolution`, `contradiction-matrix-lookup`, `separation-principle`) differ in method, not result schema. N2 must expand aliases before checking the per-mode key set; N1 must still retain all three mode keys.

## 3. Mode-by-mode output ledger

The complete 92-row, source-line-backed table is maintained in [`mode-output-ledger.md`](mode-output-ledger.md). It is normative. N1 copies its exact `produces` arrays; the prose in the examples does not create additional output fields.

## 4. Implementation handoff

N1: replace every mode-bearing node's two contract blocks with the locked syntax and populate outputs from the ledger/source files; do not retain a node-level union contract. N2: parse `mode_contracts`, expand YAML anchors, compare keys exactly to registry modes, validate each mode's delta subset, and reject legacy top-level contract keys for mode-bearing nodes. R6: host selects one registry mode, then reads the matching map entry; downstream routing remains in `recommended_jumps` and is not added to the graph schema.
