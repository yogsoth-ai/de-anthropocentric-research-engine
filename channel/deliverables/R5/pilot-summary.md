# R5 试点汇总

## 试点范围

按 roster 示例与审计高危表交集选取 7 个节点：

`synthesize-meta-analytic-evidence`、`design-experiment`、`formulate-hypotheses`（对应 roster 的 `hypothesis-formulation`）、`analyze-constraints-readiness`、`rank-candidates`、`establish-empirical-baseline`、`audit-benchmark-validity`。

`adversarial-deliberation` 虽在审计的 6 节高危表中，但不在本轮 7 节试点交集内；未生成 pilot 文件。

## 行数与压缩比

源行数按当前 920 个 `SKILL.md` 的作者正文计数（去 frontmatter 与 generated tables）；v4 行数为本目录 `body.md` 物理行数。源节点数以 architecture `old` 中可解析到当前目录者计；因此与 roster 的历史估算可能不同。

| v4 节点 | 源节点/正文行数 | v4 body | 源 threshold 数 | body 保留数 | 压缩比（源/body） | 缩减 |
|---|---:|---:|---:|---:|---:|---:|
| synthesize-meta-analytic-evidence | 9 / 805 | 167 | 89 | 89 | 4.82:1 | 79.3% |
| design-experiment | 8 / 304 | 87 | 59 | 59 | 3.49:1 | 71.4% |
| formulate-hypotheses | 9 / 493 | 151 | 85 | 85 | 3.26:1 | 69.4% |
| analyze-constraints-readiness | 22 / 1,051 | 193 | 93 | 93 | 5.45:1 | 81.6% |
| rank-candidates | 13 / 734 | 163 | 72 | 72 | 4.50:1 | 77.8% |
| establish-empirical-baseline | 9 / 696 | 137 | 97 | 97 | 5.08:1 | 80.3% |
| audit-benchmark-validity | 7 / 600 | 139 | 96 | 96 | 4.32:1 | 76.8% |
| **合计** | **77 / 4,683** | **1,037** | **591** | **591** | **4.52:1** | **77.9%** |

`design-experiment` 的 roster 估算为 6 个旧节点/~702 行，而当前 architecture 列出 9 个 `old`、8 个可解析正文；`factor-level-design` 目录缺失，已明确记录为 unresolved，不作静默推断。阈值与文本门槛列由 `validate_threshold_fidelity.py` 逐条核验；591 条模式命中均保留。正文已重写为单一 UTF-8 台账，删除重复/损坏副本。

## 编译耗时

本轮未接入逐节点 profiler。以下是 R5 的人工+脚本工作记录估算，用于容量规划，不作为性能承诺：

| 节点 | 估算耗时 |
|---|---:|
| synthesize-meta-analytic-evidence | 9 min |
| design-experiment | 7 min |
| formulate-hypotheses | 7 min |
| analyze-constraints-readiness | 13 min |
| rank-candidates | 9 min |
| establish-empirical-baseline | 7 min |
| audit-benchmark-validity | 6 min |
| **合计 / 平均** | **58 min / 8.3 min** |

## 发现的边界 case

1. R1 已落锤：contract 以 body 固定小节为唯一权威，registry 只做生成索引与 source_ref 缓存，frontmatter 不扩张。
2. `systematic-literature-review/SKILL.md` 不存在，无法验证 roster 指定的典型模板。
3. architecture 的 `old` 含跨 package/历史别名；当前目录无法解析的名称被列入 log，不猜测正文。
4. source gate 有 XML-like、Markdown、表格三种写法；统一章节但保留原数字/比较符。
5. I2 区间存在重叠（0-40、30-60、50-90、75-100）；试点保留原值，未自行归一化。
6. 208 个源文件没有可识别作者标题；解析必须支持段落/列表驱动。
7. `score-object` rubric 的最终共享库方案未定；本轮遵守保守策略，涉及处复制并标记待重构。
8. 源文件中的 Unicode 比较符在部分终端显示为 mojibake；body ledger 使用 ASCII-normalized 表格，校验器统一归一化后逐条比对，不改变数值语义。

## 通过性自检

- 七个目录均含 `body.md` 与 `compilation-log.md`。
- 每个 body 都有 Input/Output contract、执行步骤、gate、failure、provenance、Delta 说明。
- 7 个 body 的数字门槛可在对应 log 与 v3 源节点中反查；无法解析的源名未被伪造为已继承。
- body 只描述科研变换；retry、parallelism、dispatch、monitoring 未写入科学步骤。
## Validator scope and blind spots

`validate_threshold_fidelity.py` scans author-authored source text only: frontmatter and generated `available-tables` are excluded. Named patterns cover symbolic comparators (`>=`, `<=`, `≥`, `≤`, `±`), `at least N`, `top-N`, percentages, numeric ranges, `<N`/`>N`, digit-bearing table rows, mandatory predicates, preregistration, fair-comparison, reproducibility, and explicit entry-gate phrases. Physical source line numbers are retained in every ledger.

Known blind spots requiring manual review: number words or non-English thresholds; implicit domain criteria without cue words; qualitative adjectives such as adequate/relevant/representative; formulas or constraints outside matched forms; and zero/low-count nodes.

Manual `design-experiment` review covered all 8 resolvable sources and found textual gates for HARD-GATE/minimum yield, same compute/tuning, preregistration/power/stopping, and seed/environment/verification reproducibility. `factor-level-design` remains explicitly unresolved because its directory is absent.
