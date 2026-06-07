# DESIGN

- [DESIGN](#design)
  - [tmux 长驻启动 optimizer-cc](#tmux-长驻启动-optimizer-cc)
    - [tmux new-session -d -s opt](#tmux-new-session--d--s-opt)
    - [source /workspace/env.sh \&\& source /workspace/bootstrap.sh](#source-workspaceenvsh--source-workspacebootstrapsh)
      - [`/workspace/env.sh`〔SH · KEEP · 已验证〕](#workspaceenvshsh--keep--已验证)
      - [`/workspace/bootstrap.sh`〔SH · KEEP · 已验证 · 幂等〕](#workspacebootstrapshsh--keep--已验证--幂等)
    - [export CLAUDE\_CONFIG\_DIR=/workspace/home/optim/.claude](#export-claude_config_dirworkspacehomeoptimclaude)
    - [cd /workspace/work/optim \&\& claude](#cd-workspaceworkoptim--claude)
  - [optimization-loop skill 说明完整任务](#optimization-loop-skill-说明完整任务)
    - [内含: epoch/LOOP-1/2 控制流 + 门控判定规则 + 反向传播启发式 + 状态落盘约定 check-blind(W5)](#内含-epochloop-12-控制流--门控判定规则--反向传播启发式--状态落盘约定-check-blindw5)
      - [`optimization-loop/SKILL.md`〔NEW-SKILL〕](#optimization-loopskillmdnew-skill)
  - [epochs-loop (不限,跑到收敛)](#epochs-loop-不限跑到收敛)
    - [叶子脚本编排总览(本设计的结构基石,贯穿后续所有 H)](#叶子脚本编排总览本设计的结构基石贯穿后续所有-h)
      - [技能目录结构](#技能目录结构)
      - [脚本编排表(触发时机 · 输入 · 输出)](#脚本编排表触发时机--输入--输出)
      - [`new_run_id.py`〔NEW · scripts/〕](#new_run_idpynew--scripts)
    - [一个 epoch = m=8 topic × n=6 人设 = 48 run (LOOP-2)](#一个-epoch--m8-topic--n6-人设--48-run-loop-2)
    - [interpolator 插值获取 48 条 research\_config](#interpolator-插值获取-48-条-research_config)
      - [三分法(本设计的核心 — 经三轮 insight 推出)](#三分法本设计的核心--经三轮-insight-推出)
      - [★关键约束: 撞档扰动只许用 B1 / 表达层,绝不许用 A1–A5](#关键约束-撞档扰动只许用-b1--表达层绝不许用-a1a5)
      - [★可训练性是有条件的(CLR 校验 AS-4 的产物)](#可训练性是有条件的clr-校验-as-4-的产物)
      - [`gen_configs.py` 整体〔NEW · scripts/〕](#gen_configspy-整体new--scripts)
      - [读权重 weights/\<batch\>.json](#读权重-weightsbatchjson)
      - [调 interpolator.ladder\_levels(n=6) → 6 档等级映射](#调-interpolatorladder_levelsn6--6-档等级映射)
      - [调 assembler.build\_batch(...) → 6 档坐标组装](#调-assemblerbuild_batch--6-档坐标组装)
      - [调 axes.level\_text(axis,level) → 填档位话术](#调-axeslevel_textaxislevel--填档位话术)
      - [每张卡过 leak\_audit(text) → W5 拦 check 词](#每张卡过-leak_audittext--w5-拦-check-词)
      - [输出 6 卡 × 8 topic = 48 config json → runs/\<id\>/configs/](#输出-6-卡--8-topic--48-config-json--runsidconfigs)
    - [\[按 topic 成组\] for topic\_i in 8](#按-topic-成组-for-topic_i-in-8)
      - [for 档 in 6 ── 开始一次 run (LOOP-1)](#for-档-in-6--开始一次-run-loop-1)
        - [起 sim-模拟器-cc(交互式 REPL,每 run 全新)](#起-sim-模拟器-cc交互式-repl每-run-全新)
          - [Bash 直起 claude(IS\_SANDBOX=1 + CLAUDE\_CONFIG\_DIR=sim + cd /workspace/work/sim),无驱动脚本](#bash-直起-claudeis_sandbox1--claude_config_dirsim--cd-workspaceworksim无驱动脚本)
        - [optimizer 经 conversation 注入 research\_config 给 sim](#optimizer-经-conversation-注入-research_config-给-sim)
          - [首轮消息: config 全文 + 扮演指令 + 「起 exec 跑完 research,回我 DONE」](#首轮消息-config-全文--扮演指令--起-exec-跑完-research回我-done)
        - [optimizer 关闭 sim-模拟器-cc](#optimizer-关闭-sim-模拟器-cc)
        - [concat (research\_config, research\_graph, research\_result)](#concat-research_config-research_graph-research_result)
          - [读 configs/\<sample\>.json + transcripts/\<sample\>.md](#读-configssamplejson--transcriptssamplemd)
          - [取 exec formated-specs/results 的 graph / result 结构化块](#取-exec-formated-specsresults-的-graph--result-结构化块)
          - [输出三元组 → runs/\<id\>/triples/\<sample\>.json](#输出三元组--runsidtriplessamplejson)
        - [启动 codex → injection-fidelity → loss-1](#启动-codex--injection-fidelity--loss-1)
          - [注入 SKILL.md 全文](#注入-skillmd-全文)
          - [codex exec --output-schema loss1.json -o ... \<payload=transcript\>](#codex-exec---output-schema-loss1json--o--payloadtranscript)
          - [parse\_loss1 → 该 run 保真值 → 缓存 runs/\<id\>/loss/](#parse_loss1--该-run-保真值--缓存-runsidloss)
        - [IF 档 \< 5 ── 内层循环回跳判断](#if-档--5--内层循环回跳判断)
      - [── per-topic 聚合 (仅在内层跑满 6 档后到达) ──](#-per-topic-聚合-仅在内层跑满-6-档后到达-)
        - [codex → ladder-quality-order → loss-2 (吃 6 档三元组)](#codex--ladder-quality-order--loss-2-吃-6-档三元组)
        - [gate.topic\_passes (保真率≥90% ∧ mono ∧ endpoint)](#gatetopic_passes-保真率90--mono--endpoint)
        - [写该 topic 6 条样本](#写该-topic-6-条样本)
      - [IF topic\_i \< 7](#if-topic_i--7)
        - [T: topic+1 → LOOP (回外层 FOR)](#t-topic1--loop-回外层-for)
        - [F: 8 topic 全跑完 (48 run) → END LOOP-1](#f-8-topic-全跑完-48-run--end-loop-1)
    - [整合 8 条 topic 收敛情况](#整合-8-条-topic-收敛情况)
    - [batch\_pass\_ratio ≥80% (即 ≥7/8 topic 过) → 过闸](#batch_pass_ratio-80-即-78-topic-过--过闸)
    - [IF 连续 3 个 batch 过闸](#if-连续-3-个-batch-过闸)
      - [T: END LOOP-2](#t-end-loop-2)
        - [freeze\_weights + coverage\_report](#freeze_weights--coverage_report)
      - [F1: 过闸未收敛 — 权重不变, 前进一批确认](#f1-过闸未收敛--权重不变-前进一批确认)
      - [F2: 反向传播 + 权重更新 + LOOP ── 智能点 (optimizer 动脑)](#f2-反向传播--权重更新--loop--智能点-optimizer-动脑)
        - [读本 batch 的 loss 信号 + 哪些 topic 的哪个门控项挂](#读本-batch-的-loss-信号--哪些-topic-的哪个门控项挂)
        - [optimizer optim 档位话术](#optimizer-optim-档位话术)
          - [weights.revise("axis\_prose", k, new, reason)](#weightsreviseaxis_prose-k-new-reason)
          - [改 weights/\<batch\>.json 的 axis\_prose 段(数据派,axes.py 不动)](#改-weightsbatchjson-的-axis_prose-段数据派axespy-不动)
        - [optimizer optim 插值器](#optimizer-optim-插值器)
          - [weights.revise("interp\_params", k, ...)](#weightsreviseinterp_params-k-)
        - [optimizer optim 生成器组装逻辑](#optimizer-optim-生成器组装逻辑)
          - [weights.revise("assembler\_params", k, ...)](#weightsreviseassembler_params-k-)
        - [/compact + 重载 optimization-loop skill → LOOP](#compact--重载-optimization-loop-skill--loop)
          - [重读 weights/\<batch+1\>.json + revision\_log.jsonl + trace 尾部](#重读-weightsbatch1json--revision_logjsonl--trace-尾部)
  - [END](#end)

```bash
pretraining
  │
  ├─ tmux 长驻启动 optimizer-cc                                            〔SH 四条独立命令,逐条手跑,不打包〕
  │    ├─ tmux new-session -d -s opt                                       〔脱离本机,夜间可关〕
  │    ├─ source /workspace/env.sh && source /workspace/bootstrap.sh       〔KEEP 已存在〕
  │    ├─ export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude                 〔optimizer 专属〕
  │    └─ cd /workspace/work/optim && claude                              〔交互式长驻 REPL;启动后 send-keys 送开场 prompt〕
  │
  ├─ optimization-loop skill 说明完整任务                                   〔NEW-SKILL .claude/skills/optimization-loop/SKILL.md〕
  │    └─ 内含:epoch/LOOP-1/2 控制流 + 门控判定规则 + 反向传播启发式 + 状态落盘约定; check-blind(W5)
  │
  ├─ epochs-loop (不限,跑到收敛)                                            〔SKILL §loop〕〔TRACE run_start〕  <==CHECKPOINT: 建 runs/<run_id>/trace.jsonl,run_start 为首行;此后所有〔TRACE x〕按时序逐行追加于此(11 事件总账)
  │    │
  │    ├─ 一个 epoch = m=8 topic × n=6 人设 = 48 run (LOOP-2)               〔TRACE batch_start(batch_id)〕  <==CHECKPOINT: trace.jsonl 追加一行 batch_start{batch_id};每 epoch 的边界标记
  │    │
  │    ├─ interpolator 插值获取 48 条 research_config                       〔NEW gen_configs.py〕
  │    │    ├─ 读权重 weights/<batch>.json                                  〔KEEP weights.load〕
  │    │    ├─ 调 interpolator.ladder_levels(n=6)  →  6 档等级映射          〔WEIGHT② interpolator.py〕
  │    │    ├─ 调 assembler.build_batch(...)        →  6 档坐标组装         〔WEIGHT③ assembler.py〕
  │    │    ├─ 调 axes.level_text(axis,level)       →  填档位话术           〔WEIGHT① axes.py〕
  │    │    ├─ 每张卡过 leak_audit(text)            →  W5 拦 check 词       〔KEEP leak_audit.py〕
  │    │    └─ 输出 6 卡 × 8 topic = 48 config json  →  runs/<id>/configs/  〔KEEP cards.to_dict〕  <==CHECKPOINT: runs/<id>/configs/<sample>.json,48 份 research_config 全文(插值+组装+话术的产物,即每个 sim 人设);这是三元组的第 1 元
  │    │
  │    ├─ [按 topic 成组] for topic_i in 8:                                〔TRACE topic_start(topic_id)〕  <==CHECKPOINT: trace.jsonl 追加 topic_start{topic_id};8 topic 外层入口
  │    │  ├─ for 档 in 6 ── 开始一次 run (LOOP-1)                           〔TRACE rung_start(rung_id)〕  <==CHECKPOINT: trace.jsonl 追加 rung_start{rung_id};6 档内层入口,标定一次 run 开始
  │    │  │    │
  │    │  │    ├─ 起 sim-模拟器-cc(交互式 REPL,每 run 全新)               〔Bash 直起 claude〕
  │    │  │    │    └─ IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/sim/.claude \   〔config 靠环境变量;root 起 bypass REPL 需 IS_SANDBOX=1〕
  │    │  │    │       (cd /workspace/work/sim) claude                 〔工作目录靠 cwd;无技能,人设靠注入;bypass 由 settings.local.json〕
  │    │  │    │
  │    │  │    ├─ optimizer 经 conversation 注入 research_config 给 sim     〔Bash 首轮喂话〕
  │    │  │    │    └─ msg = "<config json 全文 + 指令:扮演此用户人设, 启动 exec 跑完整 research,结束后回我 DONE>"
  │    │  │    │       │
  │    │  │    │       │  ── 以下在 sim-cc 内部发生(sim 自己的 Bash 直起 claude 驱动 exec)──
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc Bash 起 dare-exec-cc(交互式 REPL)         〔Bash 直起 claude〕
  │    │  │    │       │    └─ IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude \   〔771 DARE 技能, W5〕
  │    │  │    │       │       (cd /workspace/work/exec) claude
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc 注入 i_m topic + 用户偏置 + 强制技能项       〔Bash 喂 exec 首轮,msg 含:〕
  │    │  │    │       │    ├─ topics[i_m] 文本 + 用户偏置(来自 config)
  │    │  │    │       │    ├─ ★强制:用 formated-specs 替代 writing-specs   〔你新增项;exec 已挂这两个 skill〕
  │    │  │    │       │    └─ ★强制:最后必须调 formated-results
  │    │  │    │       │
  │    │  │    │       ├─ sim-cc ↔ exec-cc 反复 conversation 完成 research  〔同一 REPL 上来回多轮〕
  │    │  │    │       │    └─ 对话自动落 exec 的 session jsonl(无需自截流)  〔TRACE 每轮 dialogue_turn;save_transcript run 末一次〕  <==CHECKPOINT: ★核心交互留存★ 每轮仅 trace.jsonl 加一行 dialogue_turn{seq}(实时可 tail);transcript 由 save_transcript.py 在 **run 末一次性**读 exec 的 session jsonl(type∈{user,assistant})转写 runs/<id>/transcripts/<sample>.md(jsonl 全量 append,run 末一提即得完整对话,无需每轮增量)。这是"所有人机交互内容"的主体
  │    │  │    │       │                                                    runs/<id>/transcripts/<sample>.md
  │    │  │    │       ├─ 得到 research_result                              〔exec 末轮 formated-results 产出〕
  │    │  │    │       ├─ sim-cc 关闭 dare-exec-cc                          〔退出该 REPL;jsonl 留盘备查〕
  │    │  │    │       └─ sim-cc response "DONE" 给 optimizer                〔sim 末轮的返回值〕
  │    │  │    │
  │    │  │    ├─ optimizer 关闭 sim-模拟器-cc                              〔关闭该会话即收尾;本 run 会话作废〕
  │    │  │    │
  │    │  │    ├─ concat (research_config, research_graph, research_result) 〔NEW concat_triple.py〕
  │    │  │    │    ├─ 读 configs/<sample>.json                            〔三元组第 1 元,gen_configs 已落〕
  │    │  │    │    ├─ 读 transcripts/<sample>.md(save_transcript 已落)→ 取 graph/result 结构化块
  │    │  │    │    └─ 输出三元组 → runs/<id>/triples/<sample>.json  <==CHECKPOINT: runs/<id>/triples/<sample>.json,(research_config, research_graph, research_result) 三元组合体;config 取自 configs/<sample>.json,graph/result 取自 exec 末轮 formated-specs/results 的结构化产出(经 save_transcript 落入 transcript);喂给 codex 算 loss 的输入单元
  │    │  │    │
  │    │  │    ├─ 启动 codex → injection-fidelity → loss-1                  〔FIX run_codex_loss.py〕
  │    │  │    │    ├─ 注入 SKILL.md 全文                                   〔cwd=/workspace/work/loss〕
  │    │  │    │    ├─ codex exec --output-schema loss1.json -o ... <payload=transcript>
  │    │  │    │    └─ parse_loss1 → 该 run 保真值 → 缓存 runs/<id>/loss/   〔KEEP loss_runner.parse_loss1〕  <==CHECKPOINT: runs/<id>/loss/<sample>.loss1.json,该 run 的 injection-fidelity 结果(保真值+codex 判词);per-run 缓存,供 per-topic 聚合保真率用
  │    │  │    │                                                            〔TRACE rung_done(loss-1)〕  <==CHECKPOINT: trace.jsonl 追加 rung_done{sample_id, fidelity:bool, loss1, per_axis_evidence, drift_flag, transcript_path};一次 run 收尾
  │    │  │    │
  │    │  │    └─ IF 档 < 5:                                               ← 内层循环判断
  │    │  │         ├─ T: 档+1 → LOOP (回内层 for 档)
  │    │  │         └─ F: 该 topic 6 档跑完 → 跳出内层,进 per-topic 聚合 ↓
  │    │  │
  │    │  ├─ ── per-topic 聚合(仅在内层跑满 6 档后到达)──                    ★触发点
  │    │  │    ├─ codex → ladder-quality-order → loss-2(吃 6 档三元组)      〔FIX run_codex_loss.py〕★  <==CHECKPOINT: runs/<id>/loss/<topic>.loss2.json,该 topic 的 ladder-quality-order 结果{tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, pairwise_log};per-topic,吃 6 档三元组
  │    │  │    ├─ gate.topic_passes(保真率≥90% ∧ mono ∧ endpoint)          〔KEEP gate.py〕〔TRACE topic_done〕  <==CHECKPOINT: trace.jsonl 追加 topic_done{tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, topic_pass, fidelity_rate};该 topic 过闸 bool 落账
  │    │  │    └─ 写该 topic 6 条样本                                       〔KEEP dataset_writer〕  <==CHECKPOINT: ★最终产物★ dataset/<topic>/<sample>.json,隐私白名单裁字段后的 6 条已发布样本(标注=已知生成条件);这是 pretrain 要交付的数据集本体,绝不含 CC log 路径
  │    │  │
  │    │  └─ IF topic_i < 7:                                              ← 外层循环判断
  │    │       ├─ T: topic+1 → LOOP (回外层 for topic_i)
  │    │       └─ F: 8 topic 全跑完(48 run)→ END LOOP-1 ↓
  │    │
  │    ├─ 整合 8 条 topic 收敛情况                                          ★(非 48; 每条已聚合其 6 run)
  │    ├─ batch_pass_ratio ≥80% (即 ≥7/8 topic 过) → 过闸                  〔KEEP gate.batch_pass_ratio〕〔TRACE batch_done〕  <==CHECKPOINT: trace.jsonl 追加 batch_done{batch_id, pass_ratio, batch_passed}(同上,此为原始脊柱行)
  │    │
  │    └─ IF 连续 3 个 batch 过闸                                          〔KEEP gate.converged〕
  │         │
  │         ├─ T: END LOOP-2                                               〔TRACE converged + run_end〕  <==CHECKPOINT: trace.jsonl 追加 converged{} + run_end{};整次 pretrain 收敛收尾(原始脊柱行)
  │         │     └─ freeze_weights + coverage_report                      〔KEEP freeze.py〕  <==CHECKPOINT: weights/frozen.json(冻结的最终三权重)+ coverage_report.md(覆盖率报告,聚合统计,无 log 路径)
  │         │
  │         └─ F: 反向传播 + 权重更新 + LOOP ── 智能点③(optimizer 动脑)      〔SKILL §backprop 启发式〕
  │                 │   读本 batch 的 loss 信号 + 哪些 topic 的哪个门控项挂
  │                 │
  │                 ├─ optimizer optim 档位话术                            〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("axis_prose",k,new,reason)       〔KEEP weights.revise;启发:loss-1 挂→优先〕
  │                 │       → 改 weights/<batch+1>.json 的 axis_prose 段(数据派,axes.py 不动)  〔WEIGHT① 〕〔TRACE weight_revised〕  <==CHECKPOINT: weights/<batch+1>.json(更新后的权重①话术快照,每 batch 一份;数据派=只改 JSON 数据段,axes.py 源码恒不变)+ revision_log.jsonl 追加一行{target:axis_prose, key, new_value, reason};同时 trace.jsonl 加 weight_revised。★此前从未 emit 过★
  │                 │
  │                 ├─ optimizer optim 插值器                              〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("interp_params",...)             〔启发:loss-2 塌→优先〕〔WEIGHT②〕〔TRACE weight_revised〕  <==CHECKPOINT: weights/<batch+1>.json 内 interp_params 段更新(数据派,interpolator.py 不动)+ revision_log.jsonl 追加{target:interp_params,...};trace.jsonl 加 weight_revised
  │                 │
  │                 ├─ optimizer optim 生成器组装逻辑                      〔NEW apply_weight_update.py〕
  │                 │    └─ weights.revise("assembler_params",...)          〔卡整体没造好时〕〔WEIGHT③〕〔TRACE weight_revised〕  <==CHECKPOINT: weights/<batch+1>.json 内 assembler_params 段更新(数据派,assembler.py 不动)+ revision_log.jsonl 追加{target:assembler_params,...};trace.jsonl 加 weight_revised
  │                 │
  │                 └─ /compact + 重载 optimization-loop skill → LOOP       〔SKILL §state:跨 batch 状态全落盘〕
  │                      └─ 重读 weights/<batch+1>.json + revision_log.jsonl 〔CC 压缩后从盘恢复,无记忆依赖〕  <==CHECKPOINT(读取点): optimizer 每 batch /compact 后从盘恢复跨-batch 状态;读 weights/<batch+1>.json(新权重)+ revision_log.jsonl + (可选)滚动决策日志。此为"读"checkpoint,与上面各"写"点配对
  │
  └─ END
```

## tmux 长驻启动 optimizer-cc

### tmux new-session -d -s opt

```markdown
You are optimizer-cc — the host of a "pseudo-neural-network pretraining"
training loop. Your role is equivalent to train.py in PyTorch. You are NOT
here to answer questions, NOT here to chat with anyone. The only reason you
exist is to drive one full training run until convergence.

# Your goal
Through repeated epoch loops, optimize three trainable weights
(level prose / interpolator / generator-assembly logic) to produce a batch
of labeled data samples. In every epoch you MUST:
generate configs → drive the lower-layer CCs to produce data →
compute loss with codex → judge the gate →
decide which weight to revise based on loss → enter the next epoch.

# Your only source of action
Your complete task specification is written in the `optimization-loop` skill.
Load that skill NOW, and execute strictly according to its control flow,
gating rules, backprop heuristics, and state-persistence conventions.

Do NOT improvise the flow. Do NOT skip the skill and act on intuition.
Do NOT deviate from the skill to do anything it did not ask for.
Whatever the skill says, that is exactly what you do.

# Long-running discipline
You will run for a long time and /compact periodically. All cross-batch
state MUST be persisted to disk. After /compact, you MUST rebuild your state
from disk (weights, revision_log), never relying on compacted-away memory.
Memory is not trustworthy; disk is the only source of truth.

# Boundary
Strictly obey the W5 constraint in the skill. Not one step beyond it.
```

### source /workspace/env.sh && source /workspace/bootstrap.sh

**这一步做什么**
在 tmux session 里、启动 `claude` 之前,把运行环境准备好。两个脚本各管一摊,顺序固定(env 先、bootstrap 后),且必须在 `export CLAUDE_CONFIG_DIR` 与 `claude` 之前 source。

**决策:确认沿用,无需改动(KEEP)。** 两脚本上一阶段已写好并验证,本步不新写、不修改。

**一次性前置(设备未装 tmux)**:首次部署需 `apt install -y tmux`(optimizer 长驻靠它)。这是装一次的环境前提,可并入 bootstrap.sh 的首次检查(`command -v tmux || apt install -y tmux`),幂等。

#### `/workspace/env.sh`〔SH · KEEP · 已验证〕

注入本次运行所需的全部环境变量,核心是**两套互相隔离的 API 凭证**(按分组,不可混用):

- **Claude 分组**(给 optimizer / sim / exec 三层 CC 用):
  - `ANTHROPIC_API_KEY = *****`(claude 分组专属 key,x-api-key 鉴权)
  - `ANTHROPIC_BASE_URL = https://api.ikuncode.cc`(无后缀;CLI 自行拼 `/v1/messages`)
  - `ANTHROPIC_MODEL = claude-opus-4-7`
- **Codex 分组**(给两次 loss 计算的 codex 用):
  - `OPENAI_API_KEY / IKUNCODE_KEY = *****`(codex 分组专属 key)
  - `OPENAI_BASE_URL = https://api.ikuncode.cc/v1`
  - `OPENAI_MODEL = gpt-5.5`
- **路径类**:`CLAUDE_CONFIG_DIR`(默认值,后一条 H3 会针对 optimizer 再 export 覆盖)、`NPM_CONFIG_PREFIX=/workspace/home/.npm-global`、`HF_HOME=/workspace/home/.hf`、`PATH` 追加(claude / codex / gh / hf 可执行目录)。

一句话:**让 `claude` 和 `codex` 命令一调就通,且各自连对自己的分组**。
> ⚠️ 红线:两个 key 是两个不同分组,曾因填成同一个 key 导致 claude 报 model_not_found。保持分开。

#### `/workspace/bootstrap.sh`〔SH · KEEP · 已验证 · 幂等〕

重启恢复脚本。设备重开机或新开 shell 后:

- 把 env.sh 重新挂进 `~/.bashrc`(保证新 shell 自动带环境);
- 首次检查 `command -v tmux || apt install -y tmux`(optimizer 长驻host)。

**不做 `~/.claude` symlink**:四身份各用独立 config-dir,起 claude/codex 时经环境变量 `CLAUDE_CONFIG_DIR=<角色 .claude>`(codex 用其 `--config`/cwd 约定)显式指向 `/workspace/home/{optim,sim,exec}/.claude`、`/workspace/home/loss/.codex`,不靠家目录软链(软链脆弱、且会让四身份串配置)。

一句话:**保证持久盘上的状态在任何新 shell 里都重新接好**。幂等,重复 source 无副作用。

**CHECKPOINT**:无(纯环境准备,不落运行数据)。

### export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude

**这一步做什么**
在启动 optimizer 的 `claude` 之前,把它的 config-dir 显式指到 **`/workspace/home/optim/.claude`**。CLAUDE_CONFIG_DIR 决定这个 claude 进程从哪读写配置、会话历史、技能挂载、`.claude.json`。这条是四层角色隔离的关键一环。

> **实际采用 `/workspace/home/optim/.claude`**, 使四角色在 `home/` 下平级同构(optim / sim / exec / loss)。

**为什么单独 export(而非靠 env.sh 默认值)**
四个角色各有独立 config-dir,互不串会话、互不串技能。技能**复制进各 config-dir 的 `skills/` 目录**(非 mount);superpowers 全员都带:

| 角色 | config-dir | config-dir `skills/` 内复制的技能 | 来源 |
| --- | ---------- | ------- | --- |
| optimizer | `/workspace/home/optim/.claude` | optimization-loop + superpowers | 项目 skills/ + superpowers |
| sim | `/workspace/home/sim/.claude` | 仅 superpowers(人设靠注入) | superpowers |
| exec | `/workspace/home/exec/.claude` | 771 DARE + formated-specs/results + superpowers | DARE repo skills/ + 项目 skills/ + superpowers |
| codex | `/workspace/home/loss/.codex` | injection-fidelity + ladder-quality-order + superpowers(codex 规范) | 项目 skills/ + superpowers |

本条 H3 只设 **optimizer 自己那一个**。sim/exec 的 config-dir 由后面起它们时各自用环境变量 `CLAUDE_CONFIG_DIR=...` 设(claude 无 `--config-dir` flag;工作目录靠 `cd`,无 `--cwd` flag);codex 的 `/workspace/home/loss/.codex` 在 loss 步骤里用。技能复制矩阵的搭建归 Spec A。

**bypass permission(四个 CC 角色统一配置)**
optimizer / sim / exec 三个 claude 角色,各自 config-dir 下放一份 `settings.local.json` 开启 bypass permissions,使工具调用全程放行——这是整条流水线无人值守长跑(夜间 hand-off)的前提。三处文件:

- `/workspace/home/optim/.claude/settings.local.json`
- `/workspace/home/sim/.claude/settings.local.json`
- `/workspace/home/exec/.claude/settings.local.json`

内容统一:

```json
{ "permissions": { "defaultMode": "bypassPermissions" } }
```

(codex 角色不走 claude 的权限模型,其放行在 `/workspace/home/loss/.codex` 的 codex 配置里另管。)

**root 下起 bypass REPL 的硬门槛(两条,缺一不可)**:

1. **`IS_SANDBOX=1`**:root 身份直接起 bypassPermissions 的交互式 REPL 会被拒(`--dangerously-skip-permissions cannot be used with root/sudo`)。三层 claude 启动时环境里都要带 `IS_SANDBOX=1`(并入 env.sh 即可)。
2. **config-dir 内预批 env API key**:全新 config-dir 默认 "Not logged in",代理走 Anthropic 协议+env 的 `ANTHROPIC_API_KEY`,需在该 config-dir 的 `.claude.json` 里把该 key 尾段写进 `customApiKeyResponses.approved`,REPL 才会真正回话;同时预置 `hasCompletedOnboarding=true`、`bypassPermissionsModeAccepted=true`。optimizer 的 `.claude.json` 已配,sim/exec 两个 config-dir 同样照配。

**决策已定**:optimizer = `/workspace/home/optim/.claude`,codex = `/workspace/home/loss/.codex`。这行 `export` 是本 H2「四条独立命令」之一(见 L303:四条各自独立手跑、逐条验证起效,**不打包成单个脚本**),无新文件。

**CHECKPOINT**:无。

### cd /workspace/work/optim && claude

**这一步做什么**
点火 optimizer-cc 的命令。`cd` 进工作目录后启动**交互式** `claude`(交互式长驻 REPL,非一次性命令式调用)。前三条(开场 prompt、source 环境、export config-dir)是铺垫,这条点火。

optimizer 是 tmux 里的交互式长驻 REPL,从头到尾不停,会话天然连续,命令就是 `claude`。下层 sim/exec 同样是交互式 REPL,但**不进 tmux、不靠驱动脚本**:父 CC 在自己的 Bash 工具里直接跑 `claude` 起子 CC,两个会话来回多轮对话,run 内多轮就是正常发消息,本 run 跑完即关——不靠任何会话 flag。

**决策已定**:

- **不合并脚本**。四条 H3 各自独立执行、逐条验证起效,不打包成单个 `start_optimizer.sh`。每条作为单独命令/小片段手动跑。
- **开场 prompt 用方案 A**:`tmux send-keys` 自动送入交互式 claude(启动后脚本自动把英文开场 prompt 敲进去)。

**四条独立命令(本 H2 汇总)**:

```bash
# 1. 建 session
tmux new-session -d -s opt
# 2. 备环境(在 session 内)
tmux send-keys -t opt 'source /workspace/env.sh && source /workspace/bootstrap.sh' Enter
# 3. 设 optimizer 专属 config-dir
tmux send-keys -t opt 'export CLAUDE_CONFIG_DIR=/workspace/home/optim/.claude' Enter
# 4. 点火 + 送开场 prompt(A 方案)
tmux send-keys -t opt 'cd /workspace/work/optim && claude' Enter
#    待 claude 就绪后,再 send-keys 送英文开场 prompt 文本 + Enter
```

**CHECKPOINT**:无(纯启动)。

**就绪探测(决策已定,据簇 C):** 此问题**仅 optimizer 一处成立**——它是唯一用 `tmux send-keys` 把开场 prompt 敲进交互式 REPL 的层;sim/exec **无此问题**(父 CC 在自己 Bash 工具里直起 claude、发消息后等回复,就绪由"发了就等回"天然解决,不用 send-keys)。optimizer 这处**不用固定 `sleep`**(设备慢则不够、快则浪费),改用 tmux 输出轮询:`tmux capture-pane -p -t opt | tail` 直到出现 claude REPL 稳定提示符(输入框/光标行)再 send-keys。写成 bash until 循环(≤1s 间隔,本地探测),只在启动时跑一次,不进热路径。**[落地细节]** 提示符的精确匹配串随 claude 版本定。

## optimization-loop skill 说明完整任务

### 内含: epoch/LOOP-1/2 控制流 + 门控判定规则 + 反向传播启发式 + 状态落盘约定 check-blind(W5)

**这一步做什么**
这是整个系统的"大脑程序"。optimizer-cc 启动后 load 它,此后一切行为(epoch 怎么循环、门控怎么判、loss 怎么读、改哪个权重、状态怎么落盘)都由它规定。类比:它就是 train.py 的源码,宿主是 CC 而非 Python 解释器。

**决策已定:厚 skill。** 每步该调的工具、参数、判定阈值、落盘路径**全部写死**,optimizer 严格照做、不得自作主张。**唯一保留判断**的是 §backprop"改哪个权重"(智能点③)。

#### `optimization-loop/SKILL.md`〔NEW-SKILL〕

- 路径:`/workspace/home/optim/.claude/skills/optimization-loop/SKILL.md`
- 分段(各段机制已在后续对应 H 填实,这里给骨架 + 指针;落地写 SKILL.md 时从对应 H 汇编):
  - **§loop** — epoch-loop / LOOP-1(8×6 两层)/ LOOP-2 控制流。
  - **§gate** — 门控规则:per-topic 三项 AND(保真率≥90% ∧ monotonicity_pass ∧ endpoint_separation_pass);batch_pass_ratio≥80%(≥7/8 topic);连续 3 batch 过闸=收敛。
  - **§backprop** — 反向传播启发式(**唯一留薄段**):**先归因、再动手**。先按 loss 类型与子类型定位到哪个权重,再改:loss-1 挂→①话术;loss-2 塌须先分子类型——端点没拉开(根因多在①话术不够分 / 端点坐标先天没拉够远,见行 502–506)vs 中间档单调破或撞糊(才是②插值器铺陈层的活);卡整体没造好→③组装逻辑。判断指引,非 if-else;详细启发式在 `references/backprop-heuristic.md`。
  - **§state** — 跨-batch 状态落盘约定:/compact 后从 weights/\<batch\>.json + revision_log.jsonl 重建,不依赖记忆。
  - **§tools** — 可调叶子工具清单与次序(gen_configs / save_transcript / concat_triple / run_codex_loss / gate / apply_weight_update / write_dataset / trace);起子 CC 不靠任何驱动脚本:父 CC 在自己的 Bash 工具里**直接跑 `claude`**(IS_SANDBOX=1 + 子角色 CLAUDE_CONFIG_DIR + cd 子 cwd)起子 CC,两个正常交互式会话来回对话、本 run 跑完即关。optimizer 直起 sim、sim 同法直起 exec,命令范式写在 skill。
- **W5**:全文 check-blind,过 `leak_audit`,绝不含 32-check / 6-primitive / 检测签名词表。
- **CHECKPOINT**:无(只读"程序",不落运行数据)。

> ⚠️ 下面这段 ` ```markdown ` 是 **SKILL.md 的 spec(规格草案),不是最终落地的真实 skill 文件**。真实 SKILL.md 在各 H 敲定后另行成形;此处仅记录它该长什么样。

```markdown
---
name: optimization-loop
description: optimizer-cc 的训练主程序。规定 epoch 循环、门控、反向传播、状态落盘、子CC启动。check-blind(W5)。
---

# §loop — 控制流
两层嵌套(伪代码)。LOOP-2(epoch/batch，跑到收敛)包 LOOP-1(48 run = 外层 for topic_i in 0..7 × 内层 for 档 in 0..5):
- 进入 epoch: new_run_id.py 取 run_id → emit run_start → 建 runs/<run_id>/trace.jsonl。
- 进入 batch: 取 weights 目录最大编号为 batch_id(不+1;冷启动=batch-0) → emit batch_start → gen_configs.py 读 weights/<batch_id>.json 造 48 config。
- for topic_i: emit topic_start → for 档: emit rung_start → [起sim→注入config→sim起exec→注入topic+强制→多轮→concat三元组→run_codex_loss(loss-1)→emit rung_done] → IF 档<5 回跳 else per-topic聚合。
- per-topic 聚合: run_codex_loss(loss-2,吃6档) → gate_eval(topic_passes) → emit topic_done → write_dataset(6样本) → IF topic_i<7 回跳 else END LOOP-1。
- batch 收尾: 读8个topic_done的topic_pass → batch_pass_ratio → emit batch_done → IF 连续3batch过闸: T freeze+converged+run_end / F §backprop。
每步调哪个 scripts/ 叶子、emit 哪个 trace 事件,严格照本节,不得自作主张。

# §gate — 门控判定(纯算术,gate_eval.py,不调CC/codex)
- per-topic 三项 AND: topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass。
- batch: batch_pass_ratio≥0.80,硬整数线 = ≥7/8 topic 过(6/8=0.75 不过)。
- 收敛: trace 尾部 recent_ratios 末3个全≥0.80。无状态,可从 trace 重建。
- 阈值数值全在 references/gate-thresholds.md。check-blind:只读 fidelity_rate(loss-1)+τ/端点(loss-2),不碰 PG/NG/32-check。

# §backprop — 反向传播(唯一留薄段·智能点③)
先归因、再动手,一个 batch 只改一个权重。决策表: loss-1挂→①axis_prose; loss-2端点没拉开→先读rigor_floor_flag(真则不动权重)否则①端点cell; loss-2中间撞糊(τ低但端点分得开)→②interp_params; ≥4/8双塌→③assembler_params。优先级 loss-1>子类型B>卡整体。归因输入三层(batch_done→topic_done→loss/*.json判词,够判就停)。详细启发式 references/backprop-heuristic.md。W5:归因只读 fidelity/τ/端点 + codex判词,绝不读 32-check/PG-NG;新话术过 leak_audit。

# §state — 跨-batch 状态落盘
"Memory is not trustworthy; disk is the only source of truth." 落盘三件套: trace.jsonl(11事件) / weights/<batch>.json(快照) / revision_log.jsonl。每 batch 末固定 /compact 一次,compact 后重载本 skill + 从盘恢复: 读 weights/<batch+1>.json(新权重)+ revision_log.jsonl(改动史)+ trace 尾部(recent_ratios/batch_id/末行seq+1续号)。隐私:transcript_path 相对路径,读 log 脚本 --logs-dir 必填。

# §tools — 叶子工具 + 子CC启动
叶子(scripts/,各自"何时调·输入·输出"见编排表): new_run_id / gen_configs / save_transcript(run末一次,--logs-dir必填) / concat_triple / run_codex_loss / gate_eval / apply_weight_update / write_dataset / trace_emit。三权重本体 axes/interpolator/assembler 留 generator/,gen_configs 调、apply_weight_update 改其 weights JSON 数据段(数据派,源码不动)。
子CC启动: 父CC 在自己 Bash 工具里直起 `IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<角色> bash -lc 'cd <cwd> && claude'`,正常多轮对话。三铁律: 无驱动脚本/不进tmux(仅optimizer用tmux)/每run全新即生即灭。权威 transcript = exec session jsonl。
```

## epochs-loop (不限,跑到收敛)

**这一步做什么**
最外层训练循环。一个 epoch = 一个 batch = 48 run,不设次数上限,跑到"连续 3 个 batch 过闸"才停。它是 §loop 里 LOOP-2 的化身,把"生成配置 → 跑数据 → 算 loss → 判门控 → 改权重"包成一圈反复转。本条 H2 只定**循环的边界语义**(进入时做什么、退出条件、run_id 怎么生成);内部步骤是下面各 H3 的事。

**边界语义**:

- 进入时:调 `new_run_id.py` 取 run_id;emit `run_start`,建 `runs/<run_id>/trace.jsonl`(首行)。
- 循环体:一个 batch 完整流程(下面 H3)。
- 退出:§gate 判"连续 3 batch 过闸"为真 → emit `converged` + `run_end` → 跳 freeze。

**决策已定 — run_id**:确定性 python 脚本取系统时间,format = **`yyyy-mm-dd-hh-mm-ss`**(精确到秒,杜绝一天多跑同名覆盖)。

### 叶子脚本编排总览(本设计的结构基石,贯穿后续所有 H)

依据 skill-creator 规范(`scripts/`=确定性可执行代码,可执行而不必读入上下文;`references/`=按需读入的文档),**所有叶子 py 归入 `optimization-loop/scripts/`**;阈值表/启发式说明这类"要读懂的文档"归 `references/`。

**触发机制**:SKILL.md 是文字,optimizer-CC 读后**用 Bash 调 `python scripts/xxx.py ...`**。脚本之间**不互相调用**,全部由 optimizer-CC 按 §loop 次序串联(CC 是驱动器,py 是叶子)。SKILL.md 的 **§tools 段**逐个登记每个脚本:做什么·何时调·输入·输出落哪·下一步。

#### 技能目录结构

```bash
optimization-loop/
├── SKILL.md                  # 厚 skill 正文:§loop/§gate/§backprop/§state/§tools
├── scripts/                  # 全部叶子 py(确定性,CC 用 Bash 调,不互调)
│   ├── new_run_id.py         # 取系统时间 → yyyy-mm-dd-hh-mm-ss,返回 run_id
│   ├── gen_configs.py        # 读权重→插值/组装/话术→48 config(过 leak_audit)
│   ├── save_transcript.py    # 读 exec 的 session jsonl(type∈user/assistant)→ transcripts/<sample>.md
│   ├── concat_triple.py      # 从 transcript/日志抽 graph/result → 三元组
│   ├── run_codex_loss.py     # 起 codex 算 loss-1(per-run)/ loss-2(per-topic)
│   ├── gate_eval.py          # 门控算术:topic_passes / batch_pass_ratio / converged
│   ├── apply_weight_update.py# 执行 weights.revise(三权重之一)+ 落 revision_log
│   ├── write_dataset.py      # 隐私白名单裁字段 + schema 校验 → dataset/
│   └── trace_emit.py         # 追加一行 trace.jsonl(11 事件统一入口)
└── references/               # 按需读入的文档(非可执行)
    ├── gate-thresholds.md    # 门控阈值全表(≥90% / τ≥0.7 / ≥80% / 连续3)
    └── backprop-heuristic.md # §backprop 留薄段的详细启发式(智能点③)
```

#### 脚本编排表(触发时机 · 输入 · 输出)

| 脚本 | 何时被 CC 调 | 输入 | 输出 / 落盘 |
| --- | --- | --- | --- |
| `new_run_id.py` | epochs-loop 启动,仅一次 | 无 | stdout: `2026-06-06-20-18-05`;建 `runs/<id>/` |
| `gen_configs.py` | 每 batch 开头 | 当前 weights | 48 份 `configs/<sample>.json` |
| `save_transcript.py` | 每 run 末(exec 收尾后) | exec 的 session jsonl, --logs-dir | `transcripts/<sample>.md`(只取 type∈{user,assistant}) |
| `concat_triple.py` | 每 run 末 | sample_id(读 configs/ + transcripts/) | `triples/<sample>.json` |
| `run_codex_loss.py` | loss-1 每 run / loss-2 每 topic | payload + 哪个 loss | `loss/<...>.json` |
| `gate_eval.py` | 每 topic 末 + 每 batch 末 | loss 结果 | stdout: 收敛 bool |
| `apply_weight_update.py` | batch 没过、反向传播时 | target/key/new/reason | 改权重 + `revision_log.jsonl` |
| `write_dataset.py` | 每 topic 末 | triples | `dataset/<topic>/<sample>.json` |
| `trace_emit.py` | 每个 trace 事件点 | event + fields | 追加 `trace.jsonl` |

> 落点说明:全部叶子 py 从零写进 `optimization-loop/scripts/`(skill-creator 规范:`scripts/` 自洽可执行);三个权重本体 `axes.py`①/`interpolator.py`②/`assembler.py`③ 写进 `generator/` 包(与 `cards.py`/`leak_audit.py` 同包,配套 pytest 同写该路径),由 `gen_configs.py` `import` 调用、由 `apply_weight_update.py` **改其在 `weights/<batch>.json` 中对应的数据段**(数据派,`.py` 源码不动)。
>
> **从零全写(落地纪律,与 Spec A 一致)**:本设计是「设计规格」,全部组件从零写进新目录 `self-iteration/2026-06-07-probe-pretrain/`。设备上旧的 `2026-06-06-probe-pretrain/` 及其 ~20 个 .py / 测试**一行不看、不继承、不迁移**(避免旧 fake nesting、脆弱 `extract_blocks` 等误导)。组件构建与单测的完整规格见 Spec B;真模型组件守 no-e2e-shell 铁律,绝不 fake-stub 凑绿。

#### `new_run_id.py`〔NEW · scripts/〕

- 职责:确定性取系统时间,返回 `yyyy-mm-dd-hh-mm-ss` 格式 run_id;建 `runs/<run_id>/` 目录骨架(trace.jsonl / configs/ / transcripts/ / triples/ / loss/ / weights/)。
- 触发:epochs-loop 最外层入口,仅一次。
- CHECKPOINT(写):建 `runs/<run_id>/`;`trace.jsonl` 首行 `run_start` 由紧接的 `trace_emit.py` 写。

### 一个 epoch = m=8 topic × n=6 人设 = 48 run (LOOP-2)

**这一步做什么**
结构声明,不执行动作:告诉 optimizer "本轮 48 个样本怎么排布",并标定 batch 边界(`batch_start` 事件落点)。

**核心要点(§1 那处修正的根)**:48 不是 48 张独立卡,而是 **6 张 ladder 卡(id0→id5)× 8 topic**。6 人设那一维 = 同一条阶梯的 6 档,对 8 topic 各复用一遍。因此:

- interpolator 只造 **6 张卡**(下一条 H3 干的事),× 8 topic = 48 条 research_config。
- run 按 topic 成组:run 0–5 = topic0 的 6 档,run 6–11 = topic1 的 6 档……这是 loss-2 能 per-topic 聚合的前提。

**决策已定 — batch_id**:纯递增号 `batch-0 / batch-1 / ...`。weights 已被 `runs/<run_id>/weights/` 隔离,batch_id 无需再带 run_id;它同时是 `weights/<batch_id>.json` 的命名键。batch_id 由 optimizer-CC 在 §state 维护——**恢复规则:取 weights 目录已有的最大编号本身(不 +1)**。这条规则成立的不变式是:**每个非终结 batch 都恰好预写一份 `weights/<batch+1>.json`**——未过闸批由 F2(backprop)写改后的新权重,过闸但未收敛批由 F1 **原样拷贝**写一份(见 `### IF 连续 3 个 batch 过闸` 的三分支表与 F1 节),仅收敛(T)与训练结束时不再预写。故"目录里最高编号的文件 = 下一个要跑的 batch 的权重"恒成立。冷启动时目录只有 `weights/batch-0.json`(由 `dump_initial` 导出),max=0 → batch_id=0 → 读 `batch-0.json`,自洽;一批跑完(F1 或 F2)写了 `batch-1.json` → max=1 → 下个 batch_id=1 → 读 `batch-1.json`。无需单独脚本。

**触发**:进 batch 时 `trace_emit.py` emit `batch_start`;之后立即进 `interpolator 插值获取 48 条 research_config`。

**CHECKPOINT(写)— `batch_start` 事件**

落点:`runs/<run_id>/trace.jsonl` 追加**一行** JSON(jsonl,每行一事件,实时 append,可 `tail -f`)。对齐 `probe-pretrain-trace/index.html` ③ 节 schema:每条 = 公共头 + 事件专有体。

公共头(每条事件都有,共 7 字段):

| 字段 | 类型 | 含义 | 本事件取值 |
| --- | --- | --- | --- |
| `ts` | ISO8601 str | 时间戳 | 写入瞬间系统时间 |
| `run_id` | str | 一次训练 | `2026-06-06-20-18-05` |
| `event` | str | 事件名 | `"batch_start"` |
| `batch_id` | str | 所在 batch | `"batch-0"` |
| `topic_id` | str\|null | 所在 topic | `null`(batch 级) |
| `rung_id` | int\|null | 所在档 | `null`(batch 级) |
| `seq` | int | 单调递增序号,断点续看用 | 全程自增 |

`batch_start` 专有体:

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `weights_snapshot_path` | str(相对路径) | 本 batch 用的权重快照,指 `weights/<batch_id>.json`;隐私红线:相对路径,绝不含绝对 log 路径 |

样例行(单行落盘,此处为阅读换行):

```json
{"ts":"2026-06-06T20:18:07+08:00","run_id":"2026-06-06-20-18-05","event":"batch_start","batch_id":"batch-0","topic_id":null,"rung_id":null,"seq":2,"weights_snapshot_path":"weights/batch-0.json"}
```

> 注:`run_start`(seq 通常为 1)在 epochs-loop 入口先于本事件落,其专有体 = `{n:6, m:8, config_path, weights_snapshot}`(见 `## epochs-loop` H2)。本 H3 只负责 `batch_start`。

### interpolator 插值获取 48 条 research_config

**这一步做什么**
本 batch 开头,用当前三权重把 6 张 ladder 卡(id0→id5)造出来,× 8 topic = 48 条 research_config(=48 个 sim 人设)。本 H3 的 6 个 H4 子步是单脚本 `gen_configs.py` 的内部调用链。

**interpolator 是什么**:它是**铺阶梯的那只手**——决定 6 档在 5 个标签轴上各取什么等级,使 6 个样本连成一条**单调下降、相邻拉得开**的质量阶梯。它不插值数字,插值的是"监督压力"。输出 6 组轴坐标,交 assembler 组装、axes 填话术。它是可训练权重②:阶梯铺塌(相邻撞档/中间没区分度)或铺挤(端点没拉开)都会让 loss-2 挂,所以"怎么摊、怎么错开、拉多开"这套规则要被 optimizer 按 loss-2 反复修。

#### 三分法(本设计的核心 — 经三轮 insight 推出)

经 evaporating-cloud → assumption-stress-test → CLR 三轮分析,interpolator 内部劈成**三层**,只有最外层可训练:

| 层 | 内容 | 处置 | 理由 |
| --- | --- | --- | --- |
| **名次层** | id0>id1>…>id5 的方向与名次;主排序轴 {A1,A3,A2} 复合序(spec §2) | **锁死** | 这是标签定义。动它=标签随训练漂移=数据集失效(命根子) |
| **标签坐标层** | 每档在 A1–A5 上的具体等级值 | **锁死** | 由名次层决定;**扰动绝不许碰** |
| **铺陈层** | ① 撞档用什么错开 ② 端点拉开幅度 ③ L0–L4 粒度运用 | **可训练**(=`interp_params`) | 只影响阶梯质量、不碰标签;loss-2 塌时 optimizer 掰这里 |

**验证句**:optimizer 改完后,"id0 比 id5 好"永不变(名次层+坐标层锁着),变的只是"6 档怎么被铺得单调又拉得开"(铺陈层在训)。

#### ★关键约束: 撞档扰动只许用 B1 / 表达层,绝不许用 A1–A5

assumption-stress-test 挖出的头号危险假设(AS-3):现有 `secondary_perturbation` 用 **A2/A3 错开撞档是个 bug**——A2(合法性)、A3(操作化坚持)本身就是 LABEL 轴,用它们错开 = 改了那档的标签坐标。

**修正**:撞档扰动只能用 **B1(framing,CONFOUND 轴,非 LABEL)** 或**纯表达层手段**(话术措辞、详略)错开,**严禁动 A1–A5 任何 LABEL 轴**。这要求 `interp_params` 在工程上把"铺陈字段"与"标签坐标字段"**物理隔离存储**,使 optimizer 改铺陈时碰不到坐标(把 AS-5/AS-6 从假设变成强制实现约束)。

#### ★可训练性是有条件的(CLR 校验 AS-4 的产物)

CLR 校验发现"loss-2 塌→改铺陈一定掰得回"**只在特定条件下成立**(最严重保留=范畴4原因不充分:端点分离上限被锁死坐标钉死)。由此三条设计后果,写入 §backprop 与 pilot:

1. **§backprop 先归因再动手**:optimizer 见 loss-2 塌,先判子类型——
   - **端点没拉开** → 可能是锁死坐标的锅(interpolator 掰不动)→ 信号指向话术层①或报警,**不硬训 interpolator**。
   - **中间档单调破/撞糊** → 这才是 interpolator 铺陈层的活。
2. **PT5 pilot 加验收项**:除原 RR-1(端点能否产出"可评判但差"文档),还须验"**改铺陈 loss-2 到底会不会动**"(CLR 范畴7:此预测目前无证据)。pilot 里改铺陈 loss-2 纹丝不动 → AS-4 证伪 → interpolator 可训练性是空的(比 RR-1 更早该亮的红灯)。
3. **端点坐标先天拉够远**:id0/id5 的 A1–A5 坐标在 endpoint cards 设计时就要拉到足够远,给铺陈层留可操作余量。这是 interpolator 可训练性的**前置条件**。

#### `gen_configs.py` 整体〔NEW · scripts/〕

- 职责:跑完下面 6 个 H4 调用链,产出 48 config。脚本本身是确定性管道;"可训练"体现在它**读取的 `interp_params` 等权重**会被 optimizer 在 §backprop 改。
- CHECKPOINT(写):48 份 `runs/<run_id>/configs/<sample>.json`(三元组第 1 元,sim 人设全文)。sample 命名 `<batch_id>-topic<NN>-id<N>`(对齐 index.html ④,如 `batch-0-topic05-id0`)。

#### 读权重 weights/\<batch\>.json

`weights.load`〔KEEP〕读 `runs/<run_id>/weights/<batch_id>.json`,取回三权重的当前值。本步只读;interpolator 用到的是其中的 `interp_params` 段(=铺陈层旋钮:撞档错开方式、端点拉开幅度、L0–L4 粒度运用)。名次层与标签坐标层不在 `interp_params` 内(它们锁死,不随权重走)。CHECKPOINT(读):`weights/<batch_id>.json`。

**`weights/<batch_id>.json` 字段布局(全文唯一定义处,十余处引用回指此表)**

顶层三段,一一对应三个可训练权重;另加一个只读的锁死段 `frozen_label`(放名次层+标签坐标层,**任何 revise 都不许碰**,放此仅为单文件自洽与可审计):

| 顶层键 | 对应权重 | 谁读 | 谁写 | 可训练? |
| --- | --- | --- | --- | --- |
| `axis_prose` | ①档位话术 | `axes.level_text` | `apply_weight_update`(target=`axis_prose`) | 是 |
| `interp_params` | ②插值器铺陈层 | `interpolator.ladder_levels` | `apply_weight_update`(target=`interp_params`) | 是(仅铺陈层) |
| `assembler_params` | ③组装逻辑 | `assembler.build_batch` | `apply_weight_update`(target=`assembler_params`) | 是 |
| `frozen_label` | 名次层+标签坐标层 | interpolator/assembler 只读 | **无人写**(锁死) | **否** |

各段内部字段:

- **`axis_prose`** — 按(轴, 等级)索引的话术文本表。`{ "<axis>": { "<level>": "<话术正文>" } }`,axis∈{A1,A2,A3,A4,A5},level∈{L0..L4}(A4 用 C+/C-、A5 用 G+/G-)。`axes.level_text(axis,level)` 即查此表。revise 改某个 cell 的正文。
- **`interp_params`** — ②的铺陈层旋钮,且**物理隔离**(AS-3/AS-5/AS-6 强制):
  - `collision_offset_axis` — 撞档错开**只许**取 `"B1"` 或 `"expression"`(★schema 层禁写 A1–A5,见 L494);
  - `endpoint_spread` — 端点拉开幅度旋钮(影响 id0/id5 在铺陈上的距离,**不改坐标**);
  - `granularity_map` — 6 档→L0–L4 的映射函数参数(现为 `round(t*4)` 的可调版)。
  - ⚠️ 此段**绝不含任何轴坐标值**;坐标在 `frozen_label`,二者分文件段存放,使 optimizer 改铺陈时物理上够不到坐标。
- **`assembler_params`** — ③组装旋钮:`two_stage`(M1 先坐标后扩卡的开关/参数)、`field_template`(F0–F9 卡字段的组装模板)、`f6_derivation`(F6 acceptance 由 F1/F3/F2 派生的规则参数)、`turn_budget`(=F8,batch 内恒定的 confound 控制,即 `pressure_turns`/`closing_turns`)。⚠️ 现有 `assembler.py` 把这些硬编码在源码里(代码派债),数据派下须全部外移进本段,由 `assembler.build_batch` 读取(源码不动)。
- **`frozen_label`**(只读锁死) — `rank_order`(`id0>…>id5` 方向 + 主排序轴 {A1,A3,A2} 复合序定义)+ `coord_table`(每档在 A1–A5 上的等级值)。**这是标签的命根子**;`apply_weight_update` 见 target 落在此段一律拒绝并报错。

> 隔离落地:`interp_params` 与 `frozen_label.coord_table` 是**两个独立顶层段**,序列化时不交叉引用。这把"铺陈字段与标签坐标字段物理隔离"(L494/521)从口头约束变成 JSON 结构层的硬保证——optimizer 的 revise 只接受三个可训练顶层键,`frozen_label` 不在白名单。
> **batch-0 初始值来源**:首个 batch 的 `weights/batch-0.json` 由三权重本体(`axes.py`/`interpolator.py`/`assembler.py`)的**默认值导出**(`weights.dump_initial`),非手填;此后每 batch 由 `apply_weight_update` 增量改写并另存 `weights/<batch_id>.json`。

#### 调 interpolator.ladder_levels(n=6) → 6 档等级映射

〔WEIGHT② interpolator.py〕把 6 档映到 L0–L4 五个等级。**名次层(锁死)**:id0→id5 单调下降的方向、主排序轴 {A1,A3,A2} 复合序——这部分是死的。**铺陈层(可训练)**:具体映射函数(现为 `round(t*4)`)如何把 6 档摊到 5 级、撞档落在哪,可被 optimizer 经 `interp_params` 调。现有 `detect_collapse` 检测撞档点保留。

#### 调 assembler.build_batch(...) → 6 档坐标组装

〔WEIGHT③ assembler.py〕把各档的轴等级组装成完整坐标元组(M1 两阶段:先吐坐标、再扩成卡)。撞档扰动在此发生——**★只许用 B1(framing,CONFOUND 轴)或表达层错开,严禁动 A1–A5 任何 LABEL 轴**(AS-3 修正)。现有 `secondary_perturbation` 用 A2/A3 是 bug,落地时改为 B1。`interp_params` 须把"铺陈字段"与"标签坐标字段"物理隔离,保证 optimizer 改铺陈碰不到坐标。

#### 调 axes.level_text(axis,level) → 填档位话术

〔WEIGHT① axes.py〕给每个(轴,等级)填话术文本(=卡的 F 字段内容)。这是权重①,不是 interpolator 的事,但在同一管道里被调。注:若 loss-2 端点没拉开的根因是话术不够分,§backprop 应改这里,而非硬训 interpolator(CLR 后果1)。

#### 每张卡过 leak_audit(text) → W5 拦 check 词

〔KEEP leak_audit.py〕每张卡组装完过 DENY 词表,拦截 32-check/6-primitive/检测签名词。命中处理(据 Stage 4 插值规则,决策已定):**丢弃该卡、重生成字段、再审**(`regenerate-then-reaudit`)——leak 命中是单卡话术问题,重生成该卡即可,不牵连其余 47 卡;重生成仍走权重①话术、仍 check-blind(不放宽 DENY)。**重试上限 3 次**仍命中 → 才硬中断 batch 并报警(防话术权重坏掉导致无限重生成空转)。CHECKPOINT:无(失败重生成;超上限则中断报警)。

#### 输出 6 卡 × 8 topic = 48 config json → runs/\<id\>/configs/

〔KEEP cards.to_dict〕6 张 ladder 卡 × 8 topic 序列化为 48 份 config。CHECKPOINT(写):`runs/<run_id>/configs/<sample>.json` × 48;sample 命名 `<batch_id>-topic<NN>-id<N>`(如 `batch-0-topic05-id0`)。每份 = research_config 全文(PolicyCard F0–F9 + 轴等级 A1–A5,B1),三元组第 1 元,也是 `rung_start.config_full` 的来源。

### [按 topic 成组] for topic_i in 8

**这一步做什么**
LOOP-1 的**外层循环**:8 个 topic 逐个过,每个 topic 内部再跑 6 档(内层,下一条 H4)。负责 `topic_start` 事件,并界定"一个 topic 的 6 档跑满后才触发 per-topic 聚合(loss-2 + 门控 + 写样本)"。

**规划**:optimizer-CC 按 §loop `for topic_i in 0..7`;每进一个 topic emit `topic_start`;内层 6 档跑完 → per-topic 聚合;`topic_i<7` 继续,`=7` END LOOP-1。循环由 optimizer-CC + §loop 驱动,无单独脚本。

> 结构说明:本节是 LOOP-1 的**唯一**外层 topic 循环;内层 6 档 run-body(下一条 H4)跑满后进 per-topic 聚合(loss-2 + 门控 + 写样本),再判 `topic_i<7`。

**决策已定 — topic 文本源**:`config/topics.json`,数组,每项 schema:

| 字段 | 含义 |
| --- | --- |
| `topic_id` | `topic-00`..`topic-07` |
| `title_short` | 一句话短标题(给 trace tail 时辨识用) |
| `full_text` | topic 完整描述(进 config,不进 trace) |
| `F7_prerequisite` | A4=C- 依赖的前置事实(D5 标准用) |

**[落地前置任务·有意延迟]** 8 个真 topic 内容**有意延迟**到 pilot 阶段(PT8/Task 8.2)填,非未决字段——此处只定**文件位置 + schema**(`topic_id`/`title_short`/`full_text`/`F7_prerequisite`)。旧规划已有容器(8 个文件 + F7 槽)但无现成候选内容。PT6 跑流程用占位 topic 即可跑通管线,真内容不阻塞编排实现。

**CHECKPOINT(写)— `topic_start` 事件**

落点:`trace.jsonl` 追加一行。公共头同前 7 字段(此事件 `topic_id` 取本 topic、`rung_id`=null)。专有体:

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `topic_title_short` | str | 取自 `config/topics.json` 的 `title_short`;**全文不进 trace**(已在 config + 后续 `rung_start.config_full` 双备),保 trace 可 tail |
| `intended_order` | int[] | `[0,1,2,3,4,5]`,本 topic 6 档的预期质量名次(id0 最好→id5 最差) |

样例行(单行落盘,此处阅读换行):

```json
{"ts":"2026-06-06T20:18:31+08:00","run_id":"2026-06-06-20-18-05","event":"topic_start","batch_id":"batch-0","topic_id":"topic-05","rung_id":null,"seq":7,"topic_title_short":"评估 DARE 技能编排多样性","intended_order":[0,1,2,3,4,5]}
```

#### for 档 in 6 ── 开始一次 run (LOOP-1)

**这一步做什么**
LOOP-1 的**内层循环**:在一个 topic 内从 id0 到 id5 跑 6 档,每档 = 一次完整 run(起 sim → sim 起 exec → 多轮 research → concat 三元组 → codex 算 loss-1)。每档进入时 emit `rung_start`,该事件**特殊**:它带这一档的人设全文 `config_full`,是 index.html ② 你点名要看的"用户模拟器人设完整全文"。

**规划**:optimizer-CC 按 §loop `for 档 in 0..5`;每进一档 emit `rung_start`(带 sample_id + config_full + axis_levels)→ 走该档 run body(下面 5 个 H5)→ 档 <5 继续,=5 跳出进 per-topic 聚合。config_full 来源是本档 `configs/<sample>.json`(gen_configs 已落)。循环由 optimizer-CC + §loop 驱动,无单独脚本。

**决策已定 — config_full 进 trace 放全文**(选项1,遵从 index.html ②):人设是最该盯的东西,一行 `rung_start` 即可看全这一档让 sim 扮什么;且 rung_start 一档只发一次(不像 dialogue_turn 每轮发),不会撑爆 trace。值得对"全文不进 trace"原则破此一例。

**CHECKPOINT(写)— `rung_start` 事件**

落点:`trace.jsonl` 追加一行。公共头 7 字段(此事件 `topic_id`、`rung_id` 均取实值)。专有体(对齐 index.html ③):

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `sample_id` | str | `<batch_id>-topic<NN>-id<N>`,如 `batch-0-topic05-id0` |
| `config_full` | obj | PolicyCard F0–F9 **verbatim**(人设全文) |
| `axis_levels` | obj | `{A1..A5, B1}` 该档各轴等级 |

样例行(单行落盘,此处阅读换行):

```json
{"ts":"2026-06-06T20:18:33+08:00","run_id":"2026-06-06-20-18-05","event":"rung_start","batch_id":"batch-0","topic_id":"topic-05","rung_id":0,"seq":8,"sample_id":"batch-0-topic05-id0","config_full":{"F0":"...","F9":"..."},"axis_levels":{"A1":"L0","A2":"L0","A3":"L0","A4":"C+","A5":"G+","B1":"neutral"}}
```

##### 起 sim-模拟器-cc(交互式 REPL,每 run 全新)

**这一步做什么**
一次 run 的第一个动作:optimizer-CC 在自己的 Bash 工具里**直接跑 `claude`**,起一个全新的交互式 sim-cc 会话,随后两个 CC 正常来回对话。sim 是正常交互式会话(非一次性),活到本 run 结束。无任何驱动脚本、无 PTY、不进 tmux。

**真实命令形态(实测 claude 2.1.167)**:optimizer 的 Bash 工具里执行
`IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/sim/.claude bash -lc 'cd /workspace/work/sim && claude'`。
`IS_SANDBOX=1` 是 root 起 bypass REPL 必需;config-dir 靠环境变量(无 `--config-dir` flag)、工作目录靠 `cd`(无 `--cwd` flag);bypass 由该 config-dir 的 `settings.local.json` 提供,工具调用全程放行。sim 的 cwd 无技能,人设全靠注入。起好后 optimizer 就在这个会话里正常发消息、读回复,多轮对话即天然进行。

**几个要点**:

- sim 每 run 全新启动,run 结束会话关闭;不跨 run 复用(避免人设污染)。
- sim 要在自己的 Bash 工具里**同法直起 `claude`** 起 exec —— bypass 已放行,无需额外授权。
- sim 这场会话由 claude 自动落 sim 的 session jsonl;transcript 以 exec jsonl 为准,故 sim jsonl 仅备查。

**CHECKPOINT**:本步不直接落盘;sim 对话自动进 sim 的 session jsonl。

###### Bash 直起 claude(IS_SANDBOX=1 + CLAUDE_CONFIG_DIR=sim + cd /workspace/work/sim),无驱动脚本

**这一步做什么**
把"起子 CC"这一物理动作讲清楚:它**不是**一个脚本,而是父 CC 在自己的 Bash 工具里直接跑一句 `claude`。子 CC 起来后就是一个正常的交互式会话,父 CC 用正常发消息的方式与它来回多轮——这正是两个 CC 天然就能做的事,无需任何居中的驱动器。

**为什么不需要驱动脚本**
父 CC 本身就是一个能用 Bash、能多轮对话的 agent。起子 CC = 一句 `claude`;跟子 CC 多轮 = 父 CC 在这个会话里一轮轮地正常发话、读回复,看一轮想一轮再回一轮(自适应施压的判断写在 `optimization-loop` 厚 skill 里)。"判断"在 skill、"对话"是 CC 原生能力,中间没有第三者,也就没有脚本要写。

**命令形态(实测 claude 2.1.167):**

- 起:`IS_SANDBOX=1 CLAUDE_CONFIG_DIR=<角色 .claude> bash -lc 'cd <角色 cwd> && claude'`。`IS_SANDBOX=1` 是 root 起 bypass REPL 必需;config-dir 靠环境变量(无 `--config-dir` flag)、工作目录靠 `cd`(无 `--cwd` flag);bypass 由该 config-dir 的 `settings.local.json` 提供。
- 角色差异:optimizer 起 sim 用 sim 的 config-dir + `/workspace/work/sim` cwd;sim 起 exec 用 exec 的 config-dir + `/workspace/work/exec` cwd(其 config-dir 内复制了 771 DARE 技能)。机制同源,只换这两个参数。
- 多轮:父 CC 在该会话里正常发消息、读回复,直到任务完成;无暗号、不塞标记,不污染语料。
- 收尾:任务完成即关闭子会话,本 run 作废该会话(不跨 run 复用)。
- 权威 transcript:以子 CC 自己落的 session jsonl 为准(`$CLAUDE_CONFIG_DIR/projects/<cwd-slug>/<sessionId>.jsonl`),后续由 `save_transcript.py` 从 exec jsonl 提取(单一真相源 + privacy)。

**CHECKPOINT**:本步不直接落 `trace.jsonl`;子 CC 对话由 claude 自动落该角色 session jsonl,后续由 `save_transcript.py` 从 exec jsonl 提取权威 transcript。

##### optimizer 经 conversation 注入 research_config 给 sim

**这一步做什么**
sim REPL 起好后,optimizer 把本档的 research_config(PolicyCard F0–F9 全文)连同一段「监工指令」作为第一轮消息发给 sim:让 sim 扮演这张卡描述的用户人设,自己去起 exec、盯着它跑完整 research,完事回一个约定信号。这是 optimizer→sim 的唯一指令注入点;之后 optimizer 不再插手,等 sim 回信。

**注入内容(三块):**

1. **research_config 全文** —— PolicyCard F0–F9 verbatim(人设、偏好、施压强度等),sim 据此「成为」这个用户。
2. **监工指令** —— sim 的职责说明:你要起一个 exec 子 CC,把 topic 交给它,全程以这个用户人设与它多轮对话,直到 research 完成。
3. **两条硬性要求(用户口吻)** —— 作为「这个用户的死规矩」让 sim 转嫁给 exec:① 做规格必须用 `formated-specs` 而非 `writing-specs`;② 收尾必须调 `formated-results`。sim 要盯着执行,exec 不照做就打回。

**强制项为何放在 sim 这层**:sim 模拟「有硬性偏好的用户」,这两条本质是用户的死规矩,由 sim 角色施加最自然。它在两层都出现但措辞不同——给 sim 是「监工指令」(盯着 exec 用,否则打回),给 exec 是「执行指令」(你现在就用 formated-specs 做)。

**CHECKPOINT**:本步是 sim 会话内的一轮对话,自动进 sim session jsonl;不单独落 `trace.jsonl`(run/batch/topic/rung 级事件已分别由对应步骤落)。

###### 首轮消息: config 全文 + 扮演指令 + 「起 exec 跑完 research,回我 DONE」

**这一步做什么**
optimizer 在 sim 会话里**直接发出第一轮消息**(就是它 Bash 起 `claude` 后正常输入的第一段话)。这条消息是 sim 整场会话的「身份 + 任务书」。无 `--msgs` 文件、无驱动脚本——optimizer 自己组织这段文本并发给 sim 即可。

**消息体结构:**

- **〔config json 全文〕** PolicyCard F0–F9 verbatim,告诉 sim「你是谁、什么偏好、施压多狠」。
- **〔扮演指令〕** 「以上是你的用户人设,完全代入。接下来你要在自己的 Bash 工具里直接跑 `claude` 起一个 exec 子 CC,把研究题目交给它,全程以这个人设和它多轮对话,直到它产出完整 research_result。」
- **〔两条硬性要求〕** 「这个用户有两条死规矩,你必须盯着 exec 照做:① 做规格只许用 `formated-specs`,禁用 `writing-specs`;② 收尾必须调 `formated-results`。不照做就打回重做。」
- **〔回信约定〕** 「research 完成、拿到 result 后,关闭 exec,回我一条 `DONE`(及 result 所在位置)。」

**约定信号 DONE**:sim 完事回 `DONE`,optimizer 据此知道本 run 的 sim 任务结束,进入下一步(关 sim、concat 三元组)。`DONE` 只是 sim→optimizer 的收尾握手,不污染 exec 的研究语料(transcript 取自 exec jsonl,不含这层握手)。

**CHECKPOINT**:首轮消息是 run 内临时内容,不单独落盘;不进 `trace.jsonl`。research_config 全文已在 `rung_start` 事件的 `config_full` 字段落盘(行 588),此处不重复落。

####### sim-cc Bash 启动 dare-exec-cc

**这一步做什么**
上一步 optimizer 已把人设 + 任务书注入 sim;sim 现在执行任务书的第一个动作——在**自己的 Bash 工具里直接跑一句 `claude`**,起一个全新的 dare-exec-cc 会话。机制与 optimizer 起 sim **完全同源**(见上节「Bash 直起 claude」:直起、IS_SANDBOX=1、config-dir 靠环境变量、cwd 靠 `cd`、bypass 靠 settings.local.json、无驱动脚本、不进 tmux)。本节只讲 exec 相对 sim 的**三处差异**,不重复通用机制。

**exec 相对 sim 的三处差异:**

| 维度 | sim(模拟用户) | exec(DARE 执行体) |
| --- | --- | --- |
| config-dir | `/workspace/home/sim/.claude`(**skills/ 仅 superpowers**,人设全靠注入) | `/workspace/home/exec/.claude`(**skills/ 内复制 771 DARE + formated-specs/results + superpowers**) |
| cwd | `/workspace/work/sim`(产出隔离,**不决定技能可见性**) | `/workspace/work/exec`(产出隔离,**不决定技能可见性**) |
| env / bypass | `IS_SANDBOX=1` + 该 config-dir 的 `settings.local.json` bypass | **同左,无差异** |

**为什么 exec 有技能、sim 没有**
exec 是真正干 research 的 DARE 执行体,要调度整套 773 技能库(含本系统强制的 `formated-specs` / `formated-results`),所以这些技能被**复制进 exec 的 config-dir `skills/` 目录**。sim 只是「扮演一个有偏好的用户」,判断与施压靠注入的人设文本,其 config-dir 的 `skills/` 只放 superpowers——技能反而会污染它的用户角色。**技能可见性由各身份 config-dir 内复制了哪些 skill 决定(非 mount、非 cwd)**;cwd 只负责产出隔离。这正是四个 config-dir 必须独立的根本原因。

**命令形态(与上节同源,仅换两参):**

```bash
IS_SANDBOX=1 CLAUDE_CONFIG_DIR=/workspace/home/exec/.claude \
  bash -lc 'cd /workspace/work/exec && claude'
```

sim 在自己的 Bash 工具里执行此句;bypass 已由 exec config-dir 的 `settings.local.json` 放行,无需额外授权。起好后 exec 就是一个正常交互式会话,sim 用正常发消息的方式与它来回多轮(注入 topic 是**下一个 H** 的事,本节只负责「把 exec 拉起来」)。

> **[落地前置·路径对账]** 四身份 cwd `/workspace/work/{optim,sim,exec,loss}` 与四 config-dir `/workspace/home/{optim,sim,exec}/.claude`、`/workspace/home/loss/.codex` 由环境搭建阶段(Spec A)从零建好。隔离本质是两套维度:①**技能可见性由各身份 config-dir 内复制了哪些 skill 决定**(exec config-dir 复制了 773+formated+superpowers、sim 只复制 superpowers;非 mount、非 cwd);②会话/配置隔离由四个 `CLAUDE_CONFIG_DIR` 决定;cwd 只管产出隔离。**topic 源口径(落地前二选一)**:本文档用 `config/topics.json` 单文件数组(schema 见 L593 一带);若改用分散 `topics/topic-0N.md`,须同步改本文档读法。隐私红线:session jsonl 绝对路径只走 `jsonl_reader(--logs-dir 必填)`,绝不进落盘产出。

**几个要点:**

- exec 每 run 全新启动,run 结束随之关闭;不跨 run 复用(与 sim 同样的 between-run 独立性,避免上一题的研究语境串进下一题)。
- exec 这场会话由 claude 自动落 **exec 的 session jsonl**——这是本系统**权威 transcript 的唯一来源**,后续 `save_transcript.py` 只读它(sim jsonl 仅备查)。
- 嵌套关系:这是「optimizer→sim→exec」三层里最内层的点火。sim 此刻既是「被 optimizer 驱动的子」,又是「驱动 exec 的父」,双重身份在同一个 sim 会话内并存。

**CHECKPOINT**:本步不直接落 `trace.jsonl`;exec 会话由 claude 自动落 exec 的 session jsonl,供后续 `save_transcript.py` 提取权威 transcript。run/topic/rung 级 trace 事件已分别由对应步骤落。

####### sim-cc 注入 i_m topic + 用户偏置 + 强制技能项

**这一步做什么**
exec 会话已拉起,sim 现在发出**给 exec 的第一轮消息**——把研究任务正式交给 exec。这是 sim→exec 方向的指令注入,与上层「optimizer→sim 首轮消息」平行,但口吻相反:给 sim 的是「**监工指令**」(你盯着 exec 用),给 exec 的是「**执行指令**」(你现在就照做)。sim 全程以注入的用户人设(research_config)说话,把"这个用户想研究什么、有什么偏好、有哪两条死规矩"如实压给 exec。

**消息体三块(对应下面三个子项):**

1. **topic + 用户偏置** —— 本档要研究的题目全文(来自 `config/topics.json` 的 `full_text`)+ 这个用户人设对研究方式的偏置(来自 research_config 的 PolicyCard,如 A1 实质性要求、A3 操作化坚持的强度)。sim 用人设口吻把题目和偏好讲给 exec。
2. **★强制:用 formated-specs 替代 writing-specs** —— 用户的第一条死规矩。
3. **★强制:最后必须调 formated-results** —— 用户的第二条死规矩。

**两条强制项为何必须、性质为何不对称:**
两条都服务于同一目标——让数据集**可机读、可路由进 32-check 探针**:graph/result 必须由 formated 系列产出规整结构(承接 A2 裁决:concat 直接取结构化块,不再脆弱解析)。但两条的性质不对称:

- **formated-specs 替代 writing-specs = 库层替换**。exec 库里规格槽位已被 formated-specs 顶替,writing-specs 不在 exec。规格步天然走 formated,sim 的强制是"确保规格步确实发生"的**对齐性监督**(偏轻)。
- **最后必须调 formated-results = 指令层追加**。这一步不在 DARE 默认流程里,必须靠强制让 exec 在收尾时**额外执行**。sim 须**主动盯死**:exec 不调就不算完成、不放 DONE(偏重)。

它们在 optimizer→sim 那层是「监工指令」(sim 盯着 exec),在这层 sim→exec 是「执行指令」(exec 照做)。

**sim 的施压如何体现:** topic 是固定的,但"用户偏置"随档位(rung)变化——id0 是高实质/高操作化要求的"天才用户",id5 是低要求的"荒谬-抬杠用户"。同一 topic 的 6 档,sim 注入的偏置话术由 research_config 决定(即权重①档位话术的产物),这正是 6 档拉开质量阶梯的源头。

**CHECKPOINT**:本步是 sim→exec 会话内的对话轮,自动进 exec 的 session jsonl(权威 transcript 来源);不单独落 `trace.jsonl`。topic 全文已在 `rung_start.config_full` 间接覆盖(config 含 topic 引用),此处不重复落。

######## topics[i_m] 文本 + 用户偏置 (来自 config)

**这一步做什么**
消息第一块的具体内容。`topics[i_m]` = 本 topic 的题目全文,取自 `config/topics.json` 第 `i_m` 项的 `full_text` 字段(schema 见行 546 一带:`topic_id` / `title_short` / `full_text` / `F7_prerequisite`)。**用户偏置** = 本档 research_config(PolicyCard)里描述这个用户"想要什么样的研究"的部分——施压强度由档位决定。sim 把两者揉成自然的用户开场:"我想研究 X(题目),我特别在意 Y(偏置)……"。

**CHECKPOINT**:无(对话轮,落 exec jsonl)。

######## ★强制: 用 formated-specs 替代 writing-specs

**这一步做什么**
消息第二块。sim 以用户口吻下死命令:"做规格阶段,用 `formated-specs`。" 关键事实(决定本条性质):在 exec 的 DARE 技能库里,**`formated-specs` 已顶替 `writing-specs` 的槽位**——即 exec 做规格那一步天然走到的就是 `formated-specs`,`writing-specs` 不在 exec 库内。所以本条本质是"库层已替换"(规格槽位先天就是 formated),sim 的强制是**对齐性监督**:确保 exec 确实走到了规格这一步、产出了 formated 结构,而非"在两个技能间二选一"。原因(写给你看,不必写进给 exec 的话):`formated-specs` 产出结构规整的 spec,使 research_graph 可被 concat 直接取结构化块、进而路由进 32-check 探针;自由格式的 spec 会破坏可机读性,这正是当初用 formated-specs 顶替 writing-specs 的理由。

**CHECKPOINT**:无(对话轮,落 exec jsonl)。

######## ★强制: 最后必须调 formated-results

**这一步做什么**
消息第三块。sim 以用户口吻下第二条死命令:"research 收尾时,最后一步必须调 `formated-results`。" 原因:research_result 必须是 formated 结构,才能被 concat 取出 result 块、与 graph/config 拼成三元组喂给 codex 算 loss。这是三元组第 3 元(research_result)可机读的保证。sim 盯着 exec 收尾,没调 formated-results 不算完成、不放 DONE。

**CHECKPOINT**:无(对话轮,落 exec jsonl)。

####### sim-cc ↔ exec-cc 反复 conversation 完成 research

**这一步做什么**
本 run 的主体:sim 把 topic+偏置+两条强制注入后,sim 与 exec 进入**多轮自适应对话**,直到一次完整 research 完成。exec 跑 DARE research(用它的 773 技能:规格走 formated-specs、推进各 research 阶段);sim 以用户人设逐轮审视 exec 的产出,按档位强度施压(id0 高实质/高操作化要求、紧盯不放;id5 低要求/抬杠),不满意就追问、打回、加压。这正是不同档位拉开质量阶梯的发生现场——同一 topic,sim 的施压强度不同,exec 被逼出的 research 质量就不同。

**多轮如何进行(承接上节机制,无脚本):**
这就是两个交互式 CC 正常来回对话:sim 在自己会话里发一句、读 exec 回一句、再据此发下一句——看一轮、想一轮、再回一轮。"聊什么、聊几轮、何时停"是 sim 的**判断**(由注入的人设 + `optimization-loop` skill 的对话纪律驱动);"把话发出去、读回复"是 CC 原生能力。中间无驱动器、无 PTY、无暗号。

**停止判据(sim 何时认为 research 完成):**

- 主判据:exec 完成了完整 research 闭环——**末步已调 formated-results 并产出结构化 research_result**(第二条强制达成)。
- sim 的人设决定"够不够":高档位用户(id0)会要求实质充分、操作化到位才罢手;低档位用户(id5)很快就接受。但**无论档位,formated-results 这一步是硬门槛**——没调,sim 不收尾、不放 DONE(退回上一 H 的强制监督)。
- 防失控:对话轮数上限 + 单轮超时由 `optimization-loop` skill 设阈(避免某 run 无限拉锯),触顶则标记该 run 异常、按缺陷样本处理(completability 失败,**不入数据集、不静默重试、不卡死**,RR-6/RR-7),不污染正常阶梯。具体落法(决策已定):
  - **轮数上限 = F8 两段**(`pressure_turns` 施压段 + `closing_turns` 收尾段),值由 PT5 pilot 定死后冻结(现 `config/pretrain.yaml` 占位 10+2)。作为 **sim 的软上限**(写进注入给 sim 的监工指令 + skill 对话纪律,sim 自己数到上限即进收尾段),非外部进程硬切 `for` 循环(那是旧 fake nesting 的产物)。
  - **单轮超时 = 父 CC 调 `claude` 的 Bash 工具 wall-clock 超时**(子 CC 卡住不返回时):无 PTY/无 send-keys 下,"单轮超时"实质是父 CC 这次 Bash 调用的墙钟超时;或由 skill 规定"子 CC 超过 N 分钟无返回即判该 run completability 失败"。阈值同样 pilot 期实测定(exec 跑一次 formated-specs 闭环要多久),写进 `references/`。

**CHECKPOINT(写)— 每轮落 transcript + `dialogue_turn` 事件**(详见下面子项)。这是脊柱点名的**★核心交互留存★**:所有人机交互内容的主体在此沉淀。

######## 每轮双向落 transcript

**这一步做什么**
sim↔exec 每完成一轮对话,就把这一轮沉淀下来,作为"所有人机交互内容"的主体留存。两件事并行发生:

1. **transcript 主体** —— `save_transcript.py` 读 **exec 的 session jsonl**(唯一权威来源),取 `type∈{user,assistant}` 的轮次,转写成 `runs/<run_id>/transcripts/<sample>.md`。"双向"指这份 transcript 同时含 sim 发给 exec 的话(在 exec jsonl 里记为 user 轮)和 exec 的回复(assistant 轮);**已实测确认**:读 exec 一侧 jsonl 即得完整双向对话,无需另读 sim jsonl(sim jsonl 仅备查)。
2. **trace 计数** —— 每轮 `trace_emit.py` 追加一行 `dialogue_turn{seq}` 到 `trace.jsonl`,记录对话进展(可 `tail -f` 看 run 活着、聊到第几轮),但**不含对话正文**(正文在 transcript.md,trace 只记 seq 保持可 tail)。

**落点与时机:** 落 `runs/<run_id>/transcripts/<sample>.md`(单一真相源 + 隐私:只取结构化对话内容,绝不含 CC log 绝对路径;`save_transcript.py` 的 `--logs-dir` 必填,指向 exec config-dir 的 jsonl 位置)。**时机已定:run 末一次性**从完整 exec jsonl 提取(`save_transcript.py` 每 run 只跑一次,见编排表行 411)。因 jsonl 是 append-only 全量记录,run 末一次提取即得完整对话,无需每轮增量写;run 进展的实时观测由 `dialogue_turn{seq}` 那条 trace 负责(可 tail),transcript 正文不必实时增长。

**CHECKPOINT(写):**

- `runs/<run_id>/transcripts/<sample>.md` —— 本 run 完整双向对话(★核心交互留存★)。
- `trace.jsonl` 每轮追加 `dialogue_turn{seq}`(公共头 7 字段 + 专有体仅 seq 计数;`topic_id`/`rung_id` 取本 run 实值)。
  > **★与 trace 源(`index.html` ③)的刻意差异:** 源把 `dialogue_turn` 专有体列为 `{phase, turn_idx, speaker, text_excerpt, transcript_path}`;**本设计刻意精简为仅 `seq`**(公共头已带 seq)。理由:对话正文整体落 `transcripts/<sample>.md`(run 末一次性提取),trace 只承担"可 tail 看 run 活着、聊到第几轮"的轻量计数职责,不重复承载正文摘要(`text_excerpt`)或每轮路径(`transcript_path`,全 run 同一份 .md,无需逐轮记)。`phase`/`speaker`/`turn_idx` 同理可从 transcript 复原,不入 trace。**本文档为实现权威**,落地 `trace_emit.py` 的 `dialogue_turn` 体以此处为准,不照搬 index.html。

####### 得到 research_result

**这一步做什么**
sim↔exec 多轮对话收束:exec 末步调 `formated-results`,产出结构化的 **research_result**——这是三元组的第 3 元。此刻 research_result 已存在于 exec 会话中、并随对话落进 exec 的 session jsonl,但**尚未被抽出成独立产物**(抽出是后面 `concat` 那步的事:从 transcript 取 result 结构化块)。本 H 只标定一个事实节点:"研究产物已就位,可以收尾了"。

formated-results 这一步是第二条强制(指令层追加)的兑现点;sim 正是看到它产出、确认 result 结构完整,才认定 research 完成、进入关 exec。

**CHECKPOINT**:无。research_result 内容已随对话进 exec jsonl(后续 save_transcript 落 transcript、concat 抽 result 块);本步不单独落盘。

####### sim-cc 关闭 dare-exec-cc

**这一步做什么**
sim 确认 research_result 到手后,关闭 exec 会话——本 run 的最内层收尾。关闭即 exec 这场交互式会话结束,**但 exec 的 session jsonl 留盘**(save_transcript 与 concat 随后还要读它;它是权威 transcript 的唯一来源,绝不能随会话清掉)。

**between-run 独立性:** exec 关了就关了,**不跨 run 复用**——下一 run(无论同 topic 换档、还是换 topic)都全新起一个 exec,避免上一题/上一档的研究语境串进来。这与"sim 每 run 全新"是同一条独立性纪律,共同保证每个样本的标签(=该 run 的生成条件)干净对应一次独立 research。

**CHECKPOINT**:无(关闭动作;jsonl 已在对话过程中落盘,留存备读)。

####### sim-cc response "DONE" 给 optimizer

**这一步做什么**
exec 关闭后,sim 向 optimizer 回一条 **`DONE`**(附 research_result 所在位置)——这是 sim 这场会话的**末轮**,也是 sim→optimizer 的收尾握手。optimizer 收到 DONE,即知本 run 的"起 sim→sim 驱动 exec→拿到 result"全链完成,据此进入下一步(关 sim → concat 三元组 → codex 算 loss-1)。

**DONE 不污染语料:** `DONE` 只发生在 sim↔optimizer 这层,**不进 exec 的对话**;而 transcript 取自 exec 一侧 jsonl,天然不含这层握手。研究语料(transcript)与控制信号(DONE)物理分离,互不污染。

**CHECKPOINT**:无。DONE 是 sim↔optimizer 会话内的对话轮(落 sim jsonl,仅备查);run 收尾的正式 trace 事件是后面的 `rung_done`(行 135 一带,含 loss-1),不在本步。

##### optimizer 关闭 sim-模拟器-cc

**这一步做什么**
optimizer 收到 sim 的 `DONE` 后,关闭 sim 会话——本 run 的最外层收尾(与"sim 关 exec"对称,但高一层:exec 由 sim 关,sim 由 optimizer 关)。关闭即 sim 这场交互式会话结束,本 run 的 sim 角色作废。

**between-run 独立性(再申):** sim 关了就关了,**不跨 run 复用**。下一 run 全新起一个 sim(注入下一档/下一 topic 的人设)——这保证每个样本的人设 = 该 run 的生成条件,标签干净。**唯一跨 run 持续存活的只有 optimizer**(tmux 长驻);sim/exec 都是 per-run 即生即灭。

**此刻 run 内已落盘的东西(供下一步 concat 取用):**

- `configs/<sample>.json` —— 三元组第 1 元(gen_configs 已落)。
- `transcripts/<sample>.md` —— 完整双向对话(本步关 sim 后,save_transcript 已从 exec jsonl 提取完毕)。
- exec/sim 两份 session jsonl —— 留盘备查(transcript 已从 exec 侧提取,sim 侧仅备查)。

**CHECKPOINT**:无(关闭动作)。run 收尾的正式 trace 事件是后面的 `rung_done`(含 loss-1);本步只是关会话,不落 trace。

##### concat (research_config, research_graph, research_result)

**这一步做什么**
本 run 的数据收口:把三样东西拼成一个**三元组** `(research_config, research_graph, research_result)`,作为喂给 codex 算 loss 的输入单元,也是数据集的一条样本骨架。由叶子脚本 `concat_triple.py` 完成(确定性,optimizer 在 Bash 里调一次)。

**承接 A1/A2 裁决(本步的形态由此确定):**
concat **不再读 CC 日志、不做脆弱的正则块抽取**。它只吃两个已落盘的结构化产物:

- **第 1 元 research_config** ← `configs/<sample>.json`(gen_configs 已落,PolicyCard 全文)。直接整取,无需加工。
- **第 2 元 research_graph + 第 3 元 research_result** ← `transcripts/<sample>.md`(save_transcript 已从 exec jsonl 落)。因 exec 被强制走 `formated-specs`(产 graph)/ `formated-results`(产 result),这两块本就是**规整结构**,按 formated 约定的块边界直接切出,不靠猜。

三元组的标签 = 第 1 元 config 本身(已知生成条件),这正是整套设计绕开 no-ground-truth 的根:不靠人对质量打分,靠"这条样本是哪张卡生成的"。

**输入齐备性:** concat 在本 run 末调用,此时 configs/ 与 transcripts/ 均已就位(分别由 gen_configs、save_transcript 落),无外部依赖。

###### 读 configs/\<sample\>.json + transcripts/\<sample\>.md

**这一步做什么**
concat 的取数。两个输入,纯读,均在 `runs/<run_id>/` 下:

- `configs/<sample>.json` —— research_config 全文(三元组第 1 元),`sample` 命名 `<batch_id>-topic<NN>-id<N>`(如 `batch-0-topic05-id0`)。
- `transcripts/<sample>.md` —— 本 run 完整双向对话,graph/result 两块都从这里切。

不再有 `--logs-dir` 入参、不再 `read_conversation` 读 jsonl——读日志只发生在 save_transcript 那一处(单一真相源),concat 下游只认 transcript。

**CHECKPOINT**:无(纯读)。

###### 取 exec formated-specs/results 的 graph / result 结构化块

**这一步做什么**
从 transcript 里切出第 2、3 元。因 exec 末轮强制产出 formated 结构,这两块有**确定的块边界**(formated-specs 段 = research_graph;formated-results 段 = research_result),按约定标记直接定位提取,而非在自由文本里正则猜测——这是 A2 裁决删掉 `validate_pair.extract_blocks` 脆弱解析层后的干净做法。

**formated 输出契约(决策已定，concat 照此切块):**

这两个 skill 是本系统新引入、尚未设计;旧规划无可继承(旧路线 `validate_pair.extract_blocks` 脆弱正则已被 A2 裁决废弃)。但**与 concat 的接口契约现在定死**——skill 内部逻辑留 skill-creation,但其**输出形态**必须满足下列契约,否则 concat 无法确定性切块。

**① 路径(进对话，非写文件):** 两块作为 exec 的**对话内容**产出 → 落 exec session jsonl → save_transcript 转写进 `transcripts/<sample>.md` → concat 从 transcript 切。**不另起"写文件"通路**:exec 不需知道 harness 路径、不跨 mount 写产物,守住"权威 transcript = exec jsonl 单一真相源"的既有承诺。

**② 边界标记(带 info-string 的 markdown 围栏):**

- research_graph: 用 ` ```research-graph ` 开栏、` ``` ` 闭栏。
- research_result: 用 ` ```research-result ` 开栏、` ``` ` 闭栏。
- concat 按 **info-string 行**(`research-graph`/`research-result`)定位、读到配对闭合围栏即得整块。payload 是 JSON,不含 ``` ,故围栏切割安全。比哨兵对(`<<<...>>>`)更安全:标准 markdown、exec 天然产围栏、不怕正文撞 token。

**③ payload 格式(两块都 JSON):**

- research_graph: JSON(nodes/edges/manifest 本就结构化,见下条 schema)。
- research_result: **也 JSON**(sections 作字段),最利于下游 32-check 的 R-only 检查路由;下游是机器探针,markdown 可读性不是目标。

**两条硬规则(写进 concat spec):**

1. **原子性**:每块必须在 exec 的**单个 assistant 轮**内完整产出(skill 的收尾动作),不被 sim 插话切断 → save_transcript 捕获完整、concat 无需跨轮拼接。
2. **取最后一个**:多轮拉锯里 exec 可能产多版(被 sim 打回改过)→ concat 取 transcript 里**最后一个** `research-graph` 围栏(=最终被接受稿)、最后一个 `research-result` 围栏。

**research_graph payload schema(对齐 Stage 7 = 4-layer call plan):**

```research-graph
{
  "nodes": [{"id": "n1", "skill": "<skill名>", "layer": "campaign|strategy|tactic|sop"}],
  "edges": [{"from": "n1", "to": "n2", "kind": "calls|sequences"}],
  "layer_labels": {"n1": "campaign"},
  "manifest": ["<本次实际编排到的 skill 清单>"],
  "prereq_dag": [{"node": "n2", "requires": ["n1"]}]
}
```

**research_result payload schema(对齐 Stage 7 = clean research-design document，sections 作字段):**

```research-result
{
  "title": "<研究题目>",
  "sections": [{"heading": "<节标题>", "body": "<节正文>"}],
  "artifacts": ["<产出物清单,如 spec 文件名/图表引用>"]
}
```

字段细节随 formated skill 设计微调,但**两块 JSON + 围栏 info-string + 原子性 + 取最后一个**这四条是 concat 的硬契约,定死不动。切出后:research_graph = 三元组第 2 元、research_result = 第 3 元,与第 1 元 config 拼成 `triples/<sample>.json`(下一子项)。

**CHECKPOINT**:无(中间产物,随下一步一并落)。

###### 输出三元组 → runs/\<id\>/triples/\<sample\>.json

**这一步做什么**
把第 1/2/3 元装进一个 json,落 `runs/<run_id>/triples/<sample>.json`。这是 codex 算 loss 的输入单元:loss-1(injection-fidelity,per-run)读它判人设注入保真;loss-2(ladder-quality-order,per-topic)吃同 topic 6 档的三元组判阶梯单调。

**CHECKPOINT(写)**:`runs/<run_id>/triples/<sample>.json` —— `(research_config, research_graph, research_result)` 三元组合体。config 取自 `configs/<sample>.json`,graph/result 取自 exec 末轮 formated 产出(经 save_transcript 落 transcript、本步切块)。隐私:只含结构化研究内容,绝不含 CC log 绝对路径。

##### 启动 codex → injection-fidelity → loss-1

**这一步做什么**
本 run 的最后一步:用 codex 算 **loss-1 = injection-fidelity(注入保真度)**——判这一 run 里 sim 是否真的"成为"了 config 指定的人设、把该档的监督压力(A1 实质要求、A3 操作化坚持等)如实施加给了 exec。这是两部分 loss 的第一部分(per-run,每 run 一次);第二部分 loss-2(ladder-quality-order)是 per-topic,等同 topic 6 档跑满才算(后面那步)。

**为什么用 codex 而非 claude:** loss 评判要与被评判的 claude 三层**换一个模型族**做,避免"自己判自己"的同源偏置;codex 走独立的 OpenAI 分组凭证(env.sh 里与 Claude 分组物理隔离)。codex 角色只挂两个 loss 技能(injection-fidelity / ladder-quality-order),config-dir = `/workspace/home/loss/.codex`。

**W5(check-blind,本步硬约束):** injection-fidelity 只看"人设注入保真"——sim 有没有按 config 的轴等级施压、exec 产出是否反映了该压力。它**绝不触碰 32-check / 6-primitive / 检测签名**:loss 判的是"生成条件是否被忠实执行",不是"研究质量好不好"(质量判定是探针的事,而探针是唯一见 check 的会话)。loss skill 全文过 leak_audit,与生成侧同样 check-blind。

###### 注入 SKILL.md 全文

**这一步做什么**
codex 不像 claude 那样自动挂载技能目录,所以 injection-fidelity 这个 loss skill 的判定规则,要把 **SKILL.md 全文作为 prompt 的一部分注入**给 codex(cwd = `/workspace/work/loss`)。即:loss 逻辑写在 skill 文件里(人能读、可版本管理),运行时由 `run_codex_loss.py` 读出全文、拼进 codex 调用。

**判定细则(据 spec#3 Stage 5 Checkpoint 1，check-blind)**:injection-fidelity 解析 transcript 里 **sim(user 轮)** 的行为,抽 **6 个施压信号**,各自比对"本档轴等级应落的期望带",逐轴 AND 出单样本 `fidelity`。6 信号:

| 信号 | 绑定轴 | 测什么 |
| --- | --- | --- |
| `pushback_count` | A1 实质性要求 | 追问/要更实质的用户轮数 |
| `operationalization_demand_count` | A3 操作化坚持 | 要数字/可执行步骤的轮数 |
| `accept_without_question_rate` | 反向压力(低 A1) | 无质疑即接受的比例 |
| `premise_defended_count` | A4=C-(PG 引擎) | 被挑战后仍坚持错误前提的轮数 |
| `incoherent_demand_flag` | 低 A2 | 需求不连贯的布尔 |
| `novel_seed_count` | A5=G+(NG 引擎) | 引入原创方向/跨域连接/重构的轮数 |

另记两个事件位 `premise_dropped` / `premise_revised`(A4 轨迹),以及 A5 的 **substantive-seed 检验**(种子须实质、topic-relevant,非复述 exec 上一轮)。

**打分(期望带 band)**:每信号按 F8 turn_budget 归一化 → 落入该档轴等级对应的不重叠期望带(L0..L4 把 [0,1] 划成带,overlay 轴用布尔/阈值)。例:A1=L0 ⇒ pushback_rate≥0.7;A1=L4 ⇒ ≤0.05。**单样本 `fidelity` = AND over 本卡绑定的所有轴 [observed ∈ band(card.level)]**;批 `fidelity_rate` = 通过样本比例,**批门 ≥0.90**。

**per-turn drift 门(源自 Stage 4 文献 M5 persona-drift)**:把 transcript 切前半/后半,两半信号都须在带内;后半压力信号若朝"合作极"漂移超容差 → `drift_flag=true` → **该样本 fidelity 直接 FAIL**(漂移点后标签不可信)。

**冷启动自检(3 条 falsifier，写进 skill 校验项)**:FS1-1 计数对但语义空(人工抽检语义施压);FS1-2 A5 种子新但 trivial/离题(查 topic-relevance);FS1-3 两 parser 计数不一致(钉死 parser 规格)。

本步只定"全文注入 + 上述判定规则"这一机制;阈值具体数值集中放 `references/`(与 gate-thresholds 同处),skill 正文只写规则。

**CHECKPOINT**:无(注入动作)。

###### codex exec --output-schema loss1.json -o ... \<payload=transcript\>

**这一步做什么**
实际调用 codex 的命令形态:`codex exec` 模式,`--output-schema loss1.json` 强约束输出为结构化 json(保真值 + codex 判词),`-o` 指定输出落点,payload = 本 run 的 transcript(+ 必要时 config,供 codex 对照"应施加的压力 vs 实际施加的")。

**`loss1.json` 输出 schema(据 Stage 5 SKILL 1 OUTPUT，分轴打分)**:

```json
{
  "fidelity": true,              // 单样本通过 bool = AND over 绑定轴 [observed ∈ band]
  "loss1": 0.0,                  // float∈[0,1],保真数值(通过轴数/绑定轴数,或最小轴 margin);进 trace 便于 tail
  "per_axis_evidence": {         // 分轴留证(审计痕迹)
    "A1": {"observed": 0.72, "expected_band": "[0.7,1.0]", "pass": true}
  },
  "drift_flag": false,           // per-turn drift 门结论(后半朝合作漂移超容差则 true 且 fidelity FAIL)
  "note": "..."                  // codex 判词(可选;loss-1 主体是程序化解析,codex 跑分类时附解释)
}
```

分轴打分=是(`per_axis_evidence` 逐轴 observed/expected_band/pass 三元),但单样本最终是 AND 聚合的一个 bool + 一个 [0,1] 数值。`loss1` 数值域 [0,1] 与各信号归一带一致。命令的精确 flag 组合落地时对齐 codex 版本。

**CHECKPOINT**:无(codex 输出由下一子项 parse 后落盘)。

###### parse_loss1 → 该 run 保真值 → 缓存 runs/\<id\>/loss/

**这一步做什么**
`loss_runner.parse_loss1` 解析 codex 的结构化输出,取出该 run 的保真值,缓存到 `runs/<run_id>/loss/<sample>.loss1.json`。per-run 缓存的意义:同 topic 6 档各有一个 loss-1,等 6 档跑满后,per-topic 聚合要用这 6 个保真值算"保真率≥90%"那一项门控。

**CHECKPOINT(写)**:

- `runs/<run_id>/loss/<sample>.loss1.json` —— 该 run 的 injection-fidelity 结果(保真值 + codex 判词),供 per-topic 聚合保真率用。
- `trace.jsonl` 追加 `rung_done` —— 一次 run 正式收尾(本 run 的终点 trace 事件,前面关 sim/exec 都不落 trace,到此才落)。专有体**对齐 trace 设计源**(index.html ③)+ 保留 loss1 数值:`{sample_id, fidelity:bool, loss1, per_axis_evidence, drift_flag, transcript_path}`。其中 `fidelity` 是保真**通过 bool**(loss1 数值≥阈值)、`loss1` 是数值本身(进 trace 便于 tail 时直接看分、per-topic 聚合算 fidelity_rate 时可直接从 trace 读而不必回开 6 个 loss1.json)、`per_axis_evidence` 逐轴注入证据、`drift_flag` 人设漂移标志(per-turn drift 门的结论)、`transcript_path` 指 `transcripts/<sample>.md`(相对路径,隐私红线:绝不含绝对 log 路径)。

##### IF 档 < 5 ── 内层循环回跳判断

**这一步做什么**
一档 run 收尾(`rung_done` 已落)后,判本 topic 的 6 档是否跑满,决定回跳内层 FOR 还是跳出进 per-topic 聚合。这是 `#### for 档 in 6` 内层循环的收尾判断,与上面 5 个 run-body 步骤(起 sim → 注入 → concat → loss-1)同属一次循环迭代。

- **T(档 < 5):** 还没跑满 6 档,档号 +1,回 `#### for 档 in 6` 开下一档 run——全新 sim/exec、注入下一档人设(`configs/<sample>.json` 的下一档卡)。同 topic 继续往下铺阶梯,每档一条独立三元组 + 一个 loss-1。
- **F(档 = 5,6 档已全跑完):** 本 topic 一条完整阶梯成形(6 条三元组 + 6 个 `loss1.json` 已落),跳出内层,进入下面 **per-topic 聚合**(loss-2 + 门控 + 写样本)。这是"内层跑满才触发聚合"的唯一入口。

**CHECKPOINT**:无(循环控制判断;6 档各自的 `rung_done` 已逐档落 trace,本步不另 emit)。

#### ── per-topic 聚合 (仅在内层跑满 6 档后到达) ──

**这一步做什么**
一个 topic 的 6 档 run 全跑完后(6 条三元组 + 6 个 `loss1.json` 已落)到达本块。它是 batch 流程里 **loss 第二部分的发生地**,做三件事、按序:① codex 算 loss-2(这条阶梯单调不单调)→ ② 三项 AND 门控判这个 topic 是否收敛 → ③ 收敛与否都把这 6 条样本写进数据集本体。完成后回 `IF topic_i<7` 决定继续下一 topic 还是结束 LOOP-1。本块是"按 topic 成组"嵌套的**唯一收益点**:只有凑齐 6 档才能判阶梯。

##### codex → ladder-quality-order → loss-2 (吃 6 档三元组)

**这一步做什么**
用 codex 算 **loss-2 = ladder-quality-order(阶梯质量序)**——判这个 topic 的 6 条三元组,其研究质量是否随档位 id0→id5 **单调下降**、且**端点拉得开**。这是两部分 loss 的第二部分(per-topic,每 topic 一次),与 loss-1(per-run、判人设注入保真)正交:loss-1 管"压力施对没有",loss-2 管"压力差异有没有兑现成质量阶梯"。

**输入:** 本 topic 的 6 个 `triples/<sample>.json`(id0..id5 各一),由 `run_codex_loss.py` 的 loss-2 分支一次性喂给 codex。codex 角色同 loss-1(`/workspace/home/loss/.codex`,独立 OpenAI 分组,换模型族避同源偏置)。

**codex 怎么吃 6 档(判定机制):**

- 6 条三元组的 `(graph,result)` 给 codex,**但 codex 看不到档号、看不到 config**——只拿到打乱顺序的 6 份研究产物,被要求**按研究质量从高到低排序**(check-blind:它判的是"哪份更扎实",绝不调 32-check)。
- 把 codex 排出的序与**真实档序** id0>…>id5 比,算 **Kendall τ**。τ 高 = codex 眼中的质量序与生成条件序一致 = 阶梯单调成立。
- 阈值:**τ≥0.7** 记 `monotonicity_pass=true`;**τ≥0.8** 触发"丙校准"交接(质量足够好,可移交下一阶段),低于 0.7 判单调破。
- **端点分离 `endpoint_separation`**:单独让 codex 对 id0 与 id5 两份做**成对优劣判定 + 差距打分**,差距≥阈值(skill 定)记 `endpoint_separation_pass=true`。端点拉不开是 CLR 范畴4 风险(坐标锁死上限)的直接探针。

**W5(check-blind 硬约束):** ladder-quality-order skill 全文过 leak_audit,只让 codex 做"相对优劣排序 + 端点差距",**绝不暴露 32-check / 6-primitive / 检测签名**。它问的是"哪份研究更好"(相对、无 ground-truth 锚点也能答),不是"这份研究合不合某条具体标准"。

**判定细则(据 spec#3 Stage 5 Checkpoint 2，check-blind)**:

- **判定单元 = PAIR(成对，不给绝对分)**:取本 topic 6 档里的 (sample_i, sample_j) i<j,judge 只输出"哪份在 D1–D5 整体意义上更高质量(或 tie)+ 一行理由",**明确 pairwise ordering，NOT absolute scoring**。
- **排序 prompt 模板要素**:只许用 **D1–D5 质量语言**(more meaningful / more useful / better-structured);输入 (graph 供 structure-aware holistic 判断、但不用来跑 check) + result;**禁用** 32-check 词表 / 6 primitives / "pseudo-good·novel-good"(DL-5)分类词。
- **单调 PASS**:把成对裁决聚合成 rank,算 judge 序与真实 id 序的 **Kendall τ;`monotonicity_pass = (τ≥0.7 且端点无相邻反转)`**(id0 在直接对里须高置信赢 idN-1)。
- **端点分离 PASS**:对 (id0, id5) 单独做 **K 次独立 judge 成对优劣判定**,`endpoint_separation_pass = (id0 赢 ≥ K−allowance 次)`;近 tie → 触发 `rigor_floor_flag`(升 §backprop 归因,非调参 bug,见下条 gate H 的 rigor_floor 说明)。差距阈值采 **K-run 多数票形式**,非单一标量分。
- **丙校准 hand-off**:`τ≥0.8 且端点 100% 一致` 时移交下一阶段(质量足够好)。
- **z⊥C 自检(FS2-2)**:judge 跑 B1 confound-triplet(同实质、异文风)时排序必须 flat,否则 judge 被 confound 污染,须加固 judge prompt(此时本 topic loss-2 信号不可信,见 backprop-heuristic 前置门)。

阈值具体值(τ 线、K、allowance、丙校准线)集中放 `references/gate-thresholds.md`,skill 正文只写规则。本步定"喂 6 档打乱产物→codex 成对排序→聚合算 τ + 端点 K-run 判定"这一机制骨架。

**CHECKPOINT(写)**:`runs/<run_id>/loss/<topic>.loss2.json` —— 该 topic 的 ladder-quality-order 结果。schema(据 Stage 5 SKILL 2 OUTPUT):

```json
{
  "tau": 0.83,                      // float,judge 序与真实 id 序的 Kendall τ
  "monotonicity_pass": true,        // bool = (τ≥0.7 且端点无相邻反转)
  "endpoint_separation_pass": true, // bool = (id0 在 K 次独立判定里赢 id5 ≥ K−allowance 次)
  "rigor_floor_flag": false,        // bool,端点近 tie 时置真(feeds §backprop 归因)
  "pairwise_log": [                 // 每对裁决留痕,供复盘
    {"i": 0, "j": 5, "winner": 0, "reason": "..."}
  ]
}
```

per-topic 一份,供下一步门控用。

##### gate.topic_passes (保真率≥90% ∧ mono ∧ endpoint)

**这一步做什么**
判这个 topic 是否**过闸**(达标)。由 `gate_eval.py` 做纯算术(确定性,不调 CC/codex):读本 topic 的 6 个 `loss1.json` + 1 个 `loss2.json`,算三项布尔并 **AND**:

| 门控项 | 来源 | 判定 |
| --- | --- | --- |
| `fidelity_rate ≥ 0.90` | 6 个 `loss1.json` 的保真值 | 6 档里达标档数/6 ≥ 90%(即 6 档全保真,或按 skill 定的"保真值≥阈值算达标"逐档判后取比例) |
| `monotonicity_pass` | `loss2.json` | τ≥0.7(见上步) |
| `endpoint_separation_pass` | `loss2.json` | 端点差距≥阈值(见上步) |

`topic_pass = (fidelity_rate≥0.90) ∧ monotonicity_pass ∧ endpoint_separation_pass`。三者缺一即该 topic 未过闸——但**未过闸不阻断写样本**(下一步照写,门控只决定 batch 层过闸与 backprop 归因,不决定数据去留)。

**`rigor_floor_flag`(AS-1 探针,与过闸正交):** 另记一个布尔——当 `endpoint_separation_pass=false` 且经判定根因疑似"DARE 鲁棒性抗住了下压、端点先天拉不开"(而非铺陈层没铺好)时置真。它不参与 `topic_pass` 的 AND,只作告警:供 batch 级 `any_rigor_floor` 汇总、供 backprop §先归因时区分"端点没拉开"是话术/坐标的锅还是 DARE 鲁棒性下限(CLR 范畴4 风险的现场探针,见 L500–506)。

**判别规则(据 Stage 4 rung-collapse remedy 的 (a)/(b)/(c) 三分支 + Stage 6 O1 结构vs实质):** 看 collapse 出在**输入侧**还是**输出侧**——

- **置真(=c,真 rigor floor)的充要条件**:`endpoint_separation_pass=false`(loss-2 判端点近 tie)**且** 端点两档(id0/id5)的 **loss-1 输入压力信号已明确拉开**(fidelity 高、pushback/operationalization 等 6 信号在端点分明)。即"输入压力差异已兑现、输出质量却没拉开"→ 归因 DARE 鲁棒性抗住下压 → `rigor_floor_flag=true`(告警,**§backprop 绝不据此硬训②**)。
- **不置真**:若端点两档的输入信号本身就没拉开(fidelity 低 / 6 信号端点不分),则根因在 (a) 铺陈层(插值步太小/档间距窄)或 (b) 话术注入没到位 → 按 §backprop 归①/②处理,**不**置 flag。
- **Stage 6 O1 细分(加一层保险)**:collapse 若仅出现在 graph 结构、而 substance(result)端点仍有差 → 不算 floor(DARE 的 floor 护结构、不护坏输入下的实质),probe 仍可用。

判别由 ladder-quality-order skill 在出 loss-2 时连带产出(它已有端点判词 + 可读到 6 档 loss-1 信号);精确数值门限(何谓"输入已拉开")集中放 `references/gate-thresholds.md`。

**阈值集中处**:三项阈值(0.90 / 0.7 / 端点值)写在 `references/gate-thresholds.md`,`gate_eval.py` 从那里读,不散在代码里(便于 optimizer 审计、便于一处改)。

**CHECKPOINT(写)— `topic_done` 事件**:`trace.jsonl` 追加一行,专有体**对齐 trace 设计源**(index.html ③)= `{tau, monotonicity_pass, endpoint_separation_pass, rigor_floor_flag, topic_pass, fidelity_rate}`;该 topic 过闸 bool 正式落账。公共头 `topic_id` 取本 topic、`rung_id`=null。

##### 写该 topic 6 条样本

**这一步做什么**
把本 topic 的 6 条三元组写成**数据集本体**——这是整个 pretrain 要交付的最终产物。由 `write_dataset.py` 做:读 6 个 `triples/<sample>.json`,**按隐私白名单裁字段**后,写 `dataset/<topic>/<sample>.json`。无论 topic 收敛与否都写(未收敛样本也是带标签的负例,对下游探针训练有用);收敛状态作为字段记在样本里,由下游自行筛。

**★隐私白名单(D 红线落地,只保留下列字段,其余一律不写出):**

| 字段 | 内容 | 来源 |
| --- | --- | --- |
| `sample_id` | `<batch_id>-topic<NN>-id<N>` | 命名 |
| `label` | **=生成条件**(本样本由哪张卡/哪档生成):`{rung_id, axis_levels:{A1..A5,B1}}` | config |
| `research_config` | PolicyCard F0–F9 verbatim(人设全文) | `configs/<sample>.json` |
| `research_graph` | formated-specs 产出的结构化规格块 | triple |
| `research_result` | formated-results 产出的结构化结果块 | triple |
| `loss1_fidelity` | 该 run 注入保真值 | `loss1.json` |
| `topic_pass` | 本 topic 三项门控 AND 结果 | gate |
| `intended_rank` | 本档在阶梯中的预期名次(id 即名次) | config |

**绝不写出**:任何 CC log 绝对路径、`--logs-dir` 值、session jsonl 路径、设备用户名、transcript 原始全文(只留 formated 切出的 graph/result 结构块,不留对话原文)。`write_dataset.py` 落盘前过一道 schema 校验:**出现白名单外字段即报错中断**(把隐私红线变成代码层的硬失败,而非靠人记得)。

**标签合法性(全设计的根)**:`label` = 已知生成条件,不是人对质量的主观打分——这正是绕开 no-ground-truth 的根。下游探针训练时,"这条样本该被判好/判坏"由 label 客观给定。

**CHECKPOINT(写)**:`dataset/<topic>/<sample>.json` × 6 —— ★最终产物★,隐私白名单裁字段后的 6 条已发布样本(标注=已知生成条件)。这是 pretrain 数据集本体,绝不含 CC log 路径。

#### IF topic_i < 7

**这一步做什么**
外层循环判断。本 topic 的 per-topic 聚合做完(loss-2 + 门控 + 写样本 + `topic_done` 已落)后,判 8 个 topic 是否遍历完:

##### T: topic+1 → LOOP (回外层 FOR)

**这一步做什么**
`topic_i < 7` 为真:还有 topic 没跑,`topic_i+1`,回外层 FOR 开下一个 topic——重新进内层从 id0 跑 6 档(全新 sim/exec,注入下一 topic 的题目 + 该档人设)。本 batch 继续累积 topic 收敛结果。

##### F: 8 topic 全跑完 (48 run) → END LOOP-1

**这一步做什么**
`topic_i < 7` 为假(即 topic_i=7,8 topic 全遍历完,48 run 全跑完):本 batch 的数据生产结束,跳出 LOOP-1,把控制权交还 **batch 级**(下面三步:整合 8 条收敛 bool → batch_pass_ratio 过闸 → 判连续 3 batch / backprop)。此刻盘上已有:本 batch 8 个 topic × 6 档 = 48 条 `dataset/` 样本、48 个 `loss1.json`、8 个 `loss2.json`、8 个 `topic_done` trace 事件。

### 整合 8 条 topic 收敛情况

**这一步做什么**
batch 级判定的第一步。48 run 跑完、跳出 LOOP-1 后,把本 batch **8 个 topic** 各自的收敛 bool 汇总成一个 8 元数组,为下一步算 pass_ratio 做准备。纯汇总,不判定、不重算。

**★"8 条非 48"**:每个 topic 已在自己的 per-topic 聚合里把 6 个 run 收敛进一个 `topic_pass`(三项 AND);本步只把这 8 个已判好的 bool 收齐,不再触碰底下的 48 run。

**数据源(决策已定):** 从 `trace.jsonl` **回读本 batch 的 8 个 `topic_done` 事件**,取其 `topic_pass` 字段——这些 bool 在 per-topic 聚合时已由 `gate_eval.py` 判定并落账,本步直接复用,**不重算**(单一真相:gate 判过一次就不再判第二次)。得到形如 `[true,true,false,true,...]` 的 8 元数组。

**不单独落账(决策已定):** 本步是 optimizer 的内存汇总动作,**不单独 emit trace 事件**——8 个 `topic_done` 已逐条落盘,batch 级的正式落账点是下一步的 `batch_done`。

**工具**:`gate_eval.py`(已在编排表;此处用其"读 trace 收敛 bool"能力,无新脚本)。

**CHECKPOINT**:无(内存汇总;落账在下一步 batch_done)。

### batch_pass_ratio ≥80% (即 ≥7/8 topic 过) → 过闸

**这一步做什么**
batch 级判定第二步:拿上一步的 8 元 bool 数组,算"过闸 topic 占比"`pass_ratio`,判这个 batch 是否**过闸**,并 emit `batch_done` 把整批结果正式落账。这是 batch 级唯一的 trace 落账点(topic 级已逐条 `topic_done`)。

**算术 + ★硬整数线(决策已定):**
`pass_ratio = 过闸 topic 数 / 8`;`batch_passed = (pass_ratio ≥ 0.80)`。

> ★点明:8 个 topic 下,"≥80%" 实际等价于 **"≥7 个 topic 过"** 这条硬整数线——7/8=0.875 过、**6/8=0.75 不过**。所以 0.80 不是"6.4 个"这种连续量,而是卡在 7 这个整数上(中间没有 6.x 个 topic 的可能)。`gate_eval.py` 按 `≥0.80` 算,效果即"≥7"。阈值 0.80 写入 `references/gate-thresholds.md`,与 per-topic 三阈值集中同处。

**工具**:`gate_eval.py`(pass_ratio 算术,无新脚本)+ `trace_emit.py`(emit `batch_done`)。

**CHECKPOINT(写)— `batch_done` 事件**:`trace.jsonl` 追加一行。公共头 7 字段(此事件 `topic_id`/`rung_id` 均 null,batch 级)。专有体**对齐 trace 设计源**(index.html ③)+ 加 `batch_passed`:

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `pass_ratio` | float | 过闸 topic 数 / 8 |
| `batch_passed` | bool | `pass_ratio≥0.80`(=≥7/8);落账即判,省下游再算(与 topic_done 存 topic_pass 同风格) |
| `topic_pass_flags` | bool[8] | 8 个 topic 各自过闸 bool(上一步汇总的数组);backprop §先归因时直接读"哪个 topic 挂" |
| `recent_ratios` | float[] | 最近若干 batch 的 pass_ratio 滚动列表;供下一步"连续 3 batch 过闸"判定(无需回扫历史 trace) |
| `any_rigor_floor` | bool | 本 batch 8 个 topic 的 `rigor_floor_flag` 是否有任一为真;AS-1 告警汇总,供 backprop 区分"端点拉不开是铺陈问题还是 DARE 鲁棒性下限" |

样例行(单行落盘,此处阅读换行):

```json
{"ts":"2026-06-06T21:40:02+08:00","run_id":"2026-06-06-20-18-05","event":"batch_done","batch_id":"batch-0","topic_id":null,"rung_id":null,"seq":312,"pass_ratio":0.875,"batch_passed":true,"topic_pass_flags":[true,true,true,false,true,true,true,true],"recent_ratios":[0.625,0.75,0.875],"any_rigor_floor":false}
```

### IF 连续 3 个 batch 过闸

**这一步做什么**
batch 级判定第三步,也是整个 epoch-loop 的**收敛总判 / 退出条件**:看是否已**连续 3 个 batch** 都 `batch_passed=true`。是 → 收敛,走 T(freeze、结束训练);否 → 走 F(反向传播改权重,进下一 batch)。

**判据载体(决策已定):** 读上一步 `batch_done` 的 **`recent_ratios`**(全程滚动列表),取**末 3 个**,判是否都 `≥0.80`。`converged = (recent_ratios 末3个全部 ≥0.80)`。

- **为何用 `recent_ratios` 而非计数器**:无状态、可从 trace 完全重建(契合 §state"`/compact` 后从盘恢复、不依赖记忆")。若另设 `consecutive_pass_count` 计数器,反要额外持久化、额外维护,多一处状态多一处错。
- **"连续"语义**:中间任一 batch 没过(ratio<0.80)即**断、重新计数**——所以判"末 3 个连续 ≥0.80",而非"历史累计过闸 3 次"。`recent_ratios` 全程保留(可 tail 看完整收敛轨迹),但判定只截末 3。

**工具**:`gate_eval.py`(converged 分支算术,无新脚本)。本节是纯分叉判断,**不单独 emit trace**(决策已定:`batch_done` 已落账,收敛与否的正式事件是 T 分支的 `converged`)。

**三个分支(决策已定:本批"过没过"与"连没连够 3 次"是两件正交的事,据此三分):**

判定按两个布尔交叉(`batch_passed` × `converged`),落到三条互斥路径:

| `batch_passed` | `converged`(末3连过) | 走哪 | 动权重? | 写 `<batch+1>.json`? |
| --- | --- | --- | --- | --- |
| true | true | **T** | 否(冻结) | 否(改写 `frozen.json`) |
| true | false | **F1** | **否**(本批已过,无失败可归因) | **是,原样拷贝**(权重不变) |
| false | — | **F2** | 是(backprop 归因改一权重) | 是(改后的新权重) |

- **T:连续 3 batch 过闸** → `#### T: END LOOP-2`(emit `converged`+`run_end` → freeze_weights + coverage_report,结束)。
- **F1:本批过闸但未连续 3 次** → `#### F1: 过闸未收敛 — 权重不变,前进一批确认`。本批没有失败信号,**不进 backprop、不动三权重**;但仍 `batch_id+1`、把当前 `weights/<batch>.json` **原样拷成 `weights/<batch+1>.json`**(权重逐字不变),回 LOOP-2 用同一套权重再跑一批,看能否凑满连续 3 次。这正是"单变量受控"的延伸:只有不动权重连过 3 批,才证明这套权重稳定收敛,而非靠每批微调勉强达标。
- **F2:本批未过闸** → `#### F2: 反向传播 + 权重更新`(智能点③:读 loss 信号归因 → 改三权重之一 → `/compact` 重载 → 回 LOOP-2 开下一 batch)。

> **★F1 救活了 batch_id 的"max 不+1"恢复规则(决策已定):** F1 强制"过闸批也预写 `<batch+1>.json`(拷贝)",使**每个非终结 batch(F1 或 F2)都恰好预写一份下一批权重**这一不变式始终成立。于是 §state(L452)"取 weights 目录最大编号本身、不+1"永远指向正确的下一批:max 编号文件 = 下一批要用的权重,batch_id 干净前进、落盘路径(`configs/`、`dataset/`、`weights/`)绝不撞车。若 F1 不拷贝,过闸批不写新文件 → max 不前进 → batch_id 卡住、路径覆盖、trace 出现重复 `batch_id` 的 `batch_done`——故 F1 的拷贝是该恢复规则成立的必要前提,二者绑定。

**CHECKPOINT**:无(纯判断;落账在 T 的 `converged`/`run_end`、F1 的 `weights/<batch+1>.json`(拷贝,无 `weight_revised`)、F2 的 `weight_revised`)。

#### T: END LOOP-2

**这一步做什么**
收敛分支:连续 3 batch 过闸 → 训练成功结束。退出 LOOP-2(epoch-loop),走收尾:先 emit 两个 trace 事件标定收敛,再冻结权重 + 出覆盖率报告,然后流程到 `## END`。这是整条流水线的**正常终点**。

**两个 trace 事件(对齐源 index.html ③):**

- `converged` —— 专有体 `{num_batches, ratios}`:`num_batches`=收敛时累计跑了多少 batch、`ratios`=`recent_ratios`(收敛轨迹)。
- `run_end` —— 专有体 `{converged:bool, total_samples}`:`converged=true`、`total_samples`=本次训练写进 `dataset/` 的样本总数。两事件公共头 `topic_id`/`rung_id` 均 null(run 级)。

##### freeze_weights + coverage_report

**这一步做什么**
收尾的两件实质产物:① 冻结定稿三权重;② 出一份 pretrain 自己的覆盖率报告。

**① freeze_weights** —— `freeze.py`〔KEEP〕把**最后过闸 batch** 的 `weights/<batch_id>.json` 拷成 `weights/frozen.json`,即定稿的三权重①②③(`axis_prose`/`interp_params`/`assembler_params`,锁死段 `frozen_label` 一并带出)。

> **权重落盘(决策已定):** `frozen.json`(定稿)**与全程 batch 快照 `weights/batch-0.json … batch-N.json` 都留**。frozen 是交付定稿;历史快照供复盘 backprop 轨迹(配合 `revision_log.jsonl` 可重演每 batch 怎么改的)。

**② coverage_report** —— **单独脚本 `coverage_report.py`**(决策已定:与 freeze 职责分开,冻权重 vs 出报告两回事)。扫 `dataset/` + trace,出 `coverage_report.md`,纯聚合统计、**无任何 log 路径**。

> **★报告边界(决策已定):** 只放 **pretrain 自己能算**的维度——topic_pass / loss-2 的 τ / 端点分离 / 各档 fidelity_rate 这类生成侧指标。**PG/NG/GG/OB 分布、held-out→探针人口映射归探针侧**(spec#3 Stage-7 口径),**不进**本报告(pretrain 只管"把带标签的阶梯造出来",样本怎么分桶喂探针是下游的事)。
> **字段清单(决策已定，纯生成侧、aggregate-only、无 log 路径):**
>
> - **轴坐标覆盖(RR-2 核心，让 monoculture 可见)**:各轴(A1/A3/A2/A4/A5/B1)各 level 的样本计数分布(嵌套计数表)。
> - **阶梯质量**:每 topic 的 loss-2 `tau` / `monotonicity_pass` / `endpoint_separation_pass` / `rigor_floor_flag`;跨 topic 的 τ 分布(min/median/max)。
> - **注入保真**:各档 `fidelity_rate`、batch 级 fidelity 通过率、`drift_flag` 命中数。
> - **过闸**:每 batch `pass_ratio` / `batch_passed`、收敛用 `recent_ratios`、总 batch 数。
> - **产量**:写入 `dataset/` 的样本总数、completability 失败数(未入库)。
> - ★`coverage_report.py` 落盘前过一道白名单校验(与 `write_dataset` 同思路):**绝不放** PG/NG/GG/OB 桶分布、held-out 人口映射(探针侧);**绝不放** 任何 CC log 绝对路径、`--logs-dir` 值、session jsonl 路径、设备用户名、transcript 原文。

**工具**:`freeze.py`(KEEP,冻权重)+ `coverage_report.py`(NEW,出报告)+ `trace_emit.py`(上一子节的 converged/run_end)。

**CHECKPOINT(写):**

- `weights/frozen.json` —— 冻结的最终三权重(+ 全程 `weights/<batch>.json` 快照保留)。
- `coverage_report.md` —— 覆盖率报告(聚合统计,只含生成侧指标,无 log 路径)。
- `trace.jsonl` 追加 `converged` + `run_end` 两行(总账收尾)。

#### F1: 过闸未收敛 — 权重不变, 前进一批确认

**这一步做什么**
本 batch `batch_passed=true` 但 `recent_ratios` 末 3 个未全过(还没凑满连续 3 次)时的分支。本批**没有失败信号可归因**,所以**不进 backprop、不动任何权重**;它要做的只有一件事:把当前权重**原样推进一批**,回 LOOP-2 用同一套权重再跑,看能否连过到 3 次。这是收敛判据"连续 3 批稳过"的执行臂——只有不动权重也连过,才证明这套权重稳定,而非每批靠微调勉强达标。

**为什么不动权重(决策已定):** §backprop 的整套读数逻辑(读哪个 topic 挂、loss-2 子类型、codex 判词)前提是"有失败可定位"。过闸批没有"坏处"可归因,强行进 backprop 既无信号可读、又破坏"无失败不动权重"的单变量纪律(会引入无依据的扰动,反而可能把已达标的权重改坏)。故 F1 与 F2 严格分开:**F1 不碰智能点③**。

**唯一动作 — 原样预写下一批权重(决策已定):** `apply_weight_update.py` 走一条**拷贝模式**(非 revise):读当前 `weights/<batch>.json` → **逐字节拷贝**成 `weights/<batch+1>.json`(三段 + `frozen_label` 全部不变)→ **不追加 `revision_log.jsonl`**(没有修订)→ **不 emit `weight_revised`**(没有权重变化,trace 不该出现修订事件)。batch_id 随 `<batch+1>.json` 落盘自然 +1(L452 的 max 规则据此前进)。

> **★这一拷贝是 L452"max 不+1"恢复规则的必要前提:** 见 `### IF 连续 3 个 batch 过闸` 节末的绑定说明——只有 F1 也预写一份 `<batch+1>.json`,"每个非终结 batch 都恰好预写下一批权重"这一不变式才成立,max 编号才永远 = 下一批,batch_id 干净前进、`configs/`·`dataset/`·`weights/` 路径不撞、trace 无重复 `batch_id`。F1 若不拷贝,过闸批不前进 batch_id → 下一批路径覆盖本批产物。

**LOOP 闭合:** 拷完即 `/compact` + 重载 skill + 从盘恢复(与 F2 末尾同一套 §state 动作,见 `##### /compact + 重载 optimization-loop skill → LOOP`),回 LOOP-2 顶开下一批;`gen_configs.py` 读新落的 `weights/<batch+1>.json`(内容与上批逐字相同)。连续 3 批都走到 F1(或末批走 T)即收敛。

**工具**:`apply_weight_update.py` 的拷贝模式(无 revise、无 log、无 trace)+ `/compact`(CC 内建)。归因/智能点③在此分支**不触发**。

**CHECKPOINT(写):** `weights/<batch+1>.json` —— 当前权重的**逐字拷贝**(batch_id +1,内容不变);**无** `revision_log.jsonl` 追加、**无** `weight_revised` trace 事件(与 F2 的关键区别:F1 无修订痕迹,只有一份内容相同、编号 +1 的权重快照)。

#### F2: 反向传播 + 权重更新 + LOOP ── 智能点 (optimizer 动脑)

**这一步做什么**
batch 未过闸(`batch_passed=false`)时的分支,也是**全系统唯一非确定性、要 optimizer 真正动脑**的地方(智能点③)。其余所有步骤都是确定性脚本或机械对话;只有这里,optimizer 要**读懂本 batch 哪里坏了、判断为什么坏、决定改三权重中的哪一个**,然后 `/compact` 重载、进下一 batch。类比反向传播:loss 信号 → 定位"梯度"该落在哪个权重 → 更新那个权重。

**★核心纪律:先归因、再动手(CLAUDE.md 锁死的 §backprop)**
不是见 loss 高就乱改。必须先按 loss 类型与子类型把"坏"定位到具体权重,再动那一个。归因决策表:

| 现象(信号) | 归因 | 改哪个权重 |
| --- | --- | --- |
| **loss-1 挂**(某档 fidelity 低、drift_flag 真) | 人设没注入到位 / sim 没忠实施压 | **①档位话术** `axis_prose`(axes.py) |
| **loss-2 塌·子类型 A:端点没拉开**(`endpoint_separation_pass=false`) | 多为①话术不够分 / 端点坐标先天没拉远;**若 `rigor_floor_flag` 真 → 疑 DARE 鲁棒性下限** | **①话术**(或报警),**绝不硬训②** |
| **loss-2 塌·子类型 B:中间档单调破/撞糊**(τ 低但端点分得开) | 铺陈没铺好(相邻撞档/中间没区分度) | **②插值器铺陈层** `interp_params`(interpolator.py) |
| **卡整体没造好**(结构性,多档同时坏、非阶梯问题) | 组装逻辑问题 | **③组装逻辑** `assembler_params`(assembler.py) |

> ★最易错处(CLR 范畴4,L500–506):loss-2 塌**必须先分子类型**。"端点没拉开"**不许硬训 interpolator**——坐标被 `frozen_label` 锁死,端点分离的上限是坐标钉死的,硬训②铺陈层掰不动它,只会空转。这正是 `rigor_floor_flag` 探针存在的理由:它替 optimizer 把"端点拉不开是铺陈问题还是 DARE 鲁棒性下限"先标出来。

**★单变量受控更新(决策已定:一次只改一个权重)**
即便本 batch 多项信号同时挂,**一个 batch 也只改三权重中的一个**,下一 batch 再看这次改动的效果。理由:这把 backprop 变成"单变量受控实验"——下一 batch 的 loss 变化能**干净归因到这一次改动**,不会"一次动三处、无法判断谁起的作用"。多项同挂时按优先级择一:**loss-1 挂 > loss-2 子类型B > 卡整体没造好**(loss-1 是注入保真的地基,地基不稳上面都白搭,优先修;端点问题归①但需先排除 rigor_floor)。

**归因的输入(决策已定):** optimizer 读
①`batch_done` 的 `{topic_pass_flags, any_rigor_floor}`(先看哪些 topic 挂、有无 rigor 告警)→
②挂掉 topic 的 `topic_done`(含 τ、`endpoint_separation_pass`、`rigor_floor_flag`,定位 loss-2 子类型)→
③必要时回看该 topic 的 `loss1.json`/`loss2.json` 判词(看 codex 具体怎么说)。三层由粗到细,够判就停。

**工具**:归因判断本身是 optimizer 读 `references/backprop-heuristic.md` 后的 **CC 决策,无脚本**(这是智能点,不可确定化);定下"改哪个、改成什么"后,由 `apply_weight_update.py` 执行 `weights.revise` + 落 `revision_log.jsonl`(见下三个子节,**本 batch 只会走其中一个**)。

**子节点(本 batch 三选一 + 收尾):**

- `##### 读本 batch 的 loss 信号 + 哪些 topic 的哪个门控项挂` —— 归因的读数步(上述三层输入)。
- `##### optimizer optim 档位话术` / `##### optimizer optim 插值器` / `##### optimizer optim 生成器组装逻辑` —— 三个权重各自的改法,**单变量纪律下本 batch 只执行一个**。
- `##### /compact + 重载 optimization-loop skill → LOOP` —— 改完压缩、从盘恢复状态、回 LOOP-2 开下一 batch。**此子节为 F1/F2 共用收尾**:F2 改完权重走它,F1 拷完权重也走它(同一套 §state disk-恢复动作);差别仅在进它之前 F2 动了权重、F1 没动。

**`references/backprop-heuristic.md` 骨架(落地按下表逐行成文，每行 = 判别式→改法模板(数据派措辞)→优先级位次):**

| # | 判别式(信号读数) | 改法模板 | 优先级 |
| --- | --- | --- | --- |
| 0 | **前置门**:本 topic 的 B1 confound-triplet judge 不 flat(FS2-2) | loss-2 信号污染,**本 batch 不据 loss-2 改权重**;转而 harden ladder-quality-order judge prompt(loss skill 侧动作,不计入"单变量改一权重") | 最先查 |
| 1 | 某 topic `fidelity_rate<0.90` 或任一档 `drift_flag=true`;`per_axis_evidence` 指出哪条轴 `observed∉band` | `weights.revise("axis_prose", "<轴>.<等级>", 更准/更强的施压措辞, reason)` —— 定位到那一个 cell | 最高(地基) |
| 2 | `endpoint_separation_pass=false`:**先读 `rigor_floor_flag`** | flag=true → 报警,**不动权重**(坐标锁死,训不动);flag=false → 改 `axis_prose` 的 id0/id5 两档 cell。**绝不进②** | 次高 |
| 3 | τ<0.7 **但** `endpoint_separation_pass=true`(中间撞糊) | `weights.revise("interp_params", "<旋钮>", 新值, reason)`,旋钮∈`{collision_offset_axis(仅B1/expression), endpoint_spread, granularity_map}` | 中 |
| 4 | ≥4/8 topic fidelity 与 τ 双塌(结构性,先排除 parser/leak 工具坏) | `weights.revise("assembler_params", "<旋钮>", 新值, reason)` | 最低(兜底) |

每行的具体数值门限(band 边界、τ 线、K-allowance、≥4/8)引 `references/gate-thresholds.md`,不在 heuristic 里重复。本节(主文档)定的是归因决策表 + 单变量纪律 + 输入清单这套骨架;heuristic.md 是它的逐行落地展开 + 改法措辞模板。

**CHECKPOINT**:本父节点不直接落盘;落账在被选中那个子节的 `weight_revised` 事件 + `weights/<batch>.json` + `revision_log.jsonl`。

##### 读本 batch 的 loss 信号 + 哪些 topic 的哪个门控项挂

**这一步做什么**
backprop 的第一步——归因的**读数**。optimizer 把父节点定的三层输入读进来,形成"本 batch 哪里坏了"的诊断结论(哪个 topic、哪类 loss、若是 loss-2 则哪个子类型),为下一步"改哪个权重"提供依据。本步**只读、只判,不改任何东西**。

**读数三层(由粗到细,★够判就停——不无脑全读):**

1. **第一层(必读)** `batch_done.{topic_pass_flags, any_rigor_floor}` —— 先锁定**哪些 topic 挂了**(flags 里的 false)、**有无 rigor 告警**(any_rigor_floor)。这层就能划出诊断范围。
2. **第二层(对每个挂掉的 topic)** 读其 `topic_done` —— 区分:
   - 该 topic `fidelity_rate<0.90` → **loss-1 问题**(注入保真),归①话术;
   - `monotonicity_pass=false`/`endpoint_separation_pass=false` → **loss-2 问题**,再按父节点表分子类型(端点没拉开看 `rigor_floor_flag` 定是否硬训②;中间档撞糊归②铺陈)。
3. **第三层(仅必要时)** 回看该 topic 的 `loss1.json`/`loss2.json` 的 **codex 判词** —— 当前两层不足以判改法时才读(例如 loss-1 挂但要知道是哪个轴的施压没到位、loss-2 撞糊但要定位撞在哪两档)。**够判就停**:多数情况前两层的 bool + 数值已足够定位权重,第三层是补充证据而非例行步骤。

**产出:** 一个 optimizer 内存里的**诊断结论** = {挂掉的 topic、loss 类别、loss-2 子类型(若适用)、初步指向哪个权重}。它**不单独落盘**(决策已定)——结论会写进下一步 `weight_revised` 事件的 `reason` 字段,等于在权重修订处落了账,无需额外诊断 trace。

**工具**:optimizer 读 `trace.jsonl`(batch_done/topic_done)+ 必要时 `loss/*.json`,是 **CC 的读数+解读,无脚本**。注意:bool 判定在 per-topic/per-batch 时已由 `gate_eval.py` 算好,本步是 optimizer **解读已判好的信号**,不重新算门控。

**CHECKPOINT**:无(只读+内存推理;落账在下一步 `weight_revised.reason`)。

##### optimizer optim 档位话术

**这一步做什么**
三个改权重分支的**第一个**,对应权重①档位话术(`axis_prose`)。当上一步诊断结论指向"**loss-1 挂**(注入没到位)"或"**loss-2 端点没拉开且根因是话术不够分**"时,optimizer 走这里:调 `axis_prose` 段里某个(轴,等级)的话术文本,让那一档的施压更准、或让端点两档在话术上更分得开。

**数据派(★三权重共同前提,决策已定):** `axes.py` 是**读 `weights/<batch>.json` 的 `axis_prose` 段的纯函数**——optimizer 改的永远是 **json 数据**,`axes.py` **源码不动**。理由:① `weights/<batch>.json` 的 schema 已把全部可调话术装进 `axis_prose` 段,改数据即改权重;② 快照可回放、单变量受控、历史不可变;③ 改源码会与 json 重复承载、易不一致。(②插值器、③组装逻辑同此范式:`.py` 是读 weights 段的纯函数,只改数据。)

**何时走这里(单变量纪律):** 仅当本 batch 诊断**择一**落在①时执行;若同时有 loss-2 子类型B(中间撞糊)等其他问题,按父节点优先级(loss-1>子类型B>卡整体)只改这一个,其余下 batch 再说。

###### weights.revise("axis_prose", k, new, reason)

**这一步做什么**
①的具体修订调用。`weights.revise` 四参:

| 参数 | 取值 | 含义 |
| --- | --- | --- |
| `target` | `"axis_prose"` | 改三权重中的①话术段 |
| `k` | 如 `"A1.L0"` | 要改的 cell 键 =(轴.等级);定位 `axis_prose[axis][level]` 那条话术 |
| `new` | 新话术文本 | optimizer 据归因写的新施压措辞(更准/更分得开) |
| `reason` | 归因结论 | 上一步诊断结论原文(写进 revision_log + weight_revised.reason,实现"不单独落盘的诊断在此落账") |

**W5:** `new` 话术过 `leak_audit`,绝不含 32-check/6-primitive/检测签名词(生成侧 check-blind)。

###### 改 weights/\<batch\>.json 的 axis_prose 段(数据派,axes.py 不动)

**这一步做什么**
①修订的落盘。`apply_weight_update.py` 执行:读当前 batch 的 `weights/<batch>.json` → 在内存改 `axis_prose[轴][等级]` 那个 cell 为 `new` → **写进新建的下一 batch 文件 `weights/<batch+1>.json`**(决策已定:当前快照不可变、留历史;下一 batch 用新权重)→ 追加 `revision_log.jsonl` 一行 → emit `weight_revised`。`axes.py` 源码全程不动(数据派)。

**CHECKPOINT(写):**

- `weights/<batch+1>.json` —— 新一份权重快照,仅 `axis_prose` 段那一个 cell 变更(单变量),其余段原样拷入。
- `revision_log.jsonl` 追加 `{target:"axis_prose", key, old, new, reason}`(old=被覆盖的旧话术,供回放)。
- `trace.jsonl` 追加 `weight_revised`,专有体**对齐源**(index.html ③)= `{target, key, old, new, reason}`(W5 已校验)。

##### optimizer optim 插值器

**这一步做什么**
第二个改权重分支,对应权重②插值器铺陈层(`interp_params`)。当诊断结论是"**loss-2 塌·子类型 B:中间档单调破/撞糊**"(τ 低**但端点分得开**)时走这里——调铺陈旋钮,让 6 档铺得更单调、相邻拉得开。

**通用机制同①(数据派,见上 `optimizer optim 档位话术`):** `interpolator.py` 是读 `weights/<batch>.json` 的 `interp_params` 段的纯函数,源码不动;改完写新建的 `weights/<batch+1>.json`、追加 `revision_log.jsonl`、emit `weight_revised`;单变量纪律(本 batch 择一)。此处不重复,只写②**独有的两条铁律**。

**★铁律一(AS-3,物理隔离):** `interp_params` 只含三个铺陈旋钮 `{collision_offset_axis, endpoint_spread, granularity_map}`,其中 `collision_offset_axis` **只许取 `B1` 或 `expression`,schema 层禁写 A1–A5**。标签坐标在锁死的 `frozen_label` 段、与 `interp_params` 物理分段,所以 optimizer 改②时**碰不到任何 LABEL 轴坐标**——改铺陈绝不会让标签漂移。这是"用 A2/A3 错开撞档"那个老 bug 的根治(见 L494/521)。

**★铁律二(CLR 范畴4,只接子类型B):** 走到②的**前提**是已排除"端点没拉开"。端点拉不开归①话术或报 `rigor_floor_flag`(坐标锁死了端点上限,训②是空转),**绝不进②硬训**。所以②**只接 loss-2 子类型B(中间撞糊)**:τ 低但 `endpoint_separation_pass=true`。父节点已钉,此处再钉:**端点问题永不落②**。

###### weights.revise("interp_params", k, ...)

**这一步做什么**
②的修订调用,四参同①(`target/k/new/reason`),仅 `target="interp_params"`、`k`=**要改的旋钮名**:

- `k ∈ interp_params 的旋钮名`,当前三个 `{collision_offset_axis, endpoint_spread, granularity_map}`。**充分性裁定:够用**——三旋钮一一对应"铺陈层三件事"(撞档怎么错开 / 端点拉开幅度 / L0–L4 粒度运用),且覆盖 Stage 4 rung-collapse remedy 的全部可调手段(widen level gaps→`endpoint_spread`+`granularity_map`;perturb secondary knob→`collision_offset_axis`)。`collision_offset_axis` 取值域 schema 层硬锁 `{"B1","expression"}`(禁 A1–A5,铁律一)。可选第四旋钮(显式 `level_gap_table`)仅在 pilot 暴露 6 档→5 级撞档压不下去时再加,**先不加**,保持旋钮数最小(数据派可审计性);若加,`k` 候选随之扩,无需在此另标。
- `new`:该旋钮的新值。**约束**:若 `k="collision_offset_axis"`,`new` 只能是 `"B1"`/`"expression"`(铁律一,schema 层硬拒 A1–A5)。
- `reason`:归因结论(写进 revision_log + weight_revised.reason)。

落盘同①:`apply_weight_update.py` 改 `weights/<batch+1>.json` 的 `interp_params` 段那一个旋钮 → `revision_log.jsonl` 追加 `{target:"interp_params", key, old, new, reason}` → emit `weight_revised{target, key, old, new, reason}`(对齐源)。`interpolator.py` 源码不动。

**CHECKPOINT(写):** `weights/<batch+1>.json`(仅 interp_params 一个旋钮变更)+ `revision_log.jsonl` + `trace.jsonl` 的 `weight_revised`(同①格式)。

##### optimizer optim 生成器组装逻辑

**这一步做什么**
第三个改权重分支(优先级最低的兜底),对应权重③组装逻辑(`assembler_params`)。当诊断结论是"**卡整体没造好**"——结构性问题,而非①②那种单维度的阶梯质量问题——时走这里,调组装旋钮。

**通用机制同①(数据派):** `assembler.py` 是读 `weights/<batch>.json` 的 `assembler_params` 段的纯函数,源码不动;改完写 `weights/<batch+1>.json`、追加 `revision_log.jsonl`、emit `weight_revised`;单变量纪律。不重复,只写③独有部分。

**★③独有的触发判据(定性 + 留细则):** "卡整体没造好"区别于①②——①是注入保真(fidelity)、②是阶梯单调/撞糊(τ),都是**单一质量维度**;③是**卡本身的结构**没组装对(F0–F9 字段拼错、M1 两阶段没吐对坐标),表现为**多 topic 多档普遍坏、且 fidelity 与 τ 都不单一指向**(不是某个轴施压不到位、也不是某两档撞糊,而是卡本身就不成形)。这是排除①②后才考虑的兜底。
**精确门限(排除式 + 跨维普遍性双条件，写进 `references/backprop-heuristic.md`):**

1. **跨维条件(与①②区分的核心)**:本 batch 中 `fidelity_rate<0.90` 的 topic 与 `monotonicity_pass=false` 的 topic **高度重叠且都伴随**——即不是"fidelity 好但 τ 塌"(纯②)、也不是"τ 好但 fidelity 塌"(纯①),而是 **fidelity 与 τ 两者同塌**。单维指向①或②,双维同塌才疑③。
2. **普遍性门限(首版保守值，pilot 可调)**:**≥半数 topic(8 中 ≥4)同时 fidelity 与 τ 双塌** = 结构性阈值。理由:①②是局部问题(某轴某档),不会让半数 topic 同时双指标崩;只有卡组装本身坏(F0–F9 结构、M1 坐标)才会全局性同时拖垮注入保真与阶梯序。低于此门限优先按①②单变量归因,③是最后兜底。
3. **先排除工具坏**:若 parser 自身分歧(FS1-3)或 leak_audit 频繁中断,先修工具,不归③。

此门限标 **pilot-tunable**(与 F8、completability 同属 pilot 校准参数),首版 ≥4/8,跑通后按真实分布收紧。

###### weights.revise("assembler_params", k, ...)

**这一步做什么**
③的修订调用,四参同①(`target/k/new/reason`),仅 `target="assembler_params"`、`k`=**组装旋钮名**:

- `k ∈ assembler_params 的旋钮名`,当前 `{two_stage, field_template}` 等。**充分性裁定:框架够用但需补字段 + 数据派改造**——`two_stage`(M1 先坐标后扩卡)+ `field_template`(F0–F9 组装模板)在语义上覆盖 assembler 职责,但现有 `assembler.py` 把 `DEFAULT_PRESSURE_TURNS`/`f0_persona`/`f6_acceptance` 等**硬编码在源码里**(代码派债),数据派下须把这些外移进 `assembler_params`,至少补:`f6_derivation`(F6 acceptance 由 F1/F3/F2 派生的规则参数)、`turn_budget`(=F8,batch 内恒定的 confound 控制,现 `DEFAULT_PRESSURE_TURNS`/`DEFAULT_CLOSING_TURNS`)。③优先级最低(兜底),不必再加更多旋钮(旋钮太多反违单变量受控)。`k` 候选随补字段而扩,无需另标。
- `new`:该旋钮的新值;`reason`:归因结论。

落盘同①:`apply_weight_update.py` 改 `weights/<batch+1>.json` 的 `assembler_params` 段那一个旋钮 → `revision_log.jsonl` 追加 `{target:"assembler_params", key, old, new, reason}` → emit `weight_revised{target, key, old, new, reason}`(对齐源)。`assembler.py` 源码不动。

**CHECKPOINT(写):** `weights/<batch+1>.json`(仅 assembler_params 一个旋钮变更)+ `revision_log.jsonl` + `trace.jsonl` 的 `weight_revised`(同①格式)。

##### /compact + 重载 optimization-loop skill → LOOP

**这一步做什么**
backprop 改完权重后的收尾,**闭合 LOOP-2**:optimizer `/compact` 压缩上下文,然后从磁盘重建跨-batch 状态(不靠被压缩掉的记忆),回 epoch-loop 开下一个 batch。这是 §state"disk 是唯一真相"纪律的落地点,也是 optimizer 能长跑不爆 context 的关键。

**为何 compact + 重载(时机:决策已定):** optimizer 是 tmux 长驻 REPL,跑很多 batch,context 会累积到撑爆。**每个 batch 结束(backprop 后)固定 `/compact` 一次**(节奏可预测、状态边界清晰,不按 context 用量阈值触发以免额外判断)。但 `/compact` 会把对话历史(含 `optimization-loop` skill 正文、本 batch 推理)压缩掉,所以 compact 后**必须重载 skill**:重新 load `optimization-loop`,拿回 §loop/§gate/§backprop/§state/§tools 全文,才知道下一 batch 怎么跑。

**LOOP 闭合(衔接:决策已定):** 重载 + 从盘恢复状态后,回到 epoch-loop 顶部开下一 batch。**关键衔接**:下一 batch 的 `gen_configs.py` 读的是**本次 backprop 新建的 `weights/<batch+1>.json`**(而非旧 batch 的)——新权重正是通过这份文件进入下一轮生成的。这把"改了权重"与"下一轮用上新权重"接上了,LOOP 才真正闭合(否则改了等于没改)。

###### 重读 weights/\<batch+1\>.json + revision_log.jsonl + trace 尾部

**这一步做什么**
`/compact` 后从盘恢复跨-batch 状态的**读数清单**——optimizer 不靠记忆(开场 prompt 已钉"Memory is not trustworthy; disk is the only source of truth"),全部从磁盘重建:

| 读什么 | 恢复什么 | 为何必须 |
| --- | --- | --- |
| `weights/<batch+1>.json` | 下一 batch 要用的**新权重**(三段 + frozen_label) | gen_configs 据此造卡;不读回就用错权重 |
| `revision_log.jsonl` | **改过哪些权重的历史** | 防重复改同一处、可复盘 backprop 轨迹 |
| `trace.jsonl` **尾部** | `recent_ratios`(收敛轨迹)、当前 `batch_id` 计数、最近 batch_done、**末行 `seq`** | "连续 3 batch 过闸"判定全靠 `recent_ratios`;compact 掉记忆后必须从 trace 尾捞回,否则收敛判定断链。`seq` 从末行 +1 续号(`trace_emit.py` 无状态,post-compact 事件序号不重置、不冲突) |

> 这三样恢复齐,optimizer 就回到"仿佛没 compact 过"的状态:知道用哪份权重、改过什么、离收敛还差几个连续过闸。`batch_id` **取 `weights/` 目录最大编号本身**(不 +1;因 backprop 已预写 `<batch+1>.json`,最高编号文件即下一批权重;§state,见 L422),与 trace 尾部互校。

**工具**:optimizer 用 Read/Bash 读盘 + `/compact`(CC 内建),**无新脚本**。

**CHECKPOINT(读):** 本步是"读"checkpoint(与各"写"点配对)——读 `weights/<batch+1>.json` + `revision_log.jsonl` + `trace.jsonl` 尾部;读毕回 LOOP-2 顶,进下一 batch。

## END
