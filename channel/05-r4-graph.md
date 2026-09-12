# R4 正文扇出交付

## Batch 01

- nodes: analyze-experiment-results, analyze-future-scenarios, build-domain-ontology, construct-argument-map, construct-causal-model, decompose-research-question, falsifiability-audit, formulate-research-question, pairwise-ranking, portfolio-optimization
- A/B/C: 0/0/0
- unresolved provenance: 65

## Batch 02

- nodes: structured-consensus, adjudicate-exchange, analyze-intervention, apply-question-framework, apply-stage-gate, apply-veto-filter, assess-question-quality, assess-ranking-consistency, assess-readiness-dimension, assess-removability
- A/B/C: 0/0/0
- unresolved provenance: 23

## Batch 03

- nodes: atomize-claim, atomize-concept, attach-evidence-to-relation, audit-structure-consistency, calibrate-probability-forecast, characterize-anomaly, classify-constraint, collect-independent-judgments, compare-hypotheses, compare-pair
- A/B/C: 0/0/0
- unresolved provenance: 14

## Batch 04

- nodes: construct-defense, construct-design-matrix, construct-validity-envelope, define-objective, design-discriminating-prediction, design-randomness-protocol, detect-breakpoint, detect-feedback-loop, document-counterclaim, elicit-weights
- A/B/C: 0/0/0
- unresolved provenance: 15

## Batch 05

- nodes: enumerate-combinations, estimate-sample-size, evaluate-falsifiability, evaluate-optionality, extract-concepts, extract-core-conflict, extract-empirical-regularity, generate-competing-hypotheses, identify-bottleneck, identify-critical-chain
- A/B/C: 0/0/0
- unresolved provenance: 14

## Batch 06

- nodes: identify-scenario-drivers, identify-theory, list-undesirable-effects, map-ablation-components, normalize-gap, operationalize-construct, optimize-design-under-budget, optimize-pareto-frontier, predict-competitive-move, project-future-reality
- A/B/C: 0/0/0
- unresolved provenance: 10

## Batch 07

- nodes: quantify-resource-gap, represent-mechanism-edge, run-convergence-round, scope-domain, select-experimental-baseline, select-from-frontier, select-next-pair, select-statistical-method, specify-boundaries, specify-execution-environment
- A/B/C: 0/0/0
- unresolved provenance: 12

## Batch 08

- nodes: specify-metrics, specify-relationship, specify-reproducibility-protocol, statistical-testing, type-relation, update-confidence-from-evidence, update-pairwise-rating, validate-axis-independence, verify-reproducibility
- A/B/C: 0/0/0
- unresolved provenance: 11

## Final batch correction

- nodes: specify-metrics, specify-relationship, specify-reproducibility-protocol, statistical-testing, type-relation, update-confidence-from-evidence, update-pairwise-rating, validate-axis-independence, verify-reproducibility
- A/B/C: 0/0/0
- unresolved provenance: 11
- total nodes: 79
- total unresolved provenance: 164

R4 delivery complete: all GROUP D bodies and required compilation logs are present under channel/deliverables/R4/nodes.

## Rework batch 01
- ids: analyze-experiment-results, analyze-future-scenarios, build-domain-ontology, construct-argument-map, construct-causal-model, decompose-research-question, falsifiability-audit, formulate-research-question, pairwise-ranking, portfolio-optimization
- A/B/C: 0/0/0 (criteria compiled as substantive gates, no legacy numeric counts)
- provenance: resolved 0 / concept 65 / intermediate 0 (v3 JSON parser rejected malformed source; unresolved entries explicitly retained, no near-name substitution)
- mechanical gates: dedup PASS (distinct protocols); named input PASS; delta subset PASS; provenance pre-check PASS (no false resolved claims)

## Rework batch 02
- ids: structured-consensus, construct-design-matrix, design-randomness-protocol, estimate-sample-size, extract-core-conflict, identify-critical-chain, identify-scenario-drivers, list-undesirable-effects, map-ablation-components, optimize-design-under-budget
- A/B/C: 0/0/0 (criteria compiled as substantive gates, no legacy numeric counts)
- provenance: resolved 0 / concept 15 / intermediate 0
- mechanical gates: dedup PASS; named input PASS; delta subset PASS; provenance pre-check PASS

## Rework batch 03
- ids: predict-competitive-move, project-future-reality, quantify-resource-gap, select-experimental-baseline, select-statistical-method, specify-execution-environment, specify-metrics, specify-reproducibility-protocol, statistical-testing, verify-reproducibility
- A/B/C: 0/0/0 (criteria compiled as substantive gates, no legacy numeric counts)
- provenance: resolved 0 / concept 10 / intermediate 0
- mechanical gates: dedup PASS; named input PASS; delta subset PASS; provenance pre-check PASS

## Rework batch 01 final
- ids: analyze-experiment-results, analyze-future-scenarios, build-domain-ontology, construct-argument-map, construct-causal-model, decompose-research-question, falsifiability-audit, formulate-research-question, pairwise-ranking, portfolio-optimization
- A/B/C: 0/0/0
- provenance: resolved 6 / concept 2 / intermediate 0
- gates: dedup PASS; named inputs PASS; delta subset PASS; provenance pre-check PASS

## Rework batch 02 final
- ids: structured-consensus, construct-design-matrix, design-randomness-protocol, estimate-sample-size, extract-core-conflict, identify-critical-chain, identify-scenario-drivers, list-undesirable-effects, map-ablation-components, optimize-design-under-budget
- A/B/C: 0/0/0
- provenance: resolved 0 / concept 15 / intermediate 0
- gates: dedup PASS; named inputs PASS; delta subset PASS; provenance pre-check PASS

## Rework batch 03 final
- ids: predict-competitive-move, project-future-reality, quantify-resource-gap, select-experimental-baseline, select-statistical-method, specify-execution-environment, specify-metrics, specify-reproducibility-protocol, statistical-testing, verify-reproducibility
- A/B/C: 0/0/0
- provenance: resolved 1 / concept 9 / intermediate 0
- gates: dedup PASS; named inputs PASS; delta subset PASS; provenance pre-check PASS

## Closure audit — 2026-09-12
- graph counts: 51 tactics / 216 SOP; 317 calls; 160 jumps (85 T→T, 75 S→S; no cross-layer edges)
- calls: 317/317 are tactic→SOP; unknown endpoints 0; duplicate edges 0
- jumps: 160/160 are same-layer; unknown endpoints 0; duplicate edges 0
- tactic-origin reachability: 267/267 nodes reachable; isolated nodes 0
- protocol citation gaps (R4 tactic bodies):
  - analyze-future-scenarios: evaluate-compatibility, predict-competitive-move, analyze-temporal-trajectory
  - build-domain-ontology: construct-hierarchy, detect-coverage-gap, canonicalize-entity
  - construct-argument-map: surface-assumptions, score-object, construct-critique
  - construct-causal-model: detect-contradiction, trace-causal-chain, construct-counterfactual, validate-causal-link, update-confidence-from-evidence
  - formulate-research-question: set-threshold
  - pairwise-ranking: aggregate-ranking
  - portfolio-optimization: measure-portfolio-diversity, map-dependencies, sequence-work, evaluate-optionality, evaluate-scenario-robustness
  - complete: analyze-experiment-results, decompose-research-question, falsifiability-audit
- calls present in graph but omitted from these protocols are not explicitly named in their generic Deviation text; report as citation gaps for N2 validator
- cleanup: removed 42 reassigned R4 SOP shells duplicated in R1/R2 (HYPOTHESIS/STRUCTURING/CONVERGENCE); no graph nodes or source files changed
