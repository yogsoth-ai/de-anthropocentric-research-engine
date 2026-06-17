---
name: ara-from-context
description: 'Campaign: Compile a context/ research record into an ARA (Agent-Native Research Artifact) and run a Level-2 epistemic review — no LaTeX, no narrative paper'
version: 1.0.0
category: ara-from-context
type: campaign
input: A context/ directory (INDEX.md + timestamped research records + produced images)
output: ara/ (4-layer ARA) + ara/level2_report.json
tactics:
- context-review
- compile-and-review
dependencies:
  tactics:
  - compile-and-review
  - context-review
  sops:
  - ara-compile
  - ara-rigor-review
  - context-exploring
  - north-star-align
---

# Campaign: ARA From Context

**What this is**: DARE 流水线最末端的"成文"环节。吃前面研究循环
(research ↔ experiment-execution 反复迭代)沉淀在 `context/` 里的全部产物,
编译成一份 **ARA**(机器可执行的四层知识包),并做认识论审查。**不写 LaTeX /
叙事论文** —— ARA 刻意反对 storytelling,要的是逻辑弧在结构上闭合。

**Source of truth**: 所有素材来自 `context/`。核心 = 末次 EE 的最终 report +
全程迭代轨迹 + 研究产出的图片。

## Flow

1. `Skill` load **context-review** —— 回顾 `context/`,分三类素材,对齐大方向,
   产出投喂计划。
2. `Skill` load **compile-and-review** —— 一次 inline 跑外部 compiler 得 `../ara/`,
   再跑 rigor-reviewer 得 `level2_report.json`。

## External dependency

运行需 ARA 的 `compiler` + `rigor-reviewer` skill 在位
(`npx @ara-commons/ara-skills`)。见本 repo README。

## Output

`ara/`(`logic/ src/ trace/ evidence/ PAPER.md`)+ `ara/level2_report.json`。

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| compile-and-review | Tactic: Compile the feeding plan into an ARA via the external compiler, then run Level-2 rigor review over it |
| context-review | Tactic: Review a context/ directory — sort material into ARA types, locate and align the north-star, and produce a feeding plan for the compiler |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ara-compile | SOP: Turn the feeding plan into the compiler's $ARGUMENTS and run the external ARA compiler once inline to produce ../ara/ |
| ara-rigor-review | SOP: Run the external ARA rigor-reviewer (Seal Level 2, six-dimension semantic review) over ../ara/ and pass its level2_report.json to the user |
| context-exploring | SOP: Read context/INDEX.md and sort the whole directory into three ARA material types (report line, process line, images), locate the north-star file, and draft a feeding plan for the ARA compiler |
| north-star-align | SOP: Deep-read the original north-star context, distill this ARA's overall direction, and align it with the user via the reused present-and-ask / present-candidates dialogue SOPs |

<!-- END available-tables (generated) -->
