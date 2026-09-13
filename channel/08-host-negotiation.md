# 08-host-negotiation

Sirelia 开题，2026-09-10 21:50。**本帖归 R6（新岗）。**

## 一、问题

v4 的所有规格都在写「host 应该怎么做」。**host 从未被定义。**

举证——`deliverables/R1/runtime-boundary.md` 里 host 承担的职责：

    §1.2   host 开始任何研究动作前，必须从当前 Phase 的 checkpoint 事件流重建 spec 投影视图
    §2.1   重建器按 checkpoint 序号递增回放
    §2.3   每次路由前重建当前 SpecView，选择第一个 active_item
    §2.4   host 先重建当前 SpecView，再读取其 context_requirements 指向的 context
    §3.3   host 将每个 Delta 作为事件追加，不做静默覆盖
    §3.4   host 不猜测、不丢弃任一事件
    §4     新 session 的固定入口（四步）
    §5.0   host 对 ResearchContext 做一次有界 preflight
    §5.1   路由优先级固定为三级
    §5.2   每次调用只加载当前投影要求的上下文
    §5.3   host 负责决定是否派发 subagent；代理不得直接修改 context/INDEX

这是十一处「host 必须」。没有一处说清 host 是什么东西。

**后果是具体的**：267 个节点的正文即将扇出，每个节点的 Input/Output Contract
都要声明「host 提供什么」「host 收到什么」。host 形态未定，
260 个正文就会各写各的假设，扇出完再改是 260 处返工。

## 二、必须回答的六个问题

按依赖顺序。前三个不答，后三个无意义。

### Q1 host 是什么形态？

候选（不限于）：

- **A. Claude Code / Codex 这类既有 agent harness 直接充当 host。**
  skills/ 目录下 267 个 SKILL.md，harness 读 frontmatter 做发现，
  投影重建靠 agent 自己读 context 文件。零新代码。
- **B. 一层薄编排脚本（Python/TS）+ 任意 LLM API。**
  脚本管事件流、投影重建、路由；LLM 只执行单个节点。
- **C. MCP server。** 节点作为 tool 暴露，host 是 MCP client。
- **D. 上述混合**：投影重建这类确定性逻辑交脚本，节点执行交 agent。

判据：v4 的 `boundaries.runtime_control_plane` 列了七项——routing policy /
context retention / budget / retry-recovery / parallelism / agent dispatch /
execution monitoring。**问：这七项由代码承担还是由 agent 的判断承担？**
答案不同，host 形态就不同。

### Q2 SpecView 重建由谁执行？

R1 §2.1 写的是确定性算法（按 checkpoint 序号递增回放，识别五种 decisions 事件）。

- 交给 agent 每次读文件重算 → 无新代码，但每轮消耗 context，且「确定性」无保证
- 交给脚本 → 确定性有保证，但引入必须实现的第一个真组件

**这个选择决定 v4 是不是纯 prompt 工程。**

### Q3 事件流的物理载体是什么？

R1 §3.1 定的是：

    context/INDEX.md
    context/<timestamp>-<phase-slug>.md     # 每个 Phase 恰好一份

checkpoint 是追加式 Markdown 段落（§3.2 九个字段）。

问：**Markdown 是最终形态，还是 v4 该用 JSONL？** Markdown 的好处是 agent
直接可读、人也可读；坏处是「按序号回放」需要解析，而解析 Markdown 段落
比读 JSONL 脆。§3.2 那九个字段已经很像一条记录了。

### Q4 267 个节点如何被 host 发现和调用？

`proposed_repo_layout` 给了两条线索：

    skills/<id>/SKILL.md          AI-readable scientific instruction
    registry/graph.json           Authoritative node kind, calls, allowed jumps, modes, aliases

R3 的 `entry-ux-spec.md` 定了 catalog discovery 返回 3–5 张能力卡片
（含 `requires`/`produces`/`source_ref`/`next_call`）。

问：**卡片从哪来？** frontmatter 只允许 `name` + `description`（R1 §2.4 已锁），
那 `requires`/`produces` 只能从正文的 `## Input Contract` / `## Output Contract`
小节解析，或者由构建期脚本预生成进 `registry/capabilities.json`。
两条路对扇出的影响不同——后者意味着 267 个正文的这两个小节必须机器可解析，
格式要现在就锁死。

### Q5 `calls` 不是线性顺序，那 tactic 执行时怎么定顺序？

`edge_semantics.calls` 原文：

    Tactic -> SOP. Declares the SOP vocabulary that a tactic may compose.
    It is not a mandatory linear order.

R1 §2.4 第 3 条：「计划项只声明 tactic/SOP 组合或顺序建议；
最终 tactic/SOP 选择可由 host 按 catalog 索引完成，但必须记录选择理由」。

问：一个 tactic 声明了 8 个 SOP 词汇表，**host 凭什么决定先调哪个？**
- 由 tactic 正文的 `## Execution protocol` 给出默认序 → 那 267 个正文里
  tactic 那 51 个必须写默认序，这是扇出规格的硬要求
- 由 agent 每次自行判断 → 那 `Execution protocol` 写什么？
- 由 `jump` 边推导 → jump 是 T→T 或 S→S，不跨层，推不出 tactic 内部序

**这一条直接决定 51 个 tactic 正文的写法。**

### Q6 最小可执行闭环是什么？

不要求全量。要求：**一个具体的 tactic + 它的下游 SOP，端到端跑一次，
产出一个真 checkpoint。** 说清需要哪些组件、哪些是新写的、哪些是既有的。

## 三、约束（不可协商）

1. **host-neutral。** 不许把 provider 细节（Anthropic/OpenAI/某个 MCP）
   写进科研图或事件流。R1 §1.2 第 4 条。
2. **科研图只有两种可执行节点**：`tactic`、`sop`。host 不是第三层节点，
   catalog / context / artifact 也不是。
3. **八字段 Delta 是唯一契约面**：`findings`、`evidence_updates`、
   `hypothesis_updates`、`assumption_updates`、`uncertainties`、`decisions`、
   `open_questions`、`recommended_jumps`。不许增删字段。
4. **追加式，不原地改历史。** 纠正靠新 checkpoint 覆盖语义。
5. **agent 自身异常处理一律不做**（Pthahnix 已裁定）。重试退避、超时缺省值、
   错误分类、并行调度、监控状态机——全部不写。host 设计里出现这些，驳回。
6. **不许新造机制。** 已有的用已有的。

## 四、交付要求

落 `deliverables/R6/host-design.md`。逐个回答 Q1–Q6，每个答案含：

| 字段 | 要求 |
|---|---|
| 选择 | 明确选哪个，不许「视情况而定」 |
| 理由 | 为什么它比其他候选好，说清代价 |
| 影响 | 这个选择让 267 个节点正文的哪个小节必须怎么写 |
| 证据 | 引 architecture.json 或 R1 规格的行号 |

**Q4、Q5 的答案要给出格式样例**——扇出正在同时进行，
这两条是 260 个正文的硬约束，含糊一天就是 260 处返工。

Q6 给出组件清单和调用顺序，不要伪代码堆砌。

## 五、只读源

- `file-transfer/2026-08-23-22-16-dare-v4-architecture.json` — v4 权威图
- `channel/deliverables/R1/runtime-boundary.md` — 十一处 host 职责的出处
- `channel/deliverables/R3/entry-ux-spec.md` — catalog discovery 与入口
- `channel/deliverables/R5/pilot/*/body.md` — 7 个已编译 tactic 正文（模板参考）
- `scripts/refactory_source.json` — v3 全量源（1.7 MB，本地在）

写权限只有 `channel/`。禁 git 写操作。禁 `superpowers` / `ara` 两个 skill。

## R6 第一批回帖：Q4 + Q5（2026-09-13）

现状核验：已运行 `python v4/scripts/validate_graph.py`，结果为 `OK: graph validation passed (0 warning(s))`。校验器当前检查 267 节点、51 tactics、216 SOP、317 calls、157 jumps、474 edges、146 capability contracts；同时锁定正文 frontmatter、固定 contract 小节、Delta 八字段和 tactic 的 calls 引用。以下裁决基于已落盘正文，不是未来格式假设。

### Q4 267 个节点如何被 host 发现和调用

**选择**：采用现有单一路径：正文 `## Input contract` / `## Output contract` 是 contract 权威；产品层按 R3 既有卡片契约生成 catalog 投影；`v4/registry/capabilities.json` 提供 146 条能力回归索引与 `source_ref` 缓存；`v4/registry/graph.json` 把卡片映射到 tactic/SOP 节点。host 不自行扫描正文猜测节点，也不新增索引。

**理由**：frontmatter 已被校验器锁定为 `name` + `description`，不能承载 `requires`/`produces`。`capabilities.json` 的真实角色是 146-row v3 -> v4 capability regression matrix，不是第二份 contract；R3 定义的产品层卡片从正文 contract、graph desc 和既有 registry 索引投影。代价是卡片只作索引摘要，不得反过来成为权威。

**影响**：267 个正文必须保持机器可解析的两个 contract 小节；产品层卡片固定为 `id, user_label, description, when_to_use, requires, produces, confidence, source_ref, next_call`。host 先做产品层 catalog discovery，再用 `source_ref` 定位正文节点，用 `next_call` 进入 graph 的合法 calls/jump。若卡片摘要与正文冲突，停止该卡片路由并交 N1/N2 修复生成链，不另造运行时机制。

**证据**：`v4/scripts/validate_graph.py:211-245`；`v4/docs/runtime-boundary.md:50-58,114-122`；`channel/deliverables/R3/entry-ux-spec.md:63-78,101-107`；`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:7091-7097`。

**格式样例**：

```markdown
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
```

对应卡片沿用既有 `capabilities.json` 形状：

```yaml
id: formulate-hypotheses
user_label: Formulate hypotheses
description: Generate and refine testable hypotheses.
when_to_use: when a research gap or observation can be stated
requires: [research_gap_or_observation]
produces: [hypothesis_set, predictions, falsification_conditions]
confidence: registry
source_ref: v4/skills/formulate-hypotheses/SKILL.md
next_call: [theory-mechanism-extraction, anomaly-driven-abduction]
```

### Q5 tactic 内部执行顺序

**选择**：host 严格按 tactic 正文 `## Execution protocol` 的编号顺序执行；编号内 SOP 按出现顺序调用。`graph.json` 的 `calls` 只声明可组合 SOP 词汇，不是线性顺序；`jump` 只作同类型节点的合法交接。

**理由**：现有 51 个 tactic 正文已写明依赖、阶段和分支；权威图明确 calls “is not a mandatory linear order”。临场让 agent 重排会使正文失去确定性，单凭 calls 又无法恢复依赖。代价是 tactic 必须明确默认顺序，分支只能使用正文已有 mode/deviation 条件。

**影响**：每个 tactic 的 `## Execution protocol` 必须是编号步骤；其中引用的 SOP 必须存在于该 tactic 的 `calls` 边，否则校验器拒绝。每一步只读取当前 state slice，完成后回传固定八字段 Delta。不得把重试、退避、超时、错误分类、并行调度或监控状态机写入 host 设计。

**证据**：`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:17-23`；`v4/scripts/validate_graph.py:225-232`；`v4/docs/runtime-boundary.md:46-58,120-126`；`v4/skills/formulate-hypotheses/SKILL.md:24-36`。

**格式样例**：

```markdown
## Execution protocol

1. State the gap/observation and relevant theory or anomaly.
2. Generate candidate hypotheses without premature filtering.
3. Operationalize variables and relationships; state scope and boundary conditions.
4. Check falsifiability and, for competing mode, create discriminating predictions and a comparison matrix.
```

host 调用顺序为 `1 -> 2 -> 3 -> 4`。若 protocol 自身给出 `Deviation` 或 mode 分支，只按正文条件选择并在已有 `decisions` Delta 记录理由；没有正文条件时不得自行重排。

交付物：`channel/deliverables/R6/host-design.md`。本批未修改 `v4/`，未新增机制。请 Sirelia 审核 Q4/Q5；通过后我继续第二批 Q1/Q2/Q3/Q6。

## R6 第二批回帖：Q1 + Q2 + Q3 + Q6（2026-09-13）

### Q1 host 是什么形态

**选择**：选 D，薄编排 host + agent 节点执行的混合形态。host 是确定性的 runtime/control-plane harness，负责事件回放、SpecView、context slice、catalog/graph 路由和 checkpoint 写入；LLM/agent 只执行一个已选 tactic/SOP，返回八字段 Delta。

**理由**：A 无法保证 checkpoint 顺序和 SpecView 重建；B 把科学节点和 runtime 混在脚本，重复实现 267 个正文；C 把科学图误作 MCP tool 图。D 复用现有边界，代价只是一个薄的确定性执行壳，不引入 provider、MCP 或第二套科研节点。

**影响**：host 承担 R1 十一处职责：回放 SpecView、读取 context、preflight、固定优先级路由、加载 state slice、接收 Delta、追加 checkpoint、决定是否派 subagent。正文不写重试、退避、超时、错误分类、并行调度或监控状态机。

**证据**：`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:17-23,35-49`；`channel/deliverables/R1/runtime-boundary.md:1.1-1.2,2.1-5.3`；`v4/docs/runtime-boundary.md:112-130`。

### Q2 SpecView 重建由谁执行

**选择**：host 内的确定性重建器执行。按单 Phase context 文件中的 checkpoint 序号递增回放；`decisions` 是计划主来源，`open_questions` 仅辅助挂接，输出内存 SpecView。

**理由**：R1 已给出确定性规则；让 agent 每轮重算会把计划结构交给概率性文本生成，无法保证同一事件流得到同一 active item。独立服务会新增机制，薄 host 内重建器已足够。代价是严格遵守既有 `decision_id`/`plan_item_id` 规则。

**影响**：每次路由前重建 `phase, objective, active_items[], context_requirements[], completion_gates[], backtrack_conditions[], status, source_checkpoint`，选择首个未完成且依赖满足项。无 `plan_item.create` 时先追加最小 decision；改变 objective/requires/completion gate/依赖时标记 `needs_revalidation`，旧 complete 不得自动前进。

**证据**：`v4/docs/runtime-boundary.md:29-48`；`channel/deliverables/R1/runtime-boundary.md:2.1-2.3,4`。

### Q3 事件流的物理载体

**选择**：沿用追加式 Markdown：`context/INDEX.md` 加 `context/<timestamp>-<phase-slug>.md`，每个 checkpoint 追加顶层段落；不改 JSONL。Markdown 是载体，固定九字段是记录格式。

**理由**：R1 已锁定单 Phase 单文件、追加 checkpoint、人工可读；改 JSONL 会令既有 context 与格式整体返工，且没有现成 JSONL 机制。代价是重建器按固定字段与序号解析 Markdown。

**影响**：checkpoint 固定 `Checkpoint, Phase, Source, Status, Input slice, Process, Results, Delta, Open questions`；Delta 八字段，空值写 `[]`。`complete` 才是恢复落点，`partial` 不能证明阶段完成；冲突追加 uncertainty，不改旧段落。

**证据**：`v4/docs/runtime-boundary.md:60-99`；`channel/deliverables/R1/runtime-boundary.md:3.1-3.4`。

### Q6 最小可执行闭环

**选择**：用现有 `rank-candidates` tactic 的 `direction-selection` mode，严格按正文执行“规范化候选与 criteria schema -> 选择 mode -> 校验已提供权重 -> `score-object` -> `aggregate-ranking` -> `assess-sensitivity`”，最后追加一个 `complete` checkpoint。输入提供 `candidates, criteria, decision_rule` 与固定权重。

**理由**：这是 graph 中已有 tactic/SOP 路径，能产出 ranking、sensitivity、recommendation，足以验证 host 链路；不增加节点、格式或执行器。代价是只验证一个科研分支，不宣称覆盖 267 节点。

**影响**：`INDEX -> Phase context replay -> SpecView -> preflight -> capabilities catalog -> graph node -> schema normalization -> mode selection -> weight validation -> scoring -> aggregation -> sensitivity -> 八字段 Delta -> complete checkpoint`。结果必须能从 checkpoint 重建相同 SpecView 与下一路由。

**证据**：`v4/registry/graph.json` 中 `rank-candidates` 的 calls；`v4/skills/rank-candidates/SKILL.md:16-31`；`v4/docs/runtime-boundary.md:29-38,46-58,71-99,114-130`。

**组件与调用顺序**：

```text
context/INDEX.md
  -> Phase context Markdown replay
  -> SpecView reconstruction
  -> ResearchContext preflight
  -> capabilities catalog card
  -> rank-candidates(direction-selection)
  -> normalize candidate/criteria schemas
  -> select direction-selection mode
  -> validate supplied weights
  -> score-object
  -> aggregate-ranking
  -> assess-sensitivity
  -> ResearchStateDelta (eight fields)
  -> complete checkpoint append
```

**checkpoint 样例**：

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

第二批已交付至 `channel/deliverables/R6/host-design.md`。未修改 `v4/`，未新增机制。请 Sirelia 审核六问。
