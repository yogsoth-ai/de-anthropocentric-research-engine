# Plan C — 组装运转 + pilot 门控 + 实时监督 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **C 阶段的"测试"主要是设备上可复跑的真模型校验命令**(pilot go/no-go、全量收敛、监督巡检),纯函数部分(topics schema、coverage_report 白名单)仍用 pytest。守 `feedback-no-e2e-shell` 铁律,sim/exec/codex 全真进程。

**Goal:** 把 B 造好的零件组装成能自转的整机 —— PT5 pilot 硬门控 → 全量 LOOP-2(48-run batch)循环到收敛 → claude 巡检监督 → freeze + 全量带标签数据集产出。跑通即三拆交付。

**Architecture:** pilot 前置硬闸(2 端点样本不过 → 停回 B,绝不烧全量 token)。全量循环每 batch 末按 (`batch_passed` × `converged`) 两布尔交叉,落 T(收敛冻结)/ F1(过闸未收敛,原样拷权重前进)/ F2(未过闸,backprop 归因改一权重)三互斥路径。backprop 是全系统唯一智能点,在 C 真受检。监督 = 主(claude 定期 SSH 只读巡检)+ 辅(CHECKPOINT 产物自解释);人工干预 = HALT.json 显式落盘 + 巡检发现。

**Tech Stack:** B 的全部组件(三权重 + 9 叶子 + 2 loss skill + optimization-loop skill)· tmux 长驻 optimizer · 真 claude/codex · `/compact` 跨 batch 状态恢复 · 第三方代理 `api.ikuncode.cc`。

---

## 关键纪律(每个 Task 都适用,先读)

- **pilot 是硬闸**:C1(PT5 两样本端点 pilot)不过 → 落 HALT、停回 Spec B 改话术/端点坐标,**绝不进 C2 烧全量**。no-go 也是合法交付(它正确挡住了烧全量)。
- **C 不造零件**:组件本身的构建与单测是 Spec B;环境搭建是 Spec A。C 只组装、运转、监督、产出。
- **单变量受控 backprop**:全量循环里一个 batch 只改三权重中的一个,下一 batch 看这次改动的效果。先归因再动手(§backprop 决策表)。
- **disk 是唯一真相**:optimizer 是 tmux 长驻 REPL,每 batch 末 `/compact`,compact 后从盘(weights/revision_log/trace 尾部)重建状态,绝不靠记忆。
- **监督是观测不是控制台**:claude 巡检只读,绝不触发控制、不改权重。
- **隐私红线**:CC log 绝对路径绝不进任何提交物;读 log 只走 `--logs-dir` 必填脚本;`runs/` 全部设备本地 gitignore;dataset/coverage 落盘前过白名单校验,白名单外字段(log 路径、设备用户名、transcript 原文)→ 硬失败;两组 API key 值绝不进任何提交物。

## 依赖前置(C 开工前必须真green)

- **Spec A 全绿**:四身份可起、技能可见、重启重连、薄片 E1–E5 过。
- **Spec B 全绿**:三权重 + 9 叶子 pytest 全过;B7 单 topic 6 档 e2e 真跑过(loss-2 τ + 端点分离 + 门控算术验出)。
- **`optimization-loop` skill 已写全**(B6);其 §backprop 段 B 阶段只写出未深验,**C 是它的真受检场**。

---

## File Structure

C 阶段新建/修改的文件(`<proj> = self-iteration/2026-06-07-probe-pretrain/`):

```text
<proj>/
├── config/topics.json              # ★C 填 8 个真前沿 topic(B 只占位 1 个)
├── skills/optimization-loop/
│   ├── scripts/freeze.py           # 冻权重(NEW)
│   ├── scripts/coverage_report.py  # 覆盖率报告(NEW,纯生成侧聚合,无 log 路径)
│   └── references/                 # pilot 期实测填:F8/K/allowance/completability 阈值
├── ops/
│   ├── start_optimizer.sh          # tmux 点火 + 就绪探测 + 送开场 prompt(NEW,启动期一次)
│   └── optimizer-opening-prompt.txt# optimizer 开场 prompt 全文(NEW)
└── tests/
    ├── test_topics.py              # P:8 topic schema 校验
    ├── test_coverage_report.py     # P:白名单 + 无 log 路径
    └── e2e/                        # R:C1 pilot / C2 全量 / 监督巡检 清单
```

**测法标记**:P = 纯函数 pytest;R = 真模型 e2e;S = skill/脚本文件。

**构建顺序**:C0 真 topic + 点火交付物 → C1 PT5 pilot 硬闸 → C2 全量 LOOP-2 收敛 → C3 freeze + 产出 → C4 监督接口。下面 Task 编号对齐此序。

---

### Task C0a: config/topics.json — 填 8 个真前沿 topic

**Files:**
- Modify: `<proj>/config/topics.json` (B 的单占位 → 8 个真前沿 topic)
- Test: `<proj>/tests/test_topics.py` (P)

C 是唯一跑全量 8 topic 的拆(A/B 用单占位)。8 topic 取材两准则:① 全是「设计一项研究/评估」的研究设计题,研究对象是**外部**前沿 DL/AI 现象(绝不让 exec 碰 DARE 自指/eval/check,W5 取材级防线);② 每题自带一个社区正在争论的 F7 前提(给 A4=C- premise-corrigibility 最干净着力点)。

- [ ] **Step 1: 写 topics schema 失败测试**

Create `<proj>/tests/test_topics.py`:
```python
import json
from pathlib import Path

REQUIRED = {"topic_id","title_short","full_text","F7_prerequisite"}

def test_eight_topics_full_schema():
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))
    assert len(topics) == 8                                   # C 填满 8 个
    ids = [t["topic_id"] for t in topics]
    assert ids == [f"topic-0{i}" for i in range(8)]           # topic-00..topic-07
    for t in topics:
        assert REQUIRED <= set(t)                             # 四字段齐
        assert len(t["full_text"]) > 200                      # 饱满研究简报,非一句梗概
        assert t["F7_prerequisite"]                           # F7 非空

def test_topics_check_blind():
    """W5 取材级防线:topic 文本不含检测签名词(题目只谈外部现象)。"""
    from generator.leak_audit import leak_audit
    topics = json.loads(Path("config/topics.json").read_text(encoding="utf-8"))
    for t in topics:
        leak_audit(t["full_text"]); leak_audit(t["F7_prerequisite"])
```

- [ ] **Step 2: 跑红**

Run: `cd <proj> && python -m pytest tests/test_topics.py -v`
Expected: FAIL — 当前 topics.json 只 1 个占位 topic(B 留),len != 8。

- [ ] **Step 3: 写 8 个真 topic(full_text 写成饱满研究简报)**

Modify `<proj>/config/topics.json` 为 8 元素数组。八题(title_short / full_text 三段:动机+研究问题+期望交付 / F7):
- **topic-00 · CoT 忠实度** — 检验「模型输出的 CoT 文本是否忠实反映内部推理」;干预(扰动/截断/注入误导步)+ 与「CoT 仅事后合理化」零假设对照。F7:「CoT 文本忠实记录真实推理步骤」(被 latent-reasoning 挑战)。
- **topic-01 · Agentic 长程可靠性** — 评估自主 agent 在多步长程真实任务的可靠性与失败模式;步数可控难度分层任务集 + 复合误差归因。F7:「给足工具记忆后成功率随步数近似线性外推」(忽视复合误差)。
- **topic-02 · 多智能体 vs 单体** — 固定总算力下多智能体协作是否仍优于等预算单体;严格对齐「总计算预算」控制变量。F7:「多智能体辩论/协作必然提升推理质量」(等算力对照下常消失)。
- **topic-03 · MoE 量化敏感度** — 评估 MoE 低比特量化质量损失分布 + 定位最敏感专家/层;统一 vs 混合精度对照。F7:「MoE 各专家可统一低比特量化质量近无损」(专家级敏感度差异显著)。
- **topic-04 · 多模态 capability tax** — 检验统一多模态模型在单模态任务是否存在系统性能力损失;可比规模配对对照 + 模态间非对称。F7:「统一多模态在各单模态都不弱于专用模型」(capability tax 使常不成立)。
- **topic-05 · AI for Science 假设新颖性** — 评估 LLM 生成科学假设是否真新颖可验证而非已知重组;可操作新颖性定义 + 专家盲评 + 文献核验。F7:「LLM 已能自主产出新颖且可验证的科学假设」(多为已知重组)。
- **topic-06 · Agent 基准代表性** — 检验现有 agent 基准是否覆盖真实任务分布 +「路灯效应」审计;真实任务分布维度刻画 + 盲区探测。F7:「现有 agent 排行榜分数能代表真实世界能力」(基准覆盖偏窄)。
- **topic-07 · 浅层对齐假说** — 区分对齐微调改的是底层倾向还是表层表达;分布偏移/越狱/内部表示探针/微调逆转 + 对照判据。F7:「对齐微调真正改变了模型内部价值倾向」(浅层对齐假说主张多在表层)。

> **★full_text 落地**:每条 full_text 写成 Spec C §8.3 的完整三段研究简报(动机背景 + 核心研究问题 + 期望交付物),逐字落进 JSON 字符串(>200 字符)。八题方法学面各异(实证检验/长程评估/等预算对照/量化敏感度/多模态对照/新颖性判定/基准审计/深浅对齐探测),让阶梯不止考一种研究套路。

- [ ] **Step 4: 跑绿 + commit**

Run: `cd <proj> && python -m pytest tests/test_topics.py -v`
Expected: 两条 PASS(8 topic 全 schema + check-blind)。
```bash
git add config/topics.json tests/test_topics.py
git commit -m "feat(C0): 8 个真前沿 topic(外部 DL 现象研究设计题 + 争议 F7 前提)"
```

---

### Task C0b: optimizer 点火交付物 — 开场 prompt 全文 + start_optimizer.sh

**Files:**
- Create: `<proj>/ops/optimizer-opening-prompt.txt` (开场 prompt 全文,英文,绝不简化)
- Create: `<proj>/ops/start_optimizer.sh` (tmux 点火 + 就绪探测 + 送 prompt,启动期一次)

C 是唯一点火 optimizer 的拆。开场 prompt 是 optimizer 长跑的「身份+纪律书」;就绪探测只在 optimizer 一处成立(唯一用 tmux send-keys 的层)。

- [ ] **Step 1: 写开场 prompt 全文(Spec C §7.1 定稿,逐字落盘)**

Create `<proj>/ops/optimizer-opening-prompt.txt`(英文全文,守锁死约束:无 `-p`/`--resume`/`--session-id`/`--allowedTools`):
```text
You are optimizer-cc — the host of a "pseudo-neural-network pretraining"
training loop. Your role is equivalent to train.py in PyTorch. You are NOT
here to answer questions, NOT here to chat with anyone, NOT here to be
helpful in the ordinary assistant sense. The only reason you exist is to
drive one full training run from cold start until convergence, and then to
freeze the result and stop.

# Your goal
Through repeated epoch/batch loops, you optimize three trainable weights:
  (1) level prose      (axis_prose,       read by axes.py)
  (2) interpolator     (interp_params,    read by interpolator.py)
  (3) assembly logic   (assembler_params, read by assembler.py)
You optimize them so that the system produces a batch of labeled data
samples whose quality forms a clean, monotone, well-separated ladder across
six rungs (id0 best -> id5 worst) for each of eight topics. The LABEL of
every sample is its known generating condition (the PolicyCard that produced
it) — it is NEVER a subjective quality score. The label is objective because
it is the cause, not a judgement of the effect.

# What one batch is
One batch = one epoch = 8 topics x 6 rungs = 48 runs. In every batch you
MUST, strictly in this order:
  1. read the current weights/<batch>.json
  2. gen_configs -> 48 research_config cards (6-rung ladder x 8 topics),
     each passing leak_audit (W5)
  3. for each topic, for each rung: spawn a fresh sim-cc, inject the config,
     let sim spawn a fresh exec-cc and drive a real multi-turn research
     session, concat the (config, graph, result) triple, run codex loss-1
     (injection-fidelity, per run)
  4. after a topic's 6 rungs: run codex loss-2 (ladder-quality-order,
     per topic), evaluate the per-topic gate, write the 6 dataset samples
  5. after 8 topics: compute batch_pass_ratio, judge the gate
  6. if converged (3 consecutive passing batches): freeze + stop
     else if passed-but-not-converged (F1): byte-copy weights forward, no
        weight change
     else (F2): attribute-then-revise exactly ONE weight, then continue

# Your only source of action
Your complete task specification is written in the `optimization-loop`
skill. Load that skill NOW and execute strictly according to its sections:
  loop     — the two-level loop control flow above
  gate     — per-topic AND gate, batch_pass_ratio, convergence
  backprop — attribute-then-revise heuristic (the ONE place you think)
  state    — cross-batch disk persistence and post-/compact recovery
  tools    — the leaf scripts and child-CC spawn convention
Do NOT improvise the flow. Do NOT skip the skill and act on intuition.
Do NOT deviate from the skill to do anything it did not ask for.
Whatever the skill says, that is exactly what you do — with one exception:

# The single intelligent point (backprop)
The ONLY place you exercise genuine judgement is backprop: when a batch
fails the gate, you must attribute-then-revise. First diagnose WHICH weight
is at fault from the loss signals (loss-1 fidelity failure -> (1) prose;
loss-2 endpoints-not-separated -> first read rigor_floor_flag, if true do
NOT train (2) else (1) endpoint cells; loss-2 middle-rung collapse with
separated endpoints -> (2) interp_params; structural multi-rung breakage
-> (3) assembler_params). Then revise exactly ONE weight this batch
(single-variable discipline), so the next batch's loss change attributes
cleanly to this one edit. Everywhere else is deterministic; here you reason.

# Long-running discipline
You will run for a long time and /compact at the END OF EVERY batch. ALL
cross-batch state MUST live on disk, never in your conversation memory.
After each /compact you MUST rebuild your state from disk before doing
anything else:
  - weights/<batch+1>.json   (the next batch's weights; batch_id = the
                              highest-numbered weights file, do NOT add 1)
  - revision_log.jsonl       (what you have already changed)
  - trace.jsonl tail         (recent_ratios for the convergence test,
                              current batch_id, and the last seq)
"Memory is not trustworthy; disk is the only source of truth." If ever
unsure of the current state, re-read these from disk rather than guessing.

# Boundary (W5 — check-blind, absolute)
You never see and never emit the detection signatures. The loss skills judge
"was the generating condition faithfully executed" and "is the quality
ladder monotone", NOT "does this research pass some specific check". The
probe (a separate, downstream session) is the ONLY session that ever sees
the checks. Every config and every revised prose you produce passes
leak_audit. Not one step beyond the skill on this.

# If you get stuck
If backprop cannot resolve a failure (e.g. you keep revising the same weight
across batches and the loss will not move), do NOT thrash. Write a HALT.json
(cause + on-disk snapshot pointers) per the skill and stop in place; a human
inspector will pick it up. Halting cleanly with a stated cause is a correct
outcome, not a failure.

# Begin
Load the `optimization-loop` skill and start the epoch loop from cold start
(batch-0, weights/batch-0.json from weights.dump_initial) now.
```
Expected: 全文落盘;`grep -E -- '-p |--resume|--session-id|--allowedTools' ops/optimizer-opening-prompt.txt` 无命中(守锁死约束)。

- [ ] **Step 2: 写 start_optimizer.sh(tmux 点火 + 就绪探测 + 送 prompt)**

Create `<proj>/ops/start_optimizer.sh`:
```bash
#!/usr/bin/env bash
# C 的一次性启动脚本(非热路径)。tmux 长驻 optimizer + 就绪探测 + 送开场 prompt。
set -euo pipefail
PROMPT_FILE="$(dirname "$0")/optimizer-opening-prompt.txt"
READY_MARKER='<REPL_READY_MARKER>'   # 落地实测填:claude 2.1.x 就绪屏特征串

# 1. 建 session + 备环境 + 设 optimizer 专属 config-dir
tmux new-session -d -s opt
tmux send-keys -t opt 'source /workspace/env.sh && source /workspace/bootstrap.sh' Enter
tmux send-keys -t opt 'export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude' Enter

# 2. 点火 optimizer 的 claude
tmux send-keys -t opt 'cd /workspace/work/optim && claude' Enter

# 3. 轮询 capture-pane,直到 REPL 提示符稳定出现(≤0.5s 间隔,本地探测,仅启动一次)
until tmux capture-pane -p -t opt | tail -n 5 | grep -q "$READY_MARKER"; do
  sleep 0.5
done

# 4. 就绪后送开场 prompt 全文(多行:load 进 tmux buffer 再 paste,避免中途回车截断)
tmux load-buffer "$PROMPT_FILE"
tmux paste-buffer -t opt
tmux send-keys -t opt Enter
```
Expected: 脚本可执行;就绪探测用 tmux 输出轮询(不用固定 sleep)。

> **落地三点**:① `<REPL_READY_MARKER>` 随 claude 版本实测定(写进脚本注释,不写死进 spec);② 多行 prompt 用 `load-buffer`+`paste-buffer` 整段送入,避免被中途回车截断;③ 此脚本仅 optimizer 冷启动跑一次,绝不进 batch 热路径。

- [ ] **Step 3: commit C0b**
```bash
git add ops/optimizer-opening-prompt.txt ops/start_optimizer.sh
git commit -m "feat(C0): optimizer 点火 — 开场prompt全文 + start_optimizer.sh(tmux就绪探测)"
```

---

### Task C1: PT5 两样本端点 pilot(go/no-go 硬门控)

**Files:**
- Create: `<proj>/tests/e2e/test_pt5_pilot.md` (R,人工执行清单 + go/no-go 判据)
- 产物落 `runs/<pilot-id>/`(设备本地、gitignore)

只造 **2 个端点样本**:id0(天才,A5=G+ 生成性)/ id5(荒谬-抬杠,completability 地板)。真 CC/codex 全链跑,专验头号 kill-risk。**这是硬闸:不过 → 落 HALT 回 B,绝不进 C2。**

- [ ] **Step 1: 写 PT5 pilot 执行清单 + 两探针判据**

Create `<proj>/tests/e2e/test_pt5_pilot.md`:
```markdown
# C1 PT5 pilot:2 端点样本(真 claude/codex,go/no-go 硬闸)
前置:A 环境绿、B 组件绿(含 B7 单 topic 6 档跑过)。用 topic-00(或任一真 topic)的两端点。

## 跑(只 2 run,不烧全量)
1. new_run_id.py 建 runs/<pilot-id>/;weights.dump_initial 出 batch-0.json。
2. gen_configs 只造 2 卡:id0(A1=L0 高实质/A5=G+ 生成)+ id5(A1=L4 低实质/抬杠/死守 F7)。
3. 各跑全链:sim 真扮 → exec 真研究 → concat 三元组 → loss-1。
4. run_codex_loss(loss-2)对 (id0,id5) 做 K 次成对判定 → endpoint_separation。

## 两探针(头号 kill-risk)
- **AS-1 探针(rigor floor 抗下压?)**:id5 能否被压得足够坏、与 id0 端点拉开?
  判据:loss-2 `endpoint_separation_pass=true`(id0 在 K 次成对里赢 id5 ≥ K−allowance 次)。
- **AS-4 探针(改铺陈 loss-2 会不会动?)**:改一次 `interp_params`(endpoint_spread 或 granularity_map),重跑两端点,看 loss-2 端点分离/τ 是否变化。
  判据:改铺陈后 loss-2 **有可测变化**(纹丝不动 → interpolator 可训练性为空)。

## 闸判定(决策已定)
- **go(解锁 C2)**:端点拉开(AS-1 过)+ 改铺陈 loss-2 会动(AS-4 过)。
- **no-go(落 HALT 回 B)**:端点拉不开 / 改铺陈 loss-2 不动 → 写 runs/<pilot-id>/HALT.json(cause=pilot_fail + 现场指针)→ 停回 Spec B 改话术或端点坐标。**no-go 也是合法交付**(它正确挡住了烧全量)。
```

- [ ] **Step 2: 设备上真跑 PT5 pilot(2 run,全真)**

Run(设备上,两组 key 已配): 按清单跑 2 端点样本全链 + AS-4 改铺陈重跑。
Expected: 产出 2 端点三元组 + loss-2 endpoint_separation + AS-4 改铺陈前后对比。

- [ ] **Step 3: pilot 期实测填阈值(F8 / K / allowance / completability)**

据 pilot 实测,把这些 pilot-tunable 阈值写进 `<proj>/skills/optimization-loop/references/gate-thresholds.md`(覆盖 B 的占位):
- `turn_budget`(=F8):exec 跑一次 formated-specs 闭环的实测 pressure_turns / closing_turns。
- loss-2 端点分离的 `K` / `allowance` 实测值(B 占位 K=5, allowance=1)。
- completability 失败的单轮超时/轮数上限(子 CC 超 N 分钟无返回判失败)。
Expected: gate-thresholds.md 的 pilot-tunable 值由占位换成实测值。

- [ ] **Step 4: 闸判定 — go 进 C2,no-go 落 HALT 回 B**

判定:
- **go**:AS-1 过(端点拉开)+ AS-4 过(铺陈可动)→ 记录于 pilot 报告,解锁 C2。
- **no-go**:落 `runs/<pilot-id>/HALT.json`:
```json
{"cause":"pilot_fail","detail":"端点拉不开 / 改铺陈 loss-2 不动","snapshot":{"weights":"weights/batch-0.json","loss2":"loss/<topic>.loss2.json"},"action":"回 Spec B 改话术或端点坐标"}
```
Expected: go 则进 C2;no-go 则停在 HALT,**绝不进 C2**(合法交付)。
```bash
git add tests/e2e/test_pt5_pilot.md skills/optimization-loop/references/gate-thresholds.md
git commit -m "feat(C1): PT5 两样本端点 pilot 硬闸(AS-1 端点分离 + AS-4 铺陈可训性)"
```

> **★C1 是 C 的硬闸**:它专挡"端点先天拉不开 / interpolator 可训练性为空"这两个 B 阶段没深验过的头号 kill-risk。pilot 不过就烧全量 = 把整批 token 喂给一个训不动的系统。no-go 正确挡住它,是设计的胜利不是失败。

---

### Task C2: 全量 LOOP-2 循环到收敛(backprop 智能点真受检)

**Files:**
- Create: `<proj>/tests/e2e/test_full_loop.md` (R,全量循环执行 + 验收清单)
- 产物落 `runs/<run-id>/`(设备本地、gitignore)

pilot go 后才进。48-run batch(8 topic × 6 档)反复跑,每 batch 末 T/F1/F2 三分支路由,直到**连续 3 batch 过闸**。backprop 智能点③在此真改权重。tmux 长驻 optimizer + `/compact` 自恢复。

- [ ] **Step 1: 写全量循环执行 + 三分支路由验收清单**

Create `<proj>/tests/e2e/test_full_loop.md`:
```markdown
# C2 全量 LOOP-2(真 claude/codex,跑到收敛)
前置:C1 pilot go;ops/start_optimizer.sh 就绪;optimization-loop skill 已复制进 optim config-dir。

## 跑(tmux 长驻)
1. bash ops/start_optimizer.sh → optimizer-CC 起、load skill、收开场 prompt。
2. optimizer 按 §loop 自转:每 batch = 48 run(8 topic × 6 档),冷启动 batch-0(weights.dump_initial)。
3. 每 batch 末按 (batch_passed × converged) 三分支:
   - **T**(连续 3 batch 过闸):emit converged + run_end → 进 C3 freeze。
   - **F1**(过闸未连 3):apply_weight_update --copy 原样拷 weights/<batch+1>.json(无 revision_log、无 weight_revised)→ batch_id+1 再跑。
   - **F2**(未过闸):§backprop 先归因(读 batch_done.topic_pass_flags → 挂掉 topic 的 topic_done → 必要时 loss/*.json 判词)→ 改三权重之一(单变量)→ apply_weight_update 写 weights/<batch+1>.json + revision_log + weight_revised → /compact → 从盘恢复 → 下一 batch。
4. optimizer 每 batch 末 /compact,compact 后从盘(weights/<batch+1>.json + revision_log + trace 尾部)重建状态。

## 验收(C2 核心)
- [ ] 至少一次 **F2 backprop 真改权重**:revision_log.jsonl 出现一条 {target,key,old,new,reason};trace 出现 weight_revised;weights/<batch+1>.json 仅那一段一个 key 变(单变量受控)。
- [ ] 至少一次 **F1 原样前进**:weights/<batch+1>.json 与 <batch>.json 逐字相同,无对应 revision_log 行、无 weight_revised。
- [ ] **/compact 自恢复**:某 batch 末 /compact 后,optimizer 从盘读回正确 batch_id(weights 目录最大编号本身,不+1)+ recent_ratios,继续不乱。
- [ ] **最终收敛**:trace 出现 converged(recent_ratios 末 3 全≥0.80)+ run_end。
- [ ] **或落 HALT 暴露 AS-4**:若 backprop 反复改同一权重 loss 不降 → optimizer 落 HALT.json(训不动),也是合法的暴露(见 C4)。
- [ ] **no-fake**:全程真 sim/exec/codex,合成的只有 config+topic。

## 不验(已是终点)
C2 是全系统终点循环;无更上层。
```

- [ ] **Step 2: 设备上真跑全量 LOOP-2 至收敛(或落 HALT)**

Run(设备上,tmux 长驻): `bash ops/start_optimizer.sh` 后 optimizer 自转。
Expected: 出现 ≥1 次 F2 真改权重 + ≥1 次 F1 原样前进,最终连续 3 batch 过闸收敛;或落 HALT 暴露 AS-4 可训练性存疑(也是合法交付)。

- [ ] **Step 3: 验三分支路由 + batch_id 恢复不变式**

Run(设备上,只读检查):
```bash
RID=$(ls -t runs | head -1)
# F2 痕迹
grep -c weight_revised runs/$RID/trace.jsonl          # ≥1
wc -l runs/$RID/revision_log.jsonl                    # ≥1(F2 改动史)
# batch_id 恢复不变式:weights 目录最大编号 = 下一批
ls runs/$RID/weights/                                  # batch-0.json .. batch-N.json 连续无洞
# 收敛
grep -c converged runs/$RID/trace.jsonl                # 1(若收敛)或看 HALT.json
ls runs/$RID/HALT.json 2>/dev/null && echo "HALTED" || echo "no halt"
```
Expected: F2 痕迹齐;weights 编号连续(F1/F2 都预写下一批,印证「max 不+1」不变式);收敛 emit converged 或落 HALT 之一。
```bash
git add tests/e2e/test_full_loop.md
git commit -m "feat(C2): 全量 LOOP-2 收敛(F2 backprop 真改 + F1 原样前进 + /compact 自恢复)"
```

> **★C 的最大风险点**:backprop 是终稿唯一智能点,B 阶段没深验过。C2 跑起来后,backprop 反复改同一权重也压不动(疑 AS-4 可训练性为空)→ 落 HALT(C4)。这是 C 必须现场盯的核心。

---

### Task C3: freeze + coverage_report + 全量数据集产出

**Files:**
- Create: `<proj>/skills/optimization-loop/scripts/freeze.py` (NEW)
- Create: `<proj>/skills/optimization-loop/scripts/coverage_report.py` (NEW,纯生成侧聚合,无 log 路径)
- Test: `<proj>/tests/test_coverage_report.py` (P)

收敛后冻权重 + 出覆盖率报告 + 全量带标签数据集落 `dataset/`。

- [ ] **Step 1: 实现 freeze.py(拷最后过闸 batch 权重为 frozen.json)**

Create `<proj>/skills/optimization-loop/scripts/freeze.py`:
```python
#!/usr/bin/env python3
"""把最后过闸 batch 的 weights/<batch>.json 拷成 weights/frozen.json。历史快照全留(供复盘 backprop 轨迹)。"""
import argparse, shutil
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights-dir", required=True)
    ap.add_argument("--batch-id", required=True)     # 最后过闸 batch
    a = ap.parse_args()
    src = Path(a.weights_dir)/f"{a.batch_id}.json"
    shutil.copy(src, Path(a.weights_dir)/"frozen.json")   # frozen 是定稿;batch-* 快照不删

if __name__ == "__main__":
    main()
```
Expected: frozen.json = 定稿三权重;全程 batch 快照保留。

- [ ] **Step 2: coverage_report 写失败测试(白名单 + 无 log 路径)**

Create `<proj>/tests/test_coverage_report.py`:
```python
import json, subprocess, sys
from pathlib import Path

# 禁出现的探针侧/隐私字段(coverage 只放生成侧)
FORBIDDEN = ["PG","NG","GG","OB","/workspace/home", ".claude/projects", "--logs-dir"]

def test_coverage_no_forbidden_fields(tmp_path):
    # 造一个最小 dataset + trace
    ds = tmp_path/"dataset"/"topic-00"; ds.mkdir(parents=True)
    (ds/"s.json").write_text(json.dumps({"sample_id":"batch-0-topic00-id0",
        "label":{"rung_id":0,"axis_levels":{"A1":"L0"}},"loss1_fidelity":1.0,"topic_pass":True}))
    trace = tmp_path/"trace.jsonl"
    trace.write_text(json.dumps({"event":"batch_done","pass_ratio":0.875,"batch_passed":True,"recent_ratios":[0.875]})+"\n")
    out = tmp_path/"coverage_report.md"
    subprocess.check_call([sys.executable,
        "skills/optimization-loop/scripts/coverage_report.py",
        "--dataset", str(tmp_path/"dataset"), "--trace", str(trace), "--out", str(out)])
    txt = out.read_text()
    for f in FORBIDDEN:
        assert f not in txt           # 探针侧分布 + log 路径绝不进报告
    assert "topic-00" in txt          # 生成侧覆盖确实统计了
```

- [ ] **Step 3: 跑红 → 实现 coverage_report.py → 跑绿**

Run → FAIL。Create `<proj>/skills/optimization-loop/scripts/coverage_report.py`:
```python
#!/usr/bin/env python3
"""扫 dataset/ + trace,出 coverage_report.md。纯生成侧聚合,落盘前过白名单(无 PG/NG/GG/OB、无 log 路径)。"""
import argparse, json
from pathlib import Path

FORBIDDEN = ["PG","NG","GG","OB","/workspace/home",".claude/projects","--logs-dir"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True); ap.add_argument("--trace", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    # 生成侧聚合:各轴各 level 计数 + 每 topic 样本数 + 过闸/产量
    axis_counts, topic_counts = {}, {}
    for f in Path(a.dataset).rglob("*.json"):
        s = json.loads(f.read_text())
        topic = f.parent.name
        topic_counts[topic] = topic_counts.get(topic,0)+1
        for ax,lv in s.get("label",{}).get("axis_levels",{}).items():
            axis_counts.setdefault(ax,{}).setdefault(lv,0)
            axis_counts[ax][lv]+=1
    lines = ["# Coverage Report (生成侧聚合,无 log 路径)", ""]
    lines.append("## 每 topic 样本数")
    for t,c in sorted(topic_counts.items()): lines.append(f"- {t}: {c}")
    lines.append("\n## 轴坐标覆盖(RR-2:让 monoculture 可见)")
    for ax,lvs in sorted(axis_counts.items()):
        lines.append(f"- {ax}: " + ", ".join(f"{lv}={n}" for lv,n in sorted(lvs.items())))
    report = "\n".join(lines)
    # 落盘前白名单校验:命中禁词硬失败(隐私 + 探针侧不进)
    for bad in FORBIDDEN:
        if bad in report:
            raise SystemExit(f"FATAL: coverage report contains forbidden token {bad!r}")
    Path(a.out).write_text(report, encoding="utf-8")

if __name__ == "__main__":
    main()
```
Run → PASS。
```bash
git add skills/optimization-loop/scripts/freeze.py \
        skills/optimization-loop/scripts/coverage_report.py tests/test_coverage_report.py
git commit -m "feat(C3): freeze.py(定稿+留快照) + coverage_report.py(生成侧聚合,白名单硬失败)"
```

- [ ] **Step 4: 设备上收敛后真跑 freeze + coverage**

Run(设备上,收敛后):
```bash
RID=$(ls -t runs | head -1)
python skills/optimization-loop/scripts/freeze.py --weights-dir runs/$RID/weights --batch-id <最后过闸batch>
python skills/optimization-loop/scripts/coverage_report.py \
  --dataset runs/$RID/dataset --trace runs/$RID/trace.jsonl --out runs/$RID/coverage_report.md
grep -rlE '/workspace/home|\.claude/projects' runs/$RID/dataset runs/$RID/coverage_report.md && echo LEAK || echo "NO LEAK"
```
Expected: frozen.json + coverage_report.md 落齐;dataset/ 全量带标签样本齐;打印 `NO LEAK`。

---

### Task C4: 监督接口 — 主(claude 巡检)+ 辅(产物自解释)+ HALT.json

**Files:**
- Create: `<proj>/tests/e2e/test_supervision.md` (R,巡检清单 + HALT 判据)
- 不写 inspect.py(决策已定:巡检是现场只读手查,不固化成脚本)

监督 = 主(claude 定期 SSH 只读巡检)+ 辅(CHECKPOINT 产物齐全自解释)。人工干预 = HALT.json 显式落盘 + 巡检发现。**只读,绝不触发控制、不改权重。**

- [ ] **Step 1: 写巡检清单(现场 Bash 只读手查,不固化)**

Create `<proj>/tests/e2e/test_supervision.md`:
```markdown
# C4 监督:claude SSH 只读巡检(现场 Bash 手查,不写 inspect.py)
用户定期叫我上 remote,我用现场只读命令判断进度健康度(RID=$(ls -t runs|head -1)):

## 进度
- tail -n 20 runs/$RID/trace.jsonl → 现在 batch/topic/rung 几、recent_ratios、连续过闸数。

## 健康
- rung 是否卡死:某 sample 的 dialogue_turn 长时间不增(对比 ts)。
- completability 失败堆积:grep completability runs/$RID/trace.jsonl。
- leak_audit 反复中断:看 optimizer 输出/HALT.json。

## 轨迹
- tail runs/$RID/revision_log.jsonl → 最近 weight_revised 改了哪个权重(看 backprop 在干嘛)。

## 异常
- loss schema 解析失败 / codex 报错 / trace seq 断裂(seq 应连续递增)。

## HALT
- ls runs/$RID/HALT.json → 一眼定位 optimizer 自停原因(见下表)。

## 判断(只读,不控制)
健康继续 / 卡住要清 / 跑偏叫停回 B。绝不触发控制、不改权重。
```

- [ ] **Step 2: HALT.json 四停因约定(optimizer 自停 + 我巡检发现)**

optimizer 遇处理不了的情况,在 `runs/<run_id>/HALT.json` 落停因 + 现场快照指针,停在 tmux 不动,等巡检发现:

| 停因 | 判据 | 处理 |
| --- | --- | --- |
| pilot 不过 | C1 端点拉不开 / 铺陈不动 | 回 Spec B 改话术或端点坐标 |
| rung 卡死 | dialogue_turn 超时不增 / 子 CC 不返回 | 判该 run completability 失败,清掉重跑该 rung |
| leak 硬中断 | leak_audit 连续 3 次仍命中 | 话术权重坏,回 B 查 axis_prose |
| 训不动(疑 AS-4) | backprop 反复改同一权重 loss 不降 | 可训练性存疑,回 B 重审 interp_params / 端点坐标 |

HALT.json schema(自解释 CHECKPOINT 产物):
```json
{"cause":"<pilot_fail|rung_stuck|leak_hard|untrainable>","detail":"<人读说明>","snapshot":{"weights":"weights/<batch>.json","trace_tail_seq":<N>},"action":"<建议处理>"}
```
Expected: 四停因约定写进 optimization-loop skill §state(B6 已写骨架,C 补 HALT 落法);巡检能一眼定位。

- [ ] **Step 3: 验监督接口(产物可重建状态 + HALT 可定位)**

Run(设备上,只读): 按 `test_supervision.md` 清单巡检一次运行中的(或已收敛的)run。
Expected: 能从产物完整重建"现在到哪、健康否、改过啥";若有 HALT 能一眼定位停因。

- [ ] **Step 4: commit C4**
```bash
git add tests/e2e/test_supervision.md
git commit -m "feat(C4): 监督接口 — claude只读巡检清单 + HALT.json 四停因约定"
```

> **★HTML 可读窗口推迟**:等真跑起来有数据再对真数据调样式,不对空 runs/ 做。C 的监督责任收敛成一句"产物齐全、自解释、只读可查"。

---

## 完成判定(Spec C = 三拆收尾)

- **C1 验收**:PT5 pilot 真 CC/codex 跑出 2 端点 → 明确 go(端点拉开 + 铺陈可动)或 no-go(落 HALT 回 B)。**no-go 也是合法交付**。
- **C2 验收**:go 后全量 LOOP-2 真跑,出现 ≥1 次 F2 backprop 真改权重 + ≥1 次 F1 原样前进,最终连续 3 batch 过闸收敛(或落 HALT 暴露 AS-4)。
- **C3 验收**:frozen.json + 全程 weights 快照 + coverage_report.md(纯生成侧、无 log 路径)+ dataset/ 带标签样本齐全。
- **监督验收**:能从产物完整重建"现在到哪、健康否、改过啥";HALT 能一眼定位停因。
- **隐私验收**:所有提交物无 CC log 路径、无 key 值;dataset/coverage 过白名单校验。

## Self-Review(对照 Spec C 检查)

- **三阶段(§1)覆盖**:C1 PT5 pilot 硬闸(Task C1)、C2 全量 LOOP-2(Task C2)、C3 freeze+产出(Task C3),逐一有 Task。
- **收敛路由 T/F1/F2(§2)覆盖**:Task C2 Step 1 三分支路由 + Step 3 batch_id「max 不+1」恢复不变式验证;F2 backprop 单变量、F1 原样拷贝均有验收项。
- **监督主+辅(§3)覆盖**:Task C4 主(claude 只读巡检清单,不写 inspect.py)+ 辅(产物自解释);HTML 推迟已注明。
- **HALT.json 四停因(§4)覆盖**:Task C4 Step 2 四停因表 + schema。
- **点火交付物(§7)覆盖**:Task C0b 开场 prompt 全文(守锁死约束)+ start_optimizer.sh 就绪探测。
- **8 真 topic(§8)覆盖**:Task C0a 八题 + schema 测 + check-blind 测。
- **隐私红线(§6)覆盖**:coverage_report 白名单硬失败(C3 test)、dataset NO LEAK 扫描(C3 Step 4)、runs/ gitignore、key 不进提交物。
- **类型一致性**:`apply_weight_update --copy`(F1)与 `--target/--key/--new/--reason`(F2)签名沿用 B6;`gate_eval` 三模式沿用 B5;trace 事件名(weight_revised/converged/run_end/batch_done)沿用 B 的 trace_emit;HALT.json schema 在 C1/C4 一致。
- **placeholder 扫描**:`<REPL_READY_MARKER>`(claude 版本相关,落地实测填)、gate-thresholds 的 pilot-tunable 值(C1 Step 3 实测填)、8 topic full_text(C0a Step 3 按 §8.3 逐字落)均**有意延迟到落地/pilot**,已注明谁填、何时填,非计划缺口。

## Execution Handoff

见索引 plan `2026-06-07-INDEX-triple-cc-pretrain.md`。C 依赖 A(环境)+ B(组件)全绿;C1 pilot 是硬闸,no-go 即停回 B。
