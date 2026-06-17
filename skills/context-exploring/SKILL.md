---
name: context-exploring
description: 'SOP: Read context/INDEX.md and sort the whole directory into three ARA material types (report line, process line, images), locate the north-star file, and draft a feeding plan for the ARA compiler'
version: 1.0.0
category: ara-from-context
type: sop
campaign: ara-from-context
input: A context/ directory containing INDEX.md + timestamped .md research records (+ any produced images)
output: A feeding plan (markdown block, headings 投喂计划/主干文件/trace 素材/图片清单/arc 范围/大方向) + the located north-star file path
dependencies: {}
---

# SOP: Context Exploring

**Key question**: 这批 `context/` 里,对生成一份 ARA 最重要的素材分别是哪些,怎么分类喂给 compiler?

## Why this matters (gap-3 的担子在这里)

ARA 的 `compiler` 是**逆向抽取器**:它只抽源里**已有**的探索过程,绝不补写
(compiler Rule 9/14)。所以 ARA 的 `exploration_tree` 丰不丰满,不取决于 compiler,
取决于 `context/` 有没有记下**失败路径 / 被否方案 / 迭代 pivot**。这把担子精确落在本
SOP:必须主动**打捞过程线**,而不是只挑末次成功 report。

## Procedure

1. **读 `context/INDEX.md`。** 它是总账:列 File / Phase / Topic / Checkpoints /
   Last Updated。正常 context 必有 INDEX;若缺失,停下并提示用户先维护 INDEX
   (不做无-INDEX 降级)。

2. **默认整目录 = 一份 ARA。** 同时把文件按 Phase/Topic 聚成 **arc 候选**
   (一条研究弧 = 一组连续推进同一 Topic 的文件)。

3. **三类素材分拣**(这是本 SOP 的核心判断):
   - **报告线 → claims / problem**:末次 experiment-execution 的最终 report、
     结论性产出、被确认的设计。这是 `logic/claims.md` + `logic/problem.md` 的源。
   - **过程线 → exploration_tree**:失败尝试、被否决的方案、迭代中的 pivot、
     "我们本来想 X 但发现 Y 所以转向 Z"。这是 `trace/exploration_tree.yaml` 的源。
     **主动打捞**:逐个 checkpoint 扫,凡是 dead_end / decision / pivot 痕迹都收。
   - **图片 → evidence**:研究产出的图表 / 图示 / 截图。这是 `evidence/figures` +
     `evidence/tables` 的源。(正常 context 会有;没有就这类为空,不报错。)

4. **定位 north-star 文件**:INDEX 里 Phase 标含 "North Star" 的那篇(通常是
   `*-north-star-*.md`)。交给下游 `north-star-align` 深读。

5. **草拟投喂计划**(交接物,markdown 块,严格用下列 heading):

   ```markdown
   ## 投喂计划
   ### 主干文件
   - <path>  — 报告线,claims/problem 源
   ### trace 素材
   - <path>  — 过程线:<失败/被否/pivot 一句话>
   ### 图片清单
   - <path>  — <图表/图示 一句话>
   ### arc 范围
   - 默认整目录;或用户手挑的 arc/文件子集
   ### 大方向
   - (留空,由 north-star-align 填)
   ```

## Output

把投喂计划 + north-star 文件路径交给本 tactic 的下一步(`north-star-align`),
不落新文件。
