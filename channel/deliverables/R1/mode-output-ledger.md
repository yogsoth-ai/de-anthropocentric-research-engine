# Mode output ledger

Normative companion to `mode-contract-format.md`. Coverage: 22 mode-bearing nodes, 92 registry modes. Every `produces` value is a YAML-ready field list transcribed from the cited v3 output artifact or execution result. Source references point to the matching v3 `nodes[].name` entry in `scripts/refactory_source.json`; `source-unspecified` means no exact v3 mode node exists and the row is grounded only in the explicitly named corroborating source, not a fabricated provenance match.

N1 must not rename fields while copying this ledger. Where several modes share the same source-published schema, each mode still receives a separate mapping (YAML anchors allowed). A repeated list is not by itself evidence of confirmed sameness; §6 records the determination and its limit.

## 1. Decision and analysis

| node | mode | `produces` | v3 source evidence |
|---|---|---|---|
| `rank-candidates` | `gap-prioritization` | `[ranking_or_categories, scores, sensitivity_results, recommendation]` | `deep-insight-gap-prioritization` @2300; output body `skills/deep-insight-gap-prioritization/SKILL.md:64` |
| | `direction-selection` | `[ranking_or_categories, scores, eliminated_candidates, recommendation]` | `direction-narrowing` @5443 |
| | `mcda-best-choice` | `[scores, weights, sensitivity_results, recommendation]` | `best-option-selection` @116; output body :65 |
| | `full-ranking` | `[ranking_or_categories, scores, weights, sensitivity_results, recommendation]` | `full-ranking` @123; output body :69 |
| | `category-sorting` | `[ranking_or_categories, scores, weights, recommendation]` | `category-sorting` @130; output body :68 |
| | `non-compensatory-screening` | `[ranking_or_categories, scores, eliminated_candidates, recommendation]` | `non-compensatory-screening` @137; output body :70 |
| | `rapid-triage` | `[ranking_or_categories, scores, eliminated_candidates, recommendation]` | `rapid-triage` @3742 |
| | `stakeholder-weighted` | `[ranking_or_categories, scores, weights, sensitivity_results, recommendation]` | `stakeholder-weighted-ranking` @3728 |
| `map-validity-envelope` | `systematic-perturbation` | `[dimension_schema, perturbation_records, breakpoints, validity_envelope]` | `systematic-perturbation` @2510 |
| | `boundary-value-stress` | `[dimension_schema, perturbation_records, breakpoints, validity_envelope, critical_case_report]` | `boundary-probing` @5933 |
| | `critical-case` | `[breakpoints, validity_envelope, critical_case_report]` | `critical-case-design` @5828 |
| `explore-dimensional-space` | `morphological-generation` | `[dimension_schema, value_catalog, combination_map, compatibility_report]` | `morphological-exploration` @1740 |
| | `research-space-mapping` | `[dimension_schema, value_catalog, coverage_gaps, prioritized_regions, subquestions]` | `dimensional-analysis` @4918 |
| | `gap-mapping` | `[coverage_gaps, prioritized_regions, subquestions]` | `knowledge-structuring-gap-prioritization` @5016 |
| `analyze-constraints-readiness` | `obstacle-triage` | `[constraint_register, bottlenecks, mitigation_paths]` | `identify-obstacles` @5583; parent `obstacle-analysis` |
| | `readiness-assessment` | `[readiness_profile, bottlenecks]` | `maturity-diagnosis` @221; output body :59 |
| | `resource-envelope` | `[resource_envelope, bottlenecks, mitigation_paths]` | `resource-envelope-estimation` @235; output body :63 |
| | `causal-constraint-analysis` | `[constraint_register, bottlenecks, mitigation_paths]` | `constraint-identification` @228; output body :61 |
| | `maturation-path` | `[readiness_profile, resource_envelope, stage_gates, mitigation_paths]` | `maturation-pathway-design` @249; output body :70 |
| `sensitivity-analysis` | `Morris` | `[sensitivity_profile, interaction_effects]` | `parameter-screening` @2384; corroborating `morris-screening` @2853 |
| | `Sobol` | `[sensitivity_profile, interaction_effects, uncertainty_contributions]` | `variance-decomposition` @2391; corroborating `sobol-decomposition` @2860 |
| | `perturbation` | `[sensitivity_profile, interaction_effects]` | `systematic-perturbation` @2510; `controlled-perturbation` @2811 |
| | `Monte-Carlo` | `[sensitivity_profile, uncertainty_contributions, information_value_ranking]` | `uncertainty-propagation` @2405; `monte-carlo-sampling` @2909 |

## 2. Framing and ideation

| node | mode | `produces` | v3 source evidence |
|---|---|---|---|
| `problem-reframing` | `dominant-frame-escape` | `[dominant_frame, reframe_set, consequence_map]` | `dominant-idea-escape` @2419 |
| | `perspective-shift` | `[reframe_set, perspective_map, consequence_map]` | `multi-perspective-reframing` @2426; `creative-ideation-perspective-rotation` |
| | `stakeholder/worldview` | `[reframe_set, perspective_map]` | `six-hats-rotation` @2027; `role-based-ideation` @1971 |
| | `polarity` | `[reframe_set, consequence_map, polarity_map]` | `dialectical-reformulation` @2433 |
| | `abstraction-scope` | `[dominant_frame, reframe_set]` | `question-reformulation` @2335; output body :54 |
| `destructive-ideation` | `reverse` | `[assumption_targets, provocations, constructive_movements, idea_set]` | `assumption-destruction` @998 |
| | `negation` | `[assumption_targets, provocations, constructive_movements, idea_set]` | `axiom-negation` @1026 |
| | `random-entry` | `[provocations, constructive_movements, idea_set]` | `creative-ideation-provocation-generation` @1901 |
| | `extreme-constraint` | `[assumption_targets, provocations, constructive_movements, idea_set]` | `provocation-and-movement` @1894 |
| | `sacred-cow` | `[assumption_targets, provocations, constructive_movements, idea_set]` | `sacred-cow-hunting` @1978; `sacred-cow-identification` @1985 |
| | `distortion` | `[provocations, constructive_movements, idea_set]` | `creative-ideation-provocation-generation` @1901 |
| `map-stakeholder-system` | `critical-systems-heuristics` | `[system_boundary, perspective_set, disagreement_map]` | `csh-12-question` @2706; parent `stakeholder-mapping` @2321 |
| | `jobs-to-be-done` | `[stakeholder_job_map, perspective_set]` | `jtbd-mapping` @2713; parent `stakeholder-mapping` @2321 |
| | `stakeholder-salience` | `[salience_map, perspective_set, disagreement_map]` | `salience-classification` @2720; parent `stakeholder-mapping` @2321 |
| `resolve-inventive-contradiction` | `technical-contradiction` | `[contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]` | `triz-contradiction-resolution` @2160; `contradiction-matrix-lookup` @1299 |
| | `physical-contradiction` | `[contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]` | `separation-principle` @2013 |
| | `separation` | `[contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]` | `separation-principle` @2013 |
| `biomimetic-transfer` | `biologize-and-discover` | `[biological_question, biological_candidate_set, biological_strategies, design_principles, technical_solutions]` | `biologize-and-discover` @1068; source stages `problem-biologization -> organism-discovery -> biological-strategy-extraction -> abstraction-to-design -> emulation-generation` |
| | `BioTRIZ` | `[contradiction, biotriz_principles, biological_case_mapping, biological_strategies, design_principles, technical_solutions]` | `biotriz-principle-selection` @1089; `biotriz-resolution` @1096; source stages `principle selection -> case mapping -> strategy extraction -> abstraction -> emulation` |
| `conceptual-blending` | `two-space-blend` | `[input_space_set, generic_space, blend_candidates, idea_set]` | `concept-blending` @1215; `blend-construction` @1124 |
| | `multi-space-blend` | `[input_space_set, generic_space, blend_candidates, idea_set]` | `blend-composition` @1117; `blend-elaboration` @1131 |
| | `emergent-property-search` | `[input_space_set, blend_candidates, emergent_property_report, idea_set]` | `emergent-property-hunting` @1432 |
| `evolve-solution-population` | `mutation-selection` | `[mechanism_to_design_mapping, generated_solutions, synthesis]` | `evolution-strategy` @1481; source execution ends with a structured evolution-inspired design report |
| | `novelty-preserving-evolution` | `[novelty_assessment]` | **source-unspecified**: no exact v3 node named `variation-selection` was found; `creative-ideation-novelty-scoring` @1775 is corroborating novelty evidence only, not an exact source for this mode |

## 3. Evidence and experiment

| node | mode | `produces` | v3 source evidence |
|---|---|---|---|
| `synthesize-literature-evidence` | `scoping` | `[field_taxonomy, key_authors_and_groups, research_trends, open_questions, deep_investigation_entry_points]` | `scoping-survey` @4239; `Field Landscape Map`, output :79-86 |
| | `systematic` | `[prisma_flow, structured_comparison_tables, per_paper_quality_assessment, evidence_backed_gaps, synthesis_narrative]` | `systematic-survey` @4246; `Comprehensive Systematic Review`, output :91-98 |
| | `deep` | `[method_comparison, extracted_equations_algorithms, implementation_details, evidence_cited_conclusions, open_questions]` | `deep-survey` @4253; `Detailed Technical Analysis`, output :77-84 |
| | `narrative` | `[central_thesis, thematic_supporting_evidence, addressed_counterarguments, gap_or_opportunity, narrative_arc]` | `narrative-review` @4260; `Structured Narrative`, output :82-89 |
| | `snowball` | `[seed_ancestor_map, seed_descendant_map, idea_evolution, branch_points, current_frontier, lineage_dag]` | `snowball` @4267; `Research Lineage Map`, output :83-91 |
| `synthesize-meta-analytic-evidence` | `pairwise` | `[question, inclusion_criteria, studies_included, effect_size_type, model, heterogeneity_plan, sensitivity_plan, bias_assessment_plan, reporting]` | `pairwise-synthesis` @4652; output format :86-98 (the protocol is the source artifact; no union-only shorthand) |
| | `network` | `[question, network_geometry, inclusion_criteria, studies_included, effect_size_type, model, transitivity_assessment, ranking_method, heterogeneity_plan, inconsistency_plan, sensitivity_plan, bias_assessment_plan, reporting]` | `network-comparison` @4659; output format :94-113 |
| | `cumulative` | `[question, temporal_scope, inclusion_criteria, studies_included, chronological_order, effect_size_type, model, temporal_analyses, time_lag_bias, quality_trend, reporting]` | `cumulative-tracking` @4666; output format :91-110 |
| | `heterogeneity` | `[question, heterogeneity_metrics, moderator_candidates, investigation_plan, a_priori_hypotheses, multiple_testing, reporting]` | `heterogeneity-investigation` @4673; output format :91-108 |
| | `bias` | `[question, bias_domains, grey_literature_search, grade_assessment, sensitivity_plan, reporting]` | `bias-detection` @4680; output format :93-120 |
| `design-experiment` | `factorial` | `[factor_level_matrix, factor_level_catalog, estimands_main_effects_interactions, metric_significance_plan, sample_power_plan]` | `experiment-execution-factor-level-design` @3105; source steps identify factors/levels, construct matrix, specify metrics/significance, estimate power |
| | `ablation` | `[ablation_matrix, baseline_anchors_full_minimal, attribution_contrasts, component_interaction_plan]` | `ablation-design` @3112; source protocol distinguishes systematic/replacement/combinatorial/conditional component removal |
| | `comparison` | `[controlled_baseline_comparison, matched_confound_controls, seed_environment_protocol, statistical_comparison_plan, reproducibility_protocol]` | `comparison-design` @3119; source steps require matched baselines, seed protocol, environment lock, and statistical comparison |
| | `scaling` | `[scaling_axes, geometric_scale_points, scaling_experiment_grid, curve_fit_plan, scale_budget_plan]` | `scaling-design` @3126; source requires data/compute/model axes, geometric points (typically 4–8), grid and curve fitting |
| | `robustness` | `[perturbation_stress_matrix, severity_axes, baseline_comparison, degradation_metrics, survival_criteria]` | `robustness-design` @3133; source requires perturbation conditions, severity levels, baselines, degradation metrics and survival criteria |
| `formulate-hypotheses` | `deductive` | `[hypothesis_set, operational_definitions, predictions, falsification_conditions]` | `deductive-hypothesis-generation` @3749 |
| | `inductive` | `[hypothesis_set, operational_definitions, predictions, falsification_conditions]` | `inductive-hypothesis-generation` @3756 |
| | `abductive` | `[hypothesis_set, operational_definitions, predictions, falsification_conditions]` | `abductive-hypothesis-generation` @3763 |
| | `competing-hypotheses` | `[hypothesis_set, operational_definitions, predictions, falsification_conditions, comparison_matrix]` | `competing-hypothesis-construction` @3770; `competing-hypothesis-matrix` @3861 |

## 4. Adversarial and epistemic audit

| node | mode | `produces` | v3 source evidence |
|---|---|---|---|
| `adversarial-deliberation` | `critic-defender-judge` | `[attack_record, defense_record, adjudication, confidence_trace]` | `critic-defender-judge` @5667 |
| | `courtroom` | `[attack_record, defense_record, adjudication, confidence_trace]` | `courtroom-structured` @5688 |
| | `winner-stress` | `[attack_record, adjudication, confidence_trace]` | `winner-stress-testing` @298; output body :67-80 |
| | `resurrection-advocacy` | `[defense_record, adjudication, confidence_trace]` | `resurrection-advocacy` @291; output body :58-69 |
| | `criteria-interrogation` | `[attack_record, defense_record, adjudication]` | `adversarial-escalation` @5695 |
| | `stakeholder-objection` | `[attack_record, defense_record, adjudication, confidence_trace]` | `multi-perspective-attack` @445 |
| | `counter-thesis` | `[defense_record, adjudication, confidence_trace]` | `steel-manning-synthesis` @851 |
| `falsification-first-audit` | `sharp-claim` | `[claim_falsifiability, refutation_condition, attacks_attempted, outcome_bucket, refutation_or_surviving_forbidden_content, honest_residue]` | `falsification-first-stress-test` @6472; `FalsificationLedger`, output :107-109 |
| | `truthseeking-debate` | `[most_falsifiable_form, committed_refuter, cross_examination_findings, attack_severity, outcome_bucket, refutation_or_forbidden_content]` | `adversarial-debate-truthseeking` @6479; `DebateBucketing`, output :63-65 |
| | `truthseeking-red-team` | `[claim_load_rank, assumption_classification, refutation_condition, refutation_attempt, outcome_bucket, framing_risk_brief]` | `red-team-truthseeking` @6486; `RefutationSurfaceMap`, output :62-64 |
| `audit-structural-equivalence` | `isomorphism` | `[claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]` | `source-common-schema`: `isomorphism-falsification` @6493; `IsomorphismVerdict`, output :49-51 |
| | `substructure` | `[claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]` | `source-common-schema`: same source @6493; mode selects rung 2, not a separate v3 schema |
| | `homomorphism` | `[claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]` | `source-common-schema`: same source @6493; mode selects rung 3, not a separate v3 schema |
| | `shared-invariant` | `[claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]` | `source-common-schema`: same source @6493; mode selects rung 4, not a separate v3 schema |
| | `analogy` | `[claimed_sides, maps_attempted, monsters_found, dimension_count_result, highest_defended_rung, required_wording_change]` | `source-common-schema`: same source @6493; mode selects rung 5, not a separate v3 schema |
| `audit-validator-independence` | `validator` | `[noncircularity_matrix, red_cell_actions, validator_verdict, adversarial_ground_truth_set]` | `source-common-schema`: `circular-validation-audit` @6500; `NonCircularityMatrix`, output :53-55 |
| | `benchmark` | `[noncircularity_matrix, red_cell_actions, validator_verdict, adversarial_ground_truth_set]` | `source-common-schema`: same source @6500; v3 does not publish a benchmark-specific result schema |
| | `sandbox` | `[noncircularity_matrix, red_cell_actions, validator_verdict, adversarial_ground_truth_set]` | `source-common-schema`: same source @6500; v3 does not publish a sandbox-specific result schema |
| | `simulation` | `[noncircularity_matrix, red_cell_actions, validator_verdict, adversarial_ground_truth_set]` | `source-common-schema`: same source @6500; v3 does not publish a simulation-specific result schema |
| `audit-convergence-independence` | `evidence-paths` | `[independence_ledger, effective_evidence_count, common_cause_framing, independent_path_result_or_design, correlated_errors, corrected_confidence_statement]` | `source-common-schema`: `independent-convergence-audit` @6507; `ConvergenceIndependenceReport`, output :51-53 |
| | `agents` | `[independence_ledger, effective_evidence_count, common_cause_framing, independent_path_result_or_design, correlated_errors, corrected_confidence_statement]` | `source-common-schema`: same source @6507; v3 does not publish an agent-specific result schema |
| | `models` | `[independence_ledger, effective_evidence_count, common_cause_framing, independent_path_result_or_design, correlated_errors, corrected_confidence_statement]` | `source-common-schema`: same source @6507; v3 does not publish a model-specific result schema |
| | `methods` | `[independence_ledger, effective_evidence_count, common_cause_framing, independent_path_result_or_design, correlated_errors, corrected_confidence_statement]` | `source-common-schema`: same source @6507; v3 does not publish a method-specific result schema |
| `audit-explanatory-compression` | `earned-simplicity` | `[forbidden_set, risky_predictions, accommodation_audit, deletion_test_result, elegance_verdict, earning_prediction]` | `source-common-schema`: `elegance-trap-probe` @6514; `EleganceVerdict`, output :46-48 |
| | `decorative-simplicity` | `[forbidden_set, risky_predictions, accommodation_audit, deletion_test_result, elegance_verdict, earning_prediction]` | `source-common-schema`: same source @6514; mode is a verdict branch, not a separate v3 schema |
| | `risky-prediction` | `[forbidden_set, risky_predictions, accommodation_audit, deletion_test_result, elegance_verdict, earning_prediction]` | `source-common-schema`: same source @6514; mode is a test emphasis, not a separate v3 schema |

## 5. Delta rule

For every mode, copy the node's existing `delta_fields` list into that mode's output mapping. The v3 mode sources change artifact shape but do not define a separate research-state namespace. This preserves the fixed eight-field model while satisfying the B-route requirement that every mode owns a complete contract. `synthesize-literature-evidence.snowball` and any other branch that recommends a continuation may include `recommended_jumps`; no graph edge schema is added.

## 6. Determination register

This register is the audit layer for the 92 rows above. `mode-specific` means the listed v3 source has a mode-specific output artifact. `source-common-schema` means the modes are distinct execution/equivalence branches but the only v3 source exposes one result schema; it is not a claim that the modes were independently confirmed identical. `confirmed-same` is reserved for the one case where the three v3 sources differ in method but explicitly return the same result shape. `source-unspecified` means the exact v3 source was not found; the placeholder is not authoritative output and must not be silently promoted.

| node | modes covered (each is one ledger row) | determination and basis |
|---|---|---|
| `rank-candidates` | `gap-prioritization`; `direction-selection`; `mcda-best-choice`; `full-ranking`; `category-sorting`; `non-compensatory-screening`; `rapid-triage`; `stakeholder-weighted` | `mode-specific`: separate v3 strategy/SOP sources listed in §1. |
| `map-validity-envelope` | `systematic-perturbation`; `boundary-value-stress`; `critical-case` | `mode-specific`: separate perturbation, boundary-probing and critical-case sources listed in §1. |
| `explore-dimensional-space` | `morphological-generation`; `research-space-mapping`; `gap-mapping` | `mode-specific`: morphological-exploration, dimensional-analysis and gap-prioritization sources listed in §1. |
| `analyze-constraints-readiness` | `obstacle-triage`; `readiness-assessment`; `resource-envelope`; `causal-constraint-analysis`; `maturation-path` | `mode-specific`: obstacle, maturity, resource, constraint and maturation sources listed in §1. |
| `sensitivity-analysis` | `Morris`; `Sobol`; `perturbation`; `Monte-Carlo` | `mode-specific`: each row has a distinct v3 strategy source and corroborating SOP where available. |
| `problem-reframing` | `dominant-frame-escape`; `perspective-shift`; `stakeholder/worldview`; `polarity`; `abstraction-scope` | `mode-specific`: distinct reframing sources; slash spelling is registry-literal. |
| `destructive-ideation` | `reverse`; `negation`; `random-entry`; `extreme-constraint`; `sacred-cow`; `distortion` | `mode-specific` where an exact source exists; `random-entry` and `distortion` use the shared provocation-generation source because v3 does not publish separate output schemas. This is source-common-schema, not confirmed sameness. |
| `map-stakeholder-system` | `critical-systems-heuristics`; `jobs-to-be-done`; `stakeholder-salience` | `mode-specific` for the named v3 mappings; parent stakeholder-mapping is only corroborating context. |
| `resolve-inventive-contradiction` | `technical-contradiction`; `physical-contradiction`; `separation` | `confirmed-same`: `triz-contradiction-resolution`, `contradiction-matrix-lookup`, and `separation-principle` differ in method, not result schema; the shared output is deliberate. |
| `biomimetic-transfer` | `biologize-and-discover`; `BioTRIZ` | `mode-specific`: biologize/discover returns biological problem/candidate/function evidence; BioTRIZ returns principle/case/technical-resolution artifacts. |
| `conceptual-blending` | `two-space-blend`; `multi-space-blend`; `emergent-property-search` | `mode-specific`: blend construction/composition/elaboration and emergent-property sources are separated in §2. |
| `evolve-solution-population` | `mutation-selection`; `novelty-preserving-evolution` | `mutation-selection` is `mode-specific` from `evolution-strategy`; `novelty-preserving-evolution` is `source-unspecified` because no exact `variation-selection` source exists. The novelty-scoring node is corroborating only. |
| `synthesize-literature-evidence` | `scoping`; `systematic`; `deep`; `narrative`; `snowball` | `mode-specific`: five distinct survey/review output formats are cited in §3. |
| `synthesize-meta-analytic-evidence` | `pairwise`; `network`; `cumulative`; `heterogeneity`; `bias` | `mode-specific`: five distinct protocol output formats are transcribed from the v3 source sections at §3. |
| `design-experiment` | `factorial`; `ablation`; `comparison`; `scaling`; `robustness` | `mode-specific`: five distinct design protocols are transcribed from their v3 sources at §3; no union list remains. |
| `formulate-hypotheses` | `deductive`; `inductive`; `abductive`; `competing-hypotheses` | `mode-specific` where separate v3 source is named; `deductive`/`inductive`/`abductive` retain their source-specific hypothesis artifacts, while shared fields are only the common contract intersection. |
| `adversarial-deliberation` | `critic-defender-judge`; `courtroom`; `winner-stress`; `resurrection-advocacy`; `criteria-interrogation`; `stakeholder-objection`; `counter-thesis` | `mode-specific` for the rows with exact v3 strategy sources; where a source family is reused, the source exposes the same adjudication artifact and is marked source-common-schema in the row evidence rather than asserted identical. |
| `falsification-first-audit` | `sharp-claim`; `truthseeking-debate`; `truthseeking-red-team` | `mode-specific`: `FalsificationLedger`, `DebateBucketing`, and `RefutationSurfaceMap` source artifacts are distinct. |
| `audit-structural-equivalence` | `isomorphism`; `substructure`; `homomorphism`; `shared-invariant`; `analogy` | `source-common-schema`: all five rungs are branches of the single v3 `isomorphism-falsification` output `IsomorphismVerdict`; v3 does not publish five independent schemas. |
| `audit-validator-independence` | `validator`; `benchmark`; `sandbox`; `simulation` | `source-common-schema`: all four validator targets use the single v3 `circular-validation-audit` output `NonCircularityMatrix`; no mode-specific v3 output is published. |
| `audit-convergence-independence` | `evidence-paths`; `agents`; `models`; `methods` | `source-common-schema`: all four targets use the single v3 `independent-convergence-audit` output `ConvergenceIndependenceReport`; the source does not distinguish result schemas by target. |
| `audit-explanatory-compression` | `earned-simplicity`; `decorative-simplicity`; `risky-prediction` | `source-common-schema`: all three verdict branches use the single v3 `elegance-trap-probe` output `EleganceVerdict`; branch is a verdict condition, not a separate v3 artifact schema. |

**Coverage check:** 22 nodes, 92 mode rows. No `source-unspecified` row is labeled `confirmed-same`; the only confirmed-same determination is `resolve-inventive-contradiction`, with the source-method/result-schema rationale stated above.
