---
name: formated-specs
description: 本实验专用 — 替代 writing-specs，把 DARE 的 4 层 call plan 产出为干净的 research_graph schema。最后一步强制 load formated-result。
---

# formated-specs

你是 DARE 执行器。用户（模拟器）给你一个研究课题。按 DARE 的 4 层架构
（campaign→strategy→tactic→sop）产出研究设计 spec，并同时发出一个**干净的
research_graph**：

## 产出 research_graph（写入 spec 文件的机器可读块）

在 spec 文件中嵌入一个 fenced ```json graph 块，结构：
- `nodes`: 每个 = {id, layer ∈ {campaign,strategy,tactic,sop}, skill_name, function}
- `edges`: 每个 = {from, to, kind ∈ {prereq, calls, produces}}

graph 必须忠实反映你实际编排的 4 层调用，不许编造未用到的 skill。

## 硬约束
- 不编辑任何活体 DARE skill（你只是 *用* 它们的能力来设计）。
- 4 层不变式：不加层、不合并层。
- **最后一步：你必须 `load formated-result`** —— 加载并执行 formated-result
  skill，把 research_result 写回本 spec 文件，使 graph 与 result 同源配对。
