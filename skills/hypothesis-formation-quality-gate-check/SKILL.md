---
name: quality-gate-check
description: 'Shared SOP: 通用质量门检查（格式完整性、逻辑一致性）'
version: 1.0.0
category: hypothesis-formation
type: sop
shared: true
campaigns:
- gap-prioritization
- hypothesis-formulation
- research-question
input: 任意产出物（gap 列表 / 假设 / RQ）
output: 通过/不通过 + 问题列表
dependencies:
  skills:
  - subagent-spawning
---

# Quality Gate Check

通用质量门检查 — 验证产出物的格式完整性和逻辑一致性。

## HARD-GATE

<HARD-GATE>
输入必须包含: 至少 1 个需要检查的产出物。
</HARD-GATE>

## Pipeline

1. **前置检查**: 产出物是否非空
2. **格式完整性**: 是否包含所有必要字段
3. **逻辑一致性**: 各部分之间是否矛盾
4. **引用完整性**: 引用的来源是否存在
5. **可操作性**: 产出是否足够具体可执行
6. **综合判定**: PASS / FAIL
7. **输出**: 判定 + 问题列表（如有）

## Check Dimensions

| 维度 | 检查内容 | FAIL 条件 |
|------|---------|----------|
| 格式完整性 | 必要字段是否齐全 | 缺少必要字段 |
| 逻辑一致性 | 各部分是否矛盾 | 存在内部矛盾 |
| 引用完整性 | 引用来源是否可追溯 | 引用无法验证 |
| 可操作性 | 是否足够具体 | 过于抽象无法执行 |
| 无歧义性 | 是否有多种解读 | 关键术语有歧义 |

## Output Format

```
Judgment: PASS / FAIL
Issues found: [数量]
Issue list:
  1. [维度]: [具体问题] — [修正建议]
  2. ...
Severity: CRITICAL / MINOR (per issue)
```
