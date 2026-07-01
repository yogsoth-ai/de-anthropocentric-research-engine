# Ladder-Foundry 代号速查

## STAGE(构建阶段 · 7)
- **STAGE1** 数据核心:L1/L2 + 三权重 L3/L4/L5 + L6(本地 pytest)
- **STAGE2** persona 内核:D1/D2/L7(首次产出完整 sim persona)
- **STAGE3** 9 leaf 脚本:L8–L14(本地 pytest)
- **STAGE4** 契约+loss+脑:L15/L16 + S1–S6(本地文本验)
- **STAGE5** 远端环境:R1/R3(首次三层 CC 真嵌套,Plan A)
- **STAGE6** 单题阶梯:D3占位 + R4(首条真阶梯)
- **STAGE7** 全机收敛:D3满 + D4 + R2/R5/R6/R7 + L17(Plan C)

## L(数据派内核 + 9 leaf 脚本 · 17)
- **L1** `weights.py` — 权重数据核心(4 段 schema,revise 守白名单)
- **L2** `leak_audit.py` — W5 检测签名词拦截
- **L3** `axes.py` ① — 纯读 axis_prose 出档位话术
- **L4** `interpolator.py` ② — 纯读 interp_params 出 6-rung 铺陈
- **L5** `assembler.py` ③ — 纯读 assembler_params 组装坐标卡
- **L6** `cards.py` — PolicyCard 序列化
- **L7** `gen_configs.py` — 生成管线,出 48(本地 6)config persona
- **L8** `new_run_id.py` — run_id + runs/ 骨架
- **L9** `trace_emit.py` — 11 事件账本追加
- **L10** `save_transcript.py` — 从 exec jsonl 提 transcript(--logs-dir 必填)
- **L11** `concat_triple.py` — fence 切块拼三元组(契约源)
- **L12** `gate_eval.py` — 闸门纯算术(三路 AND/pass_ratio/converged)
- **L13** `apply_weight_update.py` — 改一段权重(F2)/逐字节复制(F1)
- **L14** `write_dataset.py` — 白名单落数据集(label=生成条件)
- **L15** `run_codex_loss.py` — 起 codex 算 loss-1/loss-2
- **L16** `schemas/loss1.json+loss2.json` — loss 输出 schema
- **L17** `freeze.py+coverage_report.py` — 冻结权重 + 生成侧报告

## S(skill · 6)
- **S1** `formated-specs` — exec 末轮产 research-graph fence(待建)
- **S2** `formated-results` — exec 末轮产 research-result fence(待建)
- **S3** `injection-fidelity` — codex loss-1,判注入保真(check-blind)
- **S4** `ladder-quality-order` — codex loss-2,判阶梯单调 τ(check-blind)
- **S5** `optimization-loop` — optimizer 脑,§loop/gate/backprop/state/tools
- **S6** `references` — gate-thresholds + backprop-heuristic

## D(persona/数据 · 4)
- **D1** PolicyCard schema — F0–F9 + 5 轴{A1–A5}+B1 语义
- **D2** 2 端点 persona — id0 天才 / idN-1 抬杠(喂 ① 默认值)
- **D3** `topics.json` — 研究对象(STAGE6 占位1,STAGE7 满8)
- **D4** `optimizer-opening-prompt.txt` — optimizer 起跑令

## R(远端环境+运行 · 7)
- **R1** env/config-dir/skill-copy — 四身份可起+两组key隔离
- **R2** `start_optimizer.sh` — tmux 点火+readiness探针
- **R3** 竖切片 1-run e2e — 首次真嵌套(A E1–E5)
- **R4** 单topic 6-rung e2e — 首条真阶梯(B7)
- **R5** PT5 试点硬门 — AS-1端点分离+AS-4铺陈可训(C1)
- **R6** 全LOOP-2 收敛 — backprop真验,连3batch(C2)
- **R7** freeze+dataset+监督 — frozen+全标签集+HALT(C3/C4)

## 关系图

```mermaid
graph TD
  classDef tbd fill:#3a3a3a,stroke:#888,color:#ddd;
  classDef processing fill:#5a4a00,stroke:#ffc107,color:#fff;
  classDef done fill:#1b4d2e,stroke:#4caf50,color:#fff;

  subgraph ST1["STAGE1 数据核心"]
    L1[L1 weights]
    L2[L2 leak_audit]
    L3[L3 axes ①]
    L4[L4 interpolator ②]
    L5[L5 assembler ③]
    L6[L6 cards]
  end
  subgraph ST2["STAGE2 persona内核"]
    D1[D1 PolicyCard schema]
    D2[D2 端点persona]
    L7[L7 gen_configs]
  end
  subgraph ST3["STAGE3 9 leaf"]
    L8[L8 new_run_id]
    L9[L9 trace_emit]
    L10[L10 save_transcript]
    L11[L11 concat_triple]
    L12[L12 gate_eval]
    L13[L13 apply_weight_update]
    L14[L14 write_dataset]
  end
  subgraph ST4["STAGE4 契约+loss+脑"]
    L15[L15 run_codex_loss]
    L16[L16 loss schema]
    S1[S1 formated-specs]
    S2[S2 formated-results]
    S3[S3 injection-fidelity]
    S4[S4 ladder-quality-order]
    S5[S5 optimization-loop 脑]
    S6[S6 references]
  end
  subgraph ST5["STAGE5 远端环境"]
    R1[R1 env+身份+skill-copy]
    R3[R3 竖切片1-run]
  end
  subgraph ST6["STAGE6 单题阶梯"]
    D3[D3 topics]
    R4[R4 单topic6-rung]
  end
  subgraph ST7["STAGE7 全机收敛"]
    D4[D4 opening-prompt]
    R2[R2 start_optimizer]
    R5[R5 PT5硬门]
    R6[R6 全LOOP-2收敛]
    R7[R7 freeze+dataset+监督]
    L17[L17 freeze+coverage]
  end

  ST1 ==>|阶段顺序| ST2 ==>|阶段顺序| ST3 ==>|阶段顺序| ST4 ==>|阶段顺序| ST5 ==>|阶段顺序| ST6 ==>|阶段顺序| ST7

  L1 -->|依赖| L3
  L1 -->|依赖| L4
  L1 -->|依赖| L5
  L1 -->|依赖| L7
  L1 -->|依赖| L13
  L1 -->|依赖| L17
  L4 -->|依赖| L5
  D1 -->|依赖| D2
  D2 -->|供料默认权重| L1
  L2 -->|依赖| L7
  L3 -->|依赖| L7
  L5 -->|依赖| L7
  L6 -->|依赖| L7
  L16 -->|依赖| L15
  S3 -->|依赖| L15
  S4 -->|依赖| L15
  S6 -->|依赖| S3
  S6 -->|依赖| S4
  S6 -->|依赖| S5
  L11 -.->|输出契约| S1
  L11 -.->|输出契约| S2

  L7 -->|供料config| S5
  L8 -->|供料| S5
  L9 -->|供料| S5
  L10 -->|供料| S5
  L11 -->|供料三元组| S5
  L12 -->|供料| S5
  L13 -->|供料| S5
  L14 -->|供料| S5
  L15 -->|供料loss| S5
  D2 -->|供料端点坐标| S5

  R1 -->|依赖| R3
  D1 -->|供料| R3
  D2 -->|供料| R3
  L7 -->|供料config| R3
  L15 -->|依赖| R3
  S1 -->|依赖| R3
  S2 -->|依赖| R3
  S3 -->|依赖| R3
  S4 -->|依赖| R3
  R3 -->|依赖| R4
  S5 -->|依赖| R4
  D3 -->|供料题| R4
  R4 -->|依赖| R5
  D2 -->|供料端点| R5
  R5 -->|go门| R6
  D3 -->|供料8题| R6
  D4 -->|供料| R2
  R2 -->|点火| R6
  R6 -->|收敛| R7
  L17 -->|依赖| R7

  class L1,L2,L3,L4,L5,L6 done;
  class L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17 tbd;
  class S1,S2,S3,S4,S5,S6 tbd;
  class D1,D2,D3,D4 tbd;
  class R1,R2,R3,R4,R5,R6,R7 tbd;
```
