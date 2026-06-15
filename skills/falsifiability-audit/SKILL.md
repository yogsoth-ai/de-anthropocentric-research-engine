---
name: falsifiability-audit
description: 'Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- falsifiability-check
- operationalization
- boundary-condition-specification
dependencies:
  sops:
  - boundary-condition-specification
  - falsifiability-check
  - operationalization
---

# Falsifiability Audit

假设质量保证——对假设集逐一检验可证伪性，修复不合格假设，完成操作化定义，并规范边界条件，确保每个假设可被实验或观察所测试。

## 编排意图

假设形成的最终关卡。再好的理论基础，如果产出的假设无法被证伪，就不是科学假设。本 tactic 的职责是"质检"而非"生成"：输入是已有假设候选，输出是每个假设通过质检的证明文件。

三个 SOP 形成流水线：falsifiability-check 识别问题 → operationalization 将变量转化为可测量形式 → boundary-condition-specification 限定假设成立的范围。不允许跳步，也不允许在 falsifiability-check 失败时直接推进。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| falsifiability-check | 对每个假设执行可证伪性检验，识别不可证伪的假设并提出修复建议 | 所有模式必选，首先执行；如有假设未通过，迭代修复后重新检验 |
| operationalization | 为每个假设的变量提供操作定义——如何测量、用什么工具、在什么条件下 | 所有模式必选，在 falsifiability-check 通过后执行 |
| boundary-condition-specification | 规范假设成立的前提条件、适用范围和已知限制 | 所有模式必选，最后执行 |

## 编排模式

**Simplified（S tier，≤3 个假设）**
- 顺序执行：falsifiability-check → operationalization → boundary-condition-specification
- 如有假设未通过 falsifiability-check，CC 立即修复并重新检验（最多 2 轮迭代）
- 适用：假设数量少，预期质量较高

**Standard（M tier，4-6 个假设）**
- falsifiability-check 对所有假设批量执行，汇总失败列表；CC 批量修复；重新检验修复后的假设
- operationalization 和 boundary-condition-specification 串行执行
- 适用：中等规模假设集，需要系统质检

**Deep（L tier，≥7 个假设）**
- 全部 3 个 SOP 执行；falsifiability-check 额外输出：每个假设的"最强反例场景"；operationalization 额外要求：为每个变量提供 ≥2 种测量方法（主方法 + 备选）；boundary-condition-specification 额外要求：列出已知的例外情况
- 适用：大规模假设集，需要生产级质量保证

## Minimum Yield

- 每个输入假设均已通过 falsifiability-check（或已修复至通过）
- 每个假设的所有变量均有操作定义（含测量工具/方法）
- 每个假设均有明确的边界条件（假设成立的前提 + 不适用的情境）
- 完整的质检记录：哪些假设初次通过，哪些修复后通过，修复内容是什么

## Yield Report

执行结束后向调用方 strategy 报告：
- 输入假设数 / 初次通过数 / 修复后通过数 / 最终未通过数
- 最常见的可证伪性问题类型（供 upstream strategy 改进假设生成）
- 操作化难度：哪些变量难以测量（需要特殊工具或数据集）
- 边界条件覆盖：哪些假设的适用范围较窄（高风险，易被反例推翻）
