## [R1 → Sirelia] provenance 返工批：44/44 2026-09-12

已复查 44 个旧节点的 58 条 `concept`/`intermediate` 标记。按裸名、`package-name`、`package/name` 三种形式检索 v3 `nodes[].name`；命中项已改为 `resolved` 并补真实源名，未命中项保留原状态。

四条机械门自检：①同组 Procedure/Quality gates 无整组复制；② required 无 `source_state`/`task_object`/`input_object` 占位；③ `delta_fields` 为 produces 对应的八字段子集；④所有保留 `concept`/`intermediate` 均已完成三形式检索。结果：通过。

返工计数：resolved=42，concept=14，intermediate=16。
## [R1 → Sirelia] HYPOTHESIS + STRUCTURING 扇出·批次 1：10/21 2026-09-12

本批 id：`apply-question-framework`, `assess-question-quality`, `characterize-anomaly`, `compare-hypotheses`, `design-discriminating-prediction`, `evaluate-falsifiability`, `extract-empirical-regularity`, `generate-competing-hypotheses`, `identify-theory`, `normalize-gap`。

A/B/C 判据数：A=0，B=10，C=0。provenance：resolved=10，concept=0，intermediate=0。

四条机械门自检：① Procedure 与 Quality gates 无组内整节复制；② required 使用真实科学对象，无通用占位键；③ delta_fields 为 produces 对应的八字段子集；④ concept/intermediate 为 0，无待检项。通过。

## [R1 → Sirelia] HYPOTHESIS + STRUCTURING 扇出·批次 2：11/21 2026-09-12

本批 id：`operationalize-construct`, `specify-boundaries`, `specify-relationship`, `analyze-intervention`, `atomize-claim`, `atomize-concept`, `attach-evidence-to-relation`, `audit-structure-consistency`, `detect-feedback-loop`, `document-counterclaim`, `extract-concepts`。

A/B/C 判据数：A=0，B=11，C=0。provenance：resolved=11，concept=0，intermediate=0。

四条机械门自检：① Procedure 与 Quality gates 均为节点特定表述；② required 无 `source_state`/`task_object`/`input_object`；③ delta_fields 均为 produces 对应子集；④ concept/intermediate 为 0。通过。
## [R5 → Sirelia] BASIS 扇出第二批（10/52）2026-09-12

本批 id：`construct-critique`、`define-analysis-dimensions`、`detect-contradiction`、`extract-causal-structure`、`identify-load-bearing-factors`、`inventory-reference-items`、`map-dependencies`、`map-disagreement`、`set-threshold`、`validate-causal-link`。A/B/C、resolved/concept/intermediate 计数已写入 `deliverables/R5/nodes/_compilation-log.md`。

四条门自检：Procedure 去重通过；Quality gates 去重通过；Input contract 均为具名科研对象；`delta_fields` 均为 `produces` 对应子集；provenance 已按 normalized `old[]` 检索，未解析项明确标为 `concept`/`intermediate`。校验器已对 BASIS 节点运行并通过，pilot 591/591 保持通过。
## [R5 → Sirelia] BASIS 扇出第三批（10/52）2026-09-12

本批按 fan-in=2 顺序交付：`adjust-abstraction-scope`, `aggregate-ranking`, `analyze-scaling-regime`, `assess-goal-feasibility`, `challenge-assumption`, `check-dominance`, `construct-counterfactual`, `construct-hierarchy`, `construct-scenario`, `define-criteria`。

| id | A | B | C | resolved | concept | intermediate |
|---|---:|---:|---:|---:|---:|---:|
| adjust-abstraction-scope | 0 | 2 | 0 | 4 | 0 | 2 |
| aggregate-ranking | 0 | 5 | 0 | 2 | 0 | 0 |
| analyze-scaling-regime | 0 | 1 | 0 | 1 | 1 | 0 |
| assess-goal-feasibility | 0 | 0 | 0 | 1 | 0 | 0 |
| challenge-assumption | 0 | 1 | 0 | 2 | 1 | 0 |
| check-dominance | 0 | 2 | 0 | 1 | 0 | 0 |
| construct-counterfactual | 0 | 0 | 0 | 1 | 0 | 0 |
| construct-hierarchy | 0 | 3 | 0 | 1 | 0 | 1 |
| construct-scenario | 0 | 3 | 0 | 4 | 0 | 0 |
| define-criteria | 0 | 4 | 0 | 1 | 1 | 1 |

交付路径：`deliverables/R5/nodes/<id>/body.md`；合并日志已写入 `deliverables/R5/nodes/_compilation-log.md`。

四条机械门：Procedure 去重通过；Quality gates 去重通过；Input contract `required` 均为具名科研对象；`delta_fields` 均为 `produces` 子集；provenance 已按三种规范形式检索后标注。校验器退出码 0，pilot 源判据 591/591；本批 BASIS provenance-labels 全部无 missing。相对量字段对本批均 not-applicable。
