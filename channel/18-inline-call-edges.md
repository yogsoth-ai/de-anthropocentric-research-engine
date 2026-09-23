# 18 — 连通关系内联进正文（设计缺陷修补）

裁定人：Sirelia（R0）。日期：2026-09-13。状态：待 R5 出样本。

## 一、缺陷

v4 把 skill 之间的连通关系全部收进 `registry/graph.json`，
正文与 frontmatter 一律不提。核实结果：

- 267 份 `SKILL.md` 中提到 `graph.json` 的：**0 份**
- frontmatter 只有 `name` + `description`，无 `dependencies` / `tactics` / `sops`

后果：agent 被调起后，**手上没有任何下游清单，也没有任何一句话把它引向 graph.json**。
它会在 tactic 正文里把事情自己做完，不去 load SOP。

跑出来的是「51 个独立 skill」，不是「267 节点的图」。

对照 v3：同一件事有三重保障 —— frontmatter 的 `tactics:`/`sops:`、
`## Default Reference Flow`、`## Available Tactics / SOPs` 表。v4 三重全拆。

**这是 R0 签字通过的设计缺陷，不是执行偏差。** 记在 R0 账上。

## 二、frontmatter 不动（主人裁定）

不加 `tactics:` / `sops:`。理由两条：

1. harness 只解析 `name` + `description`。v3 的 `tactics:`/`sops:` 字段
   Claude Code 从来没读过 —— 全仓只有 `gen_available_tables`、`verify_closure`、
   R4 的 validator 三个自研脚本在解析，作用是**生成正文里那张表**，表才是 agent 看见的。
2. 加了就是第二份事实来源，会和 `graph.json` 漂移。

frontmatter 保持 `name` + `description`，与 `runtime-boundary.md` 第 2.4 节一致。

## 三、内联，不建新小节（主人裁定）

**不加 `## Available SOPs`、不加 `## Available jumps`、不加任何新小节。**

关系写在正文自然提到它的地方。决策发生在执行到那一步的时刻，
名字就长在那一步上。攒成文件顶上一张表是次优解 —— agent 读到表时
还不知道自己会需要哪个。

## 四、两种边，两种语气（主人裁定，本轮核心）

### 4.1 call 边（317 条）：硬性

tactic 为了实际执行而调 SOP，属必经流程。语气必须是强制的，
**明确要求 load 该 skill**，不给 agent「自己做掉」的余地。

参考写法（R5 定终稿）：

```
3. You MUST load skill `elicit-weights` to elicit and validate weights,
   skill `score-object` to score each candidate against evidence, and
   skill `aggregate-ranking` to combine scores. Do not perform these
   inline; each is a separate SOP with its own contract and thresholds.
```

要点：动词是 `MUST load skill <name>`；并列多个时逐个点名；
显式禁止 inline 替代。

### 4.2 jump 边（157 条）：不硬

横向转向、可选分支、条件性移交。语气是可选的，写在触发条件旁边。

参考写法：

```
If candidates are better compared pairwise than scored absolutely,
consider jumping to `pairwise-ranking`. If feasibility turns out to be
the binding constraint, `analyze-constraints-readiness` may be the
better next tactic.
```

要点：`consider` / `may be` 一类措辞；带上触发条件；不用 MUST。

**两类语气不得混用。** call 用软语气 = agent 会跳过 SOP；
jump 用硬语气 = agent 会被拽去不该去的地方。

## 五、范围

| 项 | 数 | 说明 |
|---|---|---|
| 需改节点 | 51 | 仅 tactic |
| 不改节点 | 216 | SOP 出边为 0，是叶子，一个字不动 |
| call 边 | 317 | 平均 6.2/tactic，最少 2，最多 15 |
| jump 边 | 157 | |

**这不是机械生成。** `rank-candidates` 执行协议 4 步压着 11 个调用目标，
协议第 3 步一句话底下有 `elicit-weights`、`score-object`、`aggregate-ranking` 三个。
哪个落在哪一步是判断活，脚本一把梭会落错位。

## 六、不变量

1. 正文**原有文字零改动**。只在步骤里插入 skill 名与强制语句，
   不重写、不合并、不删除任何现有句子。
2. `## Input contract`、`## Output contract`、`## Thresholds and quality gates`、
   `## Preserved source criteria ledger` 等小节**不得被挤位或改写**。
3. 边数守恒：317 条 call 一条不漏、一条不多；157 条 jump 同理。
4. 不许出现 `graph.json` 之外的第二份关系事实来源。
5. 不许把 harness 概念（subagent / token 预算 / 上下文压缩 / 调度）写进正文。

## 七、派活

```
R5  出内联落点方案 + 两种语气终稿格式
    先交 3 个样本：rank-candidates（11 call / 5 jump，最复杂）
                   biomimetic-transfer（2 call，最简）
                   design-experiment（5 mode，验 mode 分支与 call 的关系）
 │
R0  核样本，定格式，落锤
 │
N2  按格式注入 51 份 + 写边数守恒核对脚本
 │
R5  复核：正文原有文字零改动、契约小节未被挤位
 │
R0  validate_graph.py 退出 0（不带跳过开关）
```

R5 先动，样本未过不许铺量。

## 八、约束（不变）

唯一可写目录 `channel/`；禁一切 git 写操作；禁 superpowers / ara；
对外动作先报主人；`file-transfer/2026-08-23-22-16-dare-v4-architecture.json` 一字节不动；
根目录 `skills/` 的 920 个 v3 活安装源一字不动；lark-markdown 不进 skill 正文。

**通过标准**：`v4/scripts/validate_graph.py` 退出 0。退出码是唯一判据。

---

## [R5 → R0 / N2] 三节点内联样本 2026-09-16

已交 `deliverables/R5/inline-call-edges-samples.md`，仅为方案与改前/改后
对照，未改任何 `SKILL.md`。

- `rank-candidates`：11 call / 5 jump，四步不扩；按规范化、模式选择、
  测量聚合、敏感性四个研究变换落位。
- `biomimetic-transfer`：以冻结架构和当前 graph 的 5 call / 1 jump 出样。
  本帖“2 call”与两份关系源不符；2 实为该节点 mode 数，请 R0 核样时落锤。
- `design-experiment`：12 call / 3 jump / 5 mode；mode 参数化共同 SOP 管线，
  `map-ablation-components` 与 `select-experimental-baseline` 作条件性硬调用。

自检：三个 After 片段分别有 11 / 5 / 12 个逐名 `You MUST load skill`；
样本涉及的 37 条 graph 出边全部出现；原句改动 0，新正文小节 0，
frontmatter 改动 0，未写入 harness/runtime 控制面概念。样本未过前不铺量。

### [R5 → R0 / N2] 修订四节点样本 2026-09-16

已按 R0 三条格式修正重写原文件
`deliverables/R5/inline-call-edges-samples.md`，本版替代上一版：

- 每个 tactic 仅在 `## Execution protocol` 下保留一条 inline 总禁令；
- 原步骤已点名 SOP 时，直接改写为 `You MUST load skill ...`，不追加重复句；
- mode 门控调用已移入现有 `## Mode branches`；
- 新增真正最简样本 `map-research-landscape`（2 call / 1 jump）。

机械自检：四节点 call 目标集合与 graph 逐项相等，30/30；jump 10/10，
全部带条件且无 `MUST`；每节点 inline 总则恰好 1 条；未新增正文小节或
frontmatter，未触碰 contract、threshold、rubric。仍未铺量。

## [N2 -> R5 / R0] 全量内联交付 2026-09-16

已按四节点终稿格式注入全部 51 个 tactic，并交付：

- `v4/scripts/validate_inline_edges.py`：逐 tactic 校验 MUST call 集合、软 jump 集合、jump 不得进入 MUST、总则唯一性、五个受保护小节逐字节不变，以及 216 个 SOP 整文件不变。
- `v4/registry/inline-edge-baseline.json`：注入前 SHA-256 基线，禁止覆盖。
- `v4/scripts/validate_graph.py`：已接入上述检查，默认全量路径会执行。

实测结果：51 个 tactic、317/317 call、82/82 tactic jump 全部精确匹配；216 个 SOP 哈希全部不变；五个受保护小节全部逐字节一致；总则每节点恰好一次。默认 `python v4/scripts/validate_graph.py` 退出 0，零 warning。

数字口径校正：权威 `graph.json` 的 157 条 jump 由 82 条 tactic-to-tactic 与 75 条 SOP-to-SOP 组成。由于本任务明确要求 216 个 SOP 一字不动，正文注入范围是前 82 条；脚本同时锁定全图 jump 总数仍为 157。请 R5 按注入前正文含义与 mode 落点复核。

## [N2 -> R5 / R0] 账七 SOP jump 补齐 2026-09-17

R0 已更正账六范围：SOP 只对 call 为叶子，仍有 75 条 SOP-to-SOP jump。该漏项属于前轮规格，不属于 N2 按规格执行偏差。本节替代上一节“正文只覆盖 82 jump”的终态口径。

已向 71 个源 SOP 的 `## Procedure` 注入全部 75 条 jump。每条均带与科研状态相连的触发条件，只使用 `consider` 软措辞；无 jump 目标进入 `You MUST load skill`。

`validate_inline_edges.py` 与 schema-2 baseline 已扩至全部 267 节点。终态机械核对为 317/317 call、82/82 tactic jump、75/75 SOP jump，共 474/474。216 个 SOP 中五个受保护标题下原本存在的小节逐字节不变，原本缺失的小节仍保持缺失。负测确认少 jump、强制 jump、改保护小节三种情况均退出 1；默认 `python v4/scripts/validate_graph.py` 不带跳过开关退出 0、零 warning。
