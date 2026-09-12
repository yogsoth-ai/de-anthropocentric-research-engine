# R2 回归审计：267 份正文

审计对象：architecture JSON 中 51 tactic + 216 SOP。canonical 选择按当前分派优先取 R1/R2/R3/R5，R4 仅取未转派节点；R4 下已转派的 42 个旧副本不重复计入。

## 结论

本轮不能签发全量通过。发现的硬问题：

| 门 | 结果 | 证据 |
|---|---:|---|
| 1. 同组 Procedure/Execution protocol 不得完全相同 | FAIL | 4 组重复：`falsifiability-audit` = `decompose-research-question`；`pairwise-ranking` = `portfolio-optimization`；`build-domain-ontology` = `construct-causal-model`；BASIS 组 7 节点共用同一模板步骤。 |
| 2. required 不得使用占位符 | FAIL | 7 节点：`elicit-weights`、`detect-breakpoint`、`construct-validity-envelope`、`construct-defense`、`adjudicate-exchange`、`enumerate-combinations`、`identify-bottleneck`；均为 `required: [source_state, task_object]`。 |
| 3. delta_fields 子集且与 produces 对应 | FAIL | 上述 7 节点均全量列出八字段，未做节点级选择；其余节点未见非法字段名，但需由 N2 复跑 produces 对应性。 |
| 4. concept 前三种检索 | UNCERTAIN | 112 条 `concept` provenance 在正文/编译记录中未附裸名、`package-name`、`package/name` 三次检索证据。未把“查不到”推断为错误；要求补证据或改为真实 resolved。 |
| 5. 小节内重复句式不得三次以上 | FAIL | 5 节点：`pairwise-ranking`（3 次）、`portfolio-optimization`（3 次）、`build-domain-ontology`（4 次）、`construct-causal-model`（4 次）、`analyze-future-scenarios`（3 次）。重复句：`Transform the current artifact while preserving its provenance and uncertainty.` |

## 覆盖缺口

以下 16 个 architecture 节点没有当前分派目录中的 canonical `body.md`，不能宣称已审：

`structured-consensus`, `generate-subquestions`, `sequence-work`, `verify-evidence-independence`, `derive-consequences`, `generate-provocation`, `identify-obstacles`, `trace-causal-chain`, `design-mitigation`, `evaluate-scenario-impact`, `map-coverage-space`, `normalize-comparison-scale`, `measure-portfolio-diversity`, `construct-perspective-set`, `rotate-perspective`, `evaluate-scenario-robustness`。

## R4 → N1 的 30 节点返工清单

这 30 个仍是 R4 旧正文；按 N1 的职责直接退回重写，不把它们的形式合规当作内容通过。

### 11 tactic

| 节点 | 机械证据 | 判定 |
|---|---|---|
| `analyze-experiment-results` | `Execution protocol` 仅 2 步；仅冻结输入、整合结果，无结果分析分支与可证伪检查 | REWORK |
| `analyze-future-scenarios` | 步骤 2/3 使用同一句通用句；第 57 行起可见重复骨架 | REWORK；G5 |
| `build-domain-ontology` | 步骤 2–5 同一句通用句，出现 4 次 | REWORK；G5 |
| `construct-argument-map` | 步骤均为通用冻结/转换/整合句，未展开 claim/evidence/counterclaim 逻辑 | REWORK |
| `construct-causal-model` | 步骤 2–5 同一句通用句，出现 4 次 | REWORK；G5 |
| `decompose-research-question` | 与 `falsifiability-audit` 的三步 protocol 完全相同 | REWORK；G1 |
| `falsifiability-audit` | 与 `decompose-research-question` 的三步 protocol 完全相同 | REWORK；G1 |
| `formulate-research-question` | 步骤 2/3 为通用转换句，未写 FINER/比较/边界判据 | REWORK |
| `pairwise-ranking` | 步骤 2/3 为同一句通用转换句；与 `portfolio-optimization` protocol 完全相同 | REWORK；G1/G5 |
| `portfolio-optimization` | 步骤 2/3 为同一句通用转换句；与 `pairwise-ranking` protocol 完全相同 | REWORK；G1/G5 |
| `structured-consensus` | R4 canonical 文件缺失 | REWORK；MISSING |

### 19 EXPERIMENT SOP

以下节点的 R4 正文均为 40–41 行的统一三步壳，虽然 required 已改成节点名，仍缺少从 v3 源编译的操作语义；逐节点重写，不得沿用“Validate / Apply operation / Emit result”骨架：

`construct-design-matrix`, `design-randomness-protocol`, `estimate-sample-size`, `extract-core-conflict`, `identify-critical-chain`, `identify-scenario-drivers`, `list-undesirable-effects`, `map-ablation-components`, `optimize-design-under-budget`, `predict-competitive-move`, `project-future-reality`, `quantify-resource-gap`, `select-experimental-baseline`, `select-statistical-method`, `specify-execution-environment`, `specify-metrics`, `specify-reproducibility-protocol`, `statistical-testing`, `verify-reproducibility`。

对 `estimate-sample-size`、`select-statistical-method`、`statistical-testing` 保留固定统计阈值的要求（如 alpha/power）不等于正文已满足；须在 Procedure、Quality gates、Failure 中写出其适用条件、反例与停止理由。

## 给 N1 的最小返工接口

1. 只改上述 30 个 R4 旧壳；不要改 R1/R2/R3 已收口正文。
2. 每个 tactic 的步骤必须体现节点专属的状态变换；每个 EXPERIMENT SOP 必须从 v3 `description/update` 编译出至少一个节点专属判据和一个反例。
3. 返工后重新跑五道门；尤其清除通用句重复和全量八字段 delta。

