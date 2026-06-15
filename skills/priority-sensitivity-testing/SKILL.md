---
name: priority-sensitivity-testing
description: 'Tactic: 扰动评分权重，检验 gap 排序对权重选择的稳健性'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: gap-prioritization
sops:
- ahp-weighting
- weight-perturbation
- priority-synthesis
dependencies:
  sops:
  - ahp-weighting
  - priority-synthesis
  - weight-perturbation
---

# Priority Sensitivity Testing

对已有的 gap 评分矩阵施加权重扰动，检验最终排序是否对权重选择敏感，从而判断优先级决策的可信度。

## 编排意图

评分矩阵的最终排序依赖于各维度的权重设置。若权重稍有变化排序就大幅改变，则决策不可靠；若排序在合理权重范围内保持稳定，则优先级结论更有说服力。

本 tactic 先建立基线权重（AHP 或等权重），再系统性地扰动权重（±20%），观察排序变化，最终给出稳定性判定。

## 可用 SOPs

| SOP | 职责 | 何时调用 |
|-----|------|---------|
| ahp-weighting | 使用 AHP 方法从维度重要性判断中推导权重向量 | 第一步，建立基线权重 |
| weight-perturbation | 对每个维度权重施加 ±20% 扰动，重新计算排序 | 第二步，系统性扰动 |
| priority-synthesis | 汇总所有扰动场景的排序结果，合成稳定性报告 | 第三步，合成结论 |

## 编排模式

**Default（标准流程）**
1. ahp-weighting：从用户/策略提供的维度重要性判断推导基线权重；若无判断则使用等权重
2. weight-perturbation：对每个维度依次施加 +20% 和 -20% 扰动（其余维度等比例调整保持总和为 1），产出每个扰动场景的排序
3. priority-synthesis：统计每个 gap 在所有扰动场景中的排名分布，输出稳定性判定

**Simplified（S tier 或快速模式）**
- 跳过 ahp-weighting，直接使用等权重作为基线
- 仅扰动最高权重维度（±20%），产出 2 个扰动场景
- priority-synthesis 给出简化稳定性报告

**Deep（L tier 或高风险决策）**
- ahp-weighting 使用完整 AHP 成对比较（维度间两两比较）
- weight-perturbation 扰动幅度扩展至 ±30%，并增加极端场景（某维度权重设为 0）
- priority-synthesis 额外输出 Spearman 秩相关系数（基线排序 vs 每个扰动排序）

## Minimum Yield

- 基线权重向量（所有维度权重之和 = 1）
- 至少 3 个扰动场景的排序结果（每个场景标注扰动内容）
- 每个 gap 的排名稳定性统计（最高排名、最低排名、众数排名）
- 最终稳定性判定：**Stable**（所有场景前 N 名不变）/ **Partially Sensitive**（前 N 名有 1-2 个变化）/ **Highly Sensitive**（前 N 名变化超过 2 个）

## Yield Report

执行结束后向调用方 strategy 报告：
- 基线权重来源（AHP 推导 / 等权重 / 用户指定）
- 扰动场景数量
- 稳定性判定结论
- 最不稳定的 gap（排名波动最大）及建议（是否需要补充证据再决策）
