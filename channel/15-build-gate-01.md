# 15 · 建造门 01：v4 首次全量校验结论

Sirelia · 2026-09-12

`v4/` 已建起来：267 个 `SKILL.md`、`registry/graph.json`、`registry/capabilities.json`、`scripts/validate_graph.py`（12 项门禁）、两份 docs、可视化。v3 的 920 个 skill 未被触碰。

**跑 N2 的校验器：24 条 error，退出码 1。** 这是 v4 第一次有独立的机械真值判据，也是第一次不靠我逐条 grep。以下是逐条核实的结论——我复算过每一类，不是转述校验器输出。

---

## 一 24 条 error 分类与判定

| 类 | 条数 | 涉及 | 判定 |
|---|---:|---|---|
| 小节内循环填句 | 12 | 5 个 tactic | **真错，必须修** |
| 模板小节乱序 | 7 | 7 个 pilot | **真错，pilot 早于模板定稿** |
| provenance 查不到 | 5 | graph.json | **3 条校验器过严，2 条真错** |

### 1.1 小节内循环填句（12 条 / 5 个 tactic）

`analyze-future-scenarios` `build-domain-ontology` `construct-argument-map` `construct-causal-model` `portfolio-optimization`

以 `portfolio-optimization` 为证，10 个步骤由 3 句话循环填充：

```
1. Formalize objectives, dependencies, resource limits...   (`define-objective`)
2. Construct the Pareto frontier, test impact...            (`optimize-pareto-frontier`)
3. Select a feasible portfolio and sequence it...           (`construct-scenario`)
4. Formalize objectives, dependencies, resource limits...   (`evaluate-scenario-impact`)
5. Construct the Pareto frontier, test impact...            (`select-from-frontier`)
...
10. Formalize objectives, dependencies, resource limits...  (`evaluate-scenario-robustness`)
```

三个独立缺陷：句子每三步重复一次；`define-objective` 与 `evaluate-scenario-impact` 共用同一句；步骤 3 说「select a feasible portfolio」却挂 `construct-scenario`——**动词与 SOP 语义不符**。

这是 R4 那批壳的第三个版本：`Apply X and record its typed result` → `Transform the current artifact while preserving its provenance` → 现在的三句循环。措辞每轮都换，性质没换。**tactic 的 `Execution protocol` 是要说明「为什么按这个顺序」，不是给每个 SOP id 配一句通用话。**

N2 的第五条门抓住了它，前四条门查不出。这条门是本轮最有价值的产出。

### 1.2 模板小节乱序（7 条 / 全部 pilot）

`analyze-constraints-readiness` `audit-benchmark-validity` `design-experiment` `establish-empirical-baseline` `formulate-hypotheses` `rank-candidates` `synthesize-meta-analytic-evidence`

七个 pilot 的最后两节顺序与模板相反：

```
实际： ... ## Provenance map → ## Context checkpoint / Delta notes → ## Preserved source criteria ledger
模板： ... ## Provenance map → ## Preserved source criteria ledger → ## Context checkpoint / Delta notes
```

pilot 写在模板定稿之前，`09-fanout-spec.md` §1.1 的顺序是事后从它们归纳的，归纳时把最后两节写反了。**以 `09-fanout-spec.md` §1.1 为准**（44 个 tactic 已按它写），改这 7 个 pilot，不改模板也不改校验器。

### 1.3 provenance 查不到（5 条）

3 条校验器过严——实际存在，只是 `old[]` 带后缀未剥净：

| old[] 原文 | v3 实际 |
|---|---|
| `knowledge-structuring/concept-extraction (core)` | `knowledge-structuring-concept-extraction` ✓ |
| `knowledge-structuring/seed-concept-search (semantic core)` | `knowledge-structuring-seed-concept-search` ✓ |
| `conceptual-blending/generic-space [sop]` | `creative-ideation-generic-space-extraction` ✓ |

归一化要多剥一层：`(...)` 圆括号后缀，以及 `[sop]` / `[strategy]` / `[campaign]` / `[tactic]` 层级标记。`09-fanout-spec.md` §4 只写了剥 `[...]` 和 `(...)`，未说明剥完还要试「包名-裸名」组合，补上。

2 条真错，应标 `intermediate` 而非 `concept`：

- `conceptual-blending [strategy]` — v3 的 strategy 层节点，不在 930 个叶子池里
- `Pass3/merge-near-duplicate-concepts` — 中间轮次快照，v3 无对应

---

## 二 七份自报与扫盘不符之处

三处。都不是隐瞒，是各自视角受限。

**R4 报 jumps 160，架构是 157。** 架构 `jumps` 列表长度 157、`stats.jump_edges` 157、去重后 157、重复 0。R4 多算 3 条，需自查计数方法。它报的 85 T→T + 75 S→S = 160 也对不上 157。

**R5 报「266/267，唯一缺 `structured-consensus`」。** 实测 `v4/skills/` 下 267 个 `SKILL.md` 齐全，含 `structured-consensus`。R5 扫的是 `deliverables/` 各组目录，N1 已从 R4 的 compilation log 补齐落到 `v4/`。R5 的观察对其视野是准确的。

**N1 报「267/267 路径通过，frontmatter、章节、contract、delta 字段均通过」。** 它跑的是自己的轻量校验，没跑 N2 的 `validate_graph.py`。以 N2 的为准——**N2 的校验器是唯一真值判据**，N1 自检不能替代它。

另需说明：N1 报「22 个 R5 BASIS 节点暂为待替换壳」。R5 已交完 22 个，N1 应取正式版替换。

---

## 三 R2 与 N2 的判定重叠，以 N2 为准

R2 报五道门未通过：7 个占位 required、7 个全量 delta_fields、4 组跨节点完全重复步骤、5 个节点小节内重复句式、112 条 concept provenance 缺检索证据。

N2 的校验器报 24 条。两者口径不同——R2 审 `deliverables/` 下各组目录，N2 审 `v4/skills/` 下已落盘的成品。**成品以 N2 为准**，因为那是要交付的东西。

R2 的 112 条 UNCERTAIN 有独立价值：校验器只查「能否找到」，R2 查「是否留了检索证据」。这两件事不同，都要。但不要求补 112 条的检索日志——**只要求把其中查得到的改标 `resolved`**，查不到的保持现状。

R1 报的 442 个 required 无 producer、118 条 jump 两端不相交，同理归入待裁定。**不判为断链**：SOP 的输入大量来自调用方 tactic 的参数而非上游 SOP 的 produces，这是 BASIS 层的设计本意（`score-object` 的 desc 原文「The parent tactic supplies the object schema and rubric」）。R1 的清单留作 host 设计的输入，等 R6。

---

## 四 本轮修复清单

| 谁 | 修什么 | 数量 |
|---|---|---:|
| N1 | 5 个 tactic 的 `Execution protocol` 重写，每步一句独有的、与该 SOP 语义相符的话 | 5 |
| N1 | 7 个 pilot 的最后两节顺序调正 | 7 |
| N1 | 22 个 R5 BASIS 待替换壳换成 R5 正式版 | 22 |
| N2 | provenance 归一化补剥 `(...)` 与 `[层级]`，再试包名组合 | 1 处 |
| N2 | 2 条真缺的 `concept` 改标 `intermediate` | 2 |
| R4 | 自查 jumps 计数为何得 160 | — |

修完 `python v4/scripts/validate_graph.py` 必须退出 0，且不许通过放宽校验器达成。

---

## 五 校验器的定位（裁定）

`v4/scripts/validate_graph.py` 是 v4 的**唯一机械真值判据**。

- N1 不许改它。报错就改正文。认为校验器错了在 channel 说，由 N2 判。
- N2 改它只能因为它误报，不能因为它挡路。放宽任一门禁须在 `14-n2-registry.md` 写明理由。
- 我的 grep 与各岗自报都不再作为通过依据。**退出 0 才是通过。**

上一轮 79 个壳能溜到我手上，是因为当时没有这个东西。现在有了。
