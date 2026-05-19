---
name: scope-calibration
description: "Strategy: 调整研究问题范围 — zoom in/out 直到范围合适"
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: research-question
tactics:
  - question-refinement-loop
sops:
  - scope-assessment
  - finer-criteria-check
  - success-criteria-definition
dependencies:
  skills:
    - context-management
    - subagent-spawning
---

# Scope Calibration

调整研究问题范围 — 当问题太宽或太窄时，通过系统化的 zoom in/out 找到合适粒度。

## 适用场景

- 初始 RQ 太宽泛（无法在合理时间内回答）
- 初始 RQ 太狭窄（答案 trivial 或缺乏意义）
- 需要在 ambition 和 feasibility 之间找平衡

## 思维框架

核心逻辑: 好的研究问题有"金发姑娘"特征 — 不太宽、不太窄、刚刚好。

### Zoom In（问题太宽时）

添加约束来缩小范围:
- 时间约束: "在过去 5 年内..."
- 地点约束: "在中国高校中..."
- 人群约束: "对于初学者..."
- 方法约束: "使用 transformer 架构..."
- 现象约束: "特别是在 X 场景下..."

### Zoom Out（问题太窄时）

放松约束来扩大范围:
- 提升抽象层级: 从具体实例到一般原则
- 移除不必要的限定词
- 扩展适用范围

### 判断标准

- 太宽: 需要一本书来回答 / 无法设计单一实验
- 合适: 一篇论文可以回答 / 可以设计明确的研究方案
- 太窄: 答案显而易见 / 缺乏理论贡献

## Budget Gate

| Tier | 迭代轮次 | 产出 |
|------|---------|------|
| S | ≥1 轮 scope 调整 | 范围合适的 RQ |
| M | ≥2 轮 scope 调整 + 对比 | 调整前后对比 + 最终 RQ |
| L | ≥3 轮 + 多方向探索 | 多个粒度版本 + 最优选择理由 |

## 默认参考流

1. 对当前 RQ 进行 scope-assessment
2. 根据判定结果（太宽/太窄）选择 zoom 方向
3. 应用约束调整
4. 重新评估 scope
5. 迭代直到"合适"
6. FINER 检验确认

## context-checkpoint

Strategy 完成后必须调用 context-checkpoint，记录:
- 原始 RQ 及其 scope 判定
- 调整方向和具体操作
- 最终 RQ 及其 scope 判定
- 调整理由
