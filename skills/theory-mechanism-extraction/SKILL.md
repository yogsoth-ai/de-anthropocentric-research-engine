---
name: theory-mechanism-extraction
description: 'Tactic: 演绎路径核心——从理论出发提取机制、变量与关系，生成假设候选'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- theory-identification
- mechanism-extraction
- variable-identification
- relationship-specification
dependencies:
  sops:
  - hypothesis-formation-variable-identification
  - mechanism-extraction
  - relationship-specification
  - theory-identification
---

# Theory Mechanism Extraction

演绎路径核心——从已有理论出发，系统提取机制、识别变量、规范关系，为演绎假设生成提供结构化基础。

## 编排意图

演绎推理的起点是理论，而非数据。本 tactic 强制 CC 先识别领域内相关理论，再逐层拆解：理论 → 机制 → 变量 → 变量间关系。每一层都是下一层的前提，不允许跳步。

最终产出不是假设本身，而是假设的"原材料"——每个机制至少对应一个假设候选（含变量和方向），供上游 strategy 进一步 formalize。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| theory-identification | 识别与 gap/insight 相关的已有理论（含理论名称、核心主张、适用范围） | 所有模式必选，首先执行 |
| mechanism-extraction | 从每个理论中提取可操作的因果机制（mechanism = 连接原因与结果的过程） | 所有模式必选，在 theory-identification 之后 |
| variable-identification | 从每个机制中识别自变量、因变量、调节变量、控制变量 | 所有模式必选，在 mechanism-extraction 之后 |
| relationship-specification | 规范变量间的方向性关系（正/负/非线性/调节/中介），生成假设候选 | 所有模式必选，最后执行 |

## 编排模式

**Simplified（S tier，1 个理论）**
- 顺序执行：theory-identification → mechanism-extraction → variable-identification → relationship-specification
- 覆盖：1 个理论，≥1 个机制，≥1 个假设候选
- 适用：gap 背景清晰，理论支撑单一

**Standard（M tier，2-3 个理论）**
- 顺序执行全部 4 个 SOP，对每个识别出的理论重复 mechanism-extraction + variable-identification + relationship-specification
- 覆盖：≥2 个理论，≥3 个机制，每个机制 ≥1 个假设候选
- 适用：gap 跨越多个理论框架，需要比较演绎路径

**Deep（L tier，≥3 个理论）**
- 执行全部 4 个 SOP；mechanism-extraction 对每个理论独立执行；relationship-specification 额外输出跨理论的变量重叠分析
- 覆盖：≥3 个理论，≥5 个机制，跨理论变量映射，≥5 个假设候选
- 适用：领域理论丰富，需要系统性演绎覆盖

## Minimum Yield

- ≥2 个理论已被识别并描述（含核心主张和适用范围）
- ≥3 个机制已从理论中提取（每个机制含因果链描述）
- 每个机制至少对应 1 个假设候选，含：
  - 自变量和因变量（已命名）
  - 关系方向（正/负/非线性）
  - 来源机制（可追溯到哪个理论的哪个机制）

## Yield Report

执行结束后向调用方 strategy 报告：
- 识别理论数 / 提取机制数 / 生成假设候选数
- 理论覆盖范围（哪些理论被纳入，哪些被排除及原因）
- 变量重叠情况（多个机制共享的变量，可能是关键调节变量）
- 假设候选质量评估：哪些候选变量可操作性强，哪些需要进一步 operationalization
