---
name: framework-selection-and-application
description: 'Tactic: 选择最适合的 RQ 框架并系统应用'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: research-question
sops:
- framework-matching
- pico-application
- spider-application
- spice-application
- eclipse-application
dependencies:
  sops:
  - eclipse-application
  - framework-matching
  - pico-application
  - spice-application
  - spider-application
---

# Framework Selection and Application

选择最适合的 RQ 框架并系统应用 — 从框架匹配到完整填充。

## 编排意图

将"用框架结构化研究问题"分解为：先选框架 → 再应用框架。选择和应用是两个独立步骤，由不同 SOP 负责。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| framework-matching | 根据研究类型匹配最适合的框架 | 第一步，必调 |
| pico-application | 应用 PICO/PICOTS 框架 | 量化/干预研究 |
| spider-application | 应用 SPIDER 框架 | 定性研究 |
| spice-application | 应用 SPICE 框架 | 评估研究 |
| eclipse-application | 应用 ECLIPSE 框架 | 混合方法研究 |

## 编排模式

**标准模式**:
1. framework-matching → 获得推荐框架 + 理由
2. 根据推荐调用对应的 application SOP（pico/spider/spice/eclipse）
3. 检查填充完整性

**对比模式（M/L tier）**:
1. framework-matching → 获得 top 2-3 候选
2. 对每个候选调用对应 application SOP
3. 比较哪个框架产出的 RQ 更精确
4. 选择最优

## Minimum Yield

- ≥2 个候选框架被评估（含选择理由）
- 选定框架的每个组件有明确填充（不留空）
- 填充内容具体（不是泛泛描述）

## Yield Report

执行完成后报告:
- 评估的框架数量
- 选定的框架及理由
- 各组件填充完整度
- 是否有组件因信息不足无法填充
