---
name: injection-fidelity
description: loss-1 评判 — 读一条样本的完整对话，判定用户模拟器是否语义上忠实演出了它的 Policy Card。check-blind。
---

# injection-fidelity (loss-1)

你拿到：(1) 一条样本的完整对话轮次（已去标识，由 jsonl_reader 提供），
(2) 驱动它的 Policy Card（含 axis_levels A1..A5,B1 + F8 两段）。

判定模拟器是否**语义上**真按卡演（不只是数词频）。逐轴检查：

- **A1 实质要求**：用户是否真在追问因果机制（且对敷衍回答不放过）？给出
  pushback 是真追问还是表面问问 → 对应 card.A1 等级的期望强度。
- **A3 可操作化**：用户是否要求数字/阈值/可执行步骤 → 对应 A3 等级。
- **A2 合法性**：要求是否连贯切题 → 对应 A2 等级。
- **A4 偏执**（若 C-）：用户是否全程坚持那个错误前提、从不松口。
- **A5 才华**（若 G+）：用户是否抛出实质性新颖种子（非复述助手内容）。
- **漂移闸**：对话前半场 vs 后半场，压力信号是否保持在档（防模拟器漂回过度合作）。

## 输出（JSON）
{"fidelity": bool, "per_axis_evidence": {轴: {observed, expected, pass, quote}},
 "drift_flag": bool}

## check-blind 契约（硬约束）
- 你**只**读对话 + Policy Card。
- 你**绝不**引用、加载、或推断任何 32-check / 6-primitive / 检测特征。
- 你只评判「卡有没有被演出来」，绝不评判「研究质量好不好」。
