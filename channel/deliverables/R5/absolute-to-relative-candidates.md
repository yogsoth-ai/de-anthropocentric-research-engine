# Absolute-to-relative candidates

依据 R2 `thinned-triage.md` 的 A/B/C 分级与 7 个 pilot body 台账。此文件只提出候选，不改正文；A 类待后续落正文与扩展校验器，B/C 保持现状。

## 判定规则

- **A：可相对化**：数字代表检索/采样/资源规模或信息增益门槛，随任务规模变化；改为相对覆盖率、边际信息增益、独立来源比例、候选池比例或饱和判据。
- **B：固定保留**：数字是机械可验的输出形态、方法组合、统计设计或结构完整性约束；本轮不改。
- **C：删除**：R2 已确认属于历史存储实现的门槛；不回填 v4 body。

## 591 条命中台账的逐条归类

下表按台账中的 591 条源命中汇总。每行给出 pilot、命中类别、处理结论及理由；同一命中若同时触发多个模式，以业务语义优先，避免把表格中的普通数字误判为科学阈值。

| pilot | 台账命中类别/范围 | A 可相对化 | B 固定保留 | C 删除 | 理由与候选相对量 |
|---|---|---:|---:|---:|---|
| synthesize-meta-analytic-evidence | 研究/效应量/网页/质量评估数量；HARD-GATE 的 80% floor；NMA 的 `N>=3` 方法节点 | 主要数量门槛；80% floor | `N>=3` 方法节点；效应量定义、RoB 工具与敏感性分析次数 | 无 | 数量改为相对独立研究覆盖率、效应量覆盖率、来源多样性与边际信息增益；统计方法和最低方法数保持结构性约束。 |
| design-experiment | GPU-hours、因素数、运行数、ablation/scaling/robustness 规模表 | 资源与运行规模；部分规模梯度 | 显著性阈值、预注册、power、stopping rule、same compute/tuning、随机种子/环境/验证协议 | 无 | 资源改为资源包络占用率、相对候选因素覆盖率、每因素/每条件重复覆盖率；`p<0.05` 类显著性不可改成相对量。`factor-level-design` 缺失，不推断。 |
| formulate-hypotheses | 理论/机制/假设/解释/预测数量；“at least”覆盖要求 | 候选覆盖与解释空间规模 | 每机制至少一个候选、竞争机制差异、可证伪性、预测映射 | 无 | 改为机制覆盖率、竞争解释覆盖率、每机制候选覆盖率与预测区分度；保留“每机制至少一个”这一结构完整性要求。 |
| analyze-constraints-readiness | 维度、证据项、约束、UDE、注入、子代理/迭代/输出 token 资源表；80% floor | 资源与证据规模；部分“top-N”优先级 | BECAUSE 链、可测试/可控注入、约束类型、stage-gate 结构 | 无 | 改为维度覆盖率、证据独立性比例、约束图覆盖率、候选注入相对副作用；保留因果链与可测试性，不把结构条件稀释为比例。 |
| rank-candidates | 候选池 S/M/L、维度、参考数、top-N、保留率、±20/±30% 敏感性、方法数 | 候选池规模、保留率、参考覆盖、敏感性扰动幅度 | 评分方向、veto/threshold 语义、至少两种方法（当方法比较被要求）、稳定性分类 | 无 | 候选池改为候选覆盖率，top-N 改为决策资源允许的前段比例，参考数改为每候选独立证据覆盖率；权重敏感性仍需扰动，但幅度待 set-threshold 给理由。 |
| establish-empirical-baseline | 方法、数据点、网页、年份、分数对、条件维度；80% floor | 数据/方法/来源覆盖与可比记录比例 | 单位/条件规范化字段、比较方向、provenance、headroom 计算结构 | 无 | 改为方法空间覆盖率、可比记录比例、条件向量完整率、独立来源率；时间跨度只有在研究问题要求历史趋势时才保留为相对时间覆盖。 |
| audit-benchmark-validity | benchmark/paper/web 数量、BetterBench 46 criterion、80% floor、10–15 paper | 资源采样与目标覆盖；80% floor | 构念/污染/指标/协议审计字段；46 项 checklist 作为内容覆盖清单 | 无 | 改为 benchmark 类型覆盖率、证据来源独立性、协议元素覆盖率、目标面覆盖率；46 项是内容清单，不改成“46%”。 |

## 固定值与统计阈值边界

必须固定或按统计设计解释的绝对值：显著性水平（如 `p<0.05`，若源文有）；置信区间/效应量定义；预注册、power 与 stopping rule；相同 compute/tuning 的公平比较条件；方法组合的最小结构要求（如 NMA 至少 3 个方法节点、每机制至少一个候选）；以及评分方向、veto、缺失值政策等语义约束。它们不是“读得够不够”的代理量，不能仅凭规模换算。

## A 类统一候选模板（待 R2 后续落点确认）

```yaml
relative_gate:
  denominator: task-declared eligible universe or current evidence pool
  measure: coverage_ratio | independent_source_ratio | marginal_information_gain | saturation_state
  stop: marginal_gain <= declared floor for consecutive batches, with rationale
  audit_fields: numerator, denominator, batch_delta, rationale, source_refs
```

相对量仍须可客观复核：记录分子、分母、批次增量、停止理由和来源引用。具体分母由对应 tactic/SOP 在 R2 A 类落点时声明，不在本文件擅自设定。

## 待办边界

- 本轮未修改 7 个 body 或校验器。
- R2 A 类正式落正文后，再把相对量模式加入 `validate_threshold_fidelity.py`。
- B 类机械核验项与 C11 历史存储删除结论保持不动。
