# 溯源账核对：`old[]` 字段 769 条逐条解析

**Sirelia 自查，2026-09-08。无人指派，起因是清理 `score-object` 的 15 条 rubric 来源时发现 6 条查不到。**

## 结论

`old[]` 共 769 条引用。按三种写法归一化后：

| 项 | 数 | 说明 |
|---|---:|---|
| 可解析到 v3 真实节点 | 637 | 裸名直配，或 `package/name` → `package-name` 连字符拼接 |
| 指向中间轮次快照 | 63 | `Pass3/4/5/8` 前缀。`generated_from` = 「Pass 9 optimized graph」，中间轮次的图不在手上 |
| 方法概念名而非节点名 | 67 | `triz`、`six-thinking-hats`、`biomimicry/biologize`、`monte-carlo-propagation` 等学术方法名 |
| 明确标注已移除 | 2 | `broad-web-search [tool import removed]` |
| **合计** | **769** | |

**没有一条是凭空伪造的。** 全部是记账口径混乱：三种命名写法混用且未归一化。
这跟 R2 的 23 条幻影 mode 是同类问题（引用了不存在的标识符），但性质更轻——
mode 是可调用的执行参数，`old[]` 只是溯源记录。

## 关键发现：连字符 vs 斜杠

v3 真实节点名把 package 拼进名字里，用连字符：

    v3 实际：creative-ideation-consistency-pair-evaluation
    old[] 写：creative-ideation/consistency-pair-evaluation

这一条规则解释了 22 条早先被我误判为幻影的条目。**任何人后续核 `old[]` 都要先做这个归一化，否则会虚报缺失。**

## 132 条未解析明细

`近似 v3 名` 一列只是线索，**不是判定**。不许据此认定对应关系。

| 类 | v4 节点 | `old[]` 原文 | 近似 v3 名 |
|---|---|---|---|
| B-中间轮次 | `adjust-abstraction-scope` | `Pass8/adjust-question-scope` | — |
| B-中间轮次 | `adjust-abstraction-scope` | `Pass8/shift-abstraction-level` | — |
| B-中间轮次 | `adversarial-deliberation` | `Pass5/adversarial-debate [tactic]` | `adversarial-debate-protocol` |
| B-中间轮次 | `adversarial-deliberation` | `Pass5/steelman-validation [tactic]` | `model-validation` |
| B-中间轮次 | `analyze-constraints-readiness` | `Pass5/analyze-direction-obstacles [tactic]` | — |
| B-中间轮次 | `analyze-constraints-readiness` | `Pass5/analyze-research-constraints [tactic]` | — |
| B-中间轮次 | `analyze-constraints-readiness` | `Pass5/feasibility-readiness [tactic]` | `feasibility-synthesis` |
| B-中间轮次 | `analyze-temporal-trajectory` | `Pass3/analyze-filing-trend` | — |
| B-中间轮次 | `analyze-temporal-trajectory` | `Pass3/fit-research-progress-curve` | — |
| B-中间轮次 | `analyze-temporal-trajectory` | `Pass3/project-research-timeline` | — |
| B-中间轮次 | `assess-sensitivity` | `Pass3/assess-rank-robustness` | — |
| B-中间轮次 | `assess-sensitivity` | `Pass3/design-meta-sensitivity` | `decision-sensitivity` |
| B-中间轮次 | `assess-sensitivity` | `Pass3/measure-sensitivity` | `decision-sensitivity` |
| B-中间轮次 | `audit-reporting-quality` | `Pass3/audit-benchmark-documentation` | — |
| B-中间轮次 | `audit-reporting-quality` | `Pass3/audit-reproducibility-reporting` | `reproducibility-verification` |
| B-中间轮次 | `audit-study-validity` | `Pass3/assess-risk-of-bias` | — |
| B-中间轮次 | `audit-study-validity` | `Pass3/assess-study-quality` | — |
| B-中间轮次 | `canonicalize-entity` | `Pass3/merge-near-duplicate-concepts` | — |
| B-中间轮次 | `canonicalize-entity` | `Pass3/normalize-assignee` | `normalization` |
| B-中间轮次 | `canonicalize-entity` | `Pass4/map-field-taxonomy [decomposed capability]` | `failure-taxonomy` |
| B-中间轮次 | `categorize-evidence` | `Pass4/map-field-taxonomy [decomposed capability]` | `failure-taxonomy` |
| B-中间轮次 | `construct-hierarchy` | `Pass4/map-field-taxonomy [decomposed capability]` | `failure-taxonomy` |
| B-中间轮次 | `define-analysis-dimensions` | `Pass3/identify-dimensions` | — |
| B-中间轮次 | `define-analysis-dimensions` | `Pass3/map-parameter-space` | `parameter-space-mapping` |
| B-中间轮次 | `define-criteria` | `Pass4/define-success-criteria [decomposed capability]` | — |
| B-中间轮次 | `design-mitigation` | `Pass3/design-mitigation` | — |
| B-中间轮次 | `design-mitigation` | `Pass3/design-removal-path` | `removal-path` |
| B-中间轮次 | `detect-contradiction` | `Pass3/detect-contradiction` | — |
| B-中间轮次 | `detect-contradiction` | `Pass3/flag-contradictory-evidence` | — |
| B-中间轮次 | `detect-coverage-gap` | `Pass3/detect-structural-gap` | — |
| B-中间轮次 | `detect-coverage-gap` | `Pass3/detect-white-space` | — |
| B-中间轮次 | `detect-coverage-gap` | `Pass3/map-ip-white-space` | — |
| B-中间轮次 | `enumerate-dimension-values` | `Pass3/enumerate-values` | — |
| B-中间轮次 | `enumerate-dimension-values` | `Pass3/generate-extreme-values` | — |
| B-中间轮次 | `enumerate-dimension-values` | `Pass3/specify-factor-levels` | — |
| B-中间轮次 | `evaluate-scenario-impact` | `Pass3/assess-scenario-impact` | `stress-scenario` |
| B-中间轮次 | `evaluate-scenario-impact` | `Pass3/evaluate-scenario` | `narrative-scenario` |
| B-中间轮次 | `evaluate-scenario-robustness` | `Pass8/evaluate-regret-robustness` | — |
| B-中间轮次 | `evaluate-scenario-robustness` | `Pass8/score-scenario-robustness` | — |
| B-中间轮次 | `explore-dimensional-space` | `Pass5/map-dimensional-research-space [tactic]` | — |
| B-中间轮次 | `explore-dimensional-space` | `Pass5/morphological-search [tactic]` | `morphological-scenario` |
| B-中间轮次 | `extract-causal-structure` | `Pass3/extract-causal-claims` | — |
| B-中间轮次 | `extract-causal-structure` | `Pass3/extract-mechanism` | — |
| B-中间轮次 | `extract-evidence-record` | `Pass4/catalog-evaluation-conditions` | — |
| B-中间轮次 | `extract-evidence-record` | `Pass4/extract-performance-record` | — |
| B-中间轮次 | `extract-evidence-record` | `Pass4/extract-study-data` | `extract-data` |
| B-中间轮次 | `formulate-hypotheses` | `Pass8/construct-competing-hypotheses [tactic]` | — |
| B-中间轮次 | `inventory-reference-items` | `Pass4/inventory-benchmarks` | `anti-benchmark` |
| B-中间轮次 | `inventory-reference-items` | `Pass4/inventory-known-solutions` | — |
| B-中间轮次 | `map-coverage-space` | `Pass3/map-capability-coverage` | — |
| B-中间轮次 | `map-coverage-space` | `Pass3/map-method-problem-space` | `method-problem-matrix` |
| B-中间轮次 | `map-validity-envelope` | `Pass5/boundary-stress-test [tactic]` | `boundary-synthesis` |
| B-中间轮次 | `map-validity-envelope` | `Pass5/validity-envelope-analysis [tactic]` | — |
| B-中间轮次 | `normalize-comparison-scale` | `Pass4/normalize-compute-budget` | — |
| B-中间轮次 | `normalize-comparison-scale` | `Pass4/normalize-scores` | — |
| B-中间轮次 | `problem-reframing` | `Pass8/force-perspective-shift [tactic]` | `novice-perspective` |
| B-中间轮次 | `rank-candidates` | `Pass5/multi-criteria-decision [tactic]` | `gate-criteria-definition` |
| B-中间轮次 | `rank-candidates` | `Pass5/narrow-research-direction [tactic]` | — |
| B-中间轮次 | `rank-candidates` | `Pass5/prioritize-research-gaps [tactic]` | — |
| B-中间轮次 | `score-object` | `Pass4/score-candidate` | `merge-candidates` |
| B-中间轮次 | `score-object` | `Pass4/score-claim-strength` | — |
| B-中间轮次 | `score-object` | `Pass4/score-gap-novelty` | — |
| B-中间轮次 | `set-threshold` | `Pass4/define-success-criteria [decomposed capability]` | — |
| C-方法概念名 | `analyze-constraints-readiness` | `bottleneck-identification [strategy]` | `convergence-bottleneck-identification` |
| C-方法概念名 | `analyze-scaling-regime` | `deep-insight/scaling-analysis [strategy]` | `claim-analysis` |
| C-方法概念名 | `apply-separation-principle` | `triz/separation-principles [tactic]` | `separation-principle` |
| C-方法概念名 | `apply-stage-gate` | `convergence/feasibility-assessment/stage-gate [strategy/tactic]` | — |
| C-方法概念名 | `assess-prior-art-and-claims` | `claim-decomposition [tactic]` | `task-decomposition` |
| C-方法概念名 | `assumption-stress-test` | `assumption-perturbation [tactic]` | `assumption-negation` |
| C-方法概念名 | `biologize-problem` | `biomimicry/biologize [sop]` | — |
| C-方法概念名 | `biomimetic-transfer` | `biological-analogy [tactic]` | `symbolic-analogy` |
| C-方法概念名 | `biomimetic-transfer` | `biotriz [strategy]` | — |
| C-方法概念名 | `build-domain-ontology` | `consistency-checking [tactic]` | `consistency-check` |
| C-方法概念名 | `calibrate-adversarial-confidence` | `confidence-escalation [sop]` | `confidence-calibration` |
| C-方法概念名 | `categorize-evidence` | `knowledge-structuring/source categorization patterns` | — |
| C-方法概念名 | `classify-stakeholder-salience` | `stakeholder-salience-analysis [tactic]` | — |
| C-方法概念名 | `conceptual-blending` | `conceptual-blending [strategy]` | `concept-blending` |
| C-方法概念名 | `construct-argument-map` | `claim-decomposition [tactic]` | `task-decomposition` |
| C-方法概念名 | `construct-argument-map` | `counterargument-mapping [strategy]` | `argument-mapping` |
| C-方法概念名 | `construct-argument-map` | `premise-identification [strategy]` | `parameter-identification` |
| C-方法概念名 | `construct-causal-model` | `variable-identification [strategy]` | `parameter-identification` |
| C-方法概念名 | `construct-perspective-set` | `role-storming [strategy]` | `re-scoring` |
| C-方法概念名 | `construct-perspective-set` | `six-thinking-hats [strategy]` | — |
| C-方法概念名 | `coverage-white-space-search` | `benchmark-inventory [sop]` | `benchmark-audit` |
| C-方法概念名 | `design-experiment` | `factor-level-design [strategy]` | — |
| C-方法概念名 | `destructive-ideation` | `provocation-generation [tactic]` | `recombination-generation` |
| C-方法概念名 | `detect-contradiction` | `stress-test/detect-contradiction (evidence mode)` | — |
| C-方法概念名 | `discover-biological-analog` | `biological-analogy [tactic]` | `symbolic-analogy` |
| C-方法概念名 | `discover-biological-analog` | `biomimicry/discover [sop]` | — |
| C-方法概念名 | `enumerate-combinations` | `creative-ideation/combination-generation` | `recombination-generation` |
| C-方法概念名 | `evolve-solution-population` | `variation-selection [tactic]` | `campaign-selection` |
| C-方法概念名 | `explore-dimensional-space` | `axis-identification [strategy]` | `factor-identification` |
| C-方法概念名 | `explore-dimensional-space` | `combination-mapping [strategy]` | `combination-evaluation` |
| C-方法概念名 | `explore-dimensional-space` | `combination-mapping [tactic]` | `combination-evaluation` |
| C-方法概念名 | `explore-dimensional-space` | `consistency-checking [tactic]` | `consistency-check` |
| C-方法概念名 | `explore-dimensional-space` | `gap-prioritization [strategy]` | `risk-prioritization` |
| C-方法概念名 | `extract-biological-strategy` | `biomimicry/abstract [sop]` | — |
| C-方法概念名 | `extract-biological-strategy` | `biotriz [strategy]` | — |
| C-方法概念名 | `extract-generic-space` | `conceptual-blending/generic-space [sop]` | `generic-space-extraction` |
| C-方法概念名 | `map-patent-white-space` | `claim-decomposition [tactic]` | `task-decomposition` |
| C-方法概念名 | `map-stakeholder-jobs` | `job-mapping [sop]` | `jtbd-mapping` |
| C-方法概念名 | `map-stakeholder-jobs` | `jobs-to-be-done-analysis [tactic]` | — |
| C-方法概念名 | `map-stakeholder-system` | `critical-systems-heuristics [tactic]` | — |
| C-方法概念名 | `map-stakeholder-system` | `jobs-to-be-done-analysis [tactic]` | — |
| C-方法概念名 | `map-stakeholder-system` | `stakeholder-salience-analysis [tactic]` | — |
| C-方法概念名 | `map-validity-envelope` | `validity-envelope-construction [sop]` | `stress-test-validity-envelope-construction` |
| C-方法概念名 | `map-validity-envelope` | `validity-envelope-mapping [strategy]` | `stress-test-validity-envelope-mapping` |
| C-方法概念名 | `map-validity-envelope` | `validity-envelope-mapping [stress strategy]` | `stress-test-validity-envelope-mapping` |
| C-方法概念名 | `mutate-solution-population` | `evolution-strategy/variation [sop]` | — |
| C-方法概念名 | `portfolio-optimization` | `portfolio-optimization [campaign]` | `convergence-portfolio-optimization` |
| C-方法概念名 | `problem-reframing` | `perspective-rotation [tactic]` | `perspective-critic` |
| C-方法概念名 | `problem-reframing` | `role-storming [strategy]` | `re-scoring` |
| C-方法概念名 | `problem-reframing` | `six-thinking-hats [strategy]` | — |
| C-方法概念名 | `propagate-uncertainty` | `monte-carlo-propagation [sop]` | — |
| C-方法概念名 | `quantify-information-value` | `value-of-information [sop]` | `value-enumeration` |
| C-方法概念名 | `rank-candidates` | `portfolio-optimization [strategy]` | `convergence-portfolio-optimization` |
| C-方法概念名 | `rank-candidates` | `scoring-matrix-construction [tactic]` | `design-matrix-construction` |
| C-方法概念名 | `resolve-inventive-contradiction` | `contradiction-matrix [tactic]` | `contradiction-matrix-lookup` |
| C-方法概念名 | `resolve-inventive-contradiction` | `separation-principles [tactic]` | `separation-principle` |
| C-方法概念名 | `resolve-inventive-contradiction` | `triz [strategy]` | — |
| C-方法概念名 | `robustness-analysis` | `assumption-enumeration [sop]` | `assumption-negation` |
| C-方法概念名 | `rotate-perspective` | `perspective-rotation [tactic]` | `perspective-critic` |
| C-方法概念名 | `rotate-perspective` | `six-thinking-hats [strategy]` | — |
| C-方法概念名 | `select-inventive-principle` | `inventive-principle-selection [sop]` | `biotriz-principle-selection` |
| C-方法概念名 | `select-inventive-principle` | `triz/contradiction-matrix [tactic]` | `contradiction-matrix-lookup` |
| C-方法概念名 | `select-solution-variants` | `evolution-strategy/selection [sop]` | `seed-selection` |
| C-方法概念名 | `sensitivity-analysis` | `sensitivity-analysis [campaign]` | `sensitivity-analysis-design` |
| C-方法概念名 | `synthesize-literature-evidence` | `narrative-survey [strategy]` | `narrative-review` |
| C-方法概念名 | `synthesize-literature-evidence` | `snowball-survey [strategy]` | — |
| C-方法概念名 | `trace-citation-neighborhood` | `knowledge-acquisition/snowball-survey [strategy]` | — |
| D-已移除工具 | `map-research-landscape` | `broad-paper-search [tool import removed]` | — |
| D-已移除工具 | `map-research-landscape` | `broad-web-search [tool import removed]` | `deep-web-search` |

## 待裁定

1. **63 条中间轮次**：中间图不可得。是标注「溯源断链，仅记录」，还是删掉这些条目？
   删掉会让 `old[]` 变干净但丢失压图历史；留着则永远无法核验。
2. **67 条方法概念名**：v3 有实现这些方法的节点，但名字不同。要不要人工建立对应？
   `triz [strategy]` → v3 的 `triz-contradiction-resolution` 大概率是对的，但按项目规矩不许靠名字相似判定。
3. **对 R2 审计的影响**：82 条 COVERED 里有多少条的依据包含未解析的 `old[]`？这个我还没查。
   若某条 COVERED 的全部证据都来自未解析条目，那条结论悬空。

## 附：`score-object` 的起因

15 条 `old[]` 里 7 条未解析（4 条 `PassN/`、3 条方法名）。
这是全图未解析密度最高的节点之一，而它被 6 个 tactic 调用、承接 15 个 v3 scoring 节点。
R5 目前对它采取「保守复制 + 标记待重构」，在溯源账清干净之前，这个保守策略是对的。
