---
name: north-star-align
description: 'SOP: Deep-read the original north-star context, distill this ARA''s overall direction, and align it with the user via the reused present-and-ask / present-candidates dialogue SOPs'
version: 1.0.0
category: ara-from-context
type: sop
campaign: ara-from-context
input: The north-star file path + draft feeding plan (from context-exploring)
output: An aligned 大方向 paragraph filled into the feeding plan (constrains PAPER.md title/abstract)
dependencies:
  skills:
  - present-and-ask
  - present-candidates
---

# SOP: North-Star Align

**Key question**: 这篇 ARA 的大方向是什么?和用户对齐了吗?

## Procedure

1. **深读 north-star context 文件**(`context-exploring` 定位的那篇)。提炼:
   这条研究弧最初要回答的问题、它的范围边界、它自认的核心贡献。

2. **草拟大方向**:一段话 = (a) ARA 的 title hint,(b) abstract 应覆盖的范围
   约束。这段会进 compiler 的 `$ARGUMENTS`,用来约束 PAPER.md 的 title/abstract,
   防止逆向抽取出的 ARA 跑题。

3. **与用户对齐**(复用 north-star 的对话 SOP):
   - `Skill` load **present-candidates** —— 把 `context-exploring` 聚出的 arc 候选
     作排序候选呈现给用户(默认整目录,但给手挑口子)。
   - `Skill` load **present-and-ask** —— 把"这篇 ARA 用哪些 context / 大方向是否
     如此理解"摆给用户确认,收回用户的取舍。

4. **回填**:把对齐后的大方向写进投喂计划的 `### 大方向`,把用户手挑的范围写进
   `### arc 范围`。

## Output

完成的投喂计划(大方向已填、arc 范围已定)+ 对齐过的大方向,交给
`compile-and-review` tactic。
