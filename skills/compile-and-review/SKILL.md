---
name: compile-and-review
description: 'Tactic: Compile the feeding plan into an ARA via the external compiler, then run Level-2 rigor review over it'
version: 1.0.0
category: ara-from-context
type: tactic
campaign: ara-from-context
sops:
- ara-compile
- ara-rigor-review
dependencies:
  sops:
  - ara-compile
  - ara-rigor-review
---

# Tactic: Compile and Review

**Key question**: 把投喂计划编译成一份内部一致的 ARA,并做认识论审查。

## Flow

1. `Skill` load **ara-compile** —— 把投喂计划整理成 compiler 的 `$ARGUMENTS`
   (路径 + 标主干 + 大方向约束 + `--output ../ara/`),一次 inline 跑 compiler,
   得 `../ara/`(Seal Level 1 已过)。
2. `Skill` load **ara-rigor-review** —— 对 `../ara/` 跑 rigor-reviewer 的 Level 2
   六维审查,得 `ara/level2_report.json`,透传给用户。

整条链是**一次性前向流**,不是自动迭代循环。D5 低分由用户决定是否回
`context-review` 补打捞。

## Output

`ara/`(完整 ARA)+ `ara/level2_report.json`。

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ara-compile | SOP: Turn the feeding plan into the compiler's $ARGUMENTS and run the external ARA compiler once inline to produce ../ara/ |
| ara-rigor-review | SOP: Run the external ARA rigor-reviewer (Seal Level 2, six-dimension semantic review) over ../ara/ and pass its level2_report.json to the user |

<!-- END available-tables (generated) -->
