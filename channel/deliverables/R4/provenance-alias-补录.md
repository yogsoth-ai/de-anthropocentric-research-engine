# provenance alias 补录

重建链：v4 `old` 769 条引用串 → 636 个归一化唯一名 → 494 个真实 v3 节点名 → 未被引用候选 426。按 v3 frontmatter 排除 subagent / import-sop / import/reference 后，本地分类为：subagent 190、import/reference 38、人工判断 198。人工判断中扣除审计列明的 19 个真缺口，得到 **179 条可补录候选**；其中可唯一推导 **106 条**，无法安全推导 **73 条**。审计口径为 205，差异不凑数。

分类规则：`type: subagent` 或 `execution: subagent` → B 类；`type: import-sop`、`execution: import/reference` → A 类；其余 → 人工判断。映射规则：审计七条校准样本使用审计给定落点；其他项只在 v3 图中直接相邻节点已被 v4 `old` 引用、且目标唯一或最高票至少为次高票两倍时补录。否则标记无法推导，不以名称相似猜测。

与审计 205 的差异：审计分类为 169 subagent / 33 import / 224 人工项；本地严格 frontmatter 分类为 190 / 38 / 198，人工池少 26。再扣除 19 个真缺口后，本地候选为 179，而非 205。以下逐条列出本地候选的补录或无法推导状态。

| v3 节点 | v4 节点 | 状态 |
|---|---|---|
| `ablation-brainstorm` | `coverage-white-space-search` | 已补录 |
| `adversarial-persona` | `structured-red-team` | 已补录 |
| `ahrq-picme-assessment` | — | 无法推导 |
| `alternative-analysis` | `structured-red-team` | 已补录 |
| `anti-benchmark` | — | 无法推导 |
| `appropriateness-bounding` | `structured-consensus` | 已补录 |
| `argument-visualization` | `construct-argument-map` | 已补录 |
| `ask-constraints` | — | 无法推导 |
| `ask-intentionality` | — | 无法推导 |
| `axis-extraction` | — | 无法推导 |
| `biological-function-mapping` | `biomimetic-transfer` | 已补录 |
| `biotriz-resolution` | `instantiate-transfer` | 已补录 |
| `blend-construction` | `conceptual-blending` | 已补录 |
| `boundary-analysis` | — | 无法推导 |
| `boundary-enumeration` | `map-validity-envelope` | 已补录 |
| `boundary-probing` | `map-validity-envelope` | 已补录 |
| `boundary-unfolding` | — | 无法推导 |
| `campaign-selection` | — | 无法推导 |
| `challenge-operation` | `identify-dominant-frame` | 已补录 |
| `checkpoint-and-recover` | `analyze-experiment-results` | 已补录 |
| `clarify-resources` | — | 无法推导 |
| `closest-worlds` | `counterfactual-causal-analysis` | 已补录 |
| `coherence-diagnosis` | `pairwise-ranking` | 已补录 |
| `cold-start` | — | 无法推导 |
| `combination-enumeration` | `explore-dimensional-space` | 已补录 |
| `compressed-conflict` | `instantiate-transfer` | 已补录 |
| `concept-blending` | — | 无法推导 |
| `concept-hierarchy` | — | 无法推导 |
| `constraint-driven-ideation` | `problem-reframing` | 已补录 |
| `constraint-elicitation` | — | 无法推导 |
| `constraint-protocol` | `problem-reframing` | 已补录 |
| `convergence-multi-criteria-scoring` | `rank-candidates` | 已补录 |
| `convergence-portfolio-optimization` | `portfolio-optimization` | 已补录 |
| `convergence-scoring-matrix-construction` | `rank-candidates` | 已补录 |
| `counter-thesis-construction` | `adversarial-deliberation` | 已补录 |
| `creative-ideation` | — | 无法推导 |
| `creative-ideation-assumption-enumeration` | `destructive-ideation` | 已补录 |
| `creative-ideation-combination-mapping` | — | 无法推导 |
| `creative-ideation-consistency-checking` | `explore-dimensional-space` | 已补录 |
| `creative-ideation-perspective-rotation` | `problem-reframing` | 已补录 |
| `creative-ideation-provocation-generation` | — | 无法推导 |
| `criteria-interrogation` | `adversarial-deliberation` | 已补录 |
| `critical-path-planning` | — | 无法推导 |
| `de-anthropocentric-research-engine` | — | 无法推导 |
| `deep-insight` | `problem-reframing` | 已补录 |
| `deep-insight-assumption-perturbation` | — | 无法推导 |
| `deep-insight-dialectical-escalation` | — | 无法推导 |
| `deep-insight-failure-mode-cataloging` | `enumerate-dimension-values` | 已补录 |
| `deep-insight-gap-identification` | — | 无法推导 |
| `deep-insight-gap-prioritization` | — | 无法推导 |
| `deep-insight-sensitivity-analysis` | `sensitivity-analysis` | 已补录 |
| `deep-insight-validity-envelope-mapping` | `map-validity-envelope` | 已补录 |
| `design-space-exploration` | — | 无法推导 |
| `design-space-mapping` | `explore-dimensional-space` | 已补录 |
| `dialectical-synthesis` | `map-productive-polarity` | 已补录 |
| `dimension-discovery` | `explore-dimensional-space` | 已补录 |
| `direct-analogy` | `instantiate-transfer` | 已补录 |
| `domain-divergence` | `analogical-discovery` | 已补录 |
| `ecosystem-pattern` | `instantiate-transfer` | 已补录 |
| `emergence-detection` | `conceptual-blending` | 已补录 |
| `evaluation-filtering` | — | 无法推导 |
| `evidence-mapping` | — | 无法推导 |
| `evidence-tournament` | `adversarial-deliberation` | 已补录 |
| `excursion-method` | `instantiate-transfer` | 已补录 |
| `excursion-orchestration` | `instantiate-transfer` | 已补录 |
| `executing-specs` | — | 无法推导 |
| `experiment-execution-bottleneck-identification` | `analyze-constraints-readiness` | 已补录 |
| `experiment-execution-factor-level-design` | `design-experiment` | 已补录 |
| `experiment-running` | `analyze-experiment-results` | 已补录 |
| `explanation-generation` | `formulate-hypotheses` | 已补录 |
| `explore-resume` | — | 无法推导 |
| `facet-bisociation` | `analogical-discovery` | 已补录 |
| `factor-removal` | `counterfactual-causal-analysis` | 已补录 |
| `factorial-ideation` | `coverage-white-space-search` | 已补录 |
| `failure-mode-analysis` | `enumerate-dimension-values` | 已补录 |
| `failure-taxonomy` | `coverage-white-space-search` | 已补录 |
| `fantasy-analogy` | `instantiate-transfer` | 已补录 |
| `final-validation` | — | 无法推导 |
| `forced-bridge-construction` | `analogical-discovery` | 已补录 |
| `gap-analysis` | — | 无法推导 |
| `gap-driven-generation` | `coverage-white-space-search` | 已补录 |
| `gap-synthesis-strategy` | — | 无法推导 |
| `groupthink-mitigation` | `structured-red-team` | 已补录 |
| `hierarchy-visualization` | `build-domain-ontology` | 已补录 |
| `hot-start` | — | 无法推导 |
| `hypothesis-formation-gap-prioritization` | `rank-candidates` | 已补录 |
| `hypothesis-formation-novelty-scoring` | `score-object` | 已补录 |
| `hypothesis-formation-portfolio-optimization` | — | 无法推导 |
| `hypothesis-formation-quality-gate-check` | — | 无法推导 |
| `hypothesis-formation-saturation-detection` | `assess-evidence-saturation` | 已补录 |
| `hypothesis-formation-scoring-matrix-construction` | — | 无法推导 |
| `hypothesis-formation-variable-identification` | `formulate-hypotheses` | 已补录 |
| `hypothesis-synthesis` | `formulate-hypotheses` | 已补录 |
| `implementation-planning` | `analyze-experiment-results` | 已补录 |
| `insight` | — | 无法推导 |
| `inversion-protocol` | `destructive-ideation` | 已补录 |
| `knowledge-acquisition` | — | 无法推导 |
| `knowledge-acquisition-claim-decomposition` | — | 无法推导 |
| `knowledge-structuring-claim-decomposition` | `construct-argument-map` | 已补录 |
| `knowledge-structuring-combination-mapping` | `explore-dimensional-space` | 已补录 |
| `knowledge-structuring-consistency-checking` | `build-domain-ontology` | 已补录 |
| `knowledge-structuring-gap-prioritization` | `rank-candidates` | 已补录 |
| `knowledge-structuring-novelty-scoring` | `explore-dimensional-space` | 已补录 |
| `knowledge-structuring-variable-identification` | `construct-causal-model` | 已补录 |
| `lakatos-heuristics` | — | 无法推导 |
| `lateral-escape` | — | 无法推导 |
| `lateral-thinking` | — | 无法推导 |
| `life-principles-application` | — | 无法推导 |
| `literature-overview` | — | 无法推导 |
| `literature-research` | — | 无法推导 |
| `literature-search` | — | 无法推导 |
| `loop-documentation` | `detect-feedback-loop` | 已补录 |
| `matrix-export` | `explore-dimensional-space` | 已补录 |
| `mechanism-gap-hunting` | `drill-root-causes` | 已补录 |
| `method-problem-matrix` | `coverage-white-space-search` | 已补录 |
| `multi-judge-aggregation` | — | 无法推导 |
| `multi-level-bisociation` | `abstract-structure` | 已补录 |
| `multi-method-triangulation` | — | 无法推导 |
| `multi-perspective-panel` | — | 无法推导 |
| `narrative-framing` | — | 无法推导 |
| `narrative-review` | `synthesize-literature-evidence` | 已补录 |
| `north-star-crystallization` | — | 无法推导 |
| `north-star-synthesis` | `crystallize-north-star` | 已补录 |
| `ontology-export` | `build-domain-ontology` | 已补录 |
| `pairwise-comparison` | — | 无法推导 |
| `parameter-variation` | — | 无法推导 |
| `plan-writing` | — | 无法推导 |
| `plausibility-ranking` | `formulate-hypotheses` | 已补录 |
| `premortem-to-fmea-pipeline` | `score-fmea-risk` | 已补录 |
| `prerequisite-planning` | `identify-obstacles` | 已补录 |
| `prioritization-scoring` | — | 无法推导 |
| `prospective-hindsight` | `fmea-risk-analysis` | 已补录 |
| `question-generation` | `explore-dimensional-space` | 已补录 |
| `question-synthesis` | `formulate-research-question` | 已补录 |
| `random-entry` | `extract-constructive-movement` | 已补录 |
| `random-stimulus-entry` | `analogical-discovery` | 已补录 |
| `recombination-architecture` | `structural-transformation` | 已补录 |
| `reverse-brainstorming` | `destructive-ideation` | 已补录 |
| `role-based-ideation` | `problem-reframing` | 已补录 |
| `sacred-cow-hunting` | — | 无法推导 |
| `scope-clarification` | — | 无法推导 |
| `score-trajectory-analysis` | `audit-benchmark-validity` | 已补录 |
| `screening-then-scoring` | `rank-candidates` | 已补录 |
| `seed-concept-search` | — | 无法推导 |
| `six-hats-ideation` | `extract-constructive-movement` | 已补录 |
| `six-hats-rotation` | `problem-reframing` | 已补录 |
| `snowball` | `synthesize-literature-evidence` | 已补录 |
| `society-of-mind` | — | 无法推导 |
| `source-gathering` | `build-domain-ontology` | 已补录 |
| `spawn-agent` | — | 无法推导 |
| `stakeholder-simulation` | `problem-reframing` | 已补录 |
| `stress-test-assumption-challenge` | `structured-red-team` | 已补录 |
| `stress-test-dialectical-escalation` | `adversarial-deliberation` | 已补录 |
| `stress-test-perspective-rotation` | — | 无法推导 |
| `stress-test-validity-envelope-mapping` | `map-validity-envelope` | 已补录 |
| `subagent-execution-loop` | `analyze-experiment-results` | 已补录 |
| `success-criteria-definition` | `formulate-research-question` | 已补录 |
| `symbolic-analogy` | `instantiate-transfer` | 已补录 |
| `synectics` | — | 无法推导 |
| `synthesis-report` | `construct-argument-map` | 已补录 |
| `task-decomposition` | — | 无法推导 |
| `temporal-projection` | `problem-reframing` | 已补录 |
| `thought-experiment` | `counterfactual-causal-analysis` | 已补录 |
| `threshold-calibration` | `calibrate-probability-forecast` | 已补录 |
| `triz-contradiction-resolution` | — | 无法推导 |
| `validation-report` | `construct-causal-model` | 已补录 |
| `warm-start` | — | 无法推导 |
| `web-research` | — | 无法推导 |
| `web-search` | — | 无法推导 |
| `wiki-add-edge` | — | 无法推导 |
| `wiki-compile-page` | — | 无法推导 |
| `wiki-edge-audit` | — | 无法推导 |
| `wiki-graph-query` | — | 无法推导 |
| `wiki-ingest-source` | — | 无法推导 |
| `wiki-lint-fix` | — | 无法推导 |
| `wiki-search` | — | 无法推导 |
| `worst-method-inversion` | `destructive-ideation` | 已补录 |
| `writing-specs` | — | 无法推导 |
| `zwicky-box-construction` | `explore-dimensional-space` | 已补录 |

审计七条校准样本均已纳入：`hypothesis-formation-novelty-scoring`→`score-object`、`deep-insight-validity-envelope-mapping`→`map-validity-envelope`、`knowledge-structuring-gap-prioritization`→`rank-candidates`、`six-hats-rotation`/`role-based-ideation`→`problem-reframing`、`zwicky-box-construction`/`design-space-mapping`→`explore-dimensional-space`。

## 86 条旧账复核（2026-09-13）

检索口径：对每条旧名先剥除括号中的 `[sop]`、`[strategy]`、`[tactic]`、`[campaign]` 等后缀，再依次检索裸名、包名-裸名、包名/裸名三种形式；随后以架构 JSON 的 `old` 与 `capability_audit` 交叉核对落点。命中 v3 源名只证明 provenance 存在，不自动证明 v4 映射唯一。

### Alias 73 条

以下 4 条为当初漏查，改为 resolved；行号为 `scripts/refactory_source.json` 的 `name` 行，落点来自架构 `capability_audit`：

| v3 源名 | v4 落点 | v3 行 | 判定 |
|---|---|---:|---|
| `anti-benchmark` | `audit-benchmark-validity` → `destructive-ideation` → `coverage-white-space-search` | 991 | resolved |
| `seed-concept-search` | `extract-concepts` | 5177 | resolved |
| `synectics` | `analogical-discovery` + `conceptual-blending` + `problem-reframing(mode=perspective-shift)` | 2104 | resolved |
| `web-search` | `map-research-landscape`（由 broad/deep web-search import 覆盖） | 60 | resolved |

其余 69 条均保留「无法推导」。三种形式均能命中相应 v3 源名及行号，但 `old`/`capability_audit` 没有给出唯一 v4 落点；近似名、同包节点或泛化能力路径不能代替映射。逐条名单如下：

`ahrq-picme-assessment`(3924)、`ask-constraints`(5485)、`ask-intentionality`(5492)、`axis-extraction`(5100)、`boundary-analysis`(2258)、`boundary-unfolding`(2482)、`campaign-selection`(3056)、`clarify-resources`(5478)、`cold-start`(5408)、`concept-blending`(1215)、`concept-hierarchy`(1236)、`constraint-elicitation`(3063)、`creative-ideation`(914)、`creative-ideation-combination-mapping`(1166)、`creative-ideation-provocation-generation`(1901)、`critical-path-planning`(3210)、`de-anthropocentric-research-engine`(3021)、`deep-insight-assumption-perturbation`(2531)、`deep-insight-dialectical-escalation`(2559)、`deep-insight-gap-identification`(2279)、`deep-insight-gap-prioritization`(2300)、`design-space-exploration`(1355)、`evaluation-filtering`(1467)、`evidence-mapping`(2454)、`executing-specs`(3035)、`explore-resume`(5471)、`final-validation`(5541)、`gap-analysis`(2244)、`gap-synthesis-strategy`(2307)、`hot-start`(5422)、`hypothesis-formation-portfolio-optimization`(3735)、`hypothesis-formation-quality-gate-check`(3966)、`hypothesis-formation-scoring-matrix-construction`(3819)、`insight`(2251)、`knowledge-acquisition`(4197)、`knowledge-acquisition-claim-decomposition`(4456)、`lakatos-heuristics`(5814)、`lateral-escape`(2545)、`lateral-thinking`(1705)、`life-principles-application`(1712)、`literature-overview`(32)、`literature-research`(46)、`literature-search`(39)、`multi-judge-aggregation`(354)、`multi-method-triangulation`(333)、`multi-perspective-panel`(5674)、`narrative-framing`(4288)、`north-star-crystallization`(5401)、`pairwise-comparison`(3826)、`parameter-variation`(1824)、`plan-writing`(3224)、`prioritization-scoring`(2468)、`sacred-cow-hunting`(1978)、`scope-clarification`(3049)、`society-of-mind`(5681)、`spawn-agent`(53)、`stress-test-perspective-rotation`(5849)、`task-decomposition`(3308)、`triz-contradiction-resolution`(2160)、`warm-start`(5415)、`web-research`(67)、`wiki-add-edge`(5142)、`wiki-compile-page`(5156)、`wiki-edge-audit`(5170)、`wiki-graph-query`(5135)、`wiki-ingest-source`(5149)、`wiki-lint-fix`(5163)、`wiki-search`(5128)、`writing-specs`(3028)。

说明：这里的「无法推导」不是「v3 节点不存在」。上述 69 条均有 v3 源命中；无法推导的是从该源节点到 v4 的唯一归属。`cold-start`、`hot-start`、`warm-start` 仅在架构中形成 entry-depth policy，非单一节点；`insight`、`creative-ideation` 等为泛化能力或多路径集合，也不强行归一。

### Phantom mode 19 个 claims（原表 11 行，按实际 mode 展开）

架构 description、`modes`、`capability_audit` 现已提供明确迁移证据的条目改为 resolved：

| Contract | mode | v3 源名（行） | v4 落点 | 判定 |
|---|---|---|---|---|
| C015 | `competing` | `competing-hypothesis-construction` (3770) | `formulate-hypotheses(mode=competing-hypotheses)` | resolved |
| C019 | `scoping` / `systematic` / `deep` / `narrative` / `snowball` | `scoping-survey` (4239); `systematic-survey` (4246); `deep-survey` (4253); `narrative-review` (4260); `snowball` (4267) | `synthesize-literature-evidence(mode=...)` | resolved |
| C029 | `pairwise` / `network` | `pairwise-synthesis` (4652); `network-comparison` (4659) | `synthesize-meta-analytic-evidence(mode=...)` | resolved |
| C063 | `premortem-seeded` | `premortem-to-fmea-pipeline` (5884) | `fmea-risk-analysis(mode=premortem-seeded)` | resolved |
| C079 | `regret` | `robustness-under-uncertainty` (284) | `evaluate-scenario-robustness(mode=regret)` | resolved |
| C086 | `factorial` / `ablation` / `comparison` / `scaling` / `robustness` | `experiment-execution-factor-level-design` (3105); `ablation-design` (3112); `comparison-design` (3119); `scaling-design` (3126); `robustness-design` (3133) | `design-experiment(mode=...)` | resolved |
| C096 | `comparative` | `comparative-formulation` (3805) | `formulate-research-question(mode=comparative)` | resolved |
| C121 | `worst-case` | `worst-case-construction` (3518) | `construct-scenario(mode=worst-case)` | resolved |
| C139 | `direct` / `forced-bridge` / `design-transfer` | `direct-analogy` (1383); `forced-bridge-construction` (1572); `design-by-analogy` (1348) | `analogical-discovery(mode=direct|forced-bridge|design-transfer)` | resolved |
| C140 | `ecosystem` | `ecosystem-pattern` (1411) | `biomimetic-transfer(mode=ecosystem)`（capability audit 明确给出） | resolved（不改变 graph modes 字段判定） |
| C141 | `random-entry` | `random-entry` (1908) | `generate-provocation(mode=random-entry)` | resolved（不改变 graph modes 字段判定） |
| C143 | `combine` / `trim` / `redistribute` | `function-combination` (1593); `function-trimming` (1614); `function-redistribution` (1607) | `structural-transformation(mode=combine|trim|redistribute)` | resolved |
| C039–C041 | Morris / Sobol / perturbation / Monte-Carlo 组 | `parameter-screening` (2384); `variance-decomposition` (2391); `systematic-perturbation` (2510); `uncertainty-propagation` (2405)；corroborating SOP：`morris-screening` (2853)、`sobol-decomposition` (2860)、`controlled-perturbation` (2811)、`monte-carlo-sampling` (2909) | `sensitivity-analysis(mode=...)` | resolved |

仍为真正无法推导的 5 项：

| Contract | 保留原因 |
|---|---|
| C038 | `systematic`、`boundary` 不是 v3 精确节点名；只能找到 `systematic-perturbation`、`boundary-probing`，不能把近似名当作精确 mode provenance。 |
| C052 | `transformation operator` 是泛化描述；v3 `scamper-transformation` 是独立 strategy，不是可唯一继承的 mode。 |
| C069 | `boundary` 缺少精确 token；`boundary-probing` 为独立 tactic，不能直接替代 `critical-case` 或 `boundary-value-stress`。 |
| C087 | `resource`、`causal` 只能分别关联多个约束/资源节点，未形成唯一 v4 mode 来源。 |
| C102 | `generative-question` 仅由 capability audit 作为 inline output contract 记录，v3 未找到对应 How-Might-We 节点；不能伪造 v3 源名。 |

复核计数：alias 73 条中 resolved 4、仍无法推导 69。phantom 文件中原标为「无法推导」的 12 行（C019 为省略项，按实际 mode 展开）均已由现有架构 description / `capability_audit` 找到明确 provenance；另列的 C038、C052、C069、C087、C102 是原记录中的「不改/不确定」项，仍不提升为 resolved。所有保留项均明确区分“v3 源名命中”与“v4 映射不可唯一确定”，没有把查不到映射写成 v3 节点不存在。
