# Mode output ledger

Normative companion to `mode-contract-format.md`. Coverage: 22 mode-bearing nodes, 92 registry modes. Every `produces` value is an exact YAML-ready field list. Source references point to the matching v3 `nodes[].name` entry in `scripts/refactory_source.json`; `concept` means no exact v3 node exists and the row is grounded in the named parent source body, not a fabricated provenance match.

The ledger narrows the existing v4 tactic output vocabulary. N1 must not rename fields while copying it. Where several modes share the same list, each mode still receives a separate mapping (YAML anchors allowed).

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
| `biomimetic-transfer` | `biologize-and-discover` | `[biological_analogs, strategy_extract, transfer_candidate, compatibility_report]` | `biologize-and-discover` @1068 |
| | `BioTRIZ` | `[biological_analogs, strategy_extract, transfer_candidate, compatibility_report]` | `biotriz-principle-selection` @1089; `biotriz-resolution` @1096 |
| `conceptual-blending` | `two-space-blend` | `[input_space_set, generic_space, blend_candidates, idea_set]` | `concept-blending` @1215; `blend-construction` @1124 |
| | `multi-space-blend` | `[input_space_set, generic_space, blend_candidates, idea_set]` | `blend-composition` @1117; `blend-elaboration` @1131 |
| | `emergent-property-search` | `[input_space_set, blend_candidates, emergent_property_report, idea_set]` | `emergent-property-hunting` @1432 |
| `evolve-solution-population` | `mutation-selection` | `[evolved_population, selected_variants, diversity_report, sensitivity_report]` | `evolution-strategy` @1481 |
| | `novelty-preserving-evolution` | `[evolved_population, selected_variants, diversity_report, sensitivity_report]` | `evolution-strategy` @1481; novelty evidence `creative-ideation-novelty-scoring` @1775 |

## 3. Evidence and experiment

| node | mode | `produces` | v3 source evidence |
|---|---|---|---|
| `synthesize-literature-evidence` | `scoping` | `[evidence_corpus, synthesis_map, saturation_state]` | `scoping-survey` @4239; output body :79-86 |
| | `systematic` | `[evidence_corpus, structured_evidence_records, screening_flow, quality_assessment, synthesis_map, saturation_state]` | `systematic-survey` @4246; output body :91-98 |
| | `deep` | `[evidence_corpus, structured_evidence_records, quality_assessment, synthesis_map]` | `deep-survey` @4253; output body :77-84 |
| | `narrative` | `[evidence_corpus, structured_evidence_records, synthesis_map]` | `narrative-review` @4260; output body :82-89 |
| | `snowball` | `[evidence_corpus, structured_evidence_records, synthesis_map, saturation_state]` | `snowball` @4267; output body :83-91 |
| `synthesize-meta-analytic-evidence` | `pairwise` | `[effect_estimate, uncertainty, heterogeneity_report, bias_report, sensitivity_results]` | `pairwise-synthesis` @4652; output body :86-98 |
| | `network` | `[effect_estimate, uncertainty, heterogeneity_report, bias_report, sensitivity_results]` | `network-comparison` @4659; output body :94-113 |
| | `cumulative` | `[effect_estimate, uncertainty, heterogeneity_report, bias_report, sensitivity_results]` | `cumulative-tracking` @4666; output body :91-110 |
| | `heterogeneity` | `[uncertainty, heterogeneity_report, sensitivity_results]` | `heterogeneity-investigation` @4673; output body :91-108 |
| | `bias` | `[uncertainty, bias_report, sensitivity_results]` | `bias-detection` @4680; output body :93-117 |
| `design-experiment` | `factorial` | `[design_matrix, analysis_plan, sample_plan, preregistered_thresholds, reproducibility_checklist]` | `experiment-execution-factor-level-design` @3105 |
| | `ablation` | `[design_matrix, analysis_plan, sample_plan, preregistered_thresholds, reproducibility_checklist]` | `ablation-design` @3112 |
| | `comparison` | `[design_matrix, analysis_plan, sample_plan, preregistered_thresholds, reproducibility_checklist]` | `comparison-design` @3119 |
| | `scaling` | `[design_matrix, analysis_plan, sample_plan, preregistered_thresholds, reproducibility_checklist]` | `scaling-design` @3126 |
| | `robustness` | `[design_matrix, analysis_plan, sample_plan, preregistered_thresholds, reproducibility_checklist]` | `robustness-design` @3133 |
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
| `falsification-first-audit` | `sharp-claim` | `[sharp_claim, falsification_program, probe_record, falsification_verdict]` | `falsification-first-stress-test` @6472; output body :107-109 |
| | `truthseeking-debate` | `[sharp_claim, probe_record, falsification_verdict]` | `adversarial-debate-truthseeking` @6479; output body :63-65 |
| | `truthseeking-red-team` | `[falsification_program, probe_record, falsification_verdict]` | `red-team-truthseeking` @6486; output body :62-64 |
| `audit-structural-equivalence` | `isomorphism` | `[structural_mapping, preservation_report, counterexamples, downgraded_claim]` | `isomorphism-falsification` @6493; output body :49-51 |
| | `substructure` | `[structural_mapping, preservation_report, counterexamples, downgraded_claim]` | same source @6493 |
| | `homomorphism` | `[structural_mapping, preservation_report, counterexamples, downgraded_claim]` | same source @6493 |
| | `shared-invariant` | `[structural_mapping, preservation_report, counterexamples, downgraded_claim]` | same source @6493 |
| | `analogy` | `[structural_mapping, preservation_report, counterexamples, downgraded_claim]` | same source @6493 |
| `audit-validator-independence` | `validator` | `[assumption_inventory, noncircularity_matrix, circularity_findings, falsification_test]` | `circular-validation-audit` @6500; output body :53-55 |
| | `benchmark` | `[assumption_inventory, noncircularity_matrix, circularity_findings, falsification_test]` | same source @6500 |
| | `sandbox` | `[assumption_inventory, noncircularity_matrix, circularity_findings, falsification_test]` | same source @6500 |
| | `simulation` | `[assumption_inventory, noncircularity_matrix, circularity_findings, falsification_test]` | same source @6500 |
| `audit-convergence-independence` | `evidence-paths` | `[dependency_map, independence_audit, effective_evidence_count, sensitivity_report]` | `independent-convergence-audit` @6507; output body :51-53 |
| | `agents` | `[dependency_map, independence_audit, effective_evidence_count, sensitivity_report]` | same source @6507 |
| | `models` | `[dependency_map, independence_audit, effective_evidence_count, sensitivity_report]` | same source @6507 |
| | `methods` | `[dependency_map, independence_audit, effective_evidence_count, sensitivity_report]` | same source @6507 |
| `audit-explanatory-compression` | `earned-simplicity` | `[compression_assessment, risky_prediction_tests, critique, score]` | `elegance-trap-probe` @6514; output body :46-48 |
| | `decorative-simplicity` | `[compression_assessment, risky_prediction_tests, critique, score]` | same source @6514 |
| | `risky-prediction` | `[compression_assessment, risky_prediction_tests, critique, score]` | same source @6514 |

## 5. Delta rule

For every mode, copy the node's existing `delta_fields` list into that mode's output mapping. The v3 mode sources change artifact shape but do not define a separate research-state namespace. This preserves the fixed eight-field model while satisfying the B-route requirement that every mode owns a complete contract. `synthesize-literature-evidence.snowball` and any other branch that recommends a continuation may include `recommended_jumps`; no graph edge schema is added.
