---
name: deductive-hypothesis-generation
description: 'Strategy: 从现有理论演绎推导假设'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- theory-mechanism-extraction
- falsifiability-audit
sops:
- theory-identification
- mechanism-extraction
- variable-identification
- relationship-specification
- boundary-condition-specification
- falsifiability-check
- operationalization
dependencies:
  tactics:
  - falsifiability-audit
  - theory-mechanism-extraction
---

# Deductive Hypothesis Generation

从现有理论演绎推导假设：在理论成熟领域，通过显式推理链将理论命题转化为具体的可测试预测。

## 适用场景

- 领域拥有成熟的基础理论（有 named theories、正式模型、或公认机制）
- 研究 gap 表现为"理论预测与现实观察之间的偏差"
- 目标是检验、扩展或限定已有理论的适用范围
- 需要高度可辩护的假设（审稿人会追问理论依据）

不适用：数据丰富但理论空白的新兴领域 → 改用 inductive-hypothesis-generation。

## 思维框架

**Theory → Mechanism → Variable Relationship → Testable Prediction**

演绎的核心逻辑：

1. **Theory**：识别支撑研究问题的基础理论（命名理论、正式模型）
2. **Mechanism**：从理论中提取因果机制（"X 通过 Z 影响 Y"的中间过程）
3. **Variable Relationship**：将机制转化为变量间的方向性关系（正向/负向/调节/中介）
4. **Testable Prediction**：将变量关系具体化为在特定条件下的可观测预测

每一步都必须可追溯：每个 prediction 能回溯到机制，每个机制能回溯到理论。这是演绎假设区别于猜测的核心。

**常见陷阱**：
- 理论引用流于表面（只提名字，不提具体命题）→ 必须引用理论的核心命题
- 跳过机制直接从理论跳到预测 → 机制是演绎链的关键节点，不可省略
- 假设范围过广（"在所有情境下"）→ 演绎必须说明边界条件

## Budget Gate

| Tier | 理论覆盖 | 机制提取 | 假设产出 | 可证伪性 |
|------|---------|---------|---------|---------|
| S | ≥2 个具名理论 | ≥3 个因果机制 | ≥2 个结构化假设 | 每个假设 1 个 falsification scenario |
| M | ≥3 个具名理论 | ≥5 个因果机制 | ≥3 个结构化假设 | 每个假设 ≥1 scenario + boundary conditions |
| L | ≥5 个具名理论 | ≥8 个因果机制 | ≥5 个结构化假设 | 完整 falsifiability audit + 竞争理论比较 |

## 默认参考流

1. 调用 `theory-identification` SOP：扫描领域文献，列出与 gap 相关的具名理论及其核心命题
2. 调用 `mechanism-extraction` SOP（via `theory-mechanism-extraction` tactic）：从每个理论中提取因果机制链
3. 调用 `variable-identification` SOP：将机制中的构念（constructs）转化为可操作变量
4. 调用 `relationship-specification` SOP：明确变量间方向性关系（含调节/中介结构）
5. 调用 `boundary-condition-specification` SOP：识别理论适用的前提条件（群体、情境、时间范围等）
6. 调用 `falsifiability-check` SOP（via `falsifiability-audit` tactic）：为每个假设生成 falsification scenario
7. 调用 `operationalization` SOP：为关键变量提供测量方法草案

## context-checkpoint

每轮结束后记录：
- 已识别理论清单（名称、核心命题、来源）
- 提取的机制列表（每条机制标注来源理论）
- 当前假设草稿集（含变量关系 + 边界条件）
- 可证伪性状态（已通过 / 待审查 / 不可证伪需修改）
