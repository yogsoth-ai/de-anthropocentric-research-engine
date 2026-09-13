# R6 host design - batch 1

状态：Q4、Q5 已裁决，待 Sirelia 审核。

## Q4 267 个节点如何被 host 发现和调用

| 字段 | 内容 |
|---|---|
| 选择 | 采用现有 registry 路径：正文固定小节是 contract 权威；构建产物 `v4/registry/capabilities.json` 提供 catalog 卡片；`v4/registry/graph.json` 完成卡片到 tactic/SOP 节点的映射。host 只消费这条路径，不自行扫描正文猜测节点。 |
| 理由 | 已落盘正文的 frontmatter 被校验器锁定为 `name` + `description`，不能承载 `requires`/`produces`。R3 已把 catalog 留在 DARE 产品层，现有 capabilities registry 已有 146 条 contract；复用它能避免第二套索引。代价是 registry 必须与正文同步生成，不能把卡片当作正文事实。 |
| 影响 | 267 个 `SKILL.md` 的 `## Input contract` 与 `## Output contract` 必须机器可解析；输入字段、类型、required/optional、失败条件和输出判据写在这两个小节。frontmatter 只保留 `name`、`description`。catalog 卡片固定输出 `id, user_label, description, when_to_use, requires, produces, confidence, source_ref, next_call`；host 用 `source_ref` 回到节点，用 `next_call` 进入 graph 中的合法 calls/jump。 |
| 证据 | `v4/scripts/validate_graph.py:211-245`（frontmatter、固定小节、delta_fields 与 calls 引用校验）；`v4/docs/runtime-boundary.md:50-58,114-122`（正文 contract 唯一权威、catalog 卡片和 graph 映射）；`channel/deliverables/R3/entry-ux-spec.md:63-78,101-107`（catalog 归产品层、卡片字段）；`file-transfer/2026-08-23-22-16-dare-v4-architecture.json:7091-7097`（registry 与正文布局）。 |

格式样例（沿用已落盘格式，不新增字段）：

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

对应的既有 catalog 卡片形状：

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
