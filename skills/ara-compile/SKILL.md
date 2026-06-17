---
name: ara-compile
description: 'SOP: Turn the feeding plan into the compiler''s $ARGUMENTS and run the external ARA compiler once inline to produce ../ara/'
version: 1.0.0
category: ara-from-context
type: sop
campaign: ara-from-context
input: Completed feeding plan + aligned 大方向 (from north-star-align)
output: A populated ara/ directory (sibling to context/), ARA Seal Level 1 passed
dependencies:
  skills:
  - compiler
---

# SOP: ARA Compile

**Key question**: 怎么把投喂计划喂给外部 compiler,一次抽出一份内部一致的 ARA?

## Preflight

先确认外部 `compiler` skill 可 load(ARA skills 已装:`npx @ara-commons/ara-skills`)。
若不可用,提示用户安装并**停下**,不要静默继续。

## Why one inline call, not multi-subagent

ARA 的 cross-layer binding(claim→proof→evidence、tree→claim)必须**全局一致**。
分批 compile 会各自从 C01 起撞 ID、断 tree,汇总等于重缝半成品 —— 正是 ARA 要消灭
的事。compiler 自带覆盖度循环(max 3 轮)+ 内建 `Task` 工具;真需要并行由它**内部**
自理,本 SOP 不越俎拆分。

## Procedure

1. **把投喂计划整理成 compiler 的 `$ARGUMENTS`**:
   - 主干文件清单 + trace 素材清单 + 图片清单的**路径**(compiler 按路径读);
   - 标注哪些是主干(报告线 → claims/problem);
   - 大方向作为约束文本(约束 PAPER.md 的 title/abstract);
   - `--output ../ara/`(与 `context/` 平级,天然不会被下次 review 当 context 吃回去)。

   例:
   ```
   compiler context/2026-06-06-01-30-stage7-...md context/2026-06-05-...stage6...md \
     context/figures/*.png \
     --output ../ara/ \
     主干=stage7(报告线);其余为过程线/图片;大方向:<从 north-star-align 来的一段>
   ```

2. **一次 inline 运行**:`Skill` load **compiler**,传上面的 `$ARGUMENTS`。
   compiler 跑 4 阶段(语义解构 → 认知映射 → src 层 → 探索图抽取)+ 覆盖度循环
   + Seal Level 1。

3. **Seal Level 1 不过**:compiler 自带 fix-iterate(2–3 轮),本 SOP 不接管;
   若仍不过,把失败报告**透传**给用户,停。

## Output

`<workspace>/ara/`(`logic/ src/ trace/ evidence/ PAPER.md`),Level 1 已过。
交给 `ara-rigor-review`。
