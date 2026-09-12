# DARE v4 建造规格

Sirelia · 2026-09-12 · 交付给 Pthahnix 用于实际开发

本文件是 v4 的**开发入口**。读完这一份就能开工，不必先读 channel 里其余十一份——那些是过程与裁定，本文件是结论。

需要时的原始出处：图的权威真值在 `file-transfer/2026-08-23-22-16-dare-v4-architecture.json`（只读）；v3 全量源在 `scripts/refactory_source.json`（930 节点 / 3413 边）；正文模板与判据规则在 `channel/09-fanout-spec.md`；分配与验收在 `channel/11-rework-and-redistribution.md`。

---

## 一 v4 是什么

一张**两层科研图**，267 个可执行节点，474 条边。

| 量 | 值 |
|---|---:|
| tactic | 51 |
| sop | 216（shared-basis 45 / specialized 171） |
| 节点合计 | 267 |
| calls 边 | 317 |
| jump 边 | 157 |
| 边合计 | 474 |
| capability 契约 | 146 |

只有 `tactic` 和 `sop` 两种是可执行节点。`shared-basis` / `specialized` / `family` 是**纯视觉元数据**，不是第三层执行层——架构原文：「BASIS/family labels are metadata for inspection, not execution layers.」

v3 到 v4 的实质变化：v3 有 930 个节点、层级混杂（campaign / strategy / tactic / sop 四层加包名前缀）；v4 压到 267 个、两层、去包名。压缩不是删功能，是**合并同构节点并把差异外提到调用方参数**——45 个 shared-basis SOP 就是这么来的，其中 `score-object` 一个吞并了 v3 的 15 个 scoring 节点。

---

## 二 两种边的语义（易错，先读）

**`calls`：Tactic → SOP。** 声明这个 tactic 可以组合的 SOP 词汇表。**不是强制线性顺序。** 架构原文：「It is not a mandatory linear order.」

这一条决定了实现方式：host 不能把 `calls[]` 当成流水线顺序执行。tactic 正文的 `## Execution protocol` 里给的是**默认序**，agent 可依上下文偏离，偏离需在 `Deviation:` 记原因。

**`jump`：Tactic → Tactic 或 SOP → SOP。** 合法交接，可默认排序也可上下文触发。**不跨层**——没有 tactic→sop 的 jump，也没有 sop→tactic 的 jump。

**科研图里没有 provider / tool 边。** 架构原文：「No provider/tool edge is part of the scientific graph.」论文工具、web 工具、MCP、子 agent、存储，全部属于外部能力层，不进图。

---

## 三 三层边界（决定什么代码写在哪里）

架构里 `boundaries` 分三块，这是 v4 最重要的架构约束：

| 层 | 内容 | 谁实现 |
|---|---|---|
| **scientific_graph** | 科研认知、科学方法、证据方法学、假设/实验/压力测试推理 | 267 个节点正文（`skills/<id>/SKILL.md`） |
| **runtime_control_plane** | 路由策略、上下文保留、预算、重试恢复、并行、agent 派发、执行监控 | host，**不写进节点正文** |
| **external_capability_layer** | 论文工具、web 工具、MCP、编码执行工具、子 agent、存储/vault | 外部，节点正文只声明需要什么能力，不声明用哪个 provider |

**推论（本项目的硬规矩）**：重试、退避、超时缺省、错误分类、并行调度、监控状态机——这些属 runtime_control_plane，一律不许出现在任何节点正文里。这条在 channel 里被反复驳回过，是 Pthahnix 的裁定。

---

## 四 状态语义

状态的所有者是 **host AI / runtime**，不是节点。

节点的行为契约（架构原文）：「consume a relevant state slice and return a research-state delta; never require provider-specific storage or giant checkpoint files.」

即：节点收一个**状态切片**，返一个**research-state delta**。不许要求特定存储，不许要求巨型 checkpoint 文件。

**delta 只有八个字段，不许增删**：

```
findings              evidence_updates      hypothesis_updates    assumption_updates
uncertainties         decisions             open_questions        recommended_jumps
```

每个节点正文的 `## Output contract` 里 `delta_fields` 取这八个的**子集**，且与 `produces` 对应。八个全列等于没做选择——R4 上一轮 79 个节点全倒八字段，是驳回原因之一。

---

## 五 仓库结构

架构给的 `proposed_repo_layout`，逐条照建：

| 路径 | 内容 |
|---|---|
| `skills/<id>/SKILL.md` | AI 可读的科研指令。**YAML frontmatter 保持最小：只有 `name` + `description`** |
| `registry/graph.json` | 权威真值：节点类型、calls、允许的 jump、modes、别名与 provenance ID |
| `registry/capabilities.json` | v3 → v4 能力回归矩阵（146 条契约） |
| `docs/architecture.md` | 两层语义与状态交接契约 |
| `docs/runtime-boundary.md` | host-neutral 的运行时职责，**不含 provider 专属工具指令** |
| `scripts/validate_graph.py` | 校验 ID、边合法性、可达性、能力映射 |
| `scripts/build_graph_html.py` | 重新生成交互式架构图 |

注意 `skills/<id>/` 是**扁平的**，没有包名层级。v3 的 `knowledge-acquisition/saturation-detection` 在 v4 是 `skills/assess-evidence-saturation/`，包名只以 provenance 形式留在正文里。

frontmatter 只留 `name` + `description` 这条是硬的——不要加 `dependencies`、`used-by`、`tags`。图的关系全部住在 `registry/graph.json`，不在 frontmatter 里重复。

---

## 六 节点正文的两套模板

正文是 `skills/<id>/SKILL.md` 的主体。**tactic 与 sop 用不同模板**，不要混。

### 6.1 tactic：九小节（固定序）

```
## Purpose
## Input contract
## Execution protocol
## Output contract
## Thresholds and quality gates
## Failure and counterexamples
## Provenance map
## Preserved source criteria ledger
## Context checkpoint / Delta notes
```

条件小节：有 `modes` 的加 `## Mode branches`；边界易误用的加 `## When to use / not applicable`。

`## Execution protocol` 给**默认序**，每步括号内列本步用到的 SOP id，且该 id 必须真实存在于 `calls[<tactic-id>]`——写不在里面的是幻影引用。`calls[]` 里有而正文未用的 SOP，在末尾 `Deviation:` 说明为何可选。

`## Context checkpoint / Delta notes` 只有 tactic 有。**checkpoint 由调用方 tactic 拥有，SOP 不管 checkpoint。**

### 6.2 sop：七小节（固定序）

```
## Purpose
## Input contract
## Procedure
## Output contract
## Quality gates
## Failure and counterexamples
## Provenance map
```

第三节叫 `## Procedure`（3–7 步），**不叫** `Execution protocol`——那是 tactic 的。没有 checkpoint 小节，没有判据台账。

**shared-basis SOP 额外必写 `## Parameterization`**，位置在 `Quality gates` 之后。写清调用方必须提供什么才能让这个 SOP 具体化。这是 BASIS 层的全部要害：BASIS 的科研内容住在调用方给的参数里。`score-object` 的架构 desc 原文就是「The parent tactic supplies the object schema and rubric」。

### 6.3 契约格式（锁死，不许变体）

Input：

````
```yaml
required: [...]
optional: [...]
constraints: [...]
```
````

Output：

````
```yaml
produces: [...]
delta_fields: [...]
```
````

三反引号，不用 `~~~`。`required` 里必须是该节点真实消费的科研对象名，不许出现 `source_state` / `task_object` / `input_object` 一类通用占位符。

---

## 七 判据：A / B / C 三分法

v3 的判据里混着三种东西，v4 分开处理。这是全项目争议最多的一块，已裁定：

**A 类 · 反偷懒的采样门。** 例如「读 150 篇源」「全文 80 篇 / 30 页」「snowball 至 67%」。这类**转成相对量**，并强制附六个审计字段，缺一项不得通过：

```
declared universe / denominator   声明的全集与分母
numerator                          分子
batch increment                    批次增量
stopping reason                    停止理由
source references                  来源引用
direction + threshold rationale    方向与阈值理由
```

**B 类 · 可机械验证的结构检查。** 例如「每个排除项有唯一主因」「SCAMPER 七算子穷尽」「矩阵无空格」。**原样保留**，不动。

**C 类 · 无出处的历史数字。** v3 里查不到依据的裸数字。**删除**。

### 例外：以下一律保持固定值，相对化没有意义

统计显著性与检验力（α 0.05、power 0.8）、预注册要求、公平比较约束、方法结构性约束。相关节点：`estimate-sample-size`、`select-statistical-method`、`statistical-testing`、`verify-reproducibility`、`design-randomness-protocol`、`specify-reproducibility-protocol`。

同类例外还有 rubric 的固定标尺：`score-object` 保留 v3 的 importance 1–5（权重 40/30/30）、feasibility 1–5（四维等权，≤2 为瓶颈）、impact 1–5（两维等权）、strength 0–10 分段、obstacle 可克服性四档（1 周 / 1 月 / 6 月 / 根本性）。

---

## 八 provenance：v3 → v4 追溯

每个节点的 `## Provenance map` 记它由哪些 v3 节点合并而来。三种标记：

- `resolved:` — 在 `refactory_source.json` 的 930 个 `nodes[].name` 里查到了
- `concept:` — v3 里没有对应节点，是概念性来源
- `intermediate:` — v3 的中间层节点（campaign / strategy），非叶子

### 归一化规则（不做就会虚报）

v3 的真实节点名有三种书写形式，检索时三种都要试：

1. 裸名 —— `saturation-detection`
2. 连字符包名 —— `knowledge-acquisition-saturation-detection`
3. 斜杠包名 —— `knowledge-acquisition/saturation-detection`

检索前先剥掉 `[...]` 和 `(...)` 后缀（v3 有 `portfolio-optimization [campaign]` 这种写法）。

**标 `concept` 前必须三种形式都检索过。** R4 上一轮 164 条里 156 条误标，就是没查直接盖 `concept`；R1 有 42 条、R5 有 11 条同类误标。

**不许编造。** 查不到就标 `concept` 或 `intermediate`，绝不拿名字相似的 v3 节点顶替——那会让能力回归矩阵失真。

---

## 九 host（**未定，唯一空缺**）

`docs/runtime-boundary.md` 里有十一处「host 必须 X」，但 host 从未被定义成一个具体构件。这是 v4 目前唯一的设计空缺。

已立项交由 R6 谈，题目在 `channel/08-host-negotiation.md`，六个必答问题：

| | 问题 | 为什么卡开发 |
|---|---|---|
| Q1 | host 的形态：agent harness / 编排脚本+LLM / MCP server / 混合 | 决定整个运行时的技术选型 |
| Q2 | 谁执行 SpecView 重建：agent 还是脚本 | 决定确定性边界 |
| Q3 | 事件流的物理载体：Markdown checkpoint 还是 JSONL | 决定持久化格式 |
| Q4 | 节点发现与调用格式：运行时解析正文小节，还是预生成 `registry/capabilities.json` | 决定构建期 vs 运行期 |
| Q5 | tactic 内部执行序（`calls` 非强制序的前提下）：正文默认序 / agent 自由选 / 由 jump 推导 | 决定 agent 的自由度 |
| Q6 | 最小可执行闭环：一个 tactic + 其下游 SOP 端到端跑通一次 | 第一个可验证里程碑 |

**Q4 与 Q5 优先**，因为只有这两个会反向影响 267 个正文的写法。Q1–Q3、Q6 不影响正文，可在正文完成后定。

**开发建议**：先建 `skills/` 与 `registry/`（六、七、八节已足够），host 等 R6 结论。两者解耦，契约格式已锁死。

---

## 十 当前进度（2026-09-12 22:5x 实测）

正文由 R1–R5 五组并行编译中。下表为**扫盘实测**，非自报：

| 组 | 范围 | 应做 | 有效正文 | 剩余 |
|---|---|---:|---:|---:|
| R1 | ACQUISITION + DIRECTION | 44 | 44 | 0 |
| R2 | STRESS + CROSS | 41 | 41 | 0 |
| R3 | IDEATION + INSIGHT | 51 | 30 | 21 |
| R4 | HYPOTHESIS + EXPERIMENT + CONVERGENCE + STRUCTURING | 72 | 23 | 49 |
| R5 | BASIS（45 basis-scope + 7 specialized-BASIS） | 52 | 20 | 32 |
| pilot | 已完成 | 7 | 7 | 0 |
| | **合计** | **267** | **165** | **102** |

R4 首轮 79 个正文因内容为空壳被整组驳回（68 个 SOP 的 Procedure 逐字节相同、契约用占位符、delta_fields 八字段全倒、156 条 provenance 误标），正在重写，已重做 23 个。

另有返工待清：R1 42 条 provenance 误标、R5 11 条同类。

四条机械门在已落盘的 R1/R2/R3/R5 共 156 个正文上跑过，**全过**：无正文重复、无占位契约、无八字段全倒、无 `~~~` 围栏。

---

## 十一 建造顺序建议

依赖关系决定顺序，不建议并行开头两步：

1. **`registry/graph.json`** — 从 `architecture.json` 直接生成。267 节点 + 317 calls + 157 jumps。这是后续一切的真值源。
2. **`scripts/validate_graph.py`** — 先有校验器再灌正文。校验 ID 存在性、边合法性（calls 只能 T→S，jump 不跨层）、可达性、能力映射。
3. **`skills/<id>/SKILL.md`** — 正文灌入。已有 165 个可用，其余等 R1–R5 交付。灌入时跑第 2 步的校验器。
4. **`registry/capabilities.json`** — 146 条 v3→v4 能力回归矩阵。依赖第 3 步的 provenance map 齐全。
5. **`docs/architecture.md` + `docs/runtime-boundary.md`** — 从本文件第二、三、四节与 `channel/deliverables/R1/runtime-boundary.md` 整理。
6. **`scripts/build_graph_html.py`** — 可视化，最后做。
7. **host** — 等 R6。与 1–6 解耦。

第 1、2 步现在就能做，不依赖任何未完成的正文。

---

## 十二 不许做的事

- 不许把 runtime_control_plane 的东西写进节点正文：重试、退避、超时缺省、错误分类、并行调度、监控状态机。
- 不许在科研图里加 provider / tool 边。
- 不许增删 delta 的八个字段。
- 不许在 frontmatter 里放 `dependencies` / `used-by` / `tags`——关系住在 `registry/graph.json`。
- 不许把 `shared-basis` / `specialized` / `family` 当执行层。
- 不许编造 v3 provenance。
- 不许相对化统计固定值（α 0.05 / power 0.8 / 预注册 / 公平比较）。
- 不许修改 `file-transfer/*.json`。
