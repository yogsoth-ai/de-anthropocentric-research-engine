# 索引 — Triple-CC 伪神经网络预训练(三拆 A/B/C)Implementation Plan Index

> **For agentic workers:** 本文件是**导航索引**,不含可执行步骤。三个具体 plan 各自用 superpowers:subagent-driven-development(推荐)或 superpowers:executing-plans 逐 Task 实现。**严格按 A→B→C 顺序**,前一拆全绿才进下一拆。

**Goal:** 在租来的 RunPod 设备上,从裸机搭起一套「optimizer / sim / exec / loss 四 CC 身份协同」的伪神经网络预训练系统,跑到收敛、产出带标签的研究质量阶梯数据集。整套工程拆成三个各自可独立交付的 plan。

**Architecture:** 三层 CC(optimizer 驱动 → sim 模拟用户 → exec 跑 DARE 研究)+ codex 算 loss(换模型族避同源偏置)。数据派三权重(话术①/插值②/组装③)是 JSON 数据段,`.py` 只读不改。optimizer 是 tmux 长驻 train.py;一个 epoch = 8 topic × 6 档 = 48 run;门控算术判过闸,backprop 是全系统唯一智能点。全程 check-blind(W5)+ 隐私红线(CC log 路径、key 值绝不进提交物)。

**Tech Stack:** Ubuntu 22.04 · Python 3.11 + pytest · 真 claude/codex CLI · tmux · node(装 /workspace)· 第三方代理 `api.ikuncode.cc`。

---

## 三个 plan(严格按序)

| 拆 | Plan 文件 | 管什么 | 终点验收 |
| --- | --- | --- | --- |
| **A** | `2026-06-07-A-remote-env-from-scratch.md` | 远程环境从零搭:裸机 → 四身份可启动 + 重启不丢 | 冒烟 S1–S4 全过 + 真实纵向薄片 e2e E1–E5(1 run,全真 CC/codex) |
| **B** | `2026-06-07-B-system-build.md` | 系统构建:三权重体 + 9 叶子脚本 + 2 codex loss skill + optimization-loop skill | 纯函数 pytest 全绿 + 单 topic 6 档 e2e(loss-2 单调 τ + 端点分离 + 门控算术) |
| **C** | `2026-06-07-C-assemble-run-supervise.md` | 组装运转:PT5 pilot 硬闸 → 全量 LOOP-2 收敛 → 监督 → freeze + 全量数据集 | C1 pilot go/no-go + C2 收敛(F2 真改 + F1 前进)+ C3 freeze/coverage/dataset 齐 |

## 依赖链(为何这个顺序)

```text
A(环境)  ──►  B(组件)  ──►  C(组装运转)
  │              │              │
  │              │              └─ 依赖 B 全绿:三权重+9叶子 pytest 过、B7 单topic 6档 e2e 真跑过;
  │              │                 依赖 A 全绿:四身份可起、技能可见、薄片 E1–E5 过
  │              └─ 依赖 A 全绿:四身份可起(B 的真模型 e2e 要起真 sim/exec/codex)
  └─ 无前置(裸机起步)
```

- **A 先行**:B/C 的所有真模型组件(integration e2e)都要起真 sim/exec/codex,而四身份的起法、技能可见性、两组 key 隔离全靠 A 搭好。A 不绿,B 的 e2e 起不来。
- **B 居中**:C 组装的"零件"(三权重、9 叶子、2 loss skill、optimization-loop skill)全由 B 造好并单测。C 不造零件,只组装。
- **C 收尾**:把 B 的零件拼成自转整机,跑到收敛产出数据集。C1 pilot 是硬闸——不过即停回 B。

## 黄金合成样例(贯穿 A→C 的回归基线)

A 的薄片 e2e 用一条合成 config+topic,固定存档 `<proj>/fixtures/golden-slice/`,成为三拆共用回归场景,逐层加深、连续可比:

| 拆 | 在黄金样例上验到哪 |
| --- | --- |
| A | 1 run 纵向通路:注入→嵌套→真研究→真 loss→留痕(E1–E5) |
| B | 长成组件成品:gen_configs 真造卡、6 档阶梯、loss-2 单调、门控算术(组件 integration + 6-run e2e) |
| C | 长成全回路:48-run batch、连续 3 过闸收敛、backprop 改权重、实时监督(完整 e2e) |

## 全程铁律(三拆共用,任何 Task 都适用)

1. **一切落 `/workspace`,绝不进 `/` 或 `~`**(`/` 仅 5G overlay 重启即抹;`/workspace` 851 TB 持久)。
2. **两组 API key 物理隔离**(Claude 组给 optim/sim/exec;Codex 组给 loss),**key 值绝不进任何提交物**(脚本/spec/报告/commit),只按变量名引用、执行者手填。
3. **从零全重写**:三层架构终稿只当设计规格;设备上旧 `2026-06-06-probe-pretrain/` 一行不看、不继承(避免旧 fake nesting / 脆弱解析 / A2-A3 撞档 bug 误导)。新代码全进 `self-iteration/2026-06-07-probe-pretrain/`,push 分支 `self-iteration/probe-pretrain`,**绝不推 main**。
4. **数据派三权重**:`axes.py`①/`interpolator.py`②/`assembler.py`③ 是读 `weights/<batch>.json` 对应段的纯函数,**源码恒不动,改权重=改 JSON**。名次层+标签坐标层锁死在 `frozen_label`(无人写)。
5. **W5 check-blind**:一切生成侧产物(config、话术、loss skill、topic)全文过 `leak_audit`,绝不含 32-check / 6-primitive / 检测签名词。loss 判"生成条件是否被忠实执行 / 阶梯单调不单调",不判"研究质量好不好"。
6. **no-fake 铁律**:要真模型的组件(sim/exec/codex)必须真进程,合成的只有"输入 config+topic"。任何 fake-stub 凑绿不算通过(`feedback-no-e2e-shell`)。
7. **隐私红线**:CC log 绝对路径绝不进任何提交物;读 log 只走 `--logs-dir` 必填脚本(`save_transcript`);`runs/` 设备本地 gitignore;dataset/coverage 落盘前过白名单校验,白名单外字段(log 路径、设备用户名、transcript 原文)→ 硬失败中断。

## 三拆边界(谁管什么,互不越界)

- **A 管环境**:装包、env.sh/bootstrap.sh、四 config-dir 预批、skill 复制机制、薄片 1-run。**不管**组件代码与 skill 内容、不管全回路。
- **B 管零件 + 单 topic 6 档**:三权重、9 叶子、2 loss skill、optimization-loop skill 编写。**不管**多 batch、backprop 真改、tmux 长驻、pilot、监督、全量数据集(§backprop 段 B 写出但留 C 深验)。
- **C 管组装运转**:pilot 硬闸、全量 LOOP-2、backprop 真改、长驻、监督、freeze + 全量产出 + 8 真 topic。**不造零件、不搭环境**。

## 设备接入 + 凭证(★LOCAL-ONLY · 必须 gitignore · 绝不 push)

> ⚠️ **红线提醒**:本节含真 SSH 私钥路径与 API key 值,**违反全程铁律 2「key 值绝不进提交物」**。仅因用户显式要求登记于此,**严禁随本文件提交进 git**——执行者落地时应把本节抠出移入设备本地 `/workspace/env.sh`(A 的 Task 4),或在提交前删除本节 / 把本文件加入 `.gitignore`。git 历史一旦带 key 即永久泄漏,需轮换。

- **设备 SSH**:`ssh root@***** -p ***** -i ~/.ssh/id_ed25519`(IP/端口脱敏,执行者手填)
- **Claude 组(给 optim / sim / exec)**:
  - `ANTHROPIC_API_KEY=*****`(**用 `ANTHROPIC_API_KEY`,不是 `ANTHROPIC_AUTH_TOKEN`** — x-api-key 鉴权)
  - `ANTHROPIC_BASE_URL=https://api.ikuncode.cc`(无后缀,CLI 自拼 `/v1/messages`)
  - `ANTHROPIC_MODEL=claude-opus-4-7`
- **Codex 组(给 loss)**:
  - `OPENAI_API_KEY=*****`(亦作 `IKUNCODE_KEY`)
  - `OPENAI_BASE_URL=https://api.ikuncode.cc/v1`(带 `/v1`)
  - `OPENAI_MODEL=gpt-5.5`,wire-api=`responses`
- **★两组 key 物理隔离**:混用会让 claude 报 `model_not_found`(`.claude.json` 的 `customApiKeyResponses.approved` 写 Claude 组 key 尾段 `*****`)。
- **git 提交身份**:`Pthahnix <Pthahnix@proton.me>`。

## 信息来源(本索引及三拆 plan 的唯一依据)

- 设计规格:`docs/superpowers/specs/2026-06-07-remote-env-from-scratch-design.md`(A)、`...-system-build-design.md`(B)、`...-assemble-run-design.md`(C);三层架构终稿 `context/2026-06-06-20-18-triple-cc-architecture.md`(系统设计权威)。
- 代码源:DARE repo(771 skill 复制源,`exec` 用);项目 skills/ 的 `formated-specs` / `formated-result`(B 只对接产出契约,不重写)。

## Execution Handoff

逐拆执行,每拆两选项:

**1. Subagent-Driven(推荐)** — 每 Task 派新 subagent,Task 间审查,快迭代。REQUIRED SUB-SKILL: superpowers:subagent-driven-development。

**2. Inline Execution** — 本会话内批量执行 + checkpoint 审查。REQUIRED SUB-SKILL: superpowers:executing-plans。

**起点:Plan A。** A 全绿(S1–S4 + E1–E5)→ Plan B;B 全绿(pytest + B7 6 档 e2e)→ Plan C;C1 pilot 硬闸,no-go 即停回 B。
