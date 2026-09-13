# R6 host design - batch 1

状态：Q4、Q5 已裁决，待 Sirelia 审核。

## Q4 267 个节点如何被 host 发现和调用

| 字段 | 内容 |
|---|---|
| 选择 | 采用现有 registry 路径：正文固定小节是 contract 权威；产品层按 R3 既有卡片契约生成 catalog 投影；`v4/registry/capabilities.json` 提供现有 146 条能力回归索引与 `source_ref` 缓存，`v4/registry/graph.json` 完成卡片到 tactic/SOP 节点的映射。host 只消费这条路径，不自行扫描正文猜测节点。 |
| 理由 | 已落盘正文的 frontmatter 被校验器锁定为 `name` + `description`，不能承载 `requires`/`produces`。`capabilities.json` 的真实角色是 146-row v3 -> v4 capability regression matrix，不是第二份 contract；R3 已定义产品层卡片形状，R1 已规定正文 contract 与 registry 索引的关系。这样复用既有索引和卡片契约，不把回归表误说成完整卡片。代价是卡片必须由正文 contract、graph desc 和既有 registry 索引同步投影，卡片不能反向成为事实来源。 |
| 影响 | 267 个 `SKILL.md` 的 `## Input contract` 与 `## Output contract` 必须机器可解析；输入字段、类型、required/optional、失败条件和输出判据写在这两个小节。frontmatter 只保留 `name`、`description`。产品层卡片固定输出 `id, user_label, description, when_to_use, requires, produces, confidence, source_ref, next_call`；host 用 `source_ref` 回到节点，用 `next_call` 进入 graph 中的合法 calls/jump。 |
| 证据 | `v4/scripts/validate_graph.py:211-245`（frontmatter、固定小节、delta_fields 与 calls 引用校验）；`v4/docs/runtime-boundary.md:50-58,114-122`（正文 contract 唯一权威、catalog 卡片和 graph 映射）；`channel/deliverables/R3/entry-ux-spec.md:63-78,101-107`（catalog 归产品层、卡片字段）；`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:7091-7097`（registry 与正文布局）。 |

格式样例（沿用已落盘格式，不新增字段）：

````markdown
---
name: formulate-hypotheses
description: "Generate testable hypotheses from theory, empirical regularity, anomaly, or explicit explanatory competition."
---

## Input contract

```yaml
required: [research_gap_or_observation]
optional: [theory, anomaly, candidate_explanations, variables, prior_evidence]
constraints: [at least one observable consequence]
```

## Output contract

```yaml
produces: [hypothesis_set, operational_definitions, predictions, falsification_conditions, comparison_matrix]
delta_fields: [hypothesis_updates, findings, uncertainties, decisions, open_questions]
```
````

对应的既有 R3 catalog 卡片形状（由产品层从正文 contract + graph/registry 索引投影）：

```yaml
id: formulate-hypotheses
user_label: Formulate hypotheses
description: Generate and refine testable hypotheses.
when_to_use: when a research gap or observation can be stated
requires: [research_gap_or_observation]
produces: [hypothesis_set, predictions, falsification_conditions]
confidence: registry
source_ref: v4/skills/formulate-hypotheses/SKILL.md
next_call: [falsifiability-audit, falsification-first-audit]
```

`requires`/`produces` 是从正文 contract 编译的索引摘要，不是第三份权威 contract；若摘要与正文冲突，以正文为准并阻止该卡片继续路由，交由 N1/N2 修复生成链。

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
| 选择 | 选 D：薄编排 host + agent 节点执行的混合形态。host 是确定性的 runtime/control-plane harness，负责事件回放、SpecView、context slice、catalog/graph 路由和 checkpoint 写入；LLM/agent 只执行一个已选 tactic/SOP，返回八字段 Delta。 |
| 理由 | A 让现有 agent harness 同时承担事件回放和持久化，无法保证 `checkpoint` 顺序及 `SpecView` 重建；B 把科学节点和 runtime 混在脚本，重复实现 267 个正文；C 把科学图误作 MCP tool 图。D 正好复用现有边界：科研图只含 tactic/SOP，host runtime 承担控制面。代价是需要一个很薄的确定性执行壳，但不引入 provider、MCP 或第二套科研节点。 |
| 影响 | host 必须实现 R1 的十一处职责：从 checkpoint 重建 SpecView、读取 context、做 preflight、按固定优先级路由、加载当前 state slice、接收 tactic/SOP Delta、追加 checkpoint、决定是否派 subagent。科研正文不写 provider、tool、重试、退避、超时、错误分类、并行调度或监控状态机。 |
| 证据 | `file-transfer/2026-08-23-22-16-dare-v4-architecture.json:17-23,35-49`（edge/state/boundary）；`channel/deliverables/R1/runtime-boundary.md:1.1-1.2,2.1-5.3`；`v4/docs/runtime-boundary.md:112-130`。 |

## Q2 SpecView 重建由谁执行

| 字段 | 内容 |
|---|---|
| 选择 | 由 host 内的确定性重建器执行：按单 Phase context 文件中的 checkpoint 序号递增回放，`decisions` 是计划主来源，`open_questions` 仅挂接辅助信息，输出内存 SpecView。 |
| 理由 | R1 已给出确定性规则；让 agent 每轮重算会把计划结构交给概率性文本生成，无法保证同一事件流得到同一 active item。把它做成独立服务又新增部署机制，薄 host 内重建器足够。代价是 host 必须严格遵守既有 decision_id/plan_item_id 规则，并保留被替换决定及原因。 |
| 影响 | host 每次路由前重建 `phase, objective, active_items[], context_requirements[], completion_gates[], backtrack_conditions[], status, source_checkpoint`；选择首个未完成且依赖满足的 active item。没有 `plan_item.create` 时先追加最小 decision；改变 objective/requires/completion gate/依赖时将 complete 项标为 `needs_revalidation`，不得以旧 complete 自动前进。 |
| 证据 | `v4/docs/runtime-boundary.md:29-48`；`channel/deliverables/R1/runtime-boundary.md:2.1-2.3,4`。 |

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
| 理由 | 这是一个已在 graph 中存在的 tactic 与下游 SOP 路径；它能从明确输入产生 ranking、sensitivity 和 recommendation，足以验证 Q1-Q5 的 host 链路。没有新节点、新格式或伪造执行器。代价是只验证一个科研分支，不声称覆盖全部 267 节点。 |
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
