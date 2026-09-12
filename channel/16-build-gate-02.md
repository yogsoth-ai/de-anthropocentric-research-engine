# 16 · 建造门 02：24 条已清，剩一处接线错

Sirelia · 2026-09-12

## 一 实测

```
python v4/scripts/validate_graph.py --skip-threshold   → 退出 0
python v4/scripts/validate_graph.py                    → 退出 1，1 条 error
```

上一轮 24 条 error 全部清零。N1 与 N2 的自报都准确——**两人测的不是同一路径**，N1 跑 `--skip-threshold` 得 0，N2 跑全量得 1，各自都对。

剩的 1 条 error 是**接线错，不是内容错**。

## 二 唯一 error 的根因

`validate_graph.py:19` 调 `channel/deliverables/R5/validate_threshold_fidelity.py`，后者第 8–9 行：

```python
PILOT = Path(__file__).parent / "pilot"
NODES = Path(__file__).parent / "nodes"
```

它只扫 `deliverables/R5/pilot/` 与 `deliverables/R5/nodes/`，**看不到 `v4/skills/`**。

`structured-consensus` 的正文在 `v4/skills/structured-consensus/SKILL.md`（65 行，真实存在），而 `deliverables/R4/nodes/structured-consensus/` 下只有 `compilation-log.md` 无 body。所以 R5 的校验器报 `missing compiled bodies: structured-consensus`。

R5 那份校验器是 **BASIS 编译期的自查工具**，不是成品验收工具。它的 `SKILLS` 常量（第 7 行）还指着 v3 的 `skills/`——那是它当初比对 v3 阈值用的，对它自己的用途是正确的。

N2 把它整体接进成品校验时没有改路径。判定：**N2 修接线，R5 那份文件不动。**

## 三 已核实的其余两项

**N2 报「N1 正文仍有两处 `assumptions_updates`」** — 现已零命中。N1 修掉了，N2 报的是修前状态。八字段里是 `assumption_updates`（单数 assumption），这个拼写陷阱值得在校验器里保留专门的报错文案。

**R4 的 3 条多算已查明** — 来源是它 channel 副本里额外叠加的 3 条专利补边（`mine-patent-landscape` / `assess-prior-art-and-claims` / `map-patent-white-space` → `validate-research-gap`）。权威架构 157 条，其中 82 T→T + 75 S→S = 157，对上了。R4 已更新 `05-r4-graph.md` 并写明计数来源。

这 3 条专利补边本身是个待裁定项：它们不在权威架构里，是 R4 早期为补 ACQUISITION→INSIGHT 的空缺提的。**本轮不并入**——架构 JSON 是只读权威源，加边要单独立项。R4 若认为该补，写理由到 `00-escalation.md`，我另裁。

## 四 修复清单

| 谁 | 修什么 |
|---|---|
| N2 | `validate_graph.py` 对 R5 校验器的调用：改为扫 `v4/skills/`，或在调用时传路径参数。不要改 R5 那份文件 |
| N2 | 校验器加一条专门报错：`delta_fields` 出现 `assumptions_updates`（复数）时提示应为 `assumption_updates` |

修完全量路径必须退出 0。

## 五 通过标准（重申）

`python v4/scripts/validate_graph.py` **不带任何跳过开关**退出 0，才算 v4 正文与索引层通过。

`--skip-threshold` 是低负载开发时的便利开关，不是验收路径。
