# Host 未定落地清单

用途：供 N2 编写 `v4/docs/runtime-boundary.md`。下表只标出 host 形态尚未裁定时不能冻结的条目，不替 R6 回答 Q1–Q6。

| runtime-boundary 条目 | host 未定时无法冻结的部分 | 依赖问题 |
|---|---|---|
| §1.2 第 1 条：动作前从 checkpoint 重建 SpecView 并定位 Phase context | 重建器由谁执行、事件流解析载体、缺失时的停止/报告接口 | Q1、Q2、Q3 |
| §2.1：按 checkpoint 序号回放并识别 plan 事件 | 回放实现属于脚本、harness 还是服务；事件物理格式与确定性保证 | Q1、Q2、Q3 |
| §2.3：每次路由前重建 SpecView，选首个可执行 active_item | 路由调用者、选择结果如何交给执行器、调用顺序是否由 tactic 协议还是 host 编排 | Q1、Q2、Q5 |
| §2.4：重建 SpecView 后读取 context_requirements 指向的 context | context 读取 API/载体、按 slice 取数的边界和失败返回 | Q1、Q3、Q4 |
| §3.3：每个 Delta 作为事件追加并合并 | 持久化适配器、追加原子性、合并逻辑落在 host 还是运行时组件 | Q1、Q3 |
| §3.4：不猜测、不丢弃任何事件，冲突写 uncertainty 并暂停路径 | 事件接收与持久化责任、冲突暂停如何反馈给调用方 | Q1、Q3 |
| §4：session recovery 四步固定入口 | recovery 入口由谁触发、读取/回放工具、partial/complete 状态如何暴露 | Q1、Q2、Q3 |
| §5.0：首次路由前对 ResearchContext 做 preflight，并返回 catalog 卡片 | preflight 执行位置、catalog 发现接口和卡片生成链路 | Q1、Q4 |
| §5.1：路由优先级为 SpecView → recommended_jumps → catalog | 三层决策的实际编排者、catalog 结果如何映射为节点调用 | Q1、Q4、Q5 |
| §5.2：每次调用只加载当前投影所需上下文 | 上下文切片由 host、harness 或节点执行器实施；缓存/传递边界 | Q1、Q3、Q4 |
| §5.3：host 决定是否派发 subagent，代理只回传 Delta | host 是否具备派发能力、代理调用协议、结果回收与 checkpoint 归属 | Q1、Q6 |

说明：Q1 是全局前置依赖；Q2 影响 SpecView/recovery 的执行归属；Q3 影响事件流与持久化载体；Q4 影响 catalog/context 投影；Q5 影响 routing 顺序；Q6 影响最小闭环与 dispatch 验证。未列入表内的科研节点 contract 不因本清单改变。
