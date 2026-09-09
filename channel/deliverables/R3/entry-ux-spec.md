# DARE v4 入口与能力发现 UX 规格（R3）

> 状态：用户侧方案；Spec 归属仍为 DARE 产品层，形态按 checkpoint 事件流投影视图处理。
> 设计前提：第一次使用的用户不知道 DARE，只想问一个研究问题。

## 1. 冷启动场景

| 场景 | 用户输入 | 用户期待的首屏 | 可接受对话上限 |
|---|---|---|---:|
| 文献综述 | “总结 X 领域近五年的进展” | 直接给出范围、证据类型、综述路线和首批检索动作 | 2 轮 |
| 实验设计 | “怎样验证 Y 假设” | 变量、对照、可行性风险与下一步实验草案 | 2 轮 |
| 资源受限 | “我只有公开数据和两周，做什么研究” | 3 个带时间/资源约束的候选方向及取舍 | 3 轮 |
| 直接分析论文 | “帮我分析这篇 paper” | 识别论文输入，给出阅读/证据提取计划；只追问输出目的 | 1 轮 |
| 继续既有研究 | “继续上次关于 X 的研究” | 恢复最近有效 context，显示恢复点与待办，不重复采集 | 1 轮 |

首屏只需让用户确认“研究什么、做到什么程度、有什么硬约束”。不展示 DARE 术语，不要求填写七字段表单。

## 2. v3 冷启动流程（现状对比）

### 2.1 v4 entry orchestration: six steps as a product-layer template

R2 C1 assigns the six-step sequence (`actor-profiling -> landscape-reconnaissance -> direction-narrowing -> obstacle-analysis -> goal-decomposition -> north-star-synthesis`) to the product layer. It is an entry-depth orchestration template, not a v4 scientific-graph node and not a new layer. Each step emits `ResearchContext`, `decisions`, or `SpecView` inputs for host/runtime.

| Entry depth | Default start | Prefix-skip rule | Product-layer output |
|---|---|---|---|
| cold-start | `actor-profiling` | Skip no prefix | intent/context, direction set, obstacle report, goal decomposition, North Star |
| warm-start | `landscape-reconnaissance` or `direction-narrowing` | Skip `actor-profiling` when background/domain direction is already supplied | Complete missing scope, candidate directions, obstacles, and goal decisions |
| hot-start | `obstacle-analysis` or `goal-decomposition` | Skip the first two steps when a concrete question, paper, or dataset is supplied; create a minimal implicit plan if needed | Minimal executable plan, goal/North Star, and context preflight |
| resume | First unfinished item in current `SpecView` | Do not rerun completed work | Restored context, decisions, and plan |

The default order is retained. Only an already-covered **prefix** may be skipped; arbitrary middle-step jumps are not allowed. If a later step lacks a required predecessor output, fill that step or return `NEEDS_CONTEXT`. The six steps are not six mandatory chat turns: one turn may combine steps, and known inputs are prefilled. Users see natural-language phases such as “clarifying background” and “narrowing candidate directions,” not tactic/SOP slugs. Each step has a checkable completion condition and output for host implementation and R2 mechanical checks.

#### Mapping the five cold-start scenarios

| Scenario | Starting depth | Six-step mapping |
|---|---|---|
| Literature review | cold; warm when domain scope is known | Background/actor -> landscape -> direction -> obstacles -> review goal -> North Star |
| Experiment design | warm or hot | Start at direction when the direction is known; start at obstacle/goal for an existing hypothesis, then complete feasibility and objective |
| Resource-constrained research | warm | Enter direction + obstacle quickly while collecting `resources` and `hard_constraints`, then goal/North Star |
| Direct paper analysis | hot | Skip exploration; extract obstacle/goal from the paper, create a minimal implicit plan and North Star |
| Continue existing research | resume | Restore `SpecView`/context and continue from the first unfinished item; do not rerun the six steps |

Cold/warm/hot describe how much of the six-step prefix is already covered, not separate workflows. All five scenarios share the same template and `NEEDS_CONTEXT` fallback.

```text
用户问题
  -> research-start（entry）
  -> context-init（建 Phase context）
  -> north-star-crystallization/cold-start
       actor-profiling -> landscape-reconnaissance -> direction-narrowing
       -> obstacle-analysis -> goal-decomposition -> north-star-synthesis
  -> ResearchBrief / North Star
  -> research-catalog + campaign-selection + scope-clarification
       + constraint-elicitation + spec-self-review
  -> 用户确认 Spec
  -> executing-specs
       每个 Stage：context-init -> strategy -> context-checkpoint
  -> 研究循环
```

v3 的优点是入口和收敛路径明确；代价是冷启动用户要经历多轮对话，且 catalog 依赖四层层级。v4 删除四层后，必须保留“入口预检、最小采集、能力建议、可恢复状态”这四个产品行为，不能把责任退回 host 的自由发挥。

## 3. Catalog 机制（选择：A）

选择 **A：Catalog 留在 DARE 产品层**。v4 有 51 个 tactic、216 个 SOP；产品层需把扁平节点、contract 摘要与任务分组投影为统一索引，避免 host 自行猜入口。B 把 267 个节点退给 host。C 当前只读 920 份 v3 `SKILL.md`，源错位；待 R5 编译 v4 正文后可作为 A 的内部生成器，而非独立机制。

### C 的显式 frontmatter 契约（仅作内部生成器/备用实现）

| 字段 | 必需性 | 语义与来源 |
|---|---|---|
| `name` | 必需 | 稳定 machine id；来自 v4 tactic/SOP 节点名 |
| `description` | 必需 | 一句话“做什么/何时用”；用户卡片正文唯一来源 |
| `type` | 必需（编译产物） | `tactic` 或 `sop`；来自节点层，不从自然语言猜 |
| `category` | 必需（编译产物） | 用户任务组；源缺失时只能写 `category_source: package` 并标注 inferred |
| `execution` | 可选 | host 执行元数据，不展示给用户 |
| `dependencies` | 可选 | 机器路由引用，不承担 input/output contract |

`Input Contract`/`Output Contract` 仍以 R5 编译后的正文固定小节为权威；frontmatter 不复制 threshold、rubric 或完整 contract。C 当前不可直接上线：现有 920 份文件是 v3，`category` 仅部分存在；待 R5 产出 v4 索引后，才可作为 A 的生成器。

## 4. ResearchContext 处理

审计中的 v4 canonical context 是 `background, resources, hard_constraints, intent`（四字段）；产品界面可投影为七个可理解字段：问题/意图、领域、时间范围、证据类型、资源、硬约束、用户背景。七字段均可为空，只有以下最小启动契约必需：

```yaml
ResearchContext:
  intent: <用户要回答或完成的事>       # required
  scope_anchor: <domain 或 artifact 或 timeframe 至少一个>  # required
  background: <可选>
  resources: <可选>
  hard_constraints: <可选>
  evidence_type: <可选，映射到 intent/resources>
  time_range: <可选，映射到 intent/hard_constraints>
```

采用 **B：soft gate + 有界降级**。入口先从原问题零样本预填；只对影响路由的缺口发起一次结构化 `context-elicit`，固定询问最多 3 项。用户不回答时写入明确默认值并标记 `inferred`，继续走低风险的探索/综述；涉及实验、外部行动或不可逆资源消耗时，不得默认补齐硬约束。

Hard gate 的强制力来自两道可审计门：DARE 产品层须能从当前 Phase checkpoint 事件流重建 `SpecView`，runtime 再做 `context preflight`/schema validator。任何 tactic/sop 调用前检查 `intent` 与 `scope_anchor`；缺失即返回 `NEEDS_CONTEXT {missing, inferred, next_questions}`，Phase context 不可定位或尚无 `plan_item.create` 事件则返回 `NEEDS_PHASE_CONTEXT` 或追加最小计划 decision，不得直接调用科学节点。它不是 host 自觉，也不依赖某个 tactic 的 `precondition`。

## 5. 能力发现时机与呈现

### Host AI 合约

- session 首次建立有效 context 后、追加首个 `plan_item.create` 或进行首次科学路由前调用一次 capability discovery。
- 用户明确问“你能做什么”时进入 browse；context 改变或上次无匹配时才重新发现。
- `SpecView` 的 objective、requires、completion gate 或依赖发生实质变化，导致原能力选择失配时重新发现；描述、排序、注释变化不重扫。
- 返回 `CapabilitySet[]`：`id, user_label, description, when_to_use, requires, produces, confidence, source_ref, next_call`。
- 默认按任务相关性返回 3–5 项；完整清单是可选的 machine-readable 展开，不作为首屏。

### 用户呈现

用自然语言按“文献综述 / 实验设计 / 数据分析 / 假设检验”等任务组卡片，显示“能做什么、何时使用、需要什么、会产出什么、为什么推荐”。隐藏 package/tactic/SOP slug；允许“查看全部”和“换一组”，不强迫用户选项，host 可根据 intent 直接推荐首项。

### 计划视图何时可见、如何修改

1. **首次可见**：首个 `plan_item.create` 写入后立即向用户显示紧凑计划视图，再开始首个科学节点；这是信息告知，不是确认门。视图至少显示当前目标、接下来 3–5 项、每项预期产出、完成判据与主要约束。用户随时可要求“查看当前计划”。
2. **主动通知边界**：objective、requires、completion gate、依赖、预计资源或范围发生变化时主动显示“计划已变更”及影响项；只改描述、排序或注释时静默更新，在用户打开计划时呈现。多项同批变化合并成一次通知。
3. **用户如何改**：用户编辑的是计划视图中的目标、范围/约束、优先级、计划项、依赖和完成判据，不直接编辑文件。每次提交转换为带 `plan_item_id`、operation、changed_fields、reason、source=user 的 `decisions` 事件，再从事件流重建视图。
4. **已完成项失效**：按 R1 语义，若新 decision 改变已完成项的 objective、requires、completion gate 或依赖，界面将其显示为“需重新验证”，保留原完成时间与产出，并暂停依赖它的下游；只改描述、排序或注释时保持“已完成”。重新满足新判据后恢复为“已完成”。

## 6. 错误入口兜底

1. **已有论文/数据输入**：识别为 hot-start，跳过 north-star，生成隐式最小 plan；仅在输出目标影响路线时追问一次。
2. **问题过于模糊**：走 soft gate 的固定三问；回答不足则使用低风险默认值并标记推断，不拒绝普通综述。
3. **缺少必需 context**：停止 tactic 调用，返回 `NEEDS_CONTEXT`，列出缺失字段、已推断值和最多三项问题。
4. **约束冲突**：返回 `CONTEXT_CONFLICT`，逐条指出冲突及最小解法，等待用户选取，不静默覆盖硬约束。
5. **请求超出研究范围**：明确说明不能直接执行的外部动作，给出最近的研究分析入口，不伪装成已完成。
6. **恢复失败或 context 过期**：显示恢复失败原因，保留原问题，重新走一次最小采集；不让用户重填全部字段。

## 7. v4 必须保留 / 可删除

必须保留：一个可见入口；最小 context preflight；一次有界 elicitation；按任务的能力发现；可恢复的 context/状态引用；`NEEDS_CONTEXT` 与冲突错误码；用户可读的下一步。

可删除：四层 campaign/strategy 菜单；向用户展示 51 行 tactic 表；每轮自动重扫 catalog；把七字段全部设为 required；为 context elicitation 新增自由聊天 agent；让 host 猜测 JSON 的 entry 层。

## 8. 证据索引

- v3 入口与 cold/warm/hot 路由：`skills/north-star-crystallization/SKILL.md:19-35`。
- v3 catalog/Spec/执行链：`skills/research-catalog/SKILL.md:10-16`、`skills/writing-specs/SKILL.md:17-33`、`skills/executing-specs/SKILL.md:18-42`。
- v4 删除 catalog 后的发现缺口：`file-transfer/2026-08-24-14-22-dare-v4-capability-coverage-audit.md:241-262`。
- v4 cold-start 与 context 缺口、hard gate 降级：同审计 `:266-290`。
- v4 节点规模：`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:60-68`（51 tactics、216 SOPs、146 contracts）；v3 entry 节点：`scripts/refactory_source.json:3022-3026`。
- frontmatter 不能承接完整 contract：`channel/deliverables/R5/field-distribution-analysis.md:45-49`。
- v4 canonical context 四字段：同审计 `:268-276`；v4 runtime/product 边界：`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:39-48`。
- v3 entry 节点：`scripts/refactory_source.json` 中唯一 `"layer": "entry"` 节点（`de-anthropocentric-research-engine`）。
