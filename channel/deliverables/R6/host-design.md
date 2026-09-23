# R6 host design - batch 1

状态：Q4、Q5 已裁决，待 Sirelia 审核。

## Q4 267 个节点如何被 host 发现和调用

| 字段 | 内容 |
|---|---|
| 选择 | 采用现有 registry 路径；无 mode 节点读取正文的单一 contract，有 mode 的 22 个节点读取 `mode_contracts[选定 mode]`。`graph.json` 的 `modes` 是枚举权威，`capabilities.json` 提供 146 条能力回归索引与 `source_ref` 缓存，产品层按 R3 卡片投影。host 只消费这条路径，不自行扫描正文猜测节点。 |
| 理由 | R1 B 路已锁定每个 mode 的完整 Input/Output contract，禁止 node-level union contract。mode-bearing 卡片不投影具体 mode 或并集的 `requires`/`produces`，只声明 `modes`；否则会重新引入 B 路已拒绝的并集语义。host 选 mode 后回正文读取。代价是 catalog 不能独立完成契约判定。 |
| 影响 | 267 个 `SKILL.md` 的两个 contract 小节必须机器可解析；22 个 mode-bearing 节点各自只含一个 `mode_contracts` 顶层键，键集合与 graph `modes` 完全相等。无 mode 卡片沿用 R3 字段；mode-bearing 卡片以 `modes` 取代 `requires`/`produces`。host 先以 `source_ref` 定位节点，校验计划中的 mode 属于 graph 列表，再读取对应映射。mode 未指定、未知或映射缺失时，报错且不进入节点，不猜默认值、不静默回退；下游路由由八字段 Delta 的 `recommended_jumps` 承载。 |
| 证据 | `channel/deliverables/R1/mode-contract-format.md:5-34,120-122`（B 路语法、host 读取与 Delta 路由）；`channel/deliverables/R1/mode-output-ledger.md:119-121`（八字段与 `recommended_jumps`）；`v4/scripts/validate_graph.py:211-245`（frontmatter、固定小节、delta_fields 与 calls 引用校验）；`v4/docs/runtime-boundary.md:50-58,114-122`（正文 contract、catalog 卡片和 graph 映射）；`channel/deliverables/R3/entry-ux-spec.md:63-78,101-107`（catalog 归产品层、卡片字段）。 |

格式样例（R1 B 路 `mode_contracts`）：

````markdown
---
name: resolve-inventive-contradiction
description: "Resolve technical and physical contradictions."
---

## Input contract

```yaml
mode_contracts:
  technical-contradiction: &contradiction_input
    required: [contradiction_statement, conflicting_requirements, system_components]
    optional: [operating_conditions, target_metrics, known_principles]
    constraints: [improvement_and_worsening_parameters_must_be_explicit]
  physical-contradiction: *contradiction_input
  separation: *contradiction_input
```

## Output contract

```yaml
mode_contracts:
  technical-contradiction: &contradiction_output
    produces: [contradiction_resolution, transformed_configuration, residual_conflicts, candidate_ideas]
    delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
  physical-contradiction: *contradiction_output
  separation: *contradiction_output
```
````

对应的既有 R3 catalog 卡片形状（声明 mode；不投影具体 mode contract）：

```yaml
id: resolve-inventive-contradiction
user_label: Resolve inventive contradiction
description: Resolve technical and physical contradictions.
when_to_use: when conflicting requirements must be reconciled
modes: [technical-contradiction, physical-contradiction, separation]
confidence: registry
source_ref: v4/skills/resolve-inventive-contradiction/SKILL.md
next_call: []
```

mode-bearing 卡片不含 `requires`/`produces`；host 选定 mode 后必须回正文读取对应 `mode_contracts`。无 mode 卡片的 `requires`/`produces` 仍只是索引摘要；若与正文冲突，以正文为准并阻止该卡片继续路由，交由 N1/N2 修复生成链。

Q4 权威边界补充：mode 枚举仍由 `v4/registry/graph.json` 提供；22 个 mode-bearing 节点的正文 contract 按 R1 B 路拆为 `mode_contracts`，host 选定节点后必须确认显式 mode 并读取同名映射。mode 未指定、未知或映射缺失时，报错而非猜默认值；下游路由由 Delta 的 `recommended_jumps` 承载，不增加 `(tactic, mode)` 图维度。

## Q5 tactic 内部执行顺序

| 字段 | 内容 |
|---|---|
| 选择 | host 按 tactic 正文 `## Execution protocol` 的编号顺序执行；每个编号中列出的 SOP 按出现顺序调用。`registry/graph.json` 的 `calls` 只声明 tactic 可组合的 SOP 词汇，不声明线性顺序；`jump` 只允许同类型节点之间的合法交接。 |
| 理由 | 现有 51 个 tactic 正文已经把依赖、阶段和可选分支写在 `Execution protocol`；架构明确声明 calls “is not a mandatory linear order”。让 agent 临场重排会使 51 份正文失去确定性，单看 calls 又无法恢复依赖。代价是 tactic 作者必须把默认顺序写清楚；分支只能使用正文已有的 mode/deviation 规则。 |
| 影响 | 每个 tactic 的 `## Execution protocol` 必须给出可执行的编号步骤，并在引用 SOP 时使用 graph 中同名节点；校验器会拒绝未在 `calls` 声明的 SOP 引用。host 在每一步只传递当前 state slice，步骤完成后接收八字段 Delta；不增加重试、退避、超时、错误分类或监控状态机。 |
| 证据 | `file-transfer/2026-08-23-22-16-dare-v4-architecture.json:17-23`（calls 非线性序列、jump 语义、Delta 所有权）；`v4/scripts/validate_graph.py:225-232`（Execution protocol 引用必须在 calls）；`v4/docs/runtime-boundary.md:46-58,120-126`（按 protocol/SpecView 路由与 state slice）；`v4/skills/formulate-hypotheses/SKILL.md:24-36`（已落盘 tactic 顺序样例）。 |

格式样例：

```markdown
## Execution protocol

1. State the gap/observation and relevant theory or anomaly.
2. Generate candidate hypotheses without premature filtering.
3. Operationalize variables and relationships; state scope and boundary conditions.
4. Check falsifiability and, for competing mode, create discriminating predictions and a comparison matrix.
```

host 的调用顺序为 1 -> 2 -> 3 -> 4。`calls` 中列出的 SOP 只约束“可调用集合”；若 protocol 中明确写出 SOP 名称，该名称必须存在于该 tactic 的 `calls` 边中。若 protocol 给出 `Deviation` 或 mode 分支，host 仅按该正文条件选择分支，并把选择理由写入已有 `decisions` Delta；没有正文条件时不得自行重排。

## 本批结论

- Q4：正文 contract → 现有 capabilities catalog → graph 节点映射。
- Q5：正文 Execution protocol 定序；calls 不定序。
- 未修改任何 `v4/` 文件，未新增机制。

## Q1 host 的形态

| 字段 | 内容 |
|---|---|
| 选择 | 选 A：Claude Code、Codex、opencode、openclaw、pi、dsh、cline 等现成 agent harness 直接充当 host。host 是 harness 在一次 DARE 会话中承担的职责，不是 DARE 要开发、部署或适配的运行时构件；同一 agent 读取仓库文件，执行控制面规则与选定的 tactic/SOP。 |
| 理由 | DARE 的产品定位是纯 skill：没有 application code、runtime 或 framework，现成 harness 本身就是 runtime；选 D 会引入 clone 后还须部署的中间层，直接破坏 zero-infrastructure。B 同样新增脚本运行时，C 则把科研图误作 MCP tool 图。A 的代价是执行正确性依赖 harness 忠实遵循文本契约，不能靠单独程序提供机械保证。 |
| 影响 | R1 的十一处 host 职责不删减，只由当前 harness 中的 agent 直接完成：读取和追加 Markdown checkpoint、重建 SpecView、读取 context、做 preflight、按既有优先级及 catalog/graph 路由、加载 state slice、执行节点并写入八字段 Delta。不得要求 DARE runtime、wrapper、adapter、daemon 或 provider-specific 配置。科研图仍只有 tactic/SOP 两种可执行节点。 |
| 证据 | `README.md:123`（“There is no application code, no runtime, no framework”及“runtime is CC itself”）；`README.md:208`（zero infrastructure、clone and go）；`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:17-23,35-49`（edge/state/boundary）；`v4/docs/runtime-boundary.md:4-24,112-130`。 |

## Q2 SpecView 重建由谁执行

| 字段 | 内容 |
|---|---|
| 选择 | 由直接充当 host 的 agent 按规范回放 checkpoint 并重建；不使用脚本、服务或“确定性重建器”构件。确定性来自同一事件流上的无歧义投影规则，而不是执行者的实现形态。 |
| 理由 | Q1=A 后再要求脚本会暗中恢复 D 路。SpecView 是既有 Markdown 事件的投影，不需要新持久化对象：任何 harness 只要逐条执行同一规则，就必须得到同一字段值、active item 和下一路由。代价是每次回放占用 agent context，且一致性只能通过输入/输出复算验收，不能由独立二进制实现担保。 |
| 影响 | agent 严格按 checkpoint 数字序号、再按同一 checkpoint 中 `decisions` 的出现顺序回放；只有五类显式 decision 可改变 SpecView，`open_questions` 只能按 `plan_item_id` 挂接，其余 Delta 字段不得推断计划结构。同一 `decision_id` 取序号最新的明确决定并保留替换原因；`plan_item.update` 不改变创建顺序，`plan_item.retire` 只移出 active 集合。输出固定八个 SpecView 字段，active item 取创建顺序中首个未完成且依赖满足者。缺少所需 ID/显式决定或存在未裁决冲突时不猜值、不进入科研节点。objective、requires、completion gate 或依赖被明确改变时，旧 complete 变为 `needs_revalidation`；描述、排序或注释变化不触发。 |
| 证据 | `v4/docs/runtime-boundary.md:29-48,91-99,103-110,118-126`；`channel/deliverables/R1/runtime-boundary.md:2.1-2.3,3.3-4,5.1-5.2`。 |

### host-neutral 对 267 份正文的影响

host-neutral 的含义是：任一能读取仓库文件并执行 Markdown 指令的 agent harness，都能直接消费 DARE 的正文、registry、context 与 checkpoint，不需要 DARE 中间层；它不只是“不绑定某个 provider”。这不对 267 份正文提出新要求，也不需要正文返工：现有正文已经使用通用 Markdown/YAML、固定 contract 与 `Execution protocol`，harness 名称和 host 配置路径均为 0 命中。6 份含 `provider` 字样的正文都在禁止 provider 绑定或记录已压缩的 provenance，不构成依赖。后续正文只需继续遵守既有禁令：不加入 harness/provider 专用调用语法、配置路径或科研图 tool edge。

## Q3 事件流的物理载体

| 字段 | 内容 |
|---|---|
| 选择 | 采用既有追加式 Markdown：`context/INDEX.md` 加 `context/<timestamp>-<phase-slug>.md`，每个 checkpoint 追加一个顶层段落；不改成 JSONL。Markdown 是物理载体，固定九字段是可解析记录格式。 |
| 理由 | R1 已锁定单 Phase 单文件、追加 checkpoint、人工可读；现有 host 职责要求按 checkpoint 序号回放。改 JSONL 会让已写出的 context 与格式约束整体返工，且没有现成 JSONL 机制。代价是重建器要按固定字段和序号解析 Markdown；不增加第二种载体。 |
| 影响 | 所有 tactic/SOP/host checkpoint 使用 `Checkpoint, Phase, Source, Status, Input slice, Process, Results, Delta, Open questions`；Delta 八字段固定，空值写 `[]`。`Status=complete` 才是可恢复落点，`partial` 保留但不能证明阶段完成。冲突追加 uncertainty，不改旧段落。 |
| 证据 | `v4/docs/runtime-boundary.md:60-99`；`channel/deliverables/R1/runtime-boundary.md:3.1-3.4`。 |

## Q6 最小可执行闭环

| 字段 | 内容 |
|---|---|
| 选择 | 用现有 `rank-candidates` tactic 的 `direction-selection` mode，按其正文顺序执行：规范化候选与 criteria schema -> 选择 mode -> 校验已提供权重 -> `score-object` -> `aggregate-ranking` -> `assess-sensitivity`，最后由 host 追加一个 `complete` checkpoint。输入提供 `candidates, criteria, decision_rule` 与固定权重，避免引入额外机制。 |
| 理由 | 这是一个已在 graph 中存在的 tactic 与下游 SOP 路径；它能从明确输入产生 ranking、sensitivity 和 recommendation，足以验证科研图执行层。没有新节点、新格式或伪造执行器。代价是只验证一个科研分支；SpecView 重建、preflight 与 catalog 取卡仍未实跑，不把它们冒充为 host 验收。 |
| 影响 | 端到端顺序固定为：读取 `context/INDEX.md` -> 回放 Phase checkpoint 得到 SpecView -> context preflight -> 从 `capabilities.json` 取得 3-5 张卡片并以 `source_ref` 映射 `graph.json` -> 选 `rank-candidates` 的首个 active item -> 传入当前 state slice -> 按 tactic protocol 完成 schema 规范化、mode 选择、权重校验、评分、聚合和敏感性分析 -> 汇总八字段 Delta -> 追加 checkpoint。执行结果必须能从该 checkpoint 再次重建同一 SpecView 与下一路由。 |
| 证据 | `v4/registry/graph.json` 的 `rank-candidates` calls（`normalize-gap`, `define-criteria`, `score-object`, `aggregate-ranking`, `assess-sensitivity`）；`v4/skills/rank-candidates/SKILL.md:16-31`；`v4/docs/runtime-boundary.md:29-38,46-58,71-99,114-130`。 |

Deviation：`rank-candidates` 的另外六个 calls——`elicit-weights`、`normalize-comparison-scale`、`check-dominance`、`set-threshold`、`apply-veto-filter`、`assess-goal-feasibility`——在本次 `direction-selection` 最小闭环中不调用。它们分别保留给权重未给定、尺度需转换、支配关系审查、非补偿阈值、否决筛选或目标可行性模式；不从 graph 删除，后续由相应输入模式验证。

组件与调用顺序：

```text
context/INDEX.md
  -> Phase context Markdown replay
  -> SpecView reconstruction
  -> ResearchContext preflight
  -> capabilities catalog card
  -> graph node: rank-candidates(direction-selection)
  -> normalize candidate/criteria schemas
  -> select direction-selection mode
  -> validate supplied weights
  -> score-object
  -> aggregate-ranking
  -> assess-sensitivity
  -> ResearchStateDelta (eight fields)
  -> complete checkpoint append
```

最小 checkpoint 样例（沿用既有九字段）：

```text
Checkpoint: 0001-2026-09-13T12:00:00Z
Phase: direction-selection
Source: rank-candidates
Status: complete
Input slice: candidates=gap-A,gap-B; criteria=impact,feasibility; decision_rule=direction-selection; weights={impact:0.6,feasibility:0.4}
Process: normalize schemas -> select direction-selection -> validate weights -> score-object -> aggregate-ranking -> assess-sensitivity
Results: gap-B ranked first; ranking stable under declared sensitivity scenarios
Delta: {findings: ["gap-B is the leading direction under supplied criteria"], evidence_updates: [], hypothesis_updates: [], assumption_updates: [], uncertainties: [], decisions: ["select gap-B as current direction"], open_questions: [], recommended_jumps: []}
Open questions: []
```

Q6 只证明最小闭环可执行；未把 agent 异常处理、调度策略或监控状态机写入 host 设计。
