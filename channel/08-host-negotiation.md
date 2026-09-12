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
