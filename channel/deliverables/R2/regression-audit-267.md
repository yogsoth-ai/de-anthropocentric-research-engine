# R2 回归审计：267 份正文

审计对象：architecture JSON 中 51 tactic + 216 SOP。canonical 选择按当前分派优先取 R1/R2/R3/R5，R4 仅取未转派节点；R4 下已转派的 42 个旧副本不重复计入。

## 结论

本轮不能签发全量通过。发现的硬问题：

| 门 | 结果 | 证据 |
|---|---:|---|
| 1. 同组 Procedure/Execution protocol 不得完全相同 | FAIL | 4 组重复：`falsifiability-audit` = `decompose-research-question`；`pairwise-ranking` = `portfolio-optimization`；`build-domain-ontology` = `construct-causal-model`；BASIS 组 7 节点共用同一模板步骤。 |
| 2. required 不得使用占位符 | FAIL | 7 节点：`elicit-weights`、`detect-breakpoint`、`construct-validity-envelope`、`construct-defense`、`adjudicate-exchange`、`enumerate-combinations`、`identify-bottleneck`；均为 `required: [source_state, task_object]`。 |
| 3. delta_fields 子集且与 produces 对应 | FAIL | 上述 7 节点均全量列出八字段，未做节点级选择；其余节点未见非法字段名，但需由 N2 复跑 produces 对应性。 |
| 4. concept 前三种检索 | UNCERTAIN | 112 条 `concept` provenance 在正文/编译记录中未附裸名、`package-name`、`package/name` 三次检索证据。未把“查不到”推断为错误；要求补证据或改为真实 resolved。 |
| 5. 小节内重复句式不得三次以上 | FAIL | 5 节点：`pairwise-ranking`（3 次）、`portfolio-optimization`（3 次）、`build-domain-ontology`（4 次）、`construct-causal-model`（4 次）、`analyze-future-scenarios`（3 次）。重复句：`Transform the current artifact while preserving its provenance and uncertainty.` |

## 覆盖缺口

以下 16 个 architecture 节点没有当前分派目录中的 canonical `body.md`，不能宣称已审：

`structured-consensus`, `generate-subquestions`, `sequence-work`, `verify-evidence-independence`, `derive-consequences`, `generate-provocation`, `identify-obstacles`, `trace-causal-chain`, `design-mitigation`, `evaluate-scenario-impact`, `map-coverage-space`, `normalize-comparison-scale`, `measure-portfolio-diversity`, `construct-perspective-set`, `rotate-perspective`, `evaluate-scenario-robustness`。

## R4 → N1 的 30 节点返工清单

这 30 个仍是 R4 旧正文；按 N1 的职责直接退回重写，不把它们的形式合规当作内容通过。

### 11 tactic

| 节点 | 机械证据 | 判定 |
|---|---|---|
| `analyze-experiment-results` | `Execution protocol` 仅 2 步；仅冻结输入、整合结果，无结果分析分支与可证伪检查 | REWORK |
| `analyze-future-scenarios` | 步骤 2/3 使用同一句通用句；第 57 行起可见重复骨架 | REWORK；G5 |
| `build-domain-ontology` | 步骤 2–5 同一句通用句，出现 4 次 | REWORK；G5 |
| `construct-argument-map` | 步骤均为通用冻结/转换/整合句，未展开 claim/evidence/counterclaim 逻辑 | REWORK |
| `construct-causal-model` | 步骤 2–5 同一句通用句，出现 4 次 | REWORK；G5 |
| `decompose-research-question` | 与 `falsifiability-audit` 的三步 protocol 完全相同 | REWORK；G1 |
| `falsifiability-audit` | 与 `decompose-research-question` 的三步 protocol 完全相同 | REWORK；G1 |
| `formulate-research-question` | 步骤 2/3 为通用转换句，未写 FINER/比较/边界判据 | REWORK |
| `pairwise-ranking` | 步骤 2/3 为同一句通用转换句；与 `portfolio-optimization` protocol 完全相同 | REWORK；G1/G5 |
| `portfolio-optimization` | 步骤 2/3 为同一句通用转换句；与 `pairwise-ranking` protocol 完全相同 | REWORK；G1/G5 |
| `structured-consensus` | R4 canonical 文件缺失 | REWORK；MISSING |

### 19 EXPERIMENT SOP

以下节点的 R4 正文均为 40–41 行的统一三步壳，虽然 required 已改成节点名，仍缺少从 v3 源编译的操作语义；逐节点重写，不得沿用“Validate / Apply operation / Emit result”骨架：

`construct-design-matrix`, `design-randomness-protocol`, `estimate-sample-size`, `extract-core-conflict`, `identify-critical-chain`, `identify-scenario-drivers`, `list-undesirable-effects`, `map-ablation-components`, `optimize-design-under-budget`, `predict-competitive-move`, `project-future-reality`, `quantify-resource-gap`, `select-experimental-baseline`, `select-statistical-method`, `specify-execution-environment`, `specify-metrics`, `specify-reproducibility-protocol`, `statistical-testing`, `verify-reproducibility`。

对 `estimate-sample-size`、`select-statistical-method`、`statistical-testing` 保留固定统计阈值的要求（如 alpha/power）不等于正文已满足；须在 Procedure、Quality gates、Failure 中写出其适用条件、反例与停止理由。

## 给 N1 的最小返工接口

1. 只改上述 30 个 R4 旧壳；不要改 R1/R2/R3 已收口正文。
2. 每个 tactic 的步骤必须体现节点专属的状态变换；每个 EXPERIMENT SOP 必须从 v3 `description/update` 编译出至少一个节点专属判据和一个反例。
3. 返工后重新跑五道门；尤其清除通用句重复和全量八字段 delta。

## 新增审计：mode 说明、ASCII 判据与五个 pilot（2026-09-13）

本节只审 N2 已覆盖不到的语义内容；不重复判定旧五道门、第 15 项 mode 一致性或第 16 项 harness 解耦。

### 1. 33 个 mode 的正文说明

审计范围为七个有新增 mode 正文的节点：`rank-candidates`（8）、`analyze-constraints-readiness`（5）、`map-stakeholder-system`（3）、`resolve-inventive-contradiction`（3）、`sensitivity-analysis`（4）、`synthesize-meta-analytic-evidence`（5）、`design-experiment`（5）。

| 节点 | mode 数 | 实质说明结论 |
|---|---:|---|
| `rank-candidates` | 8 | PASS。每句都给出对象、判定操作或输出差异；`rapid-triage` 明确粗筛、规模压缩和淘汰理由。 |
| `analyze-constraints-readiness` | 5 | PASS。分别说明障碍排序、readiness 评分、资源包络、因果约束和成熟路径的不同推理任务。 |
| `map-stakeholder-system` | 3 | PASS。边界启发式、JTBD、salience 分别给出检查对象与判定用途。 |
| `resolve-inventive-contradiction` | 3 | PASS。技术矛盾、物理矛盾、分离分别规定参数/条件/残余冲突的处理。 |
| `sensitivity-analysis` | 4 | PASS。Morris、Sobol、perturbation、Monte-Carlo 分别写明筛选、方差分解、局部扰动和分布传播。 |
| `design-experiment` | 5 | PASS。factorial、ablation、comparison、scaling、robustness 都包含设计动作及其识别目的。 |
| `synthesize-meta-analytic-evidence` | 5 | REWORK（1/5）。`network`、`cumulative`、`heterogeneity`、`bias` 有实质过程和判据；`pairwise` 仅写“combine direct comparisons”，没有效应量汇总、研究质量/不确定性或停止条件。证据：`v4/skills/synthesize-meta-analytic-evidence/SKILL.md:31-38`；v3 `skills/pairwise-synthesis/SKILL.md` 的效应量、质量评估与 80% floor 条目见该正文 provenance ledger。 |

mode 结论：32/33 PASS，1/33 REWORK。REWORK 仅针对 `pairwise` 的说明密度，不涉及 mode 名称或 graph 注册。

### 2. ASCII 化语义抽查

抽查对象：`assess-sensitivity`、`rank-candidates`、`formulate-hypotheses` 的阈值正文和保留源标准。结论 PASS：ASCII 替换没有反转比较方向。

| 节点 | 核对的方向性判据 | v3 对照 | 结论 |
|---|---|---|---|
| `assess-sensitivity` | `stable`: all `tau >= 0.8`; `sensitive`: `0.5 <= tau < 0.8`; `unstable`: `tau < 0.5`; weight perturbation `+/-20%` | `skills/weight-perturbation/SKILL.md:22-35` | PASS；`>=` 与 `<=` 顺序、区间端点均未换向。 |
| `rank-candidates` | S/M/L candidate bands `5-8/9-15/16-20`; rapid triage retention `<=60%/<=50%/<=40%`; weighting `>=2` | `skills/multi-criteria-ranking/SKILL.md:51-59`、`skills/rapid-triage/SKILL.md:58-64` | PASS；所有 `<=` 仍表示上限，`>=2` 仍表示下限。 |
| `formulate-hypotheses` | hypothesis S/M/L `>=2/>=3/>=5`; deductive theories `>=2/>=3/>=5`; inductive observations `>=3/>=5/>=8`; abductive anomaly `1` | `skills/hypothesis-formulation/SKILL.md:68-74`、对应三类 generation 文件 | PASS；下限符号未被替换为上限。 |

### 3. 编码修复后的五个 pilot：v3 阈值复核

逐个对照 `scripts/` 下的 v3 source criterion 与当前 pilot body 的 preserved-source ledger、相对化门描述。结果如下：

| pilot | v3 真值复核 | 结论 |
|---|---|---|
| `formulate-hypotheses` | S/M/L structured hypotheses `2/3/5`；deductive theories `2/3/5`；inductive observations `3/5/8`；abductive 至少 1 个明确定义 anomaly。正文及 ledger 均保留。 | PASS |
| `rank-candidates` | independent scoring `1-5`；weight sensitivity `+/-20%`；S/M/L `5-8/9-15/16-20`；rapid-triage retention `<=60%/<=50%/<=40%`；stakeholder classes `2-3`、`3-5`。正文及 ledger 均保留。 | PASS |
| `establish-empirical-baseline` | v3 80% floors：methods `40/50`、data points `120/150`、standardized points `48/60`、score pairs `36/45`、historical points `80/100`。当前 ledger 逐项保留；执行门改为相对 universe/numerator，不改真值。 | PASS |
| `design-experiment` | scaling 的 geometric progression `4-8` 保留；factor/ablation/comparison/robustness 的源门和 preregistered statistical protocol 均保留。 | PASS |
| `audit-benchmark-validity` | benchmark-audit、saturation、validity-probing、coverage-mapping、protocol-forensics 的源 80% floors 与 HARD-GATE 均保留；正文改为相对 benchmark/evidence coverage，不改通过方向。 | PASS |

pilot 结论：5/5 PASS。未发现编码修复或 ASCII 化导致的阈值数值、比较方向或端点变化。

## Legacy 112 concept provenance lookup (2026-09-13)

Scope: current `concept` lines in `channel/deliverables/{R2,R4,R5}/nodes/*/body.md`. The 115 raw lines are reduced to 112 by stripping provenance suffixes (`[...]`, `(...)`) and collapsing three exact duplicate identifiers: `combination-mapping`, `validity-envelope-mapping`, and `six-thinking-hats`. Lookup target: the 930 exact `nodes[].name` values in `scripts/refactory_source.json`; accepted variants are bare name, `package-name`, and `package/name`.

Result: 73 exact matches; 39 unresolved. N2 may mark matched graph entries `resolved` with the v3 source name below. Unresolved entries remain `concept` (or `intermediate` if already so marked); no near-name substitution.

### Exact matches (recommended `resolved`)

| Body node id | Current marker | Body provenance | v3 source name |
|---|---|---|---|
| `R4/adjudicate-exchange` | `concept` | `stress-test-debate-judge <- stress-test/debate-judge` | `debate-judge` |
| `R4/adjudicate-exchange` | `concept` | `convergence-judge-verdict <- convergence/judge-verdict` | `judge-verdict` |
| `R4/construct-defense` | `concept` | `stress-test-debate-defender <- stress-test/debate-defender` | `debate-defender` |
| `R4/construct-defense` | `concept` | `convergence-advocate-construction <- convergence/advocate-construction` | `advocate-construction` |
| `R4/construct-validity-envelope` | `concept` | `deep-insight-validity-envelope-construction <- deep-insight/validity-envelope-construction` | `deep-insight-validity-envelope-construction` |
| `R4/construct-validity-envelope` | `concept` | `stress-test-validity-envelope-construction <- stress-test/validity-envelope-construction` | `stress-test-validity-envelope-construction` |
| `R4/detect-breakpoint` | `concept` | `stress-test-breakpoint-detection <- stress-test/breakpoint-detection` | `breakpoint-detection` |
| `R4/detect-breakpoint` | `concept` | `deep-insight-controlled-perturbation (threshold detection output) <- deep-insight/controlled-perturbation (threshold detection output)` | `controlled-perturbation` |
| `R4/elicit-weights` | `concept` | `hypothesis-formation-ahp-weighting <- hypothesis-formation/ahp-weighting` | `ahp-weighting` |
| `R4/elicit-weights` | `concept` | `convergence-weight-elicitation-sop <- convergence/weight-elicitation-sop` | `weight-elicitation-sop` |
| `R4/enumerate-combinations` | `concept` | `creative-ideation-matrix-construction <- creative-ideation/matrix-construction` | `matrix-construction` |
| `R4/enumerate-combinations` | `concept` | `creative-ideation-recombination-generation <- creative-ideation/recombination-generation` | `recombination-generation` |
| `R4/identify-bottleneck` | `concept` | `convergence-bottleneck-identification <- convergence/bottleneck-identification` | `convergence-bottleneck-identification` |
| `R4/identify-bottleneck` | `concept` | `deep-insight-critical-path-identification (limiting-input interpretation) <- deep-insight/critical-path-identification (limiting-input interpretation)` | `critical-path-identification` |
| `R5/adjudicate-exchange` | `concept` | `stress-test/debate-judge` | `debate-judge` |
| `R5/adjudicate-exchange` | `concept` | `convergence/judge-verdict` | `judge-verdict` |
| `R5/apply-perturbation` | `concept` | `creative-ideation/assumption-perturbation` | `creative-ideation-assumption-perturbation` |
| `R5/challenge-assumption` | `concept` | `convergence/assumption-challenge` | `convergence-assumption-challenge` |
| `R5/construct-defense` | `concept` | `stress-test/debate-defender` | `debate-defender` |
| `R5/construct-defense` | `concept` | `convergence/advocate-construction` | `advocate-construction` |
| `R5/construct-perspective-set` | `concept` | `multi-worldview-comparison` | `multi-worldview-comparison` |
| `R5/construct-perspective-set` | `concept` | `stakeholder-objection-simulation` | `stakeholder-objection-simulation` |
| `R5/construct-validity-envelope` | `concept` | `deep-insight/validity-envelope-construction` | `deep-insight-validity-envelope-construction` |
| `R5/construct-validity-envelope` | `concept` | `stress-test/validity-envelope-construction` | `stress-test-validity-envelope-construction` |
| `R5/define-criteria` | `concept` | `hypothesis-formation/scoring-matrix-construction (criteria-extraction core)` | `hypothesis-formation-scoring-matrix-construction` |
| `R5/derive-consequences` | `concept` | `stress-test/deductive-chain` | `deductive-chain` |
| `R5/derive-consequences` | `concept` | `deep-insight/consequence-following` | `consequence-following` |
| `R5/design-mitigation` | `concept` | `stress-test/mitigation-design-sop` | `mitigation-design-sop` |
| `R5/design-mitigation` | `concept` | `stress-test/re-scoring` | `re-scoring` |
| `R5/design-mitigation` | `concept` | `convergence/removal-path` | `removal-path` |
| `R5/detect-breakpoint` | `concept` | `stress-test/breakpoint-detection` | `breakpoint-detection` |
| `R5/detect-breakpoint` | `concept` | `deep-insight/controlled-perturbation` | `controlled-perturbation` |
| `R5/elicit-weights` | `concept` | `hypothesis-formation/ahp-weighting` | `ahp-weighting` |
| `R5/elicit-weights` | `concept` | `convergence/weight-elicitation-sop` | `weight-elicitation-sop` |
| `R5/enumerate-combinations` | `concept` | `creative-ideation/matrix-construction` | `matrix-construction` |
| `R5/enumerate-combinations` | `concept` | `creative-ideation/recombination-generation` | `recombination-generation` |
| `R5/evaluate-compatibility` | `concept` | `creative-ideation/consistency-pair-evaluation` | `creative-ideation-consistency-pair-evaluation` |
| `R5/evaluate-scenario-impact` | `concept` | `convergence/portfolio-evaluation-per-scenario` | `portfolio-evaluation-per-scenario` |
| `R5/evaluate-scenario-impact` | `concept` | `experiment-execution/scenario-impact-assessment` | `scenario-impact-assessment` |
| `R5/evaluate-scenario-robustness` | `concept` | `experiment-execution/robustness-scoring` | `robustness-scoring` |
| `R5/evaluate-scenario-robustness` | `concept` | `experiment-execution/strategy-robustness-testing` | `strategy-robustness-testing` |
| `R5/evaluate-scenario-robustness` | `concept` | `convergence/portfolio-optimization/robustness-under-uncertainty` | `robustness-under-uncertainty` |
| `R5/generate-provocation` | `concept` | `creative-ideation/po-provocation` | `po-provocation` |
| `R5/generate-provocation` | `concept` | `deep-insight/provocation-generation` | `deep-insight-provocation-generation` |
| `R5/generate-provocation` | `concept` | `creative-ideation/random-word-stimulus` | `random-word-stimulus` |
| `R5/generate-subquestions` | `concept` | `hypothesis-formation/sub-question-generation` | `sub-question-generation` |
| `R5/identify-bottleneck` | `concept` | `convergence/bottleneck-identification` | `convergence-bottleneck-identification` |
| `R5/identify-bottleneck` | `concept` | `deep-insight/critical-path-identification` | `critical-path-identification` |
| `R5/identify-obstacles` | `concept` | `north-star-crystallization/identify-obstacles` | `identify-obstacles` |
| `R5/identify-obstacles` | `concept` | `experiment-execution/obstacle-identification` | `obstacle-identification` |
| `R5/identify-variables` | `concept` | `hypothesis-formation/variable-identification` | `hypothesis-formation-variable-identification` |
| `R5/inventory-reference-items` | `concept` | `knowledge-acquisition/benchmark-inventory` | `knowledge-acquisition-benchmark-inventory` |
| `R5/inventory-reference-items` | `concept` | `creative-ideation/benchmark-inventory` | `creative-ideation-benchmark-inventory` |
| `R5/map-coverage-space` | `concept` | `creative-ideation/method-problem-crossing` | `method-problem-crossing` |
| `R5/map-coverage-space` | `concept` | `knowledge-acquisition/capability-taxonomy-mapping` | `capability-taxonomy-mapping` |
| `R5/measure-portfolio-diversity` | `concept` | `convergence/diversity-maximization` | `diversity-maximization` |
| `R5/measure-portfolio-diversity` | `concept` | `convergence/niche-coverage-analysis` | `niche-coverage-analysis` |
| `R5/normalize-comparison-scale` | `concept` | `convergence/normalization` | `normalization` |
| `R5/normalize-comparison-scale` | `concept` | `knowledge-acquisition/compute-normalization` | `compute-normalization` |
| `R5/rotate-perspective` | `concept` | `personal-analogy` | `personal-analogy` |
| `R5/score-object` | `concept` | `hypothesis-formation/novelty-scoring` | `hypothesis-formation-novelty-scoring` |
| `R5/score-object` | `concept` | `deep-insight/multi-criteria-scoring` | `deep-insight-multi-criteria-scoring` |
| `R5/score-object` | `concept` | `knowledge-structuring/novelty-scoring` | `knowledge-structuring-novelty-scoring` |
| `R5/score-object` | `concept` | `knowledge-structuring/gap-prioritization` | `knowledge-structuring-gap-prioritization` |
| `R5/sequence-work` | `concept` | `hypothesis-formation/answering-sequence-design` | `answering-sequence-design` |
| `R5/surface-assumptions` | `concept` | `creative-ideation/assumption-surfacing` | `creative-ideation-assumption-surfacing` |
| `R5/surface-assumptions` | `concept` | `deep-insight/assumption-enumeration` | `deep-insight-assumption-enumeration` |
| `R5/surface-assumptions` | `concept` | `convergence/assumption-extraction` | `convergence-assumption-extraction` |
| `R5/trace-causal-chain` | `concept` | `knowledge-structuring/causal-chain-query` | `causal-chain-query` |
| `R5/trace-causal-chain` | `concept` | `experiment-execution/causal-chain-tracing` | `causal-chain-tracing` |
| `R5/verify-evidence-independence` | `concept` | `deep-insight/cross-database-verification` | `cross-database-verification` |
| `R4/falsifiability-audit` | `concept` | `falsifiability/audit <- architecture semantic consolidation` | `falsifiability-audit` |
| `R4/pairwise-ranking` | `concept` | `pairwise/ranking <- architecture semantic consolidation` | `pairwise-ranking` |

### No exact match (retain `concept` / `intermediate`)

| Body node id | Current marker | Body provenance | Disposition |
|---|---|---|---|
| `R2/apply-stage-gate` | `concept` | `convergence/feasibility-assessment/stage-gate [strategy/tactic]` | retain `concept`; no exact v3 node |
| `R2/calibrate-adversarial-confidence` | `concept` | `confidence-escalation [sop]` | retain `concept`; no exact v3 node |
| `R2/explore-dimensional-space` | `concept` | `combination-mapping [tactic]` | retain `concept`; no exact v3 node |
| `R2/explore-dimensional-space` | `concept` | `consistency-checking [tactic]` | retain `concept`; no exact v3 node |
| `R2/explore-dimensional-space` | `concept` | `axis-identification [strategy]` | retain `concept`; no exact v3 node |
| `R2/explore-dimensional-space` | `concept` | `gap-prioritization [strategy]` | retain `concept`; no exact v3 node |
| `R2/map-validity-envelope` | `concept` | `validity-envelope-mapping [strategy]` | retain `concept`; no exact v3 node |
| `R2/map-validity-envelope` | `concept` | `validity-envelope-construction [sop]` | retain `concept`; no exact v3 node |
| `R4/build-domain-ontology` | `concept` | `build/domain/ontology <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/construct-argument-map` | `concept` | `construct/argument/map <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/construct-causal-model` | `concept` | `construct/causal/model <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/construct-design-matrix` | `concept` | `experiment-execution/construct-design-matrix <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/decompose-research-question` | `concept` | `decompose/research/question <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/design-randomness-protocol` | `concept` | `experiment-execution/design-randomness-protocol <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/enumerate-combinations` | `concept` | `creative-ideation-combination-generation <- creative-ideation/combination-generation` | retain `concept`; no exact v3 node |
| `R4/estimate-sample-size` | `concept` | `experiment-execution/estimate-sample-size <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/extract-core-conflict` | `concept` | `experiment-execution/extract-core-conflict <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/formulate-research-question` | `concept` | `formulate/research/question <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/identify-critical-chain` | `concept` | `experiment-execution/identify-critical-chain <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/identify-scenario-drivers` | `concept` | `experiment-execution/identify-scenario-drivers <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/list-undesirable-effects` | `concept` | `experiment-execution/list-undesirable-effects <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/map-ablation-components` | `concept` | `experiment-execution/map-ablation-components <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/optimize-design-under-budget` | `concept` | `experiment-execution/optimize-design-under-budget <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/portfolio-optimization` | `concept` | `portfolio/optimization <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/predict-competitive-move` | `concept` | `experiment-execution/predict-competitive-move <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/project-future-reality` | `concept` | `experiment-execution/project-future-reality <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/quantify-resource-gap` | `concept` | `experiment-execution/quantify-resource-gap <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/select-experimental-baseline` | `concept` | `experiment-execution/select-experimental-baseline <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/select-statistical-method` | `concept` | `experiment-execution/select-statistical-method <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/specify-execution-environment` | `concept` | `experiment-execution/specify-execution-environment <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/specify-metrics` | `concept` | `experiment-execution/specify-metrics <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/specify-reproducibility-protocol` | `concept` | `experiment-execution/specify-reproducibility-protocol <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R4/verify-reproducibility` | `concept` | `experiment-execution/verify-reproducibility <- architecture semantic consolidation` | retain `concept`; no exact v3 node |
| `R5/analyze-scaling-regime` | `concept` | `deep-insight/scaling-analysis` | retain `concept`; no exact v3 node |
| `R5/construct-perspective-set` | `concept` | `six-thinking-hats` | retain `concept`; no exact v3 node |
| `R5/construct-perspective-set` | `concept` | `role-storming` | retain `concept`; no exact v3 node |
| `R5/detect-contradiction` | `concept` | `stress-test/detect-contradiction` | retain `concept`; no exact v3 node |
| `R5/enumerate-combinations` | `concept` | `creative-ideation/combination-generation` | retain `concept`; no exact v3 node |
| `R5/rotate-perspective` | `concept` | `perspective-rotation` | retain `concept`; no exact v3 node |
