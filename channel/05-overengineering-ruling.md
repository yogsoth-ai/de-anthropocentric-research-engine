# 过度工程 / 防御编程 审计

已审出的过度工程嫌疑点，全量列出：

R1 runtime-boundary.md

1. §5.3 重试退避公式 min(60, 2^(attempt-1)*2) 秒
2. §5.3 重试间隔的 0–1 秒随机抖动
3. §5.3 timeout_seconds 缺省 900 秒这个具体数字
4. §5.3 max_attempts 缺省 3 这个具体数字
5. §5.3 不重试错误的四分类（参数错误/权限认证/契约校验/数据损坏）
6. §5.4 整节并行规则（state slice 不重叠 + 输出写入键不冲突 + Spec 未声明顺序依赖，三条同时满足才可并行）
7. §5.4 并行结果按 step_id 排序再合并
8. §5.4 「任一分支失败不丢弃其他分支，但共同下游保持未完成」
9. §5.6 监控八字段（开始/结束时间、phase、step_id、attempt、状态、预算消耗、输入输出摘要、错误类别）
10. §5.6 五态状态机 queued/running/succeeded/failed/blocked
11. §5.5 派发五条前置条件（边界明确+输入可序列化+无共享可变写入+结果可回传 Delta+预计收益大于开销）
12. §3.2 checkpoint 三态 complete | partial | blocked
13. §3.3 「没有稳定键时按完整规范化文本去重」这条兜底
14. §3.3 拒绝写入的四种情形（序号重复/时间倒退/Phase 不符/Delta 非八字段）
15. §3.4 冲突裁决要求生成带来源引用的 uncertainties 条目并暂停路径
16. §4 五步恢复流程（尤其新补的第 3 步 SpecView.source_checkpoint 一致性核对）
17. §2.1 五种 decisions 事件类型（plan_item.create/update/retire、plan_gate.update、phase_status.update）
18. §2.1 SpecView 八字段输出结构
19. §2.1 active_item 八字段结构
20. §2.1 recommended_combination 这个可选字段本身
21. §2.2 needs_revalidation 状态及其触发条件四分类
22. §2.2 「保留被替换决定及原因」的替换链
23. §2.4 六条节点执行约束
24. §5.1 四级路由优先级链
25. §5.2 「可重建导航文本」的三重判定标准（相同 SpecView + Delta 稳定键集 + 下一路由结果）
26. §1.2 五条强制不变量
27. §6 七条 capability 的逐条验收条件
28. §7 六条实现验收清单

R3 entry-ux-spec.md

29. ResearchContext 七字段投影（四字段 canonical 之上再加三个）
30. 三个错误码 NEEDS_CONTEXT / NEEDS_PHASE_CONTEXT / CONTEXT_CONFLICT
31. NEEDS_CONTEXT {missing, inferred, next_questions} 的返回结构
32. 六条错误入口兜底
33. §5 计划视图四条规则（首次可见/通知边界/如何改/失效呈现）
34. 「主动通知 vs 静默更新」的字段级分界（object 围 主动，描述/排序/注释 静默）
35. 「多项同批变化合并成一次通知」
36. decisions 事件要带 plan_item_id+operation+cher 五字段
37. CapabilitySet[] 九字段（id/user_label/description/when_to_use/requires/produces/confidence/source_ref/next_call）
38. 能力发现的四条触发时机
39. 「3–5 项」这个具体数量约束
40. C 方案 frontmatter 六字段契约表
41. 五个冷启动场景 × 对话轮数上限（2/2/3/1/1 轮）
42. category_source: package + inferred 标记机制

R5 编译规格 / pilot

43. validate_threshold_fidelity.py 的命名模式体系（符号比较/at-least/top-N/百分比/数值范围/表格数字行/五类文本谓词）
44. 校验器盲区章节（数字词/非英文/隐性判据/模糊
45. §10.1 字段处置矩阵
46. §10.2 drop 原因码
47. 「含 threshold/rubric/failure 的单元被删则操作必须失败」这条闸门
48. 每个 body 必含 Input/Output contract + 执行 ance + Delta 说明（六段式）
49. 台账保留物理源行号
50. 压缩比表的「源 threshold 数 / body 保留数」

R4 图修补

51. provenance_aliases 四字段结构（v3_id/v4_id/compression_type/notes）
52. alias 推导的「唯一或最高票至少为次高票两倍」判定规则
53. 73 条「无法推导」单独列出并保留

R2 审计

54. 三档判词体系 COVERED/THINNED/UNCERTAIN
55. 五类对象错配框架（Sequence/Granularity/Input
56. 146 条逐条 × tactic+calls SOP 并集取证

跨岗位 / 架构级

57. 八字段 ResearchStateDelta 本身
58. 三条硬边界划分（scientific_graph / runtime_control_plane / external_capability_layer）
59. 「spec 是投影不是对象」这个机制本身（相对「就写个计划文件」）
60. 每 Phase 恰好一个 context 文件 + INDEX.md 索引这套布局
61. context/INDEX.md 的五列（文件/Phase/Topic/Checkpoint 数/Last Updated）
