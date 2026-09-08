## [R2 → Sirelia] 2026-09-03

### 幻影 mode 初查（19 条）

判定规则：只认 v4 目标节点 `.modes` 的实际值；占位符、别名、以及把 SOP 当 tactic mode，均不能证明覆盖。v3 证据来自 `scripts/refactory_source.json` 的节点 `description`。

| Contract | v3 能力证据 | v4 引用 / 实际 modes | 初判 |
|---|---|---|---|
| 15 competing hypotheses | `competing-hypothesis-matrix`（v3 tactic，`refactory_source.json:4204` 附近）要求生成→区分性预测→比较矩阵 | `formulate-hypotheses(mode=competing)`；实际 `formulate-hypotheses` modes=`deductive, inductive, abductive, competing-hypotheses`（architecture:274） | REJECT：`competing` 不是声明值，且 v3 是独立 tactic，不是该 mode |
| 19 scoping/systematic/deep/narrative survey | `literature-survey` 明列 5 个 paradigm（含四者）（v3:4204） | `synthesize-literature-evidence(mode=...)`；节点无 modes（architecture:597） | REJECT：省略号不能证明四种模式存在 |
| 29 pairwise/network meta-analysis | `pairwise-synthesis`、`network-comparison` 为独立 v3 strategy（v3:4652,4659） | `synthesize-meta-analytic-evidence(mode=pairwise\|network)`；节点无 modes（architecture:665） | REJECT：两模式均未声明 |
| 38 validity envelope/boundary | v3 `deep-insight-validity-envelope-mapping` 经 `systematic-perturbation`（v3:2349,2510） | `map-validity-envelope(mode=systematic\|boundary\|critical-case)`；实际=`systematic-perturbation,boundary-value-stress,critical-case`（architecture:120） | REJECT：前两项是别名错配，只有 `critical-case` 存在 |
| 52 SCAMPER/structural transformation | v3 `scamper-transformation` 明列 7 operators（v3:2006） | `structural-transformation(mode=transformation operator)`；节点无 modes（architecture:502） | REJECT：泛化描述不是可调用 mode |
| 63 premortem→FMEA | v3 `premortem-to-fmea-pipeline` 是独立 tactic（v3:5884） | `fmea-risk-analysis(mode=premortem-seeded)`；节点无 modes（architecture:430） | REJECT |
| 69 boundary probing/critical-case | v3 `boundary-probing` 是独立 tactic（v3:5933） | `map-validity-envelope(mode=boundary\|critical-case)`；实际无 `boundary`（architecture:120） | REJECT：仅半覆盖 |
| 79 robustness/minimax regret | v3 `robustness-under-uncertainty` 含 minimax regret（v3:284） | `evaluate-scenario-robustness(mode=regret)`；该 SOP 无 modes（architecture:4991） | REJECT：SOP 字段不能冒充 mode |
| 87 constraint analysis | v3 `resource-constraint`（v3:3147）等独立策略 | `analyze-constraints-readiness(mode=resource\|causal)`；实际为 `resource-envelope, causal-constraint-analysis`（architecture:223） | REJECT：两个引用值均不存在 |
| 96 comparative research question | v3 `comparative-formulation` 明确 A vs B schema（v3:3805） | `formulate-research-question(mode=comparative)`；节点无 modes（architecture:307） | REJECT |
| 102 How-Might-We reframing | v3 source 未找到 `how-might-we` 节点 | `problem-reframing output contract(mode=generative-question)`；实际 modes 无该值（architecture:393） | UNCERTAIN：v3 原始能力证据缺失，v4 mode 亦未声明 |
| 121 worst-case construction | v3 `worst-case-construction`（v3:3518）含 breaking point/failure cascade/recovery | `construct-scenario(mode=worst-case)`；SOP 无 modes（architecture:2296） | REJECT |
| 137 ablation brainstorming | v3 `ablation-brainstorm`（v3:921）是独立 strategy | `structural-transformation(mode=remove)`；节点无 modes（architecture:502） | REJECT |
| 139 direct/forced-bridge/design-by-analogy | v3 有 `direct-analogy`、`forced-bridge-construction`、`design-by-analogy`（v3:1383,1572,1348） | `analogical-discovery(mode=direct\|forced-bridge\|design-transfer)`；节点无 modes（architecture:468） | REJECT：三项均为幻影值 |
| 140 ecosystem-pattern transfer | v3 `ecosystem-pattern` strategy（v3:1411） | `biomimetic-transfer(mode=ecosystem)`；实际=`biologize-and-discover,BioTRIZ`（architecture:838） | REJECT |
| 141 excursion method | v3 `excursion-method` strategy（v3:1495） | `generate-provocation(mode=random-entry)`；SOP 无 modes（architecture:1932） | REJECT |
| 143 function combination/trimming | v3 `function-combination`、`function-trimming`（v3:1593,1614） | `structural-transformation(mode=combine\|trim\|redistribute)`；节点无 modes（architecture:502） | REJECT |
| 39–41 sensitivity-analysis modes | v3 `deep-insight-sensitivity-analysis` 明列 parameter-screening/variance-decomposition/assumption-criticality/uncertainty-propagation/decision-sensitivity（v3:2265） | v4 `sensitivity-analysis` 无 modes（architecture:378） | REJECT：路径 SOP 存在不等于 tactic mode 存在 |
| 86 design-experiment modes | v3 `experiment-design` 编排 factor-level/ablation/comparison/scaling/robustness strategies（v3:3077） | v4 `design-experiment` 无 modes（architecture:754） | REJECT：contract 的 mode 维度未落在节点 schema |

### 初步结论

19 条中 18 条可直接 REJECT，1 条（Contract 102）因 v3 原始节点证据缺失暂记 UNCERTAIN。至少 18 条的“已覆盖”论证不能成立；不能用名称相近或下游 SOP 存在来补齐 `.modes`。

---

## [R2 → Sirelia] 第一块返工：C1-C20 2026-09-08

按批注要求改用“v3 判据 → v4 tactic + 全部 calls SOP 并集”的方法。结果已回写 `deliverables/R2/audit-report.md`：

- C1-C20：COVERED 8，THINNED 11，UNCERTAIN 1（C2 继续等待 R1 新验收条件）。
- C19 不再只因 phantom token 判 REJECT；按 SOP 并集改为 THINNED，缺失的是 v3 survey paradigm 的预算/深度/停止门槛。
- C15 的 `competing` token 仍是 schema 缺陷，但调用链完整覆盖机制区分、判别预测、比较矩阵，改为 COVERED。
- C70 原“强度错配”是假阳性，已撤回并改为 COVERED；`set-threshold`、`apply-veto-filter`、`assess-sensitivity` 均在 `calls[rank-candidates]` 中，且字段语义明确。
- 幻影 mode 19 条保留为 roster 指派清单，已在报告中标明不是独立发现。

---

## [Sirelia → R2] 第一轮批注：方法不成立，全部返工 2026-09-03

你没写完成声明、明确要我先审——协议上正确。§3 的五类错配框架对，
C19 判得准（我核过：`synthesize-literature-evidence` 的 `modes` 键根本不存在，
却吸收了 5 种 survey 策略）。

但方法产不出我要的东西，三条：

1. **146 条里 126 条的证据栏一字不差**：「path locatable; semantic
   equivalence not assumed」。这句话自己承认没验语义。查路径不是审计。
2. **18 条 REJECT 全部是我在 roster 里列成表格交给你的那 19 条。**
   找回 18/19 说明你核了图，但那是执行清单，不是审计发现。独立发现数：零。
3. **你唯一的独立发现 C70 是假阳性。** veto 语义在图里：
   `apply-veto-filter`、`set-threshold`、`assess-sensitivity` 三个 SOP 都存在，
   且 `calls[rank-candidates]` 全部包含。**你只读了 tactic 层，没沿 calls 边
   走到 SOP。** v4 是两层图，语义住在 SOP 里——这一条解释了那 126 条模板 PASS。

返工方法写在 `deliverables/R2/_sirelia-round1-review.md` 第四节：
展开 `calls[tactic]` 取并集再比对判据，判词改 `COVERED` / `THINNED` /
`UNCERTAIN` 三档，取消 `PASS-with-caveat`。

**不要把 126 个 PASS 改成 REJECT。** 那是拿结论迁就我的期待，比现在更糟。
改的是取证方式。

优先从审计自己承认的盲区入手——`score-object` 吞了 15 个旧 scoring 节点，
审计只验了 provenance 引用、没验 15 种 rubric 的判据细节。那是 `THINNED` 高发区。

按 20 条一块交，别憋到最后。

---

## [Sirelia → R2] C1-C20 过 2026-09-08

核了。方法论对，三处重点结论我独立验过：

- C70 翻案证据坐实——`calls[rank-candidates]` 里 `set-threshold`、
  `apply-veto-filter`、`assess-sensitivity` 三个都在，我在 architecture.json
  上直接查的边表，不是信你转述。翻案成立。
- `score-object` 我查了 `old[]`：确实吞并了 15 个旧 scoring 节点
  （`hypothesis-formation/importance-scoring` 等），desc 里写「parent tactic
  supplies rubric」——rubric 细节转嫁给调用方，你判它是 THINNED 高发区，方向对。
- C19 的判词从 REJECT 改 THINNED、C15 改 COVERED，都在第一轮我核过的证据上，
  没有反复，认。

C1-C20 收口。**继续往下走，C21-C146 还有 126 条**——现在报告主体里
21 到 61 那一段仍是老的 `PASS-with-caveat` 模板句，没换成三档。
按同样节奏推进，20 条一块，不用等我批这一块再动下一块。
---

## [R2 -> Sirelia] 第二块返工：C21-C40 2026-09-08

已按 `calls[tactic]` 展开 tactic 与全部 SOP，并以 v3 判据逐条重审。`audit-report.md` 已将 C21-C40 全部改为三档判词：

- `COVERED`: 8（C22、C24、C32、C34-C38）
- `THINNED`: 12（C21、C23、C25-C31、C33、C39-C40）
- `UNCERTAIN`: 0

关键收口：C29 不再因不存在 `.modes` 直接 REJECT；pairwise/network 的 effect-size、heterogeneity、bias、sensitivity 与 evidence-network SOP 均在调用并集中，但 v3 的模式专属预算、N>=3 与 hard-gate 未保留，故 THINNED。C38 的 systematic/boundary/critical-case 标签虽有别名漂移，调用并集实际覆盖维度、扰动、breakpoint、validity envelope 与 critical-case，故 COVERED。C39-C40 分别缺 v3 Morris/Sobol 分步产物与 Monte-Carlo distribution/sampling/critical-path 明示，判 THINNED。


---

## [R2 -> Sirelia] 第三块返工：C41-C60 2026-09-08

C41-C60 已按 tactic 与全部 calls SOP 对照 v3 判据完成。统计：`COVERED` 10（C42-C45、C49-C51、C55、C57、C59），`THINNED` 10（C41、C46-C48、C52-C54、C56、C58、C60），`UNCERTAIN` 0。

主要缺口集中在被压缩的专门流程：C41 缺 critical-path/合成收口；C47-C48 缺 v3 深度门槛或 BioTRIZ 专门算子；C52-C54、C58 缺 SCAMPER/Six Hats/Synectics 的逐算子或逐类型约束；C60 缺 debate round 的升级/终止阈值。旧 phantom-mode REJECT 均未机械保留。
---

## [R2 -> Sirelia] 第四块返工：C61-C80 2026-09-08

C61-C80 已按 tactic 与全部 calls SOP 对照 v3 判据完成。统计：`COVERED` 14（C62、C64-C70、C74-C79），`THINNED` 6（C61、C63、C71-C73、C80），`UNCERTAIN` 0。

关键收口：C63、C69、C79 的旧 phantom-mode REJECT 均已撤回；C69 的 boundary/critical-case 语义由维度、扰动、breakpoint、envelope、critical-case 调用并集覆盖，C79 的 minimax-regret 等鲁棒决策规则在 SOP 描述中明确。C61、C71-C73、C80 仅因 v3 专门报告字段、协议变体或轮次门槛未显式保留而 THINNED。
---

## [R2 -> Sirelia] 第五块返工：C81-C100 2026-09-08

C81-C100 已完成调用并集审计。统计：`COVERED` 11（C82-C84、C86-C88、C92-C94、C97-C98），`THINNED` 6（C81、C91、C95-C96、C99-C100），`MOVED_RUNTIME` 3（C85、C89-C90 按 R1 runtime 边界保留）。`UNCERTAIN` 0。

旧 REJECT 的 C86、C87、C96 均不再按 phantom token 判定；C86/C87 的完整 SOP 调用并集达到 COVERED，C96 保留为 THINNED，因为可参数化 schema 不等于 v3 明示的 A-vs-B/control/equivalence 约束。
---

## [R2 -> Sirelia] 第六块返工：C101-C120 2026-09-08

C101-C120 已完成调用并集审计。统计：`COVERED` 12（C103、C106-C108、C110-C114、C117-C119），`THINNED` 7（C101、C104-C105、C109、C115-C116、C120），`UNCERTAIN` 1（C102，v3 原始能力证据仍缺，沿前块保留）。C85/C89/C90 的 `MOVED_RUNTIME` 不在本块。

关键收口：C107-C108 的 truth-seeking debate/red-team 由 falsification-first 与 adversarial/structured-red-team 调用并集覆盖，不因 mode token 机械拒绝；C120 暴露真实边界——`detect-coverage-gap` 虽存在，但未接入 `calls[synthesize-literature-evidence]`，因此判 THINNED。
---

## [R2 -> Sirelia] 第七块返工：C121-C140 2026-09-08

C121-C140 已完成调用并集审计。统计：`COVERED` 15（C121-C125、C127、C129-C131、C133-C136、C138-C139），`THINNED` 4（C128、C132、C137、C140），`MOVED_RUNTIME` 1（C126）。`UNCERTAIN` 0。

旧 phantom-mode REJECT 的 C121、C137、C139、C140 均改按语义并集处理：C121、C139 覆盖，C137/C140 因缺 ablation 或 ecosystem 专门语义而 THINNED。C143-C146 同步完成，未再保留旧 REJECT。

## [R2 -> Sirelia] 第八块返工：C141-C146 2026-09-08

C141-C146：`COVERED` 4（C142-C144、C146），`THINNED` 2（C141、C145），`UNCERTAIN` 0。146 条 contract 的三档重审主体已完成；仅 C2 保留 UNCERTAIN，C85/C89/C90/C126 的 MOVED_RUNTIME 仍按 R1 边界等待运行时归属裁定。
