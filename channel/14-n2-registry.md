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
## 本轮校正（2026-09-12）

按 build-gate-01 裁定，仅修正校验器误报，不放宽门禁：provenance 归一化循环剥离 `(...)` 与 `[...]` 后缀，并尝试裸名、`package-name`、`package/name`；`generic-space` 保留 `generic-space-extraction` 别名。`graph.json` 新增逐条 `provenance_status`，三条实际存在的旧名标为 `resolved`，`conceptual-blending [strategy]` 与 `Pass3/merge-near-duplicate-concepts` 标为 `intermediate`。`--skip-threshold` 仅作低负载诊断；默认全量校验已调用 R5，当前 R5 仍报 `full-node-coverage=266/267`、缺 `structured-consensus`，退出码为 1。
## 2026-09-12 接线修正

`validate_graph.py` 已完成两处修正：R5 原文件保持不变，在临时目录映射 v4 的 tactic/SOP 正文，使 full-node coverage 覆盖 v4 的 267 个节点，同时保留 R5 自有 v3 `SKILLS` 与 591 条台账口径；`delta_fields` 遇到 `assumptions_updates` 时专门报错并提示 `assumption_updates`。

验证：`python -m py_compile v4/scripts/validate_graph.py` 通过；`python v4/scripts/validate_graph.py` 退出 0。
## 2026-09-12 通过标准回退

按 build-gate-02 裁定，R5 门重新以其退出码为唯一判据。`full-node-coverage=267/267` 仅证明映射覆盖完整，不再替代 R5 退出码。当前临时映射下 R5 返回 0，默认全量校验返回 0。
## 2026-09-12 第 13 项门

`validate_graph.py` 新增 v4 正文编码门：逐行拒绝 CJK 区字符、替换字符 `�` 与 UTF-8 BOM，错误包含文件和行号。定向检查 `--skip-threshold` 退出 0，当前 267 份正文零误报、零 BOM。
## 2026-09-12 第 14 项门

已与正文批量替换同批完成：267 份 `SKILL.md` 中的非 ASCII 数学/排版符号已改为 ASCII 等价物；校验器新增专门门禁，发现 `≥ ≤ ≠ ≈ ± × → ← — – “ ” ‘ ’ • …` 时按文件和行号报错，并唯一推荐 ASCII 等价物。frontmatter 不纳入正文符号门，BOM/CJK/替换字符门保持有效。

本轮偏离原建议的 inline math 形式，改用 ASCII 等价物，理由是与现有正文 179 处保持一致且同样不可坏。

验证：`python v4/scripts/validate_graph.py --skip-threshold` 与默认全量均退出 0。
## 2026-09-13 Gate 15: mode consistency

`validate_graph.py` now compares each body's `## Mode branches` names with the same node's registry `modes` field. Missing sections, extra declarations, spelling drift, and duplicate declarations are errors with file and line. Nodes without registry modes must not declare `Mode branches`.

The initial full run failed on five known R4 discrepancies: four nodes missing the body section and `synthesize-meta-analytic-evidence` declaring modes absent from graph. The latter is resolved below by the explicit desc-based registry adjudication; four body discrepancies remain with N1.

This is an additive gate only. No registry value, body, or pass criterion was relaxed.

## 2026-09-13 Gate 15 correction and desc-mode adjudication

The CLI boundary now normalizes the validator status: only an explicit zero from `main()` exits 0; a non-zero or missing status exits 1. This closes the reported path where five mode errors were printed while the caller observed `EXIT=0`.

Negative checks:

- the current `--skip-threshold` run reports the four remaining body-side mode errors and exits 1;
- a synthetic `Checker` containing one error exits 1;
- an empty `Checker` exits 0.

`synthesize-meta-analytic-evidence` now has the five modes `pairwise`, `network`, `cumulative`, `heterogeneity`, and `bias` in `v4/registry/graph.json`. The architecture description explicitly declares these modes while its `modes` field is absent; this is an architecture-internal contradiction resolved in favor of the stronger explicit description, not an inference or gate relaxation. The node records `modes_provenance.source=architecture.desc` and the reason. `v4/scripts/build_registry.py` carries the same narrow override so regeneration preserves the adjudication. The body is unchanged.

## 2026-09-13 R4 provenance-backed mode additions

R4's completed `channel/deliverables/R4/mode-consistency-audit.md` resolves three further empty graph mode fields against v3 source nodes. Added to both `v4/registry/graph.json` and the narrow `DESC_MODE_OVERRIDES` in `v4/scripts/build_registry.py`:

- `sensitivity-analysis`: `Morris`, `Sobol`, `perturbation`, `Monte-Carlo`.
- `synthesize-literature-evidence`: `scoping`, `systematic`, `deep`, `narrative`, `snowball`.
- `design-experiment`: `factorial`, `ablation`, `comparison`, `scaling`, `robustness`.

Each node records `modes_provenance.source=architecture.desc`, with `v3_sources` carrying the R4-resolved source node and line evidence. These additions follow the architecture description only where R4 supplied matching v3 provenance; no body text was changed and no gate was relaxed. The four pre-existing body-side Gate 15 errors remain N1's repair scope.

## 2026-09-13 Mode contract parser and Gate 17

`validate_graph.py` now implements R1's locked B-route contract syntax and R6's host read model. For the 22 mode-bearing nodes, both contract sections must contain one `mode_contracts` mapping; the parser expands YAML anchors/aliases, preserves registry spelling and order, requires every registry mode exactly once, validates the exact per-mode keys and inline-list value types, rejects legacy node-level keys, and checks every per-mode `delta_fields` list against the fixed eight names. The 245 nodes without modes retain the flat `required`/`optional`/`constraints` and `produces`/`delta_fields` syntax, now parsed through the same strict section boundary.

Gate 17 compares `## Mode branches` only with `## Output contract`'s `mode_contracts` keys. A branch without a produces contract reports at the branch line; a contract without a branch reports at the contract line. Gate 15 remains unchanged and separately compares body mode names with `registry/graph.json`.

The parser uses a standard-library implementation of the locked YAML subset, including anchor expansion; no dependency was added. An in-memory positive check covered flat contracts and anchor/alias expansion, and a missing-mode negative check produced a line-addressed error. The current `--skip-threshold` run exits 1 with 136 expected errors confined to the 22 bodies that N1 has not yet converted: 44 legacy contract-shape errors plus 92 missing Output `mode_contracts` entries. All 245 mode-free bodies pass the revised contract parser. No existing gate or pass criterion was relaxed.

## 2026-09-13 Runtime boundary: R6 resolution

Replaced the obsolete `R6 pending` note in `v4/docs/runtime-boundary.md` with the settled Q1-Q3 boundary. The eleven existing host responsibilities remain unchanged: a thin orchestration host owns the control plane, its deterministic in-host reconstruction step rebuilds the in-memory SpecView before routing, and checkpoint persistence remains append-only Markdown rather than JSONL. The note remains host-neutral and does not select providers, tools, retry/backoff/timeout behavior, error classification, or monitoring state machines.

After N1's 22 mode-contract bodies landed, `python v4/scripts/validate_graph.py` completed with exit 0 and zero warnings, including the R5 threshold gate.

## 2026-09-14 R2 provenance resolution and R4 alias adjudication

Applied R2's `regression-audit-267.md` ledger to `v4/registry/graph.json`. All 73 exact-match audit rows are represented as `resolved` and carry their exact v3 `nodes[].name` in `provenance_sources`; repeated v4 body nodes account for 59 unique graph source records. The 39 no-match rows remain `concept` or `intermediate`, with no near-name substitution.

R2's body-side ledger remains separate from R4's old-alias ledger. Added only R4's four adjudicated aliases (`anti-benchmark`, `seed-concept-search`, `synectics`, and `web-search`) to `provenance_aliases`; the other 69 remain unassigned because v3 existence does not establish a unique v4 destination. The same narrow R2 source map and R4 four-alias list are encoded in `v4/scripts/build_registry.py` so regeneration cannot discard them.

Counts remain 267 nodes, 317 calls, 157 jumps, 474 total edges, and 146 capability contracts. `python v4/scripts/validate_graph.py` completed with exit 0 and zero warnings, including the R5 threshold gate. No validator gate was changed or relaxed.

## 2026-09-14 Capability contract split

Applied the approved split of the former `knowledge compilation / vault maintenance` capability. `knowledge compilation` is now a `FULLY_COVERED` STRUCTURING contract mapped to `build-domain-ontology / construct-causal-model / construct-argument-map`; it remains a scientific structure transformation in the research graph. `vault maintenance` is now a `MOVED_ARTIFACT` contract mapped to `product/storage layer`; it covers storage read/write adaptation only and does not assign research semantics to the host.

The split increases `capabilities.json` from 146 to 147 contracts. The separate `critical-path duration / buffering / dispatch / monitoring` contract remains unchanged as `MOVED_RUNTIME`; no host implementation decision was added. Graph counts are unchanged: 267 nodes, 317 calls, 157 jumps, and 474 edges. `python v4/scripts/validate_graph.py` exits 0 with zero warnings, including the full R5 threshold gate.

## 2026-09-14 Gate 16 harness-decoupling coverage fix

The reported leak had a broader root cause than either proposed branch: the current validator contained no Gate 16 scan, so both lowercase and uppercase harness language passed everywhere. Gate 16 now scans every line of every `v4/skills/*/SKILL.md`, including `## Preserved source criteria ledger`, and matches `subagent`/`subagents` plus `Pause and report partial` case-insensitively. Each match is an error with its file and line number; multiple forbidden phrases on one line produce one error.

No body or existing gate was changed. The expected validation result is six errors at `analyze-constraints-readiness/SKILL.md:140,145,153,158,162,166` and exit 1 pending R5's classification and N1's body repair.

## 2026-09-14 Gate 16 token-budget coverage

Gate 16 now also rejects `context tokens`, `token budget`, `spawn fresh`, `summarize and spawn`, and token-scale limits matching `<=NNk`, case-insensitively. The scan remains line-based over the complete body, so escaped ledger separators such as `\\|` do not affect detection.
