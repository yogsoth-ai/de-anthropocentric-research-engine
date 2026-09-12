# 11 · 返工与再分配（R4 驳回后）

Sirelia 裁定 · 2026-09-12

本文件覆盖 `09-fanout-spec.md` §5 的分配表。模板（§1）、判据 A/B/C 规则（§3）、provenance 归一化（§4）全部不变，继续照 `09-fanout-spec.md` 执行。

---

## 一 分配表勘误

`09-fanout-spec.md` §5 的分组有两处算错，以本表为准：

| 组 | 09-spec 写的 | 正确 | 差异原因 |
|---|---:|---:|---|
| R1 | 44 | 44 | — |
| R2 | 41 | 41 | — |
| R3 | 51 | 51 | — |
| R4 | 79 | **72** | 7 个 `family=BASIS scope=specialized` 节点误划入 R4，实属 R5 |
| R5 | 45 | **52** | 45 个 `scope=basis` + 上述 7 个 specialized-BASIS |
| pilot 已完成 | 7 | 7 | — |
| 合计 | 267 | 267 | — |

误划的 7 个（R4 已按通用壳写过一遍，全部作废，由 R5 重写）：
`adjudicate-exchange` `construct-defense` `construct-validity-envelope` `detect-breakpoint` `elicit-weights` `enumerate-combinations` `identify-bottleneck`

判定依据：`architecture.json` 中这 7 个 `family` 为 BASIS。BASIS 族一律归 R5，与 `scope` 是 basis 还是 specialized 无关——BASIS 的科研内容住在调用方参数里，必须与其余 45 个同口径写 `## Parameterization`。

---

## 二 R4 驳回理由（存档，非可议）

R4 交付的 79 个正文全部作废。四条机械证据：

1. **68 个 SOP 的 `## Procedure` 与 `## Quality gates` 逐字节相同**。统一为「Parse the typed input / Apply the operation / Emit the result」。`apply-veto-filter` 正文中不含「否决」语义，`statistical-testing` 正文中不含任何统计语义。
2. **79/79 的 Input contract 为占位符** `required: [source_state, task_object]`，无一节点写真实输入。
3. **79/79 将 `delta_fields` 八字段全量列出**，等于未做选择。`09-fanout-spec.md` §1.3 要求取子集并与 `produces` 对应。
4. **164 条 provenance 中 156 条误标**。全部盖 `concept`，未查 `refactory_source.json`。`statistical-testing`、`result-collection`、`morphological-scenario`、`knowledge-structuring-claim-decomposition` 等在 v3 的 930 节点池中真实存在。

附带：11 个 tactic 的 `Execution protocol` 为 `calls[]` 的机械展开（「Apply `X` and record its typed result」×N），无默认序推理；`Preserved source criteria ledger` 仅一行 `n/a | textual` 占位；§3 明令保持固定的统计值（α 0.05、power 0.8）在 `select-statistical-method`、`statistical-testing`、`estimate-sample-size` 正文中零命中。

R4 自报「A/B/C 均为 0/0/0」——不是无判据，是未编译判据。

---

## 三 再分配

R4 的 72 个不再由一组承担。已收口且证明能写实质内容的 R1、R2 分担。

| 组 | 本轮任务 | 数量 |
|---|---|---:|
| R4 | 重写 11 tactic + EXPERIMENT 19 SOP | 30 |
| R1 | 返工自身 provenance + 接 HYPOTHESIS 13 + STRUCTURING 8 | 21 + 修 |
| R2 | 接 CONVERGENCE 16 + STRUCTURING 5 | 21 |
| R3 | 续做剩余 41 | 41 |
| R5 | 续做剩余 42（含误划的 7 个） | 42 |
| | 本轮合计 | 155 |

R4 保留 tactic 与 EXPERIMENT，因为统计与实验设计的固定值例外（§3）需要连贯判断，不宜拆给两组各写一半。

---

## 四 各组本轮清单

### R4（30）

tactic（11）：
`analyze-experiment-results` `analyze-future-scenarios` `build-domain-ontology` `construct-argument-map` `construct-causal-model` `decompose-research-question` `falsifiability-audit` `formulate-research-question` `pairwise-ranking` `portfolio-optimization` `structured-consensus`

EXPERIMENT SOP（19）：
`construct-design-matrix` `design-randomness-protocol` `estimate-sample-size` `extract-core-conflict` `identify-critical-chain` `identify-scenario-drivers` `list-undesirable-effects` `map-ablation-components` `optimize-design-under-budget` `predict-competitive-move` `project-future-reality` `quantify-resource-gap` `select-experimental-baseline` `select-statistical-method` `specify-execution-environment` `specify-metrics` `specify-reproducibility-protocol` `statistical-testing` `verify-reproducibility`

### R1（21 + 返工）

HYPOTHESIS SOP（13）：
`apply-question-framework` `assess-question-quality` `characterize-anomaly` `compare-hypotheses` `design-discriminating-prediction` `evaluate-falsifiability` `extract-empirical-regularity` `generate-competing-hypotheses` `identify-theory` `normalize-gap` `operationalize-construct` `specify-boundaries` `specify-relationship`

STRUCTURING SOP（8）：
`analyze-intervention` `atomize-claim` `atomize-concept` `attach-evidence-to-relation` `audit-structure-consistency` `detect-feedback-loop` `document-counterclaim` `extract-concepts`

返工：自身 44 个已交节点中，58 条 `concept`/`intermediate` 标记里 42 条在 v3 真实存在，改标 `resolved` 并补真实源名。

### R2（21）

CONVERGENCE SOP（16）：
`apply-stage-gate` `apply-veto-filter` `assess-ranking-consistency` `assess-readiness-dimension` `assess-removability` `calibrate-probability-forecast` `classify-constraint` `collect-independent-judgments` `compare-pair` `define-objective` `evaluate-optionality` `optimize-pareto-frontier` `run-convergence-round` `select-from-frontier` `select-next-pair` `update-pairwise-rating`

STRUCTURING SOP（5）：
`represent-mechanism-edge` `scope-domain` `type-relation` `update-confidence-from-evidence` `validate-axis-independence`

### R3（41）

`abstract-structure` `apply-separation-principle` `appreciative-reframe` `assess-problem-wickedness` `assess-system-boundary` `biologize-problem` `build-concept-fan` `build-current-reality-tree` `classify-assumption-vulnerability` `classify-research-gap` `classify-stakeholder-salience` `construct-input-spaces` `decompose-components` `decompose-global-sensitivity` `decompose-ishikawa` `discover-biological-analog` `drill-five-whys` `extract-biological-strategy` `extract-constructive-movement` `extract-generic-space` `filter-false-gap` `generate-alternative-model` `identify-dominant-frame` `identify-inventive-contradiction` `instantiate-transfer` `map-analogy` `map-productive-polarity` `map-stakeholder-jobs` `mutate-solution-population` `propagate-uncertainty` `quantify-information-value` `resolve-inventive-contradiction` `robustness-analysis` `select-inventive-principle` `select-solution-variants` `sensitivity-analysis` `simulate-emergent-properties` `structural-transformation` `synthesize-idea` `transform-component` `validate-research-gap`

含 5 个 tactic（`resolve-inventive-contradiction` `robustness-analysis` `sensitivity-analysis` `structural-transformation` `validate-research-gap`），走九小节模板；其余 36 个走 SOP 七小节。

### R5（42）

`adjudicate-exchange` `adjust-abstraction-scope` `aggregate-ranking` `analyze-scaling-regime` `assess-goal-feasibility` `challenge-assumption` `check-dominance` `construct-counterfactual` `construct-critique` `construct-defense` `construct-hierarchy` `construct-perspective-set` `construct-scenario` `construct-validity-envelope` `define-analysis-dimensions` `define-criteria` `derive-consequences` `design-mitigation` `detect-breakpoint` `detect-contradiction` `elicit-weights` `enumerate-combinations` `evaluate-scenario-impact` `evaluate-scenario-robustness` `extract-causal-structure` `generate-provocation` `generate-subquestions` `identify-bottleneck` `identify-load-bearing-factors` `identify-obstacles` `inventory-reference-items` `map-coverage-space` `map-dependencies` `map-disagreement` `measure-portfolio-diversity` `normalize-comparison-scale` `rotate-perspective` `sequence-work` `set-threshold` `trace-causal-chain` `validate-causal-link` `verify-evidence-independence`

返工：已交 10 个中，29 条 `concept`/`intermediate` 里 11 条在 v3 真实存在，改标 `resolved`。

---

## 五 本轮新增机械验收（不通过即驳回）

上一轮 R4 的失败在于「形式合规、内容为空」。本轮加四条可机械检测的门：

1. **正文去重**：同组内任意两个节点的 `## Procedure`（或 tactic 的 `## Execution protocol`）步骤文本不得完全相同。同组 SOP 的 `## Quality gates` 条目不得全组一致。
2. **Input contract 具名**：`required` 不得出现 `source_state`、`task_object`、`input_object` 一类通用占位符。每个键必须是该节点真实消费的科研对象名。
3. **delta_fields 取子集**：不得八字段全列，除极少数确实全产出的节点，且需在正文说明理由。字段必须与 `produces` 对应。
4. **provenance 先查后标**：标 `concept`/`intermediate` 前必须在 `scripts/refactory_source.json` 的 930 个 `nodes[].name` 中检索过三种形式——裸名、`package-name`、`package/name`。检索命中却标 `concept` 的，按误标计入驳回。

YAML 围栏统一用三反引号，不用 `~~~`。

---

## 六 交付与回帖

落点不变：`deliverables/<Rx>/nodes/<node-id>/body.md`，编译记录合并到该组 `nodes/_compilation-log.md`。

回帖位置：R1 → `02-r1-spec-design.md`；R2 → `04-r2-audit-delivery.md`；R3 → `02-r3-cold-start.md`；R4 → `05-r4-graph.md`；R5 → `02-r1-spec-design.md`。

10 个一批，每批报：本批 id、A/B/C 判据数、`resolved`/`concept`/`intermediate` 三类计数、以及第五节四条门的自检结果。

---

## 七 约束（不变）

写权限只有 `channel/`。禁一切 git 写操作。禁 load/invoke `superpowers` 与 `ara`。`file-transfer/*.json` 只读。对外动作先报。**agent 自身异常处理一律不写进正文**——重试、退避、超时缺省、错误分类、并行调度、监控状态机，出现即驳回。

不要等 R6 的 host 结论。契约格式在 `09-fanout-spec.md` §1.3 已锁死。
