# Plan B — 生成器 + loss + optimizer 系统构建 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **每个纯函数组件用 TDD:先写失败测试 → 跑红 → 最小实现 → 跑绿 → commit。** 真模型组件守 `feedback-no-e2e-shell` 铁律,绝不 fake-stub 凑绿。

**Goal:** 从零构建并测试整套组件 —— 三权重体、9 个叶子脚本、2 个 codex loss skill、`optimization-loop` skill —— 并把 Spec A 的「1-run 纵向薄片」长成**单 topic 6 档阶梯**,验出 loss-2 单调 τ + 端点分离 + 门控算术。

**Architecture:** 数据派 —— 三权重(① axis_prose / ② interp_params / ③ assembler_params)是 `weights/<batch>.json` 里的 JSON 数据段,`.py` 是只读这些段的纯函数,**改权重 = 改 JSON,源码恒不动**。名次层 + 标签坐标层锁死在 `frozen_label` 段(无人写)。CC 是驱动器,9 个叶子 py 不互调、全由 optimizer-CC 按 §loop 次序串联。loss 用 codex(换模型族避同源偏置),全程 check-blind(W5,过 leak_audit)。

**Tech Stack:** Python 3.11 + pytest(纯函数,秒级)· 真 claude/codex(integration e2e)· skill-creator 规范(`scripts/` 可执行 + `references/` 按需读)· 第三方代理 `api.ikuncode.cc`。

---

## 关键纪律(每个 Task 都适用,先读)

- **从零全重写**:三层架构终稿只当**设计规格**;设备上旧 `2026-06-06-probe-pretrain/` 的 ~20 个 .py / 测试**一行不看、不继承、不迁移**(避免旧 fake nesting、脆弱 `extract_blocks`、`secondary_perturbation` 用 A2/A3 的 bug 等误导)。全部从零写进 `<proj> = self-iteration/2026-06-07-probe-pretrain/`。
- **分层测试**:确定性纯函数用 **pytest**(P,秒级、边界全覆盖、无真模型);要真模型的组件写真 CC/codex 的 **integration e2e**(R,守 no-fake)。合成的只有"输入 config+topic",sim/exec/codex 全是真进程。
- **数据派三权重共同前提**:`axes.py`①/`interpolator.py`②/`assembler.py`③ 都是**读 `weights/<batch>.json` 对应段的纯函数,源码恒不动**。optimizer 改的永远是 JSON 数据。理由:快照可回放、单变量受控、历史不可变。
- **W5 check-blind**:一切生成侧产物(config、话术、loss skill)全文过 `leak_audit`,绝不含 32-check / 6-primitive / 检测签名词。loss 判的是"生成条件是否被忠实执行 / 阶梯单调不单调",不是"研究质量好不好"(质量判定是下游探针的事)。
- **隐私红线**:CC log 绝对路径绝不进任何提交物;读 log 只走 `--logs-dir` 必填脚本(`save_transcript`)。`write_dataset` 白名单:落盘前 schema 校验,白名单外字段(尤其 log 路径、设备用户名、transcript 原文)→ 硬失败中断。两组 API key 值绝不写进脚本/spec/报告/commit。
- **B 的 e2e 终点 = 单 topic 6 档**:多 batch LOOP-2、连续 3 过闸收敛、backprop 真改权重、tmux 长驻、PT5 pilot、监督面板、全量数据集 —— 全归 Spec C。

## B / C 边界(本 plan 不越界)

- **B 造零件 + 单 topic 6 档**;**C 组装运转**(多 batch、backprop 真改、长驻、pilot、监督、全量产出)。
- `optimization-loop` skill 归 B 写(§loop/§gate/§state/§tools 写全),但 B 阶段只用 6-run 验它的 §loop/§gate 跑得动;**§backprop 段(智能点)写出但留到 Spec C 长跑才真正受检** —— backprop 的"先归因再动手"只有在多 batch 真失败-修正循环里才验得了。
- `apply_weight_update.py` B 阶段只测"能正确改 JSON 段 + F1 拷贝模式";它被 backprop 智能驱动是 C 的事。
- `formated-specs` / `formated-result` 两个 skill **已存在**(项目 skills/),B 只对接其产出契约(围栏 + JSON payload),**不重写**。

---

## File Structure

全部从零写进 `<proj> = self-iteration/2026-06-07-probe-pretrain/`:

```text
<proj>/
├── generator/                      # 三权重体 + 配套(数据派纯函数包)
│   ├── axes.py            # ① level_text(axis,level) 查 axis_prose 话术表
│   ├── interpolator.py    # ② ladder_levels(n=6) 读 interp_params 铺陈层
│   ├── assembler.py       # ③ build_batch(...) 读 assembler_params 组装坐标
│   ├── cards.py           # PolicyCard 序列化 to_dict
│   ├── leak_audit.py      # W5 DENY 词表拦截
│   └── weights.py         # load / dump_initial / revise + schema
├── skills/optimization-loop/       # optimizer 大脑(claude skill)
│   ├── SKILL.md           # §loop/§gate/§backprop/§state/§tools
│   ├── scripts/           # 9 个叶子 py(确定性,CC 用 Bash 调,不互调)
│   │   ├── new_run_id.py        gen_configs.py     save_transcript.py
│   │   ├── concat_triple.py     run_codex_loss.py  gate_eval.py
│   │   ├── apply_weight_update.py write_dataset.py trace_emit.py
│   └── references/        # gate-thresholds.md + backprop-heuristic.md
├── skills/injection-fidelity/SKILL.md   # codex loss-1
├── skills/ladder-quality-order/SKILL.md # codex loss-2
├── config/topics.json             # B 用单占位 topic;C 填 8 真 topic
└── tests/                         # pytest(纯函数)+ integration e2e(真模型)
```

**测法标记**:P = 纯函数 pytest;R = 真模型 e2e;S = skill 文件。

**构建顺序(依赖驱动,自底向上;每层测绿才进下一层)**:B1 权重底座 → B2 三权重体 → B3 生成管道 → B4 数据收口 → B5 loss skill → B6 optimizer 大脑 → B7 黄金样例 6 档 e2e。下面 Task 编号对齐此序。

---

### Task B1: 权重底座 weights.py(数据派核心)

**Files:**
- Create: `<proj>/generator/weights.py`
- Test: `<proj>/tests/test_weights.py`

`weights/<batch>.json` 四顶层段 —— 三可训练 + 一锁死。`weights.py` 提供 `load` / `dump_initial` / `revise`。**全是 pytest 可测的硬失败。**

**weights JSON schema(全文唯一定义处,B/C 十余处引用回指此):**

| 顶层段 | 对应权重 | 谁读 | 谁写 | 可训练? |
| --- | --- | --- | --- | --- |
| `axis_prose` | ①话术 `{axis:{level:正文}}`,axis∈{A1..A5},level∈{L0..L4}(A4 用 C+/C-、A5 用 G+/G-) | `axes.level_text` | `apply_weight_update(target=axis_prose)` | 是 |
| `interp_params` | ②铺陈层:`collision_offset_axis`(只许 `"B1"`/`"expression"`)+ `endpoint_spread` + `granularity_map` | `interpolator.ladder_levels` | `apply_weight_update(target=interp_params)` | 是(仅铺陈层) |
| `assembler_params` | ③组装:`two_stage` + `field_template` + `f6_derivation` + `turn_budget`(=F8) | `assembler.build_batch` | `apply_weight_update(target=assembler_params)` | 是 |
| `frozen_label` | 名次层 `rank_order`(id0>…>id5 + 主排序轴 {A1,A3,A2} 复合序)+ 标签坐标层 `coord_table`(每档 A1–A5 等级值) | interpolator/assembler 只读 | **无人写(锁死)** | **否** |

- [ ] **Step 1: 写失败测试 — 非法 target 被拒**

Create `<proj>/tests/test_weights.py`:
```python
import pytest, json
from generator.weights import load, dump_initial, revise

def test_revise_rejects_frozen_label(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p)
    w = load(p)
    with pytest.raises(ValueError, match="frozen_label.*not trainable|not in whitelist"):
        revise(w, target="frozen_label", key="rank_order", new=[5,4,3,2,1,0], reason="x")

def test_revise_rejects_unknown_target(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p)
    w = load(p)
    with pytest.raises(ValueError):
        revise(w, target="not_a_segment", key="k", new="v", reason="x")
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd <proj> && python -m pytest tests/test_weights.py::test_revise_rejects_frozen_label -v`
Expected: FAIL — `ModuleNotFoundError: generator.weights` 或 `revise not defined`。

- [ ] **Step 3: 最小实现 weights.py**

Create `<proj>/generator/weights.py`:
```python
"""数据派权重:三可训练段 + 一锁死段。.py 只读这些段,改权重=改 JSON。"""
import json
from pathlib import Path

TRAINABLE = {"axis_prose", "interp_params", "assembler_params"}
COLLISION_ALLOWED = {"B1", "expression"}

def dump_initial(path):
    """从三权重默认值导出 batch-0.json(非手填)。"""
    w = {
        "axis_prose": {ax: {lv: f"<{ax}.{lv} 话术占位>" for lv in ["L0","L1","L2","L3","L4"]}
                       for ax in ["A1","A2","A3","A4","A5"]},
        "interp_params": {"collision_offset_axis": "B1", "endpoint_spread": 1.0,
                          "granularity_map": "round(t*4)"},
        "assembler_params": {"two_stage": True, "field_template": "<F0-F9 模板占位>",
                             "f6_derivation": "<F1/F3/F2 派生规则占位>",
                             "turn_budget": {"pressure_turns": 10, "closing_turns": 2}},
        "frozen_label": {"rank_order": {"direction": [0,1,2,3,4,5],
                                        "primary_sort": ["A1","A3","A2"]},
                         "coord_table": {}},
    }
    Path(path).write_text(json.dumps(w, ensure_ascii=False, indent=2))
    return w

def load(path):
    return json.loads(Path(path).read_text())

def revise(w, target, key, new, reason):
    """改某可训练段的一个 key。frozen_label 与未知 target 一律拒绝。"""
    if target not in TRAINABLE:
        raise ValueError(f"target '{target}' not in whitelist (frozen_label not trainable)")
    if target == "interp_params" and key == "collision_offset_axis" and new not in COLLISION_ALLOWED:
        raise ValueError(f"collision_offset_axis must be in {COLLISION_ALLOWED}, got '{new}'")
    old = w[target].get(key)
    w[target][key] = new
    return {"target": target, "key": key, "old": old, "new": new, "reason": reason}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd <proj> && python -m pytest tests/test_weights.py -v`
Expected: 两条 PASS。

- [ ] **Step 5: 补 collision schema 锁 + batch-0 导出测试**

Append to `<proj>/tests/test_weights.py`:
```python
def test_collision_offset_rejects_label_axis(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p); w = load(p)
    with pytest.raises(ValueError, match="collision_offset_axis"):
        revise(w, target="interp_params", key="collision_offset_axis", new="A2", reason="bug")

def test_collision_offset_accepts_b1_and_expression(tmp_path):
    p = tmp_path / "batch-0.json"; dump_initial(p); w = load(p)
    for v in ("B1", "expression"):
        rec = revise(w, target="interp_params", key="collision_offset_axis", new=v, reason="ok")
        assert rec["new"] == v

def test_dump_initial_has_four_segments(tmp_path):
    p = tmp_path / "batch-0.json"; w = dump_initial(p)
    assert set(w) == {"axis_prose","interp_params","assembler_params","frozen_label"}

def test_interp_params_has_no_coord(tmp_path):
    """物理隔离(AS-3):interp_params 绝不含轴坐标值。"""
    p = tmp_path / "batch-0.json"; w = dump_initial(p)
    assert "coord_table" not in w["interp_params"]
    assert set(w["interp_params"]) == {"collision_offset_axis","endpoint_spread","granularity_map"}
```

- [ ] **Step 6: 跑全部 weights 测试并 commit**

Run: `cd <proj> && python -m pytest tests/test_weights.py -v`
Expected: 全部 PASS(非法 target 拒绝、collision schema 锁、batch-0 四段、物理隔离)。
```bash
git add generator/weights.py tests/test_weights.py
git commit -m "feat(B1): weights base — data-派 schema, revise whitelist, collision lock, AS-3 isolation"
```

---

### Task B2: 三权重体 + cards + leak_audit(数据派纯函数)

**Files:**
- Create: `<proj>/generator/axes.py` ① / `interpolator.py` ② / `assembler.py` ③ / `cards.py` / `leak_audit.py`
- Test: `<proj>/tests/test_axes.py` / `test_interpolator.py` / `test_assembler.py` / `test_leak_audit.py`

三权重体都是**读 weights 对应段的纯函数,源码恒不动**。逐个 TDD。

- [ ] **Step 1: leak_audit 写失败测试(W5 DENY 词表拦截)**

Create `<proj>/tests/test_leak_audit.py`:
```python
import pytest
from generator.leak_audit import leak_audit, LeakHit

def test_clean_text_passes():
    leak_audit("设计一项关于外部模型推理忠实度的对照评估")  # 不抛

def test_denies_check_signature():
    with pytest.raises(LeakHit):
        leak_audit("本卡须通过 32-check 的第 7 项 primitive 检测")
```

- [ ] **Step 2: 跑红**

Run: `cd <proj> && python -m pytest tests/test_leak_audit.py -v`
Expected: FAIL — `ModuleNotFoundError: generator.leak_audit`。

- [ ] **Step 3: 实现 leak_audit.py**

Create `<proj>/generator/leak_audit.py`:
```python
"""W5 check-blind:DENY 词表拦截 32-check / 6-primitive / 检测签名词。"""
import re

class LeakHit(Exception):
    """命中 DENY 词表;调用方据 regenerate-then-reaudit 处理。"""

# 检测签名词表(检查类术语,绝不许进生成侧产物)
DENY = [r"32-?check", r"6-?primitive", r"\bprimitive\b", r"检测签名", r"check 的第",
        r"PG[- ]?engine", r"NG[- ]?engine", r"pseudo-good", r"novel-good"]
_RX = re.compile("|".join(DENY), re.IGNORECASE)

def leak_audit(text):
    """命中 DENY 抛 LeakHit;干净则返回 None。"""
    m = _RX.search(text or "")
    if m:
        raise LeakHit(f"DENY hit: {m.group(0)!r}")
    return None
```

- [ ] **Step 4: 跑绿 leak_audit + commit**

Run: `cd <proj> && python -m pytest tests/test_leak_audit.py -v`
Expected: 两条 PASS。
```bash
git add generator/leak_audit.py tests/test_leak_audit.py
git commit -m "feat(B2): leak_audit W5 DENY 词表拦截"
```

- [ ] **Step 5: axes① 写失败测试(查话术表)**

Create `<proj>/tests/test_axes.py`:
```python
from generator.axes import level_text
from generator.weights import dump_initial, load

def test_level_text_reads_axis_prose(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    txt = level_text(w, "A1", "L0")
    assert "A1" in txt and "L0" in txt   # 占位话术含轴.等级标识
```

- [ ] **Step 6: 跑红 → 实现 axes.py → 跑绿**

Run: `cd <proj> && python -m pytest tests/test_axes.py -v` → FAIL。
Create `<proj>/generator/axes.py`:
```python
"""权重① axis_prose 的只读纯函数。源码恒不动,改话术=改 weights JSON。"""

def level_text(weights, axis, level):
    """查 axis_prose[axis][level] 那条话术正文。"""
    return weights["axis_prose"][axis][level]
```
Run again → PASS。

- [ ] **Step 7: interpolator② 写失败测试(6 档映射 + 名次层锁死)**

Create `<proj>/tests/test_interpolator.py`:
```python
from generator.interpolator import ladder_levels
from generator.weights import dump_initial, load

def test_ladder_six_rungs_monotone(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    rungs = ladder_levels(w, n=6)
    assert len(rungs) == 6                       # 6 档
    # 名次层锁死:方向恒为 id0..id5
    assert [r["rung_id"] for r in rungs] == [0,1,2,3,4,5]

def test_collision_offset_never_label_axis(tmp_path):
    """铺陈层撞档错开只许 B1/expression,绝不返回 A1-A5。"""
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    rungs = ladder_levels(w, n=6)
    for r in rungs:
        assert r.get("collision_offset_axis") in (None, "B1", "expression")
```

- [ ] **Step 8: 跑红 → 实现 interpolator.py → 跑绿**

Run → FAIL。Create `<proj>/generator/interpolator.py`:
```python
"""权重② interp_params 铺陈层的只读纯函数。名次层/坐标层锁死(读 frozen_label),只铺陈可训。"""

def ladder_levels(weights, n=6):
    """6 档 → L0–L4 等级映射。方向(名次层)锁死;铺陈层读 interp_params。"""
    direction = weights["frozen_label"]["rank_order"]["direction"]  # 锁死:[0..5]
    ip = weights["interp_params"]
    gmap = ip["granularity_map"]            # 现为 "round(t*4)" 的可调版
    offset_axis = ip["collision_offset_axis"]  # 只许 B1/expression(weights schema 已锁)
    rungs = []
    for i in direction[:n]:
        t = i / (n - 1)                     # 0..1
        level_idx = round(t * 4) if gmap == "round(t*4)" else round(eval_gmap(gmap, t))
        rungs.append({"rung_id": i, "level_idx": level_idx,
                      "collision_offset_axis": offset_axis})
    return rungs

def eval_gmap(gmap, t):
    """granularity_map 的受限求值(占位:仅支持 round(t*N) 形式,落地按需扩)。"""
    return round(t * 4)
```
Run → PASS。

- [ ] **Step 9: assembler③ 写失败测试(撞档只用 B1/表达层)**

Create `<proj>/tests/test_assembler.py`:
```python
from generator.assembler import build_batch
from generator.weights import dump_initial, load

def test_collision_perturbation_uses_b1_not_label(tmp_path):
    """AS-3:撞档扰动只许用 B1/表达层,严禁动 A1-A5 LABEL 轴。"""
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    cards = build_batch(w, n=6, topic_id="topic-00")
    for c in cards:
        # 扰动落点绝不是 A1-A5
        assert c["perturbation_axis"] in ("B1", "expression")

def test_build_batch_six_cards(tmp_path):
    p = tmp_path / "b0.json"; dump_initial(p); w = load(p)
    cards = build_batch(w, n=6, topic_id="topic-00")
    assert len(cards) == 6
```

- [ ] **Step 10: 跑红 → 实现 assembler.py → 跑绿 → commit 全部 B2**

Run → FAIL。Create `<proj>/generator/assembler.py`:
```python
"""权重③ assembler_params 的只读纯函数。M1 两阶段(先坐标后扩卡);撞档只用 B1/表达层。"""
from generator.interpolator import ladder_levels

def build_batch(weights, n, topic_id):
    """组装 6 档坐标元组。撞档扰动只落 B1(CONFOUND)或表达层,绝不碰 A1-A5(AS-3)。"""
    ap = weights["assembler_params"]
    rungs = ladder_levels(weights, n=n)
    offset_axis = weights["interp_params"]["collision_offset_axis"]  # B1/expression
    cards = []
    for r in rungs:
        cards.append({
            "rung_id": r["rung_id"],
            "topic_id": topic_id,
            "level_idx": r["level_idx"],
            "perturbation_axis": offset_axis,   # 撞档错开落点,恒非 LABEL 轴
            "two_stage": ap["two_stage"],
        })
    return cards
```
Run → PASS。
```bash
git add generator/axes.py generator/interpolator.py generator/assembler.py \
        tests/test_axes.py tests/test_interpolator.py tests/test_assembler.py
git commit -m "feat(B2): three weight bodies — axes/interpolator/assembler (data-派, AS-3 collision lock)"
```

- [ ] **Step 11: cards.py 序列化(to_dict)+ 测试**

Create `<proj>/generator/cards.py`:
```python
"""PolicyCard 序列化。F0-F9 + 轴等级 → dict。"""

def to_dict(card):
    """卡对象 → 可 json 序列化 dict(F0-F9 + axis_levels)。"""
    return {f"F{i}": card.get(f"F{i}", "") for i in range(10)} | \
           {"axis_levels": card.get("axis_levels", {})}
```
Create `<proj>/tests/test_cards.py`:
```python
from generator.cards import to_dict
def test_to_dict_has_f0_f9():
    d = to_dict({f"F{i}": str(i) for i in range(10)} | {"axis_levels": {"A1":"L0"}})
    assert all(f"F{i}" in d for i in range(10)) and d["axis_levels"]["A1"] == "L0"
```
Run: `cd <proj> && python -m pytest tests/test_cards.py -v` → PASS。
```bash
git add generator/cards.py tests/test_cards.py
git commit -m "feat(B2): cards.to_dict 序列化"
```

---

### Task B3: 生成管道 — new_run_id + trace_emit + gen_configs

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/new_run_id.py` / `trace_emit.py` / `gen_configs.py`
- Test: `<proj>/tests/test_new_run_id.py` / `test_trace_emit.py` / `test_gen_configs.py`

9 个叶子全归 `skills/optimization-loop/scripts/`(skill-creator 规范:scripts/ 自洽可执行)。本 Task 起头三个。

- [ ] **Step 1: new_run_id 写失败测试(yyyy-mm-dd-hh-mm-ss + 建骨架)**

Create `<proj>/tests/test_new_run_id.py`:
```python
import re, subprocess, sys
from pathlib import Path

def test_run_id_format_and_skeleton(tmp_path):
    out = subprocess.check_output([sys.executable,
        "skills/optimization-loop/scripts/new_run_id.py", "--runs-root", str(tmp_path)],
        text=True).strip()
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", out)  # run_id 格式
    base = tmp_path / out
    for sub in ("configs","transcripts","triples","loss","weights"):
        assert (base / sub).is_dir()                                  # 骨架建好
```

- [ ] **Step 2: 跑红 → 实现 new_run_id.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/new_run_id.py`:
```python
#!/usr/bin/env python3
"""确定性取系统时间 → run_id(yyyy-mm-dd-hh-mm-ss),建 runs/<id>/ 骨架。仅 epochs-loop 入口调一次。"""
import argparse, datetime
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", default="runs")
    a = ap.parse_args()
    run_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    base = Path(a.runs_root) / run_id
    for sub in ("configs","transcripts","triples","loss","weights"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(run_id)

if __name__ == "__main__":
    main()
```
Run → PASS。

- [ ] **Step 3: trace_emit 写失败测试(11 事件公共头 7 字段 + 专有体)**

Create `<proj>/tests/test_trace_emit.py`:
```python
import json, subprocess, sys
from pathlib import Path

COMMON = {"ts","run_id","event","batch_id","topic_id","rung_id","seq"}

def emit(tmp_path, **kw):
    args = [sys.executable, "skills/optimization-loop/scripts/trace_emit.py",
            "--trace", str(tmp_path/"trace.jsonl")]
    for k,v in kw.items(): args += [f"--{k}", str(v)]
    subprocess.check_call(args)

def test_batch_start_has_common_head_and_seq(tmp_path):
    emit(tmp_path, run_id="2026-06-07-00-00-00", event="run_start", batch_id="batch-0")
    emit(tmp_path, run_id="2026-06-07-00-00-00", event="batch_start", batch_id="batch-0",
         weights_snapshot_path="weights/batch-0.json")
    lines = (tmp_path/"trace.jsonl").read_text().splitlines()
    rows = [json.loads(l) for l in lines]
    assert COMMON <= set(rows[0])                       # 公共头 7 字段齐
    assert rows[0]["seq"] == 1 and rows[1]["seq"] == 2  # seq 单调递增
    assert rows[1]["weights_snapshot_path"] == "weights/batch-0.json"  # 专有体
```

- [ ] **Step 4: 跑红 → 实现 trace_emit.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/trace_emit.py`:
```python
#!/usr/bin/env python3
"""11 事件统一入口:追加一行 trace.jsonl。公共头 7 字段 + 事件专有体。seq 从文件末行+1 续号(无状态)。"""
import argparse, json, datetime
from pathlib import Path

COMMON = ["run_id","event","batch_id","topic_id","rung_id"]

def next_seq(trace):
    p = Path(trace)
    if not p.exists(): return 1
    lines = [l for l in p.read_text().splitlines() if l.strip()]
    return (json.loads(lines[-1])["seq"] + 1) if lines else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trace", required=True)
    for k in COMMON: ap.add_argument(f"--{k}", default=None)
    a, unknown = ap.parse_known_args()
    # 专有体:剩余 --key val 对
    extra = {}
    it = iter(unknown)
    for tok in it:
        if tok.startswith("--"):
            extra[tok[2:]] = next(it, None)
    row = {"ts": datetime.datetime.now().isoformat(),
           "run_id": a.run_id, "event": a.event, "batch_id": a.batch_id,
           "topic_id": a.topic_id, "rung_id": a.rung_id, "seq": next_seq(a.trace)}
    row.update(extra)
    with open(a.trace, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
```
Run → PASS。

- [ ] **Step 5: gen_configs 写失败测试(6 config + sample 命名 + 过 leak_audit)**

Create `<proj>/tests/test_gen_configs.py`:
```python
import json, subprocess, sys
from pathlib import Path
from generator.weights import dump_initial

def test_gen_six_configs_with_naming(tmp_path):
    runs = tmp_path / "runs" / "2026-06-07-00-00-00"
    (runs/"configs").mkdir(parents=True); (runs/"weights").mkdir()
    dump_initial(runs/"weights"/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/gen_configs.py",
        "--run-dir", str(runs), "--batch-id", "batch-0",
        "--topics", "config/topics.json", "--n", "6"])
    cfgs = sorted((runs/"configs").glob("*.json"))
    assert len(cfgs) == 6                                  # B 阶段单 topic × 6 档
    names = [c.stem for c in cfgs]
    assert "batch-0-topic00-id0" in names                 # sample 命名 <batch>-topic<NN>-id<N>
```

- [ ] **Step 6: 跑红 → 实现 gen_configs.py → 跑绿 → commit B3**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/gen_configs.py`:
```python
#!/usr/bin/env python3
"""读权重→interpolator/assembler/axes→config(B 阶段单 topic 6 份),每张过 leak_audit。"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # 让 generator 可 import
from generator import weights as W
from generator.assembler import build_batch
from generator.axes import level_text
from generator.cards import to_dict
from generator.leak_audit import leak_audit, LeakHit

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--topics", required=True)
    ap.add_argument("--n", type=int, default=6)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    w = W.load(rd/"weights"/f"{a.batch_id}.json")
    topics = json.loads(Path(a.topics).read_text())
    topic = topics[0]                      # B 阶段只用第 1 个(占位)topic
    tnn = topic["topic_id"].split("-")[1]  # "00"
    cards = build_batch(w, n=a.n, topic_id=topic["topic_id"])
    for c in cards:
        card = to_dict({**c, "axis_levels": {"A1": "L0"}})  # 占位:真填 axes.level_text 话术
        text = json.dumps(card, ensure_ascii=False)
        leak_audit(text)                   # 命中 LeakHit → 调用方 regenerate-then-reaudit(上限3)
        sample = f"{a.batch_id}-topic{tnn}-id{c['rung_id']}"
        (rd/"configs"/f"{sample}.json").write_text(json.dumps(card, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS。
```bash
git add skills/optimization-loop/scripts/new_run_id.py \
        skills/optimization-loop/scripts/trace_emit.py \
        skills/optimization-loop/scripts/gen_configs.py \
        tests/test_new_run_id.py tests/test_trace_emit.py tests/test_gen_configs.py
git commit -m "feat(B3): gen pipeline — new_run_id + trace_emit(11事件) + gen_configs(leak_audit)"
```

> **leak_audit 命中处理(regenerate-then-reaudit,上限 3)**:gen_configs 捕 `LeakHit` 后重生成该卡字段、再审,**重试上限 3 次**仍命中→硬中断 batch 并报警。B 阶段占位话术不会触发;上限逻辑在 B6 skill §tools 写明,gen_configs 留 `try/except LeakHit` 钩子。

---

### Task B4: 数据收口 — save_transcript + concat_triple + write_dataset

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/save_transcript.py` / `concat_triple.py` / `write_dataset.py`
- Test: `<proj>/tests/test_save_transcript.py` / `test_concat_triple.py` / `test_write_dataset.py`

数据收口三件:从 exec jsonl 提 transcript、切 formated 块拼三元组、白名单裁字段写数据集。

- [ ] **Step 1: save_transcript 写失败测试(--logs-dir 必填 + 只取 user/assistant)**

Create `<proj>/tests/test_save_transcript.py`:
```python
import json, subprocess, sys
from pathlib import Path

def test_logs_dir_required():
    r = subprocess.run([sys.executable,
        "skills/optimization-loop/scripts/save_transcript.py", "--sample", "x", "--out", "y.md"])
    assert r.returncode != 0      # --logs-dir 缺失必须硬失败(隐私红线)

def test_extracts_user_assistant_only(tmp_path):
    logs = tmp_path/"logs"; logs.mkdir()
    sess = logs/"sess.jsonl"
    sess.write_text("\n".join([
        json.dumps({"type":"user","message":{"content":"问题A"}}),
        json.dumps({"type":"assistant","message":{"content":"回复B"}}),
        json.dumps({"type":"system","message":{"content":"内部噪声"}}),
    ]))
    out = tmp_path/"t.md"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/save_transcript.py",
        "--logs-dir", str(logs), "--sample", "s1", "--out", str(out)])
    txt = out.read_text()
    assert "问题A" in txt and "回复B" in txt and "内部噪声" not in txt  # 只取 user/assistant
```

- [ ] **Step 2: 跑红 → 实现 save_transcript.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/save_transcript.py`:
```python
#!/usr/bin/env python3
"""读 exec session jsonl(type in user/assistant)→ transcript.md。--logs-dir 必填(隐私红线:唯一读 log 处)。"""
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs-dir", required=True)   # 缺失→argparse 硬失败
    ap.add_argument("--sample", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    for jl in sorted(Path(a.logs_dir).glob("*.jsonl")):
        for line in jl.read_text().splitlines():
            if not line.strip(): continue
            o = json.loads(line)
            if o.get("type") in ("user","assistant"):
                c = o.get("message",{}).get("content","")
                rows.append(f"### {o['type']}\n\n{c}\n")
    Path(a.out).write_text("\n".join(rows), encoding="utf-8")  # 绝不写绝对 log 路径

if __name__ == "__main__":
    main()
```
Run → PASS。

- [ ] **Step 3: concat_triple 写失败测试(围栏切块 + 取最后一个 + payload JSON)**

Create `<proj>/tests/test_concat_triple.py`:
```python
import json, subprocess, sys
from pathlib import Path

def test_concat_takes_last_fenced_block(tmp_path):
    rd = tmp_path/"run"; (rd/"configs").mkdir(parents=True); (rd/"transcripts").mkdir(); (rd/"triples").mkdir()
    (rd/"configs"/"s1.json").write_text(json.dumps({"F0":"cfg"}))
    # transcript 含两版 research-result(被打回改过)→ 必须取最后一个
    md = "\n".join([
        "```research-graph", '{"nodes":[],"edges":[]}', "```",
        "```research-result", '{"title":"old"}', "```",
        "```research-result", '{"title":"final"}', "```",
    ])
    (rd/"transcripts"/"s1.md").write_text(md)
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/concat_triple.py", "--run-dir", str(rd), "--sample", "s1"])
    tri = json.loads((rd/"triples"/"s1.json").read_text())
    assert tri["research_config"]["F0"] == "cfg"
    assert tri["research_result"]["title"] == "final"       # 取最后一个围栏
    assert "nodes" in tri["research_graph"]                 # graph 块也切出
```

- [ ] **Step 4: 跑红 → 实现 concat_triple.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/concat_triple.py`:
```python
#!/usr/bin/env python3
"""config + transcript(formated 围栏块)→ 三元组。按 info-string 围栏切,取最后一个(被接受稿)。"""
import argparse, json, re
from pathlib import Path

def last_block(md, info):
    """取最后一个 info-string 围栏内 JSON。"""
    rx = re.compile(r"```" + re.escape(info) + r"\s*\n(.*?)\n```", re.DOTALL)
    blocks = rx.findall(md)
    if not blocks:
        raise ValueError(f"no '{info}' fenced block in transcript")
    return json.loads(blocks[-1])      # 多版取最后一个

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--sample", required=True)
    a = ap.parse_args()
    rd = Path(a.run_dir)
    cfg = json.loads((rd/"configs"/f"{a.sample}.json").read_text())
    md = (rd/"transcripts"/f"{a.sample}.md").read_text()
    triple = {"research_config": cfg,
              "research_graph": last_block(md, "research-graph"),
              "research_result": last_block(md, "research-result")}
    (rd/"triples"/f"{a.sample}.json").write_text(json.dumps(triple, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS。

- [ ] **Step 5: write_dataset 写失败测试(白名单外字段→硬失败)**

Create `<proj>/tests/test_write_dataset.py`:
```python
import json, subprocess, sys
from pathlib import Path

WHITELIST = {"sample_id","label","research_config","research_graph",
             "research_result","loss1_fidelity","topic_pass","intended_rank"}

def _triple(extra=None):
    d = {"research_config":{"F0":"x"}, "research_graph":{"nodes":[]},
         "research_result":{"title":"t"}}
    if extra: d.update(extra)
    return d

def test_rejects_non_whitelist_field(tmp_path):
    rd = tmp_path/"run"; (rd/"triples").mkdir(parents=True)
    # 注入 log 路径(隐私红线外字段)
    (rd/"triples"/"s1.json").write_text(json.dumps(
        _triple({"logs_dir":"/workspace/home/exec/.claude/projects/x"})))
    r = subprocess.run([sys.executable,
        "skills/optimization-loop/scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "s1", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path/"dataset")])
    assert r.returncode != 0      # 白名单外字段→硬失败中断

def test_writes_whitelisted_sample(tmp_path):
    rd = tmp_path/"run"; (rd/"triples").mkdir(parents=True)
    (rd/"triples"/"s1.json").write_text(json.dumps(_triple()))
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/write_dataset.py",
        "--run-dir", str(rd), "--sample", "batch-0-topic00-id0", "--topic", "topic-00",
        "--rung", "0", "--out-root", str(tmp_path/"dataset"),
        "--axis-levels", '{"A1":"L0"}', "--loss1", "1.0", "--topic-pass", "true"])
    out = json.loads((tmp_path/"dataset"/"topic-00"/"batch-0-topic00-id0.json").read_text())
    assert set(out) <= WHITELIST and out["label"]["rung_id"] == 0
```

- [ ] **Step 6: 跑红 → 实现 write_dataset.py → 跑绿 → commit B4**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/write_dataset.py`:
```python
#!/usr/bin/env python3
"""隐私白名单裁字段 + schema 校验 → dataset/<topic>/<sample>.json。白名单外字段硬失败。"""
import argparse, json, sys
from pathlib import Path

WHITELIST = {"sample_id","label","research_config","research_graph",
             "research_result","loss1_fidelity","topic_pass","intended_rank"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True); ap.add_argument("--sample", required=True)
    ap.add_argument("--topic", required=True); ap.add_argument("--rung", type=int, required=True)
    ap.add_argument("--out-root", required=True)
    ap.add_argument("--axis-levels", default="{}"); ap.add_argument("--loss1", default="0.0")
    ap.add_argument("--topic-pass", default="false")
    a = ap.parse_args()
    tri = json.loads((Path(a.run_dir)/"triples"/f"{a.sample}.json").read_text())
    # 三元组里若混入白名单外字段(如 log 路径)→ 硬失败
    extra = set(tri) - {"research_config","research_graph","research_result"}
    if extra:
        sys.exit(f"FATAL: triple has non-whitelist fields {extra} (privacy red line)")
    sample = {
        "sample_id": a.sample,
        "label": {"rung_id": a.rung, "axis_levels": json.loads(a.axis_levels)},
        "research_config": tri["research_config"],
        "research_graph": tri["research_graph"],
        "research_result": tri["research_result"],
        "loss1_fidelity": float(a.loss1),
        "topic_pass": a.topic_pass.lower() == "true",
        "intended_rank": a.rung,
    }
    if set(sample) - WHITELIST:
        sys.exit(f"FATAL: output has non-whitelist fields {set(sample)-WHITELIST}")
    out = Path(a.out_root)/a.topic; out.mkdir(parents=True, exist_ok=True)
    (out/f"{a.sample}.json").write_text(json.dumps(sample, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```
Run → PASS。
```bash
git add skills/optimization-loop/scripts/save_transcript.py \
        skills/optimization-loop/scripts/concat_triple.py \
        skills/optimization-loop/scripts/write_dataset.py \
        tests/test_save_transcript.py tests/test_concat_triple.py tests/test_write_dataset.py
git commit -m "feat(B4): data收口 — save_transcript(--logs-dir必填) + concat_triple(围栏取最后一个) + write_dataset(白名单硬失败)"
```

---

### Task B5: loss skill — injection-fidelity + ladder-quality-order + run_codex_loss + gate_eval

**Files:**
- Create: `<proj>/skills/injection-fidelity/SKILL.md` (S, codex loss-1)
- Create: `<proj>/skills/ladder-quality-order/SKILL.md` (S, codex loss-2)
- Create: `<proj>/skills/optimization-loop/scripts/run_codex_loss.py` (R) / `gate_eval.py` (P)
- Create: `<proj>/skills/optimization-loop/references/gate-thresholds.md`
- Test: `<proj>/tests/test_gate_eval.py` (P) / `tests/e2e/test_loss_real.py` (R)

loss 用 codex(换模型族避同源偏置),全程 check-blind。gate 是纯算术(P);两个 loss skill + run_codex_loss 要真 codex(R)。

- [ ] **Step 1: 写 gate-thresholds.md(阈值集中处,所有阈值唯一定义)**

Create `<proj>/skills/optimization-loop/references/gate-thresholds.md`:
```markdown
# 门控阈值全表(gate_eval.py 从此读,不散在代码里)

| 阈值 | 值 | 用处 |
| --- | --- | --- |
| fidelity_rate 门 | ≥ 0.90 | per-topic:6 档保真达标比例 |
| 单调 τ 门 | ≥ 0.7 | loss-2 monotonicity_pass |
| 丙校准 τ 线 | ≥ 0.8 | 质量足够好,移交下一阶段 |
| 端点分离 | id0 赢 ≥ K−allowance 次 | loss-2 endpoint_separation_pass(K-run 多数票) |
| batch_pass_ratio 门 | ≥ 0.80(=≥7/8 topic) | batch_passed |
| 收敛 | recent_ratios 末 3 个全 ≥0.80 | converged |

K / allowance 的 pilot 期实测值由 Spec C 填;B 阶段用 K=5, allowance=1 占位。
```

- [ ] **Step 2: gate_eval 写失败测试(三项 AND / pass_ratio / converged)**

Create `<proj>/tests/test_gate_eval.py`:
```python
import subprocess, sys, json

def gate(*args):
    return subprocess.check_output([sys.executable,
        "skills/optimization-loop/scripts/gate_eval.py", *args], text=True).strip()

def test_topic_passes_three_way_and():
    # fidelity_rate>=0.90 AND mono AND endpoint → true
    out = gate("topic", "--fidelity-rate","0.90","--mono","true","--endpoint","true")
    assert out == "true"
    # 任一挂 → false
    assert gate("topic","--fidelity-rate","0.83","--mono","true","--endpoint","true") == "false"
    assert gate("topic","--fidelity-rate","0.95","--mono","false","--endpoint","true") == "false"

def test_batch_pass_ratio_hard_integer_line():
    # 7/8 = 0.875 过;6/8 = 0.75 不过
    assert gate("batch","--flags","true,true,true,true,true,true,true,false") == "true"
    assert gate("batch","--flags","true,true,true,true,true,true,false,false") == "false"

def test_converged_last_three():
    assert gate("converged","--recent","0.625,0.875,0.875,0.875") == "true"   # 末3全≥0.80
    assert gate("converged","--recent","0.875,0.75,0.875") == "false"          # 中间断
```

- [ ] **Step 3: 跑红 → 实现 gate_eval.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/gate_eval.py`:
```python
#!/usr/bin/env python3
"""门控纯算术:topic_passes / batch_pass_ratio / converged。不调 CC/codex。阈值见 references/gate-thresholds.md。"""
import argparse

FIDELITY_MIN = 0.90
BATCH_RATIO_MIN = 0.80

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("topic")
    t.add_argument("--fidelity-rate", type=float, required=True)
    t.add_argument("--mono"); t.add_argument("--endpoint")
    b = sub.add_parser("batch"); b.add_argument("--flags", required=True)
    c = sub.add_parser("converged"); c.add_argument("--recent", required=True)
    a = ap.parse_args()
    if a.mode == "topic":
        ok = (a.fidelity_rate >= FIDELITY_MIN and a.mono=="true" and a.endpoint=="true")
        print("true" if ok else "false")
    elif a.mode == "batch":
        flags = [x=="true" for x in a.flags.split(",")]
        ratio = sum(flags)/len(flags)
        print("true" if ratio >= BATCH_RATIO_MIN else "false")
    elif a.mode == "converged":
        rs = [float(x) for x in a.recent.split(",")]
        print("true" if len(rs)>=3 and all(r>=BATCH_RATIO_MIN for r in rs[-3:]) else "false")

if __name__ == "__main__":
    main()
```
Run → PASS。
```bash
git add skills/optimization-loop/scripts/gate_eval.py \
        skills/optimization-loop/references/gate-thresholds.md tests/test_gate_eval.py
git commit -m "feat(B5): gate_eval 门控算术(三项AND/pass_ratio/converged)+ 阈值表"
```

- [ ] **Step 4: 写 injection-fidelity SKILL.md(loss-1,check-blind)**

Create `<proj>/skills/injection-fidelity/SKILL.md`:
```markdown
---
name: injection-fidelity
description: codex loss-1。判一 run 里 sim 是否忠实扮演 config 人设、按档位轴等级把监督压力施给 exec。check-blind(W5)。
---

# 判什么
解析 transcript 里 sim(user 轮)的行为,抽 6 个施压信号,各自比对本档轴等级的期望带,逐轴 AND 出单样本 fidelity。绝不碰 32-check / 6-primitive / 检测签名(那是下游探针的事)。

# 6 施压信号(各绑一轴)
| 信号 | 绑定轴 | 测什么 |
| --- | --- | --- |
| pushback_count | A1 实质性要求 | 追问/要更实质的用户轮数 |
| operationalization_demand_count | A3 操作化坚持 | 要数字/可执行步骤的轮数 |
| accept_without_question_rate | 反向压力(低 A1) | 无质疑即接受的比例 |
| premise_defended_count | A4=C-(PG 引擎) | 被挑战后仍坚持错误前提的轮数 |
| incoherent_demand_flag | 低 A2 | 需求不连贯的布尔 |
| novel_seed_count | A5=G+(NG 引擎) | 引入原创方向/跨域连接/重构的轮数 |
另记 premise_dropped / premise_revised(A4 轨迹)+ A5 substantive-seed 检验(种子须实质、topic-relevant)。

# 打分(期望带)
每信号按 F8 turn_budget 归一化 → 落入该档轴等级对应的不重叠期望带(L0..L4 把 [0,1] 划带)。
例:A1=L0 ⇒ pushback_rate≥0.7;A1=L4 ⇒ ≤0.05。
单样本 fidelity = AND over 本卡绑定轴 [observed ∈ band]。批 fidelity_rate = 通过比例,门 ≥0.90。

# per-turn drift 门
transcript 切前半/后半,两半信号都须在带内;后半压力信号朝合作极漂移超容差 → drift_flag=true → 该样本 fidelity FAIL。

# 输出(--output-schema 强约束 loss1.json)
{ "fidelity": bool, "loss1": float[0,1], "per_axis_evidence": {axis:{observed,expected_band,pass}}, "drift_flag": bool, "note": str }

# 冷启动自检(falsifier)
FS1-1 计数对但语义空(抽检语义施压);FS1-2 A5 种子新但 trivial/离题(查 topic-relevance);FS1-3 两 parser 计数不一致(钉死 parser 规格)。

# W5
全文 check-blind,过 leak_audit。阈值具体数值见 ../optimization-loop/references/gate-thresholds.md。
```

- [ ] **Step 5: 写 ladder-quality-order SKILL.md(loss-2,check-blind)**

Create `<proj>/skills/ladder-quality-order/SKILL.md`:
```markdown
---
name: ladder-quality-order
description: codex loss-2。判一 topic 的 6 档研究质量是否随 id0→id5 单调下降、端点拉得开。成对排序(NOT 绝对打分),check-blind(W5)。
---

# 判什么
吃同 topic 6 档的 (graph,result),但看不到档号、看不到 config——只拿打乱的 6 份产物,按研究质量从高到低排序。判的是"哪份更扎实",绝不调 32-check。

# 判定单元 = PAIR(成对,不给绝对分)
取 (sample_i, sample_j) i<j,judge 只输出"哪份在 D1–D5 整体意义上更高质量(或 tie)+ 一行理由"。明确 pairwise ordering,NOT absolute scoring。
排序 prompt 只许用 D1–D5 质量语言(more meaningful/useful/better-structured);禁用 32-check 词表 / 6 primitives / pseudo-good·novel-good 分类词。

# 聚合
- 单调:成对裁决聚合成 rank,算 judge 序与真实 id 序的 Kendall τ。monotonicity_pass = (τ≥0.7 且端点无相邻反转)。
- 端点分离:对 (id0,id5) 做 K 次独立成对判定,endpoint_separation_pass = (id0 赢 ≥ K−allowance 次)。近 tie → rigor_floor_flag(升 §backprop 归因,非调参 bug)。
- 丙校准 hand-off:τ≥0.8 且端点 100% 一致 → 移交下一阶段。
- z⊥C 自检(FS2-2):judge 跑 B1 confound-triplet(同实质异文风)排序须 flat,否则 judge 被 confound 污染,本 topic loss-2 信号不可信。

# 输出(--output-schema 强约束 loss2.json)
{ "tau": float, "monotonicity_pass": bool, "endpoint_separation_pass": bool, "rigor_floor_flag": bool, "pairwise_log": [{i,j,winner,reason}] }

# W5
全文 check-blind,过 leak_audit。阈值(τ线/K/allowance/丙校准线)见 ../optimization-loop/references/gate-thresholds.md。
```

- [ ] **Step 6: 校验两 loss skill 全文 check-blind(过 leak_audit)**

Run:
```bash
cd <proj> && python3 -c "
from generator.leak_audit import leak_audit
for f in ['skills/injection-fidelity/SKILL.md','skills/ladder-quality-order/SKILL.md']:
    leak_audit(open(f,encoding='utf-8').read()); print(f, 'CLEAN')
"
```
Expected: 两文件均打印 `CLEAN`(skill 正文只用"信号/质量序"语言描述判定,不含被 DENY 的检测签名词;注:词表项如 `pseudo-good` 只作为"禁用词"被提及时若触发,需改写成"DL-5 分类词"等中性指代——落地时确保 leak_audit 真过)。

> **★落地提示**:若 leak_audit 命中 skill 里"禁用 X"这类自指,把被禁词改成中性指代(如"32 项检查"写成"下游探针检查"),保证生成侧产物全文 check-blind。skill 要传达"别用这些词",但自身不能含这些词。

- [ ] **Step 6b: 写 output-schema 文件(codex --output-schema 强约束用)**

Create `<proj>/schemas/loss1.json`(JSON Schema,字段对齐 injection-fidelity SKILL.md 输出段):
```json
{
  "type": "object",
  "required": ["fidelity","loss1","per_axis_evidence","drift_flag"],
  "properties": {
    "fidelity": {"type": "boolean"},
    "loss1": {"type": "number", "minimum": 0, "maximum": 1},
    "per_axis_evidence": {"type": "object"},
    "drift_flag": {"type": "boolean"},
    "note": {"type": "string"}
  }
}
```
Create `<proj>/schemas/loss2.json`(对齐 ladder-quality-order SKILL.md 输出段):
```json
{
  "type": "object",
  "required": ["tau","monotonicity_pass","endpoint_separation_pass","rigor_floor_flag"],
  "properties": {
    "tau": {"type": "number"},
    "monotonicity_pass": {"type": "boolean"},
    "endpoint_separation_pass": {"type": "boolean"},
    "rigor_floor_flag": {"type": "boolean"},
    "pairwise_log": {"type": "array"}
  }
}
```
Expected: 两 schema 文件就位;`run_codex_loss.py --schema schemas/loss1.json` 可引用。

- [ ] **Step 7: 实现 run_codex_loss.py(起 codex,注入 SKILL.md 全文 + payload)**

Create `<proj>/skills/optimization-loop/scripts/run_codex_loss.py`:
```python
#!/usr/bin/env python3
"""起 codex 算 loss-1(per-run)/ loss-2(per-topic)。注入 SKILL.md 全文(codex 不自动挂载)+ payload。
codex 走 Codex 分组凭证(CODEX_HOME=/workspace/home/loss/.codex,独立 OpenAI 组,换模型族避同源偏置)。"""
import argparse, json, subprocess, os
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--which", choices=["loss1","loss2"], required=True)
    ap.add_argument("--skill", required=True)        # SKILL.md 路径
    ap.add_argument("--payload", required=True)      # transcript(.md)或 6 三元组目录
    ap.add_argument("--schema", required=True)       # loss1.json/loss2.json output-schema
    ap.add_argument("--out", required=True)
    ap.add_argument("--codex-home", default="/workspace/home/loss/.codex")
    a = ap.parse_args()
    skill = Path(a.skill).read_text(encoding="utf-8")
    payload = Path(a.payload).read_text(encoding="utf-8")
    prompt = f"{skill}\n\n# INPUT PAYLOAD\n{payload}\n"
    env = {**os.environ, "CODEX_HOME": a.codex_home}
    # codex exec --output-schema <schema> -o <out> ;prompt 走 stdin
    subprocess.run(["codex","exec","--output-schema",a.schema,"-o",a.out,"-"],
                   input=prompt, text=True, env=env, check=True)

def parse_loss1(out_path):
    """解析 codex loss1 输出 → 保真值。"""
    return json.loads(Path(out_path).read_text())

if __name__ == "__main__":
    main()
```

- [ ] **Step 8: 真模型 e2e — injection-fidelity 喂黄金样例 transcript(R,守 no-fake)**

Create `<proj>/tests/e2e/test_loss_real.py`:
```python
"""R:真 codex。需设备上两组 key 已配(CODEX_HOME 指向 loss config-dir)。CI 无 key 时 skip。"""
import json, os, subprocess, sys
import pytest
from pathlib import Path

CODEX_HOME = os.environ.get("CODEX_HOME","/workspace/home/loss/.codex")
pytestmark = pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"),
                                reason="needs Codex 组 key; real-model e2e (no fake)")

def test_injection_fidelity_real(tmp_path):
    # 黄金样例真 transcript(A 薄片产出的那份;此处用 fixtures/golden-slice 的 e2e 产物)
    transcript = Path("fixtures/golden-slice/transcript.md")
    out = tmp_path/"loss1.json"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/run_codex_loss.py",
        "--which","loss1","--skill","skills/injection-fidelity/SKILL.md",
        "--payload",str(transcript),"--schema","schemas/loss1.json","--out",str(out)])
    r = json.loads(out.read_text())
    assert isinstance(r["fidelity"], bool)          # schema 合
    assert 0.0 <= r["loss1"] <= 1.0                 # 保真数值域
    assert "per_axis_evidence" in r                 # 分轴留证
```

- [ ] **Step 9: 跑真模型 e2e(设备上,key 已配)→ 跑绿 → commit B5**

Run(设备上): `cd <proj> && OPENAI_API_KEY=$OPENAI_API_KEY python -m pytest tests/e2e/test_loss_real.py -v`
Expected: PASS — 真 codex 吐合 schema 的 loss1.json,保真值可解释。无 key 环境 SKIP(不算失败,但**设备上必须真跑过**,守 no-fake)。
```bash
git add skills/injection-fidelity/SKILL.md skills/ladder-quality-order/SKILL.md \
        skills/optimization-loop/scripts/run_codex_loss.py tests/e2e/test_loss_real.py
git commit -m "feat(B5): codex loss skills(injection-fidelity/ladder-quality-order)+ run_codex_loss(真codex) check-blind"
```

> **ladder-quality-order 的 R e2e(loss-2)** 同形:喂 6 档真三元组,验 codex 成对排序 → τ + 端点 + loss2.json schema。它依赖 B7 的 6 档产物,故 loss-2 的真跑放 B7 一并验(B5 先验 loss-1 单 run)。

---

### Task B6: optimizer 大脑 — apply_weight_update + optimization-loop SKILL.md

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/apply_weight_update.py` (P)
- Create: `<proj>/skills/optimization-loop/SKILL.md` (S,厚 skill)
- Create: `<proj>/skills/optimization-loop/references/backprop-heuristic.md` (S)
- Test: `<proj>/tests/test_apply_weight_update.py` (P)

第 9 个叶子 + 大脑程序。B 阶段 apply_weight_update 只测「能正确改 JSON 段 + F1 拷贝模式」(被 backprop 智能驱动是 C)。SKILL.md §loop/§gate/§state/§tools 写全,§backprop 写出但留 C 深验。

- [ ] **Step 1: apply_weight_update 写失败测试(revise 改段 + F1 拷贝 + revision_log)**

Create `<proj>/tests/test_apply_weight_update.py`:
```python
import json, subprocess, sys
from pathlib import Path
from generator.weights import dump_initial

def test_revise_writes_next_batch_and_log(tmp_path):
    wd = tmp_path/"weights"; wd.mkdir(); dump_initial(wd/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0",
        "--target","axis_prose","--key","A1.L0","--new","更强的施压话术","--reason","loss-1挂"])
    nxt = json.loads((wd/"batch-1.json").read_text())
    assert nxt["axis_prose"]["A1"]["L0"] == "更强的施压话术"      # 改了那一个 cell
    log = (wd.parent/"revision_log.jsonl").read_text().splitlines()
    rec = json.loads(log[-1])
    assert rec["target"]=="axis_prose" and rec["key"]=="A1.L0"  # 落 revision_log

def test_f1_copy_mode_byte_identical(tmp_path):
    wd = tmp_path/"weights"; wd.mkdir(); dump_initial(wd/"batch-0.json")
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/apply_weight_update.py",
        "--weights-dir", str(wd), "--batch-id", "batch-0", "--copy"])
    # F1:逐字拷贝,无 revision_log、无 weight_revised
    assert json.loads((wd/"batch-1.json").read_text()) == json.loads((wd/"batch-0.json").read_text())
    assert not (wd.parent/"revision_log.jsonl").exists()        # 拷贝模式不写 log
```

- [ ] **Step 2: 跑红 → 实现 apply_weight_update.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/apply_weight_update.py`:
```python
#!/usr/bin/env python3
"""F2:revise 三权重之一 + 落 revision_log + 写 weights/<batch+1>.json。F1:--copy 逐字拷贝(无 log)。"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from generator import weights as W

def next_id(batch_id):
    return f"batch-{int(batch_id.split('-')[1]) + 1}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True); ap.add_argument("--batch-id", required=True)
    ap.add_argument("--copy", action="store_true")     # F1 拷贝模式
    ap.add_argument("--target"); ap.add_argument("--key"); ap.add_argument("--new"); ap.add_argument("--reason")
    a = ap.parse_args()
    wd = Path(a.weights_dir)
    cur = W.load(wd/f"{a.batch_id}.json")
    nxt_path = wd/f"{next_id(a.batch_id)}.json"
    if a.copy:
        # F1:逐字拷贝,不改、不 log、不 emit weight_revised
        nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2)); return
    rec = W.revise(cur, target=a.target, key=a.key, new=a.new, reason=a.reason)  # 改一段(校验在 weights.revise)
    nxt_path.write_text(json.dumps(cur, ensure_ascii=False, indent=2))
    with open(wd.parent/"revision_log.jsonl","a",encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))         # 供 CC 拼 weight_revised trace 事件

if __name__ == "__main__":
    main()
```
Run → PASS。
```bash
git add skills/optimization-loop/scripts/apply_weight_update.py tests/test_apply_weight_update.py
git commit -m "feat(B6): apply_weight_update — revise段+revision_log(F2) / 逐字拷贝(F1)"
```

- [ ] **Step 3: 写 optimization-loop SKILL.md(厚 skill,§loop/§gate/§backprop/§state/§tools)**

Create `<proj>/skills/optimization-loop/SKILL.md`:
```markdown
---
name: optimization-loop
description: optimizer-cc 的训练主程序。规定 epoch 循环、门控、反向传播、状态落盘、子CC启动。check-blind(W5)。
---

# §loop — 控制流
两层嵌套。LOOP-2(epoch/batch,跑到收敛)包 LOOP-1(48 run = 外层 for topic_i in 0..7 × 内层 for 档 in 0..5):
- 进入 epoch:new_run_id.py 取 run_id → emit run_start → 建 runs/<run_id>/trace.jsonl。
- 进入 batch:取 weights 目录最大编号为 batch_id(不+1;冷启动=batch-0)→ emit batch_start → gen_configs.py 读 weights/<batch_id>.json 造 config。
- for topic_i:emit topic_start → for 档:emit rung_start → [起sim→注入config→sim起exec→注入topic+强制→多轮→concat三元组→run_codex_loss(loss-1)→emit rung_done] → IF 档<5 回跳 else per-topic聚合。
- per-topic 聚合:run_codex_loss(loss-2,吃6档)→ gate_eval(topic)→ emit topic_done → write_dataset(6样本)→ IF topic_i<7 回跳 else END LOOP-1。
- batch 收尾:读8个topic_done的topic_pass → gate_eval(batch)→ emit batch_done → IF 连续3batch过闸:T freeze+converged+run_end / F1 拷贝前进 / F2 §backprop。
每步调哪个 scripts/ 叶子、emit 哪个 trace 事件,严格照本节,不得自作主张。

# §gate — 门控判定(纯算术,gate_eval.py,不调CC/codex)
- per-topic 三项 AND:topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass。
- batch:batch_pass_ratio≥0.80,硬整数线 = ≥7/8 topic 过(6/8=0.75 不过)。
- 收敛:trace 尾部 recent_ratios 末3个全≥0.80。无状态,可从 trace 重建。
- 阈值数值全在 references/gate-thresholds.md。check-blind:只读 fidelity_rate(loss-1)+τ/端点(loss-2)。

# §backprop — 反向传播(唯一留薄段·智能点③·B写出留C深验)
先归因、再动手,一个 batch 只改一个权重。决策表:loss-1挂→①axis_prose;loss-2端点没拉开→先读rigor_floor_flag(真则不动权重)否则①端点cell;loss-2中间撞糊(τ低但端点分得开)→②interp_params;≥4/8双塌→③assembler_params。优先级 loss-1>子类型B>卡整体。归因输入三层(batch_done→topic_done→loss/*.json判词,够判就停)。详细启发式 references/backprop-heuristic.md。W5:归因只读 fidelity/τ/端点 + codex判词;新话术过 leak_audit。

# §state — 跨-batch 状态落盘
"Memory is not trustworthy; disk is the only source of truth." 落盘三件套:trace.jsonl(11事件)/ weights/<batch>.json(快照)/ revision_log.jsonl。每 batch 末固定 /compact 一次,compact 后重载本 skill + 从盘恢复:读 weights/<batch+1>.json(新权重)+ revision_log.jsonl + trace 尾部(recent_ratios/batch_id/末行seq+1续号)。batch_id 取 weights 目录最大编号本身(不+1)。隐私:transcript_path 相对路径,读 log 脚本 --logs-dir 必填。

# §tools — 叶子工具 + 子CC启动
叶子(scripts/):new_run_id / gen_configs / save_transcript(run末一次,--logs-dir必填)/ concat_triple / run_codex_loss / gate_eval / apply_weight_update / write_dataset / trace_emit。三权重本体 axes/interpolator/assembler 留 generator/,gen_configs 调、apply_weight_update 改其 weights JSON 数据段(数据派,源码不动)。
leak_audit 命中:regenerate-then-reaudit,上限 3 次仍命中→硬中断 batch 报警。
子CC启动:父CC 在自己 Bash 工具里直起 IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<角色> bash -lc 'cd <cwd> && claude',正常多轮对话。三铁律:无驱动脚本/不进tmux(仅optimizer用tmux)/每run全新即生即灭。权威 transcript = exec session jsonl。
```

- [ ] **Step 4: 写 backprop-heuristic.md(§backprop 逐行落地,B 写出留 C 深验)**

Create `<proj>/skills/optimization-loop/references/backprop-heuristic.md`:
```markdown
# §backprop 详细启发式(智能点③·一个 batch 只改一个权重)

| # | 判别式(信号读数) | 改法模板 | 优先级 |
| --- | --- | --- | --- |
| 0 | 前置门:本 topic B1 confound-triplet judge 不 flat(FS2-2) | loss-2 信号污染,本 batch 不据 loss-2 改权重;harden judge prompt(不计入"改一权重") | 最先查 |
| 1 | 某 topic fidelity_rate<0.90 或任一档 drift_flag;per_axis_evidence 指出哪轴 observed∉band | revise("axis_prose","<轴>.<等级>",更准/更强施压措辞,reason) | 最高(地基) |
| 2 | endpoint_separation_pass=false:先读 rigor_floor_flag | flag真→报警不动权重(坐标锁死,训不动);flag假→改 axis_prose 的 id0/id5 cell。绝不进② | 次高 |
| 3 | τ<0.7 但 endpoint_separation_pass=true(中间撞糊) | revise("interp_params","<旋钮>",新值,reason),旋钮∈{collision_offset_axis(仅B1/expression),endpoint_spread,granularity_map} | 中 |
| 4 | ≥4/8 topic fidelity 与 τ 双塌(先排除 parser/leak 工具坏) | revise("assembler_params","<旋钮>",新值,reason) | 最低(兜底) |

具体数值门限(band 边界、τ 线、K-allowance、≥4/8)引 gate-thresholds.md。归因输入三层由粗到细:batch_done.{topic_pass_flags,any_rigor_floor} → 挂掉 topic 的 topic_done → 必要时 loss/*.json 判词。够判就停。
```

- [ ] **Step 5: 真模型 e2e — optimization-loop 6-run 编排走通单 topic(R)**

这是 B6 的验收:真 optimizer-CC load skill,按 §loop 把单 topic 6 档跑通(§gate 算出 topic_pass)。**§backprop 不在此深验**(留 C)。落 `<proj>/tests/e2e/test_loop_6run.md`(人工执行清单,真 CC):
```markdown
# B6 e2e:optimization-loop 6-run 单 topic(真 claude/codex)
1. 设备上起 optimizer-CC(占位:本机起 claude load optimization-loop skill)。
2. 喂"跑 batch-0 的 topic-00 全 6 档"指令。
3. 验:trace.jsonl 出现 run_start→batch_start→topic_start→(rung_start→dialogue_turn→rung_done)×6→topic_done。
4. 验:6 个 configs/、6 个 transcripts/、6 个 triples/、6 个 loss1.json 落盘。
5. 验:topic_done 含 tau / monotonicity_pass / endpoint_separation_pass / topic_pass。
6. no-fake:sim/exec/codex 全真进程,产物非桩。
```
Expected: §loop/§gate 编排走通,产物形态对。

- [ ] **Step 6: commit B6**
```bash
git add skills/optimization-loop/SKILL.md \
        skills/optimization-loop/references/backprop-heuristic.md tests/e2e/test_loop_6run.md
git commit -m "feat(B6): optimization-loop 厚skill(§loop/§gate/§state/§tools全 + §backprop写出留C)"
```

---

### Task B7: 黄金样例 6 档 e2e(B 阶段终点验收)

**Files:**
- Create: `<proj>/config/topics.json` (B 阶段单占位 topic)
- Create: `<proj>/tests/e2e/test_golden_6rung.md` (R,人工执行清单)
- 产物落 `runs/`(设备本地、gitignore)

把 Spec A 的「1-run 薄片」长成**单 topic 6 档完整跑**,验 loss-2 单调 τ + 端点分离 + 门控算术。全程真 claude/codex,守 no-fake。

- [ ] **Step 1: 写 config/topics.json(B 阶段单占位 topic)**

Create `<proj>/config/topics.json`:
```json
[
  {
    "topic_id": "topic-00",
    "title_short": "占位:外部 DL 现象最小对照评估",
    "full_text": "研究一个极小的外部 DL 现象:设计一项最小可执行的对照评估。要求 exec 用 formated-specs 做规格、收尾调 formated-results。(B 阶段占位;C 阶段填 8 个真前沿 topic。)",
    "F7_prerequisite": "占位:一个可被挑战的事实前提(C 阶段填真前沿论断)"
  }
]
```
Expected: 单元素数组,四字段齐(`topic_id`/`title_short`/`full_text`/`F7_prerequisite`)。**8 个真 topic 由 Spec C 填**,B 只需占位跑通管线。

- [ ] **Step 2: 写 B7 e2e 执行清单(真 claude/codex,6 档全链)**

Create `<proj>/tests/e2e/test_golden_6rung.md`:
```markdown
# B7 e2e:黄金样例单 topic 6 档(真 claude/codex,守 no-fake)
前置:Spec A 环境就位(四身份可起);B1–B6 全 pytest 绿。

## 跑
1. new_run_id.py 建 runs/<id>/;trace_emit run_start。
2. gen_configs.py 读 weights/batch-0.json(dump_initial 导出)→ 6 config(topic-00 × id0..id5),各过 leak_audit。
3. for 档 in 0..5:
   - 真起 sim(注入 config_full)→ sim 真起 exec(注入 topic + 两条强制)→ 真多轮 → exec 末步 formated-results 围栏块。
   - save_transcript(--logs-dir 指 exec config-dir)→ concat_triple → triples/<sample>.json。
   - run_codex_loss(loss1)→ loss/<sample>.loss1.json;trace_emit rung_done。
4. per-topic 聚合:run_codex_loss(loss2,吃 6 三元组)→ loss/topic-00.loss2.json。
5. gate_eval(topic, fidelity_rate, mono, endpoint)→ topic_pass;trace_emit topic_done。
6. write_dataset × 6 → dataset/topic-00/。

## 验收(B 的核心增益,超 A 薄片)
- [ ] 6 档三元组齐,loss2.json 有 tau(float)。
- [ ] **loss-2 单调**:codex 对打乱 6 档排序,τ 与真实 id 序算出(≥0.7 记 monotonicity_pass)。
- [ ] **端点分离**:id0 vs id5 的 K 次成对判定,endpoint_separation_pass 算出。
- [ ] **门控算术**:gate_eval 三项 AND 出 topic_pass。
- [ ] **隐私**:dataset/ 与 triples/ 无 CC log 绝对路径(grep NO LEAK)。
- [ ] **no-fake**:sim/exec/codex 全真进程,合成的只有 config+topic。

## 不验(留 C)
多 batch、连续 3 过闸、backprop 真改、tmux 长驻、48-run、监督面板。
```

- [ ] **Step 3: 设备上真跑 B7 e2e,逐条验收**

Run(设备上,两组 key 已配): 按 `test_golden_6rung.md` 清单跑完单 topic 6 档。
Expected: 6 档阶梯产出;loss-2 τ 算出;端点分离判出;topic_pass 由 gate_eval 算出;NO LEAK;全真无桩。

- [ ] **Step 4: 全量 pytest 回归 + 隐私扫描 + commit B7**

Run:
```bash
cd <proj> && python -m pytest tests/ -v --ignore=tests/e2e   # 纯函数全绿
grep -rl '/workspace/home/.*/.claude/projects' dataset/ runs/*/triples 2>/dev/null && echo LEAK || echo "NO LEAK"
```
Expected: 所有 pytest PASS;打印 `NO LEAK`。
```bash
git add config/topics.json tests/e2e/test_golden_6rung.md
git commit -m "feat(B7): 黄金样例6档e2e — loss-2单调τ+端点分离+门控算术(真claude/codex)"
```

---

## Self-Review(对照 Spec B 检查)

- **组件清单(§2)覆盖**:三权重体 axes①/interpolator②/assembler③ + cards + leak_audit + weights(B1/B2);9 叶子 new_run_id/gen_configs/save_transcript/concat_triple/run_codex_loss/gate_eval/apply_weight_update/write_dataset/trace_emit(B3/B4/B5/B6);2 codex loss skill(B5);optimization-loop skill(B6)。逐一有 Task,无缺。
- **构建顺序(§4)对齐**:B1 底座→B2 三权重→B3 生成管道→B4 数据收口→B5 loss→B6 大脑→B7 6 档 e2e,Task 编号一一对应。
- **weights schema(§3)硬约束覆盖**:物理隔离 AS-3(B1 test_interp_params_has_no_coord)、revise 白名单(B1 test_revise_rejects_frozen_label)、collision schema 锁(B1 test_collision_offset_rejects_label_axis)、batch-0 dump_initial(B1)。齐。
- **测试矩阵(§5)对齐**:P(weights/三权重/leak/concat/gate/apply/trace/write_dataset 全 pytest)、R(loss1 真 codex B5、6-run 编排 B6、6 档全链 B7)、no-fake 守约。
- **隐私红线(§6)覆盖**:save_transcript --logs-dir 必填(B4 test_logs_dir_required)、write_dataset 白名单硬失败(B4 test_rejects_non_whitelist_field)、key 不进提交物(全程占位)、NO LEAK 扫描(B7)。
- **类型一致性**:`revise(w,target,key,new,reason)` 签名在 B1 定义,B6 apply_weight_update 调用一致;sample 命名 `<batch>-topic<NN>-id<N>` 在 B3/B4/B7 一致;loss1.json/loss2.json schema 在 B5 skill 与 B7 验收一致;trace 公共头 7 字段在 B3 trace_emit 定义、B6 §loop 引用一致。
- **placeholder 扫描**:topics.json 单占位 topic、gen_configs 的占位话术、SKILL.md §backprop "留 C 深验"是**有意的 B/C 边界**,非计划缺口——已注明谁填、何时填。`schemas/loss1.json`/`loss2.json` 的 output-schema 文件在 B5 run_codex_loss 引用——**补:B5 Step 7 落地时需一并创建 `<proj>/schemas/loss1.json` 与 `loss2.json`(JSON Schema,字段对齐 SKILL.md 输出段)**。

## Execution Handoff

见索引 plan `2026-06-07-INDEX-triple-cc-pretrain.md`。B 依赖 A(环境就位);B 全绿(pytest + B7 6 档 e2e)才进 C。
