# 19 — v4 入口层（内测前置）

## [R0 → all] 2026-09-16

账六（连通关系内联）主线已闭：317/317 call、82/82 tactic jump、五个保护小节
逐字节不变、216 个 SOP 哈希不变、`validate_graph.py` 退出 0 零 warning。
我独立复核过，不采信自检表。

本帖开三件新活，**并行**。目标不是再验一遍图，是让 v4 直接能跑。
主人的话原样记下：内测测的是「这个 v4 到底能不能用」，
交付物必须是「直接能用、比 v3 更强的 DARE」，不是一轮一轮的分项验证。

---

## 一 缺口：v4 没有入口（R0 漏项）

v3 的起法：

```
AGENTS.md:10   先读 de-anthropocentric-research-engine/SKILL.md   总编排器
AGENTS.md:11   选包前读 research-catalog/SKILL.md                  能力菜单
               → writing-specs      北极星 → 可执行 spec
               → executing-specs    按 spec 逐阶段执行，多 session 恢复
```

`ls v4/skills/ | grep -iE "de-anthropocentric|research-catalog"` 返回空。
**四个入口在 v4 一个都没有。**

v4 是 267 个平铺节点，51 个 tactic 全部无入边（已核）。
主人说「研究一下 X」时，agent 面前是 267 个等价 skill，没有编排器、
没有阶段流水线、没有「北极星先做」的强制，会随手抓一个 tactic 开工。

这是内测跑不起来的结构性原因。我此前把它当成「发现机制缺口」，
两次都说轻了。记在 R0 账上。

## 二 缺口：75 条 SOP jump 未注入（R0 漏项）

`graph.json` 的 157 条 jump 实际拆分：

```
tactic → tactic    82   已注入
sop    → sop       75   未注入，分布在 71 个 SOP 上
```

我上轮把范围写成「仅 51 个 tactic，216 个 SOP 出边为 0，是叶子」。
**那句只对 call 成立。** N2 按我的规格执行，无过错，是我的账。

样例：`generate-candidate-directions → synthesize-field-panorama`、
`formulate-top-goal → decompose-and-or-goal → validate-goal-tree → assess-goal-feasibility`。

## 三 缺口：AGENTS.md 与 v4 硬冲突

```
AGENTS.md:12   Treat YAML `dependencies` in each `SKILL.md` as the authoritative call graph.
```

v4 的 frontmatter 只有 `name` + `description`，267 份带 `dependencies` 的：**0 份**。
第 10、11 行指向的两个入口 skill 在 v4 不存在。

---

## 四 派活

```
N2 ─── ① 75 条 SOP jump 注入 + 脚本扩到 474/474
                                                  ┐
R5 ─── ② 入口层 4 份正文（只出正文，不落盘）        ├── 三家并行
                                                  │
R6 ─── ③ AGENTS.md v4 稿                          ┘
        │
    N1 ─── ② 落盘 v4/skills/
        │
    R0 ─── 474/474 + validator 退出 0 + 入口链实走
```

### ① N2 — 补齐 75 条 SOP jump

按 R5 已落锤的软措辞格式注入 71 个 SOP 上的 75 条 jump：
`consider \`X\`` / `\`X\` may be the better next tactic`，带触发条件。
**jump 目标绝不许出现 `MUST`。**

`validate_inline_edges.py` 扩到覆盖 SOP jump，终态必须校到 **474/474**：
317 call + 82 tactic jump + 75 sop jump。

216 个 SOP 的五个保护小节（`## Input contract`、`## Output contract`、
`## Thresholds and quality gates`、`## Preserved source criteria ledger`、
`## Provenance map`）仍须与注入前逐字节一致 —— 这轮改的是执行协议与
jump 落点，不是契约。`inline-edge-baseline.json` 需追加 SOP 基线，不覆盖旧基线。

写区：`v4/registry` / `v4/scripts` / `v4/docs`。

### ② R5 — 入口层 4 份正文

只出正文，落 `deliverables/R5/`，不写 `v4/skills/` —— 那是 N1 的写区。

| 节点 | 职责 |
|---|---|
| `dare-v4` | 总编排器。强制 北极星 → spec → 执行，不许跳阶段 |
| `research-catalog-v4` | 能力菜单。51 个 tactic 按 10 个 family 索引，带「何时用」 |
| `write-research-spec` | 北极星 + 用户输入 → 可执行 spec |
| `execute-research-spec` | 按 checkpoint 逐阶段执行 + 断点恢复 |

约束：

1. **菜单只列 51 个 tactic，不列 216 个 SOP。** SOP 由 tactic 的
   `You MUST load skill` 拉起，菜单管的是 tactic 选择。
2. `execute-research-spec` 的机制照 `v4/docs/runtime-boundary.md` 第 2、3 节
   已写死的来，不许发明第二套持久化。三条不许改：
   八字段 `ResearchStateDelta`、追加式 checkpoint、`SpecView` 是投影不落盘。
3. **这 4 个是产品外壳，不是科研图节点。** 进 `v4/skills/`，
   **不进 `graph.json` 的 267**，不得伪装成第三层。
   依据 `runtime-boundary.md` 开篇：这类资源「不得伪装成第三层节点」。R0 已签此边界。
4. 参考 v3 的 `skills/de-anthropocentric-research-engine/`、`research-catalog/`、
   `writing-specs/`、`executing-specs/`，但**不许照抄** —— v3 是 4 层 920 个，
   v4 是 2 层 267 个，编排逻辑不同。
5. 入口层内部若相互调用，同样用 `You MUST load skill` 硬语气，与账六格式一致。

### ③ R6 — AGENTS.md v4 稿

落 `deliverables/R6/`，不动真文件 —— `AGENTS.md` 在 repo 根，是 R0 定稿后的事。

逐条处理：

- 第 12 行改为：正文里的 `You MUST load skill X` 是权威调用关系；
  `registry/graph.json` 是机器索引，不是 agent 的运行时读物。
- 第 10、11 行改指 R5 正在建的 `dare-v4` 与 `research-catalog-v4`。
- 第 15 行（`context/INDEX.md`）与 `runtime-boundary.md` 第 3.1 节一致，保留。
- 说明 v4 替换 v3 后 skill root 怎么解析。**主人已定：替换，不并存。**

不许写 harness 概念（subagent / token 预算 / 上下文压缩 / 调度）。

---

## 五 通过标准

`python v4/scripts/validate_graph.py` 不带跳过开关退出 0。退出码是唯一判据。
另加：474/474 边全覆盖；入口链 `dare-v4 → research-catalog-v4 → tactic → SOP`
能被实际走通一遍。

## 六 约束（不变）

R1–R6 只写 `deliverables/<代号>/`；N1 写 `v4/skills`，N2 写
`v4/registry` / `v4/scripts` / `v4/docs`；R0 只写 `channel/*.md`。
禁一切 git 写操作。禁 superpowers / ara。对外动作先报主人。
`file-transfer/2026-08-23-22-16-dare-v4-architecture.json` 一字节不动。
根目录 `skills/` 的 920 个 v3 活安装源一字不动。lark-markdown 不进 skill 正文。
