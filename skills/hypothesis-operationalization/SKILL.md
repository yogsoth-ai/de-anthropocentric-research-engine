---
name: hypothesis-operationalization
description: 'Strategy: 将 working hypothesis 精确化为可测试形式'
version: 1.0.0
category: hypothesis-formation
type: strategy
campaign: hypothesis-formulation
tactics:
- falsifiability-audit
sops:
- operationalization
- falsifiability-check
- boundary-condition-specification
- variable-identification
dependencies:
  tactics:
  - falsifiability-audit
  sops:
  - hypothesis-formation-variable-identification
---

# Hypothesis Operationalization

将 working hypothesis 精确化为可测试形式：将模糊的方向性想法或概念性假设转化为每个术语都有操作定义、每个变量都有测量方法的精确可测试命题。

## 适用场景

- 已有方向性假设（"我认为 X 可能影响 Y"），但尚未精确化
- 假设含有抽象构念（construct），需要具体化为可观测指标
- 准备进入研究设计阶段，需要给出可直接操作的假设版本
- 审稿人或合作者反馈"假设太模糊"

不适用：尚未有任何假设方向 → 先用其他三个 strategy 生成假设，再回到本 strategy 精化。

## 思维框架

**Abstract → Concrete**

每个术语获得操作定义，每个变量获得测量方法。

操作化的五个层次：

1. **构念澄清**（Construct clarification）：假设中的每个术语意味着什么？（概念层面）
2. **变量识别**（Variable identification）：哪些是可操作的变量？（分析层面）
3. **操作定义**（Operational definition）：如何测量/操作每个变量？（方法层面）
4. **边界条件**（Boundary conditions）：假设在什么范围内成立？（适用层面）
5. **可证伪标准**（Falsifiability criteria）：什么观察结果会推翻此假设？（判断层面）

**常见的操作化失败模式**：
- 循环定义（用 X 定义 X）→ 操作定义必须引用可观测行为或测量
- 测量与构念不匹配（operationalism gap）→ 需要论证测量工具确实捕捉到构念
- 边界条件过于宽泛（"在所有情境下"）→ 必须具体到样本、情境、时间范围

## Budget Gate

| Tier | 操作化完整性 | 变量测量 | 边界条件 | 可证伪性 |
|------|---------|---------|---------|---------|
| S | 所有抽象术语有操作定义 | 所有变量有测量方法草案 | 主要边界条件明确 | 1 个 falsification scenario |
| M | 同上 + 操作化合理性论证 | 变量测量含信效度考量 | 完整边界条件 | ≥2 个 falsification scenarios |
| L | 同上 + 竞争操作化方案比较 | 主要变量含多操作化方案 | 边界条件 + 外部效度声明 | 完整 falsifiability audit |

## 默认参考流

1. 调用 `variable-identification` SOP：识别假设中所有构念，分类为 IV/DV/调节变量/中介变量
2. 调用 `operationalization` SOP：为每个构念提供操作定义（含测量方法/工具/指标）
3. 调用 `boundary-condition-specification` SOP：明确假设的适用范围（群体、情境、时间、文化）
4. 调用 `falsifiability-check` SOP（via `falsifiability-audit` tactic）：生成 falsification scenarios，确认假设可证伪性

## context-checkpoint

每轮结束后记录：
- 操作化前的假设原始版本
- 每个构念的操作定义（含测量方法）
- 操作化后的精确假设（If [operationalized X], then [operationalized Y]）
- 边界条件清单
- Falsification scenarios
- 操作化质量自评（是否有循环定义、测量-构念匹配度）

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| falsifiability-audit | Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范 |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-variable-identification | SOP: 识别变量及其在假设中的角色 |

<!-- END available-tables (generated) -->
