# 20 — v4 内测：16 课题

## [R0 → Pthahnix] 2026-09-20

账七全闭，v4 具备可跑条件。本帖是内测方案，等主人给宏观方向后开跑。

## 一 前置状态（R0 独立复核，不采信自检）

```
validator          EXIT=0，0 warning
边覆盖             317 call + 82 tactic jump + 75 sop jump = 474/474，差集空
边界               graph.json 267 节点；v4/skills/ 271 目录（4 个产品外壳）
入口链             dare-v4 → {catalog, write-spec, execute-spec} 硬调
                   catalog 索引 51/51 tactic
                   execute-research-spec 硬拉选中 tactic
                   rank-candidates 硬调 11 个 SOP
                   score-object(SOP) 出 call 0 —— SOP 是 call 叶子，正确
负测               假目录 / 外壳混入图 / 删真 tactic 目录，三项各 EXIT=1
```

## 二 内测形状

```
[主人]  宏观理念与方向
   │
[R0]   拆成 16 个课题 + 逐个转成 research prompt
   │
A1 … A16   各自起 DARE：dare-v4 → 北极星 → spec
   │
[主人]  人工审 16 份 spec / 北极星   过 → 启动；不过 → R0 重拆
   │
[R0]   正式执行期间全程对接 16 个 agent，需求上报主人
```

## 三 DIY 梯度（R0 拟，四档各 4 个）

内测要同时验「给死」和「放养」两端，否则测不出图的自主性。

| 档 | 我给 agent 的东西 | 验什么 |
|---|---|---|
| D1 全指定 | 北极星 + spec 骨架 + 指定起始 tactic | 契约与阈值是否可执行 |
| D2 半指定 | 北极星 + 方向，spec 自己写 | write-research-spec 是否可用 |
| D3 仅方向 | 一句话方向，北极星自己结晶 | dare-v4 强制顺序是否被遵守 |
| D4 放养 | 一个粗糙兴趣，全自主 | catalog 选 tactic 是否选得对 |

D1 测执行层，D4 测编排层。中间两档测衔接。

## 四 每个 agent 的启动 prompt 骨架

```
读 <skill-root>/dare-v4/SKILL.md，按它的强制顺序执行。
不许直接从平铺目录挑 tactic。

课题：<R0 转译后的具体研究问题>
已有输入：<按 DIY 档提供，D4 档此处只有一句兴趣>
约束：<资源、时间、范围>

先做到 spec（或北极星）为止，停下来等人工审核，不要直接进执行阶段。
```

## 五 我需要主人给的

**只有一样：宏观理念与方向。**

不用具体课题，说领域和你在意什么就够，16 个怎么拆是我的活。
DIY 梯度那张表如果不合，直接改。

## 六 内测要记什么

每个 agent 跑完落一份 `deliverables/internal-test/A<NN>.md`，只记三件：

1. 哪一步卡住 / 哪个 tactic 的 MUST 没被执行
2. catalog 选的 tactic 是否合理，不合理的选了什么
3. 与 v3 比，同一课题下哪里更强、哪里更弱

**第 3 条是内测的真目的** —— 主人的要求是「比 v3 更牛逼」，不是「跑得通」。
