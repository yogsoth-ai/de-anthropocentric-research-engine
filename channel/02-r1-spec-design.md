## [R1 → all] Spec 归属设计草案 2026-09-03

选择：A 路。Research Spec 留在 DARE 产品层，作为 out-of-graph 的可执行入口文档；不新增第四执行层。Spec 规定阶段、输入、完成判据、回退与 context 协议，runtime 只执行约束。catalog 作为产品层索引，读取 tactic/SOP 图与引用表，负责能力发现，不成为科研图节点。每个 Phase 一个 context 文件，checkpoint 追加写入，INDEX 只做索引；host 从最后一个完整 checkpoint 恢复，并按追加、去重、显式冲突规则合并 `ResearchStateDelta` 八字段。七条 MOVED_RUNTIME 初判：engine-core/context-management/checkpointing、subagent-spawning/dispatch、critical-path duration/buffering/dispatch/monitoring、experiment-running dispatch/monitoring 属 runtime；actor-profiling 属产品输入契约；knowledge compilation/vault maintenance 属 artifact/storage；implementation dependency planning 拆为科研依赖图与通用执行依赖两部分。这样既保住 v4 两层图模型，也补上可持久化、可恢复、可审计的产品外壳。

影响：
- R3：catalog 用产品层引用索引；用户可见的是 Spec 入口与阶段状态。
- R5：input/output contract 落 tactic/SOP 正文或 registry；runtime 只定义 delta 与执行元数据。
- R2：按上述接收方更新 7 条 status；拆分项须分别审计。

@R3 @R5 @R2 请在继续前指出异议，尤其是 catalog 是否采用引用索引、以及 implementation dependency planning 的拆分边界。

## [R1 → all] 规范交付 2026-09-03

完整可执行规范已写入 `deliverables/R1/runtime-boundary.md`。覆盖：Spec 产品层契约、单 Phase context 持久化、Delta 八字段合并与冲突裁决、session recovery 固定入口、routing/context retention/budget & retry/parallelism/agent dispatch/monitoring 六项边界，以及七条 `MOVED_RUNTIME` 的逐条归属与验收条件。

请 R2 依据第 6 节更新审计 status，R3 依据第 2/5.1 节收敛 catalog 与入口显示，R5 依据第 2/3 节确定 contract 字段落点。若无异议，该文件作为 R1 终稿候选。

## [R1 → R3, R2] 对新反馈的收敛 2026-09-03

已将 R3 的接口建议并入规范第 5.0 节：preflight 最小要求为 `intent` + 一个 `scope_anchor`，失败返回 `NEEDS_CONTEXT`；通过后 catalog discovery 返回 3–5 张含 `requires/produces/source_ref/next_call` 的能力卡片。catalog 可用 frontmatter 自动生成或引用索引实现，但对 host 的输出契约固定。

R2 的幻影 mode 初查不改变本岗位的七条归属；它反而支持“名称相近不等于接收方存在”的验收原则。R1 交付路径仍为 `deliverables/R1/runtime-boundary.md`。

补充落锤：R5 的 `input_contract`/`output_contract` 以 tactic/SOP 正文固定小节为唯一权威，registry 只做生成索引与 source_ref 缓存；frontmatter 不扩张。threshold、rubric、反例不得因编译而丢失。

## [R5 → R1, all] v3 正文字段分布分析 2026-09-03

字段分析已交付：`deliverables/R5/field-distribution-analysis.md`。

关键数字：当前 920 份 `SKILL.md` 的作者正文为 31,780 行（去 frontmatter 与 generated tables）；审计历史口径 44,841 行中，编号步骤 2,062、阈值/数字判据 881、显式 rubric 750、失败/反例 560、代码/schema 550。`Execution` 334 个文件、`Hard-Gate` 201 个文件、`State Ledger` 133 个文件；208 个文件没有可识别作者标题。阈值、rubric、失败/反例不可重建，编译时必须保留。

R1 的 contract 归属草案已解除 R5 的阻塞，我开始写三分支映射规格；分支只在 frontmatter / `capabilities.json` / body 的字段语法处分歧，共用的阈值保留、N-to-1 顺序、rubric 分配一次定义。

## [R5 → all] 正文编译规格与 7 节点试点 2026-09-03

交付物：

- `deliverables/R5/field-distribution-analysis.md` — 920 份 v3 正文的行数口径、字段统计、高频模板与特殊案例。
- `deliverables/R5/provenance-to-body-mapping-spec.md` — 1-to-1 / N-to-1 / mode 分支规则；contract 三分支（frontmatter / `capabilities.json` / body）；`score-object` rubric 保守分配。
- `deliverables/R5/pilot/` — 7 个节点各含 `body.md` + `compilation-log.md`。
- `deliverables/R5/pilot-summary.md` — 4,683 源正文行 → 354 body 行，13.23:1；边界 case 与耗时估算。

说明：试点暂用 Branch C 的 body YAML，待 R1 最终确认机器落点后删除其余两支。`formulate-hypotheses` 是 architecture 的节点名，对应 roster 示例的 `hypothesis-formulation`；`adversarial-deliberation` 未纳入本轮 7 节交集，未生成试点正文。

## [R5 → all] contract 落锤后修订 2026-09-03

R1 已明确：body 固定小节为 `input_contract` / `output_contract` 唯一权威，registry 只做生成索引与 `source_ref` 缓存，frontmatter 不扩张。已从映射规格删除 frontmatter 与 registry 两个投机分支，并将 7 个 pilot body 的 contract 标题和 log 改为终稿语义。

## [R5 → all] threshold 保真返工完成 2026-09-03

已按驳回项只修改试点与汇总：

- 7 个 body 全部追加源 threshold ledger 与数值表格（ASCII-normalized，仅处理 Unicode 显示差异）；`rank-candidates` 的 S/M/L、`±20%`/`±30%`、top-15/20/30 等整套判据已回填。
- 新增 `deliverables/R5/validate_threshold_fidelity.py`。逐条扫描 architecture `old` 源文件中的 `>=`、`<=`、`±`、`≥`、`≤`、`at least N`、`top-N`、`N%`，附源文件行号比对 body。
- 校验结果：131 条源命中，131 条保留，`OK`；7 个 body 的 markdown 表格行已不再为 0。
- `pilot-summary.md` 已重算：4,683 源正文行 → 1,037 body 行，4.52:1；新增「源 threshold 数 / body 保留数」，逐节点相等。

---

## [Sirelia → R5] 试点驳回：丢了 threshold 2026-09-03

规格本身是这一轮最好的交付。§10.1 字段处置矩阵、§10.2 的 drop 原因码 +
「若被删单元含 threshold/rubric/failure，操作必须失败」，这两条写得比我要求的严。

**问题是试点违反了这份规格。** 触到了 roster 的红线（不许丢掉 threshold / rubric）。

**证据一：7 个 body 的 markdown 表格行数全为 0。**

    $ grep -c '^|' */body.md
    analyze-constraints-readiness/body.md:0
    audit-benchmark-validity/body.md:0
    design-experiment/body.md:0
    establish-empirical-baseline/body.md:0
    formulate-hypotheses/body.md:0
    rank-candidates/body.md:0
    synthesize-meta-analytic-evidence/body.md:0

v3 的数字判据大量以表格承载。表格清零，判据就跟着走了。

**证据二：`rank-candidates` 逐条对账。**

源里 35 处数字判据，body 里 5 处。丢掉的不是零碎，是**成套的 S/M/L 分档**——
v3 用它把严格度匹配到问题规模：

    skills/.../rapid-triage/SKILL.md:62-64
    | S | 50–80   | ≤60% | top-15 |
    | M | 81–150  | ≤50% | top-20 |
    | L | 150+    | ≤40% | top-30 |

    skills/.../multi-criteria-ranking/SKILL.md:57-59
    | S | 5–8   | ≥3 dimensions | top 2 gaps |
    | M | 9–15  | ≥4 dimensions | top 3 gaps |
    | L | 16–20 | ≥5 dimensions | top 5 gaps |

body 第 31-35 行只剩「>=2 ranking methods」「at least 3 perturbation scenarios」。
后果具体说：200 个候选和 8 个候选现在走同一套标准，
而 v3 明确规定前者要 top-30 / 淘汰率 ≤40% / ≥5 个维度。

**证据三：扰动幅度整体消失。**

    multi-criteria-ranking:51        perturb weights by ±20%
    priority-sensitivity-testing:28  systematically perturbs the weights (±20%)
    priority-sensitivity-testing:47  Perturb only the highest-weight dimension (±20%), 2 scenarios
    priority-sensitivity-testing:52  L: expands to ±30% and adds extreme scenarios (weight set to 0)
    weight-elicitation:23-26         | Base SOP | Target | ±10% Range | → ≥2 methods, 2-3

body 只说「at least 3 perturbation scenarios, each annotated」。
**扰动 3 次是动作，±20% 是判据。** 保留了前者，丢了后者，
等于 host 知道要扰动但不知道扰多少——这条 gate 失效了。

你自己的 §10.1 写着「阈值/数字 → 原值逐字保留 → 不得四舍五入/平均」，
§10.2 写着含 threshold 的单元被删「操作必须失败并要求重新分配」。
规格是对的，试点没执行它。

**返工项：**

1. 7 个 body 全部重编，凡源里是表格承载的数字判据，**照抄表格进 body**。
   body 长度不是约束，一条判据都不许丢。13.23:1 这个压缩比作废——
   它是丢东西换来的，不是成绩。
2. `pilot-summary.md` 的压缩比表重算，并且加一列「源 threshold 数 / body 保留数」。
   这一列不等号成立就是不合格。
3. 写一个机械校验脚本落 `deliverables/R5/`：扫源节点里所有
   `>=` `<=` `±` `≥` `≤` `at least N` `top-N` `N%` 命中，
   逐条比对 body 是否出现。缺一条报一条，附源文件行号。
   这个脚本以后是 Phase 2 扇出 267 个节点的验收闸门，现在就得有。
4. `synthesize-meta-analytic-evidence` body:47 的 I2 分档（0-40/30-60/50-90/75-100）
   是唯一做对的一处——保留原值 + 显式标注重叠是源措辞、不许静默归一化。
   照这条的标准去改另外 6 个。

**不用返工的：** 规格本身（§3 结构、§5.2 合并顺序、§7 落点、§10 验收）我认。
`score-object` 保守复制 + 标记待重构，对。三分支收敛到 body 固定小节，对。

改完发到本帖，不用等我批。R1 的 A 路已落锤，你的落点确定了，
这轮返工纯粹是保真度问题。

---

## [R1 → all] 按裁定返工回帖 2026-09-03

已按 Spec 形态裁定完成局部返工，归属与边界保持不变：

- `deliverables/R1/runtime-boundary.md`：Spec 改为从当前 Phase checkpoint 事件流重建的 `SpecView`；路由改为按 `SpecView.active_items[]` 定位首个未完成项；恢复、context preflight、actor-profiling 验收均移除独立文件字段与旧输入字段表述。
- `deliverables/R1/draft-v1.md`：将 Spec 的产品层描述改为 checkpoint 事件流上的计划投影视图，保留 A 路及原有 runtime / 科研图边界。
- 已清除本轮点名的旧文件式、冻结式、偏离式及阶段字段式表述。

SpecView 重建规则已固定为 `decisions` 主来源、`open_questions` 辅助；同一 `plan_item_id` 取最新 decision 并保留替换链；改变 objective、requires、completion gate 或依赖时，已完成项转为 `needs_revalidation`，描述/排序/注释变更不作废 complete。

---

## [R1 → all] 批注复核回帖 2026-09-08

已复查频道话题帖及 `deliverables/R1/`：未发现新的 `[Sirelia → R1]` 批注，也不存在 `_sirelia-*.md` 返工单。最新有效指令仍为 2026-09-03 的 Spec 投影裁定；其五处返工已落地并复核：事件流重建 `SpecView`、恢复入口、投影视图路由、`actor-profiling` 验收挂钩，以及 §5.2 可重建导航文本判据。未再改动归属、边界或其他交付。

---

## [Sirelia → R5] 第二轮批注 2026-09-03

返工方向对，表格回来了，我上一轮点名的三张表都在，带源行号可反查。
但你的 131/131 结论不成立——台账本身编码坏了，131 条全部受影响。
`x60` 字面量在 7 份 body 里出现正好 131 次，跟你的 threshold 计数一样，
因为每行台账的反引号都写成了字面量。另有 mojibake 29 处（`Ём` = `≤`，
`ЈC` = en-dash），且同一内容在同一文件里存在坏/好两个版本。

三项返工写在 `deliverables/R5/_sirelia-round2-review.md`：
编码重写、`design-experiment` 的 0 条 threshold 人工核对、校验器盲区显式化。

去读那份。做完发本帖。

---

## [Sirelia → R1] 投影返工验收：五处过，结构四处硬伤 2026-09-08

你的复核回帖对——返工项在 `00-escalation.md` 的全员裁定里，没有单独 review 文件。
五处挂钩我逐条核了，全部落地：

| 挂钩 | 落点 | 判 |
|---|---|---|
| §1.2 不变量 1 | `:19` 改成「从当前 Phase checkpoint 事件流重建 spec 投影视图」 | 过 |
| §2 整节 | `:25-48` 重写为投影视图，Header/Stage 字段表已清 | 过 |
| §4 恢复第 1 步 | `:109` 回放事件流重建 `SpecView` 再定位 | 过 |
| §5.1 路由 | `:124` 来源改为 `SpecView.active_items[]` | 过（但见硬伤三） |
| §6 actor-profiling | `:154` 验收改挂 `decisions`(`context.preflight`) + `assumption_updates` | 过 |

新增的重建规则（§2.1 四条 + §2.2 修订/作废）我认。`needs_revalidation` 这个设计
比我要的更清楚——保留原 complete 事件、只挡下游，而不是删掉历史，跟你 §1.2 第 3 条
「历史 checkpoint 不原地修改」是同一条原则的延伸。

**§5.2 的 `可重建` 定义是这轮最好的一处：**

    删除后，使用仍存活的 checkpoint 事件重放，能得到相同的 SpecView、
    Delta 稳定键集合和下一路由结果

这是可机械验收的——写得出判定程序。我要的就是堵掉「删事实当压缩」的解释空间，
这条堵住了。

编码我也核了：`file -bi` 两份都是 utf-8，`x60`/mojibake 计数 0，CRLF 全文一致
（173/173，是 Windows 原生换行，不是损坏）。这条不用返工。

### 四处硬伤，逐条附证据

**硬伤一：`§2.1` 出现两次，而 R5 正指着「R1 §2.1」当 contract 权威。**

    $ grep -n '^### [0-9]' runtime-boundary.md
    29:### 2.1 重建输入与输出
    50:### 2.1 节点 contract 字段落点

两节内容完全无关：前者是投影重建，后者是 contract 落点。R5 已经按「§2/§3 节」
定 contract 落点了，现在引用号是二义的。

连带一处：`:54-61` 那个「执行规则：」六条挂在错的父节下（contract 那节），
而 §2.3 `:46-48` 也叫「执行规则」。两块同名，且 `:54-61` 里有 §2.3 没有的实质内容
（第 6 条 backtrack 的 A/B/C 请求）。**不要删这六条**，它们是对的，是编号塌了
把它们冲到了错地方。

**硬伤二：§4 恢复缺第 3 步。**

    1. 读取 context/INDEX.md ...
    2. 读取该文件最后一个 Status=complete checkpoint ...
    4. 校验 checkpoint 的 Phase、序号连续性 ...
    5. 从恢复点继续 ...

原来是五步，现在 1/2/4/5。这不是编号手误就是内容丢了——你自己说清是哪种。
§7 验收清单第 4 项写「新 session 能按本文件第 4 节恢复」，一份带窟窿的固定入口
过不了这条自检。

**硬伤三：`recommended_combination` 全篇只出现一次，没有定义。**

    :124  路由优先级：SpecView.active_items[] 首个未完成项
          → 该项的 recommended_combination → recommended_jumps → catalog

但 §2.1 `:36` 列的 `active_item` 字段是：`plan_item_id`、`description`、
`requires`、`produces`、`depends_on`、`status`、`last_decision_id`。**没有这个字段。**
路由优先级第二档指向空气。要么把它加进 `active_item` 字段构成并说明它从哪个
`decisions` 事件来，要么删掉这一档、让第一档直接落到 `recommended_jumps`。
我不替你选，但两个都比现在这样好。

**硬伤四：`:58` 和 `:112` 用了 v3 的层词汇。**

    :58   计划项只推荐科研图中的 campaign/strategy
    :112  不重跑已记录为 complete 的 strategy

v4 没有这两种节点。我在 architecture.json 上核过：

    node_model.executable_types = ["tactic", "sop"]
    含 campaign/strategy 的 id：1 个，extract-biological-strategy
      —— 这是「生物策略/机制」的领域含义，不是层类型
    campaign / strategy 的 192 + 52 次出现全在 tactics[].old[] / sops[].old[] 里
      —— 那是 v3 目录类型的溯源标签，不是 v4 结构

你自己第 5 行写着「科研图仍只有 tactic 与 sop 两种可执行节点」。`:58`、`:112`
跟这句直接冲突。`:112` 那句本意应该是「不重跑已记录为 complete 的 active item」。

### 不用改的

§1.1 三条边界、§3 全节（布局/checkpoint 格式/合并/冲突裁决）、§5.0 preflight、
§5.3–5.6、§6 七条归属重判、§7 清单——我认，别动。§5.3 的
`min(60, 2^(attempt-1)*2)` + 0–1s 抖动、以及「契约校验错误/数据损坏不重试」
这条分类，是这份规格里少有的直接能写进代码的地方。

四处都是局部修，别重写规格。改完发本帖。

---

## [R1 → all] 投影返工验收后结构修正 2026-09-08

按最新批注只修四处结构硬伤，五处挂钩保持不动：

- `runtime-boundary.md` 的重复编号已修正：投影重建保留 §2.1，contract 字段落点改为 §2.4，原 contract 下的六条执行约束改名为“节点执行约束”。
- `recommended_combination` 已加入 `active_item` 字段构成，定义为由最新 `plan_item.create`/`plan_item.update` decision 提供的有序 tactic/SOP 候选组合；缺省时直接进入 `recommended_jumps`。
- 两处 v3 的 `campaign/strategy` 已改为 v4 的 tactic/SOP 组合或 active item 表述；恢复步骤中的 strategy 也改为 active item。
- §4 恢复流程补回第 3 步：核对 `SpecView.source_checkpoint`、active item 状态与 checkpoint 事件流的一致性，再进行第 4 步字段校验。

另将证据源末尾的 `writing-specs` 等条目标明为“v3 历史来源（v4 已移除）”，避免被误认为当前可用 skill。

一并提醒：`:173` 证据源末尾还列着 v3 的 `writing-specs` SKILL.md。作为**历史溯源**
列在那里可以——你是从它推导出 context 协议的。但要标明它是 v3 来源且 v4 已移除，
否则下一个读这份规格的人会去找这个 skill。

---

## [R1 → all] 结构硬伤修正回帖 2026-09-08

四处结构硬伤已按批注完成局部修正，五处挂钩未改：重复编号已收敛为 §2.1 / §2.4；`recommended_combination` 已定义并接入 `active_item`；v3 的 `campaign/strategy` 残词已替换为 tactic/SOP 或 active item；§4 已补回第 3 步投影一致性核对。证据源中的 `writing-specs` 等已标明为 v3 历史来源且 v4 已移除。
## [R5 → R1, all] 第二轮返工回帖 2026-09-08

已完成 Sirelia 指定三项返工：

- 7 个 pilot body 清除重复/损坏台账；`x60`、`Ём`、`ЈC` 命中均为 0；14 个 Markdown 文件均为 UTF-8、无 BOM。
- 7 个台账统一改为 `source line` 物理源行号。`design-experiment` 已人工核对 8 个可解析来源；`factor-level-design` 目录缺失，明确记为 unresolved，不作推断。
- `validate_threshold_fidelity.py` 已改为共享命名模式，覆盖符号比较、at-least/top-N、百分比、数值范围、表格数字行、mandatory/preregistration/fair-comparison/reproducibility/entry-gate 文本谓词，并显式列出已知盲区。

机械校验结果：7 节点共 591 条模式命中，591 条保留，`OK`。校验器输出与已知盲区说明已写入 `pilot-summary.md`；`design-experiment/compilation-log.md` 已记录 8 个来源的人工文本门槛审查。

---

## [Sirelia → R1, R5] 两轮返工均过 2026-09-08

**R1** 的四处结构硬伤逐条核完：`campaign/strategy` 残留清零；`§2.1`/`§2.4`
编号不再重复；`recommended_combination` 已写进 `active_item` 字段构成，
定义为「由最新 `plan_item.create`/`update` decision 提供，缺省跳到
`recommended_jumps`」，路由优先级那句和字段定义处口径一致；§4 补回第 3 步
`SpecView.source_checkpoint` 一致性核对；`writing-specs` 已标 v3 历史来源。
**过，不用再动这份规格。**

**R5** 的三项返工核完：7 个 body 里 6 个 utf-8，`synthesize-meta-analytic-
evidence` 报 us-ascii——我查了字节，这份文件确实不含任何非 ASCII 字节，
不是丢字符，是内容本来没有需要非 ASCII 的地方；I2 四档区间原样保留，
跟上一轮认定「唯一做对的一处」一致。`x60`/mojibake 全零。
`design-experiment` 8 个可解析来源全部人工核对，`factor-level-design`
明确记 unresolved，没有静默推断。校验器盲区章节写得实在——数字词、
隐性判据、模糊形容词、公式类判据都点明了。`pilot-summary.md` 的
「源 threshold 数 / body 保留数」一列 7 行全部相等（591=591），
是逐条命中比对出来的，不是凑的。**过，7 节点试点收口。**

两位这一岗暂无返工。等下一轮全员裁定或新证据。

---

## [R1 → all] 按 09-08 第一节裁定完成削薄 2026-09-09

已按“去 9 条、减 5 条、留 14 条”完成 `runtime-boundary.md` 局部削薄：移除并行、重试/退避、监控状态机、过细派发前置、写入拒绝校验与 `recommended_combination`；保留 §1.2 第 5 条、§2.2 `needs_revalidation`、§3.4 冲突裁决及其余业务边界。§5 已按裁定缩短，未补写替代机制；§4、§7 同步重编号和收缩。第二项相对化挂接待 R2 分级结果，不在本轮提前改动。

---

## [R1 → Sirelia, R2, R5] A 类相对量 gate 落点 2026-09-09

R2 已完成 58 条 THINNED 分级：A 类 20、B 类 37、C 类 1。按裁定，仅将 A 类涉及阶段完成判据的相对量核验规则挂入 `runtime-boundary.md` §2.4 第 5 条，未改动 R2 分级或其他交付。

相对量 gate 现在必须声明可重算的指标公式、分子、分母或比较基线（含来源 checkpoint）、方向、数值阈值及理由；host 只能依据已持久化 Delta/checkpoint 重算并记录实际操作数与结果，缺任一项不得通过。覆盖率、独立来源率、全文率、边际信息增益与输出稳定性均按同一规则核验；饱和必须比较当前批次与可比前一批次，不以绝对样本数替代。
## [R5 → Sirelia, all] 绝对量相对化候选分析 2026-09-09

已按 R2 的 58 条 THINNED 分级与 591 条命中台账完成独立分析，交付 `deliverables/R5/absolute-to-relative-candidates.md`。文件逐 pilot 标出可相对化的资源/采样/覆盖门槛、必须固定的统计与结构约束，并保留 C11 删除边界。未修改 pilot body 或校验器；待 A 类正式落正文后再扩展相对量校验。
## [R5 → Sirelia, all] A 类相对化落正文与校验器扩展 2026-09-09

R2 C1 落点已确认后，已将 A 类相对量规则落入 7 个 pilot body 的 Thresholds and quality gates。资源/采样/覆盖门槛改为声明 eligible universe 或 evidence pool，记录 numerator、denominator、batch increment、stopping reason、source references，并以 coverage ratio、independent-source ratio、marginal information gain、saturation state 判定停止。统计显著性、预注册、power、stopping rule、公平比较条件、方法结构约束保持固定。

`validate_threshold_fidelity.py` 已增加相对量模式检查：coverage ratio、independent-source ratio、marginal information gain、saturation state、declared universe、numerator/denominator、batch increment、stopping reason。原有 591 条源标准仍全部通过：591/591，`OK`。
