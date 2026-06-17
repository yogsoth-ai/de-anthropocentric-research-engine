---
name: context-review
description: 'Tactic: Review a context/ directory — sort material into ARA types, locate and align the north-star, and produce a feeding plan for the compiler'
version: 1.0.0
category: ara-from-context
type: tactic
campaign: ara-from-context
sops:
- context-exploring
- north-star-align
dependencies:
  sops:
  - context-exploring
  - north-star-align
---

# Tactic: Context Review

**Key question**: 这批 context 里,生成 ARA 最重要的素材是什么?大方向和用户对齐了吗?

## Flow

1. `Skill` load **context-exploring** —— 读 INDEX → 整目录分三类素材(报告线/过程线/
   图片)→ 聚 arc 候选 → 定位 north-star 文件 → 草拟投喂计划。
2. `Skill` load **north-star-align** —— 深读 north-star → 提炼大方向 → 复用
   present-candidates/present-and-ask 与用户对齐 → 回填投喂计划的大方向 + arc 范围。

## Output

① 对齐过的大方向 ② 完整投喂计划(主干文件 / trace 素材 / 图片清单 / arc 范围 /
大方向),交给 `compile-and-review`。

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| context-exploring | SOP: Read context/INDEX.md and sort the whole directory into three ARA material types (report line, process line, images), locate the north-star file, and draft a feeding plan for the ARA compiler |
| north-star-align | SOP: Deep-read the original north-star context, distill this ARA's overall direction, and align it with the user via the reused present-and-ask / present-candidates dialogue SOPs |

<!-- END available-tables (generated) -->
