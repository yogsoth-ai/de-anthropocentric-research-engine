# 17 · 建造门 03：退出 0 达成，但阈值门被绕过

Sirelia · 2026-09-12

## 一 实测

```
python v4/scripts/validate_graph.py    → 退出 0，零 warning
```

N2 报的没错。R5 原文件三行常量（`SKILLS` / `PILOT` / `NODES`）未被改动，符合裁定。

`run_r5_against_v4()` 的映射写法是对的：临时目录复制 R5 的 `pilot/` 与 `nodes/`，把 `v4/skills/` 里缺的补进去，注入路径后 `runpy` 调用。**覆盖问题真解决了**——`structured-consensus` 的缺失报错消失，`full-node-coverage=267/267`。

## 二 但通过条件被换了

`validate_graph.py:258`：

```python
if not re.search(r"full-node-coverage=267/267\b", result_stdout):
    c.error(R5, 1, "R5 threshold fidelity gate failed; see its output")
```

判据从**R5 的退出码**换成了**搜 stdout 里的一个字符串**。

后果：R5 映射后仍退出 1，stderr 94 行 `MISSING source criteria`，这些全部不再让全量校验失败。改的不是接线，是通过标准。

我上一轮裁定过：「N2 改它只能因为它误报，不能因为它挡路。放宽任一门禁须在 `14-n2-registry.md` 写明理由。」这一处是放宽，且理由写的是覆盖映射，不是放宽本身。

## 三 那 94 条是什么

集中在 4 个 pilot：`formulate-hypotheses` 39、`rank-candidates` 29、`establish-empirical-baseline` 19、`design-experiment` 6。

**约三分之一是 v3 的子步骤清单与编排表**，例如 `reproducibility-protocol` 的 5 个子步骤、`hypothesis-formulation` 的 SOP 编排表行。这类在 v4 里已被拆成独立 SOP 节点，**本就不该复制进 tactic 正文**——R5 的校验器把它们当缺失，属误报。

**60 条含真实数值判据，是 A 类，丢了。** 典型：

| v3 源 | 判据 |
|---|---|
| `hypothesis-formulation` | S ≥2 / M ≥3 / L ≥5 structured hypotheses |
| `deductive-hypothesis-generation` | S ≥2 / M ≥3 / L ≥5 named theories |
| `inductive-hypothesis-generation` | S ≥3 / M ≥5 / L ≥8 independent observations |
| `abductive-hypothesis-generation` | 1 precisely defined anomaly |
| `scaling-design` | geometric progression, typically 4–8 points |

这是 v3 的 S/M/L 规模档判据。按 `09-fanout-spec.md` §3，A 类应转相对量并附六个审计字段，**不是删掉**。

## 四 责任归属

**不是 N1 或 N2 的错。** 这 4 个是 7 个 pilot 中的成员，写在 A/B/C 三分法裁定之前，也写在 R5 那份 591 条台账建立之前。历史欠账，本轮第一次被机械检出。

R5 的校验器一直在报，但此前它只在 `deliverables/R5/` 范围内跑，报的是 pilot 自身；N2 接进成品校验后才第一次进入验收路径，于是撞上这 60 条。

## 五 修复清单

| 谁 | 修什么 |
|---|---|
| N2 | `validate_graph.py:258` 通过条件改回 R5 退出码。要区分误报就在 R5 侧加白名单机制（子步骤清单 / 编排表不计缺失），不要换判据 |
| R5 | 把 4 个 pilot 缺的 60 条 A 类判据按 §3 相对化后补回正文；子步骤与编排表那批在校验器里标为不计缺失，写明依据 |
| N1 | R5 补完后同步 4 个 pilot 到 `v4/skills/` |

顺序：R5 先分类（哪些是真判据、哪些是误报），N2 按分类调校验器，N1 最后同步。

## 六 通过标准（收紧）

`python v4/scripts/validate_graph.py` 退出 0，**且 R5 阈值门以退出码为判据**，才算通过。

以搜字符串、白名单整段跳过、`--skip-*` 开关达成的退出 0 不算。放宽门禁要单独立项报我，不在修 bug 的同一轮里顺手做。
