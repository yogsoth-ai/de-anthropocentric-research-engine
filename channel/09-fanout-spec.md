# 09-fanout-spec

Sirelia，2026-09-10 21:55。**260 个节点正文的扇出规格。全员适用。**

7 个 tactic 已编译（R5 pilot）。剩 260 个：44 tactic + 216 SOP。
本文件定模板、分区、验收。分区已按 id 全量枚举，无重叠无缺口。

---

## 一、两个模板

### 1.1 tactic 正文（44 个）

照抄 `deliverables/R5/pilot/establish-empirical-baseline/body.md` 的骨架。
九个固定小节，顺序不许变：

    # <node-id>
    ## Purpose
    ## Input contract          ← YAML block
    ## Execution protocol      ← 编号步骤
    ## Output contract         ← YAML block
    ## Thresholds and quality gates
    ## Failure and counterexamples
    ## Provenance map
    ## Preserved source criteria ledger
    ## Context checkpoint / Delta notes

条件小节，仅在适用时加：
- `## Mode branches` —— 节点在 architecture.json 里有 `modes` 字段时必写
- `## When to use / not applicable` —— 存在明确不适用场景时写

### 1.2 SOP 正文（216 个）—— 新模板，比 tactic 短

SOP 是单一变换，不编排。**七个固定小节：**

    # <node-id>
    ## Purpose
    ## Input contract          ← YAML block
    ## Procedure               ← 编号步骤，3–7 步
    ## Output contract         ← YAML block
    ## Quality gates
    ## Failure and counterexamples
    ## Provenance map

**SOP 不写 `Execution protocol`**（那是 tactic 的编排词），写 `Procedure`。
**SOP 不写 `Context checkpoint / Delta notes`**——checkpoint 由调用它的
tactic 统一落盘，SOP 只返回 Delta 片段。

**BASIS SOP（45 个）额外必写：**

    ## Parameterization        ← 调用方必须提供什么才能让这个 SOP 具体化

理由：BASIS 的科研内容住在调用方给的参数里。`score-object` 的 desc 原文：
「The parent tactic supplies the object schema and rubric」。
不写清参数契约，6 个调用方各写各的。

### 1.3 两个 contract 小节的格式锁死

**这是机器解析面，格式不许自由发挥。** 一律 YAML block，键固定：

```yaml
required: [field_a, field_b]
optional: [field_c]
constraints: [自然语言约束，逗号分隔]
```

```yaml
produces: [artifact_a, artifact_b]
delta_fields: [findings, evidence_updates, decisions]
```

`delta_fields` 只能取八字段子集：`findings`、`evidence_updates`、
`hypothesis_updates`、`assumption_updates`、`uncertainties`、`decisions`、
`open_questions`、`recommended_jumps`。写别的名字直接驳回。

---

## 二、tactic 的 Execution protocol 必须给默认序

`edge_semantics.calls` 原文：「Declares the SOP vocabulary that a tactic may
compose. **It is not a mandatory linear order.**」

不是强制序，**不等于没有默认序**。44 个 tactic 的 `Execution protocol`
必须给出一个默认执行顺序，并说明什么条件下偏离。

格式：

    ## Execution protocol

    1. <步骤>（`sop-id-a`, `sop-id-b`）
    2. <步骤>（`sop-id-c`）
    3. ...

    Deviation: <什么情况下跳过/重排，判据是什么>

**每个步骤后括号里必须列出本步用到的 SOP id，且这些 id 必须在
architecture.json 的 `calls[<tactic-id>]` 里存在。** 写不在里面的 id = 幻影引用，
驳回。反过来，`calls` 里列了但正文一次都没提到的 SOP，要在 `Deviation`
里说明为什么它是可选的。

---

## 三、判据继续按 A/B/C 三类办

2026-09-08 裁定继续有效，扇出时逐节点适用：

| 类 | 判据防的是什么 | 处置 |
|---|---|---|
| A | 敷衍（没看内容就下结论） | 留，绝对数字改相对量 |
| B | 可机械核验的形式检查 | 留，保持原样 |
| C | 无依据的历史遗留数字 | 删 |

**A 类相对量的六个必需字段**（R5 已落进 7 个 pilot，照抄那个口径）：
declared universe（分母是什么）、numerator、batch increment、
stopping reason、source references、方向与阈值理由。缺一项不得通过。

饱和判定挂 `assess-evidence-saturation`；需要具体数的挂 `set-threshold`
并给理由。**不许新造机制。**

统计显著性、power、预注册、公平比较条件、方法结构约束——**保持固定值，
不许相对化**。0.05 相对化没有意义。

---

## 四、Provenance map 与源判据保真

每个节点的 `## Provenance map` 列出它在 architecture.json 里 `old[]` 的全部条目，
逐条标注三种状态之一：

- `resolved: <v3 真实节点名>` —— 已在 `scripts/refactory_source.json` 找到
- `intermediate: PassN/<name>` —— 中间轮次快照，v3 无对应，不追
- `concept` —— 方法概念名而非节点名，不追

**归一化规则（必读，否则虚报缺失）**：v3 真实节点名用连字符连接 package，
`old[]` 写斜杠形式。查 `refactory_source.json` 前先转换：

    old[] 写：  creative-ideation/consistency-pair-evaluation
    v3 实际：  creative-ideation-consistency-pair-evaluation

比对前还要剥掉 `[...]` 和 `(...)` 后缀。详见 `07-provenance-reconciliation.md`。

`resolved` 的源节点里凡有数字判据、rubric、失败反例，**逐字进正文**，
不许四舍五入、不许平均、不许「等价改写」。这条是红线。

`## Preserved source criteria ledger`（tactic 必写，SOP 有源判据时必写）
格式沿用 pilot：源文件名、物理行号、类型、原文。

---

## 五、分区（按 id 全量枚举，260 个）

### R1 —— GROUP A：ACQUISITION + DIRECTION，44 个（6 tactic + 38 SOP）

tactic：
`assess-prior-art-and-claims` `decompose-research-goal` `map-patent-white-space`
`map-research-landscape` `mine-patent-landscape` `synthesize-literature-evidence`

SOP：
`analyze-heterogeneity` `analyze-leaderboard-dynamics` `analyze-patent-citation-network`
`assess-construct-validity` `assess-evidence-saturation` `assess-patent-claim-scope`
`assess-patent-legal-status` `assess-publication-bias` `audit-data-contamination`
`audit-reporting-quality` `audit-study-validity` `categorize-evidence`
`compare-evaluation-protocols` `construct-evidence-network` `crystallize-north-star`
`decompose-and-or-goal` `decompose-evaluation-metric` `define-evidence-protocol`
`design-data-extraction` `design-study-inclusion` `detect-performance-discrepancy`
`estimate-performance-headroom` `extract-evaluation-protocol` `extract-evidence-record`
`formulate-meta-analysis-scope` `formulate-top-goal` `generate-candidate-directions`
`navigate-patent-classification` `parse-patent-claim` `plan-effect-size`
`probe-benchmark-artifact` `screen-evidence-multistage` `select-seed-evidence`
`synthesize-field-panorama` `trace-citation-neighborhood` `trace-patent-family`
`update-cumulative-evidence` `validate-goal-tree`

**R1 注意**：本组含 C3/C4/C19/C20 四条 A 类重灾区（150 源、80 篇/30 页全文、
survey paradigm 100/20/0、snowball 67%）。相对化方案见
`deliverables/R2/thinned-triage.md`，照它落，不要另发明。

### R2 —— GROUP B：STRESS + CROSS，41 个（12 tactic + 29 SOP）

tactic：
`adversarial-deliberation` `audit-convergence-independence` `audit-explanatory-compression`
`audit-structural-equivalence` `audit-validator-independence` `counterfactual-causal-analysis`
`explore-dimensional-space` `falsification-first-audit` `fmea-risk-analysis`
`map-validity-envelope` `reductio-counterexample-analysis` `structured-red-team`

SOP：
`build-failure-chain` `build-noncircularity-matrix` `calibrate-adversarial-confidence`
`classify-falsification-verdict` `classify-simplicity-evidence` `cross-examine`
`design-falsification-test` `detect-pass-by-construction` `downgrade-equivalence-claim`
`enumerate-failure-modes` `enumerate-validator-assumptions` `estimate-effective-evidence-count`
`evaluate-necessity-sufficiency` `execute-probe` `extract-structural-mapping`
`generate-attack-vector` `generate-counterexample` `identify-shared-priors`
`map-threat-surface` `negate-claim` `refine-claim` `score-fmea-risk`
`search-minimal-flip` `select-critical-case` `sharpen-falsifiable-claim`
`test-risky-prediction` `test-structure-preservation` `trace-assumption-cascade`
`validate-mitigation-effect`

**R2 注意**：`map-validity-envelope` 的 `modes` 实际值是
`systematic-perturbation, boundary-value-stress, critical-case`——
你自己第一轮查出来的。`Mode branches` 按实际值写，不按引用里的别名。
`adversarial-deliberation` 你判过它留在高危审计表，本轮补正文。

### R3 —— GROUP C：IDEATION + INSIGHT，51 个（15 tactic + 36 SOP）

tactic：
`analogical-discovery` `assumption-stress-test` `biomimetic-transfer`
`conceptual-blending` `coverage-white-space-search` `destructive-ideation`
`drill-root-causes` `evolve-solution-population` `map-stakeholder-system`
`problem-reframing` `resolve-inventive-contradiction` `robustness-analysis`
`sensitivity-analysis` `structural-transformation` `validate-research-gap`

SOP：
`abstract-structure` `apply-separation-principle` `appreciative-reframe`
`assess-problem-wickedness` `assess-system-boundary` `biologize-problem`
`build-concept-fan` `build-current-reality-tree` `classify-assumption-vulnerability`
`classify-research-gap` `classify-stakeholder-salience` `construct-input-spaces`
`decompose-components` `decompose-global-sensitivity` `decompose-ishikawa`
`discover-biological-analog` `drill-five-whys` `extract-biological-strategy`
`extract-constructive-movement` `extract-generic-space` `filter-false-gap`
`generate-alternative-model` `identify-dominant-frame` `identify-inventive-contradiction`
`instantiate-transfer` `map-analogy` `map-productive-polarity` `map-stakeholder-jobs`
`mutate-solution-population` `propagate-uncertainty` `quantify-information-value`
`select-inventive-principle` `select-solution-variants` `simulate-emergent-properties`
`synthesize-idea` `transform-component`

**R3 注意**：本组是 SCAMPER / Six Hats / Synectics / TRIZ / 生物类比的落点。
R2 审出 C52–C54、C58 缺「逐算子约束」——`structural-transformation` 的
7 个 SCAMPER 算子、`select-inventive-principle` 的 TRIZ 原理，
必须逐个列出，不许用「apply appropriate operator」这种糊话概括。
你上一轮做的入口 UX 完成了，本轮转正文编译，模板照 pilot。

### R5 —— BASIS 45 个（全部 SOP，含 `## Parameterization`）

按 fan-in 降序，前 22 个（fan-in ≥ 3）优先：

`assess-sensitivity`(7) `evaluate-compatibility`(6) `score-object`(6)
`surface-assumptions`(6) `detect-coverage-gap`(5) `analyze-temporal-trajectory`(4)
`enumerate-dimension-values`(4) `identify-variables`(4) `apply-perturbation`(3)
`canonicalize-entity`(3) `construct-critique`(3) `construct-perspective-set`(3)
`define-analysis-dimensions`(3) `detect-contradiction`(3) `extract-causal-structure`(3)
`identify-load-bearing-factors`(3) `inventory-reference-items`(3) `map-dependencies`(3)
`map-disagreement`(3) `set-threshold`(3) `validate-causal-link`(3)
`verify-evidence-independence`(3)

其余 23 个（fan-in ≤ 2）：
`adjust-abstraction-scope` `aggregate-ranking` `analyze-scaling-regime`
`assess-goal-feasibility` `challenge-assumption` `check-dominance`
`construct-counterfactual` `construct-hierarchy` `construct-scenario`
`define-criteria` `derive-consequences` `design-mitigation`
`evaluate-scenario-impact` `evaluate-scenario-robustness` `generate-provocation`
`generate-subquestions` `map-coverage-space` `measure-portfolio-diversity`
`normalize-comparison-scale` `sequence-work` `trace-causal-chain`
`identify-obstacles` `rotate-perspective`

**R5 注意 ——`score-object` 是本组第一优先，且要连带做一个决定。**
它吞并了 15 个 v3 scoring 节点，被 6 个 tactic 调用，`old[]` 里 7 条未解析
（全图密度最高）。你上一轮的处置是「保守复制 + 标记待重构」。
**本轮把它做成终态**：15 个 rubric 是抽成一个共享 rubric 目录，
还是全部作为 `Parameterization` 的调用方责任。选一个，给理由。
这个决定影响 6 个调用方的正文，先做它，做完在 channel 说一声，
R1/R2/R3 按结论写他们的 tactic。

### R4 —— GROUP D：HYPOTHESIS + EXPERIMENT + CONVERGENCE + STRUCTURING，79 个（11 tactic + 68 SOP）

tactic：
`analyze-experiment-results` `analyze-future-scenarios` `build-domain-ontology`
`construct-argument-map` `construct-causal-model` `decompose-research-question`
`falsifiability-audit` `formulate-research-question` `pairwise-ranking`
`portfolio-optimization` `structured-consensus`

SOP：
`adjudicate-exchange` `analyze-intervention` `apply-question-framework`
`apply-stage-gate` `apply-veto-filter` `assess-question-quality`
`assess-ranking-consistency` `assess-readiness-dimension` `assess-removability`
`atomize-claim` `atomize-concept` `attach-evidence-to-relation`
`audit-structure-consistency` `calibrate-probability-forecast` `characterize-anomaly`
`classify-constraint` `collect-independent-judgments` `compare-hypotheses`
`compare-pair` `construct-defense` `construct-design-matrix`
`construct-validity-envelope` `define-objective` `design-discriminating-prediction`
`design-randomness-protocol` `detect-breakpoint` `detect-feedback-loop`
`document-counterclaim` `elicit-weights` `enumerate-combinations`
`estimate-sample-size` `evaluate-falsifiability` `evaluate-optionality`
`extract-concepts` `extract-core-conflict` `extract-empirical-regularity`
`generate-competing-hypotheses` `identify-bottleneck` `identify-critical-chain`
`identify-scenario-drivers` `identify-theory` `list-undesirable-effects`
`map-ablation-components` `normalize-gap` `operationalize-construct`
`optimize-design-under-budget` `optimize-pareto-frontier` `predict-competitive-move`
`project-future-reality` `quantify-resource-gap` `represent-mechanism-edge`
`run-convergence-round` `scope-domain` `select-experimental-baseline`
`select-from-frontier` `select-next-pair` `select-statistical-method`
`specify-boundaries` `specify-execution-environment` `specify-metrics`
`specify-relationship` `specify-reproducibility-protocol` `statistical-testing`
`type-relation` `update-confidence-from-evidence` `update-pairwise-rating`
`validate-axis-independence` `verify-reproducibility`

**R4 注意**：本组最大（79 个），但你的图修补活已完，产能腾出来了。
含统计与实验设计——`estimate-sample-size`、`select-statistical-method`、
`statistical-testing`、`verify-reproducibility` 这些**保持固定值判据**
（power 0.8、α 0.05 之类），不许相对化，是第三节明示的例外。
`portfolio-optimization`、`optimize-pareto-frontier` 属决策方法，
判据按 A/B 判，不要机械套「读够没读够」。

---

## 六、落点与提交节奏

落 `deliverables/<代号>/nodes/<node-id>/body.md`。
tactic 另加 `compilation-log.md`；SOP 的编译记录合并到本组一份
`deliverables/<代号>/nodes/_compilation-log.md`，逐节点一段，不必一节点一文件。

**按 10 个一批交，写进你自己的 topic 帖**（R1→`02-`，R2→`03-`/`04-`，
R3→`02-r3-cold-start.md`，R4→`05-` 新建，R5→`02-r1-spec-design.md` 沿用或另开）。
不要憋到最后。每批说明：本批 id、A/B/C 判据数、未解析 provenance 数。

**不要等 host 结论。** R6 正在并行谈 host（`08-host-negotiation.md`）。
Q4/Q5 的结论只影响 contract 小节的**解析格式**，不影响科研内容。
本文件第 1.3 节已把格式锁死，按它写就不会返工。

## 七、硬约束（违反直接驳回）

1. 写权限只有 `channel/`。repo 其余目录只读。
2. 禁一切 git 写操作。
3. 禁 `superpowers` / `ara` 两个 skill。出现 superpowers 模板痕迹或 ARA 的
   `logic/ src/ trace/ evidence/` 四层结构，驳回。
4. 对外动作（提交/推送/发布/装包/调外部服务）一律先报，不许自己做。
5. **不许编造 v3 源。** 查不到就标 `concept` 或 `intermediate`，
   不许拿名字相似的顶上。这条上一轮已经出过事。
6. **不许把 agent 异常处理写进正文。** 重试、超时、退避、错误分类、
   并行调度、监控状态机——全部不写。Pthahnix 已裁定。
7. `Input contract` / `Output contract` 的 YAML 键固定为第 1.3 节那五个，
   `delta_fields` 只取八字段子集。

## 八、只读源

- `file-transfer/2026-08-23-22-16-dare-v4-architecture.json` — v4 权威图，节点 desc/old/modes/calls 全在这
- `scripts/refactory_source.json` — v3 全量源（1.7 MB）
- `deliverables/R5/pilot/*/body.md` — 7 个 tactic 正文范例
- `deliverables/R2/thinned-triage.md` — 58 条 A/B/C 分级与相对化方案
- `deliverables/R5/validate_threshold_fidelity.py` — 保真校验器，可直接跑自己的节点
- `07-provenance-reconciliation.md` — `old[]` 归一化规则与 132 条未解析明细
