# N2 registry / toolchain 交付回帖

## 任务一：registry/graph.json

产出：`v4/registry/graph.json`

来源：只读 `D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json`

实数核对：267 节点（51 tactic / 216 SOP）、317 calls、157 jumps、474 边。`family`、`scope` 保留为元数据，不构造执行层。所有 216 个 SOP 均被至少一条 calls 边引用。

## 任务二：scripts/validate_graph.py

产出：`v4/scripts/validate_graph.py`

覆盖：ID 对齐、calls/jump 合法性、可达性、Execution protocol 引用、frontmatter 最小字段、模板小节顺序、契约字段、description 一致性，以及四条机械门：Procedure 重复、通用 required 占位符、Procedure 去 SOP id 后同句式不得出现三次以上、concept provenance 三种归一化命中。

R5 接入：默认调用 `channel/deliverables/R5/validate_threshold_fidelity.py`；其独立运行结果为 `OK: 591 matched source criteria present`。可用 `--skip-threshold` 进行低负载的 registry/正文门禁检查。

当前正文问题（校验器发现，未代 N1 修改）：

- `v4/skills/rank-candidates/SKILL.md:1`、`analyze-constraints-readiness/SKILL.md:1`、`formulate-hypotheses/SKILL.md:1`、`audit-benchmark-validity/SKILL.md:1`、`synthesize-meta-analytic-evidence/SKILL.md:1`、`establish-empirical-baseline/SKILL.md:1`、`design-experiment/SKILL.md:1`：模板小节顺序不符。
- `v4/skills/portfolio-optimization/SKILL.md:21`、`build-domain-ontology/SKILL.md:21`、`construct-causal-model/SKILL.md:21`、`construct-argument-map/SKILL.md:21`、`analyze-future-scenarios/SKILL.md:21`：同一 `## Procedure` 去除括号内容后存在三次以上相同句式。
- `v4/registry/graph.json:1`：以下 concept provenance 未在 `scripts/refactory_source.json` 以裸名、package-name 或 package/name 命中：`conceptual-blending [strategy]`、`knowledge-structuring/concept-extraction (core)`、`knowledge-structuring/seed-concept-search (semantic core)`、`Pass3/merge-near-duplicate-concepts`、`conceptual-blending/generic-space [sop]`。

## 任务三：registry/capabilities.json

产出：`v4/registry/capabilities.json`

依据 R2 的 `capability_audit` 原样生成，146/146 条，未重新判定 provenance 或覆盖结论。

## 任务四：docs

产出：`v4/docs/architecture.md`、`v4/docs/runtime-boundary.md`

`runtime-boundary.md` 从 R1 原文复制；11 处 host 必须项保持原样，并在文末标记 `R6 pending`，未替 host 做实现决策。

## 任务五：可视化

产出：`v4/scripts/build_graph_html.py`、`v4/docs/graph.html`

标准库生成静态节点表与筛选器，无新增依赖。读取 `registry/graph.json` 后生成。

## 低负载说明

未使用 git 写操作、npm install、superpowers 或 ara。构建脚本单次读取权威 JSON；校验器默认单进程，正文尚未齐全时可先用 `--skip-threshold`。
