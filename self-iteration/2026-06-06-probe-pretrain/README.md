# probe-pretrain (self-iteration / 2026-06-06)

DARE 探针数据集生成器 — Pretrain 阶段。三层 CC 嵌套生成带标签的
(research_config, research_graph, research_result) 样本。范围：训练→冻结→落盘。
Held-out 产出属阶段 B，另起 spec。做在本 DARE repo 的 self-iteration 子目录内，
不另开 repo。

## 设计与计划

- Spec: `docs/superpowers/specs/2026-06-06-dual-cc-pretrain-design.md`
- Plan: `docs/superpowers/plans/2026-06-06-dual-cc-pretrain.md`

## 跑测试

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## 硬约束

- **4 层不变式**：不编辑活体 DARE skill；本目录全是附加 probe-tooling。
- **隐私红线**：读 session jsonl 的工具 `--logs-dir` 必填、无默认；落盘去标识。
- **W5 check-blind**：两个 loss 评判 skill + 生成全程不见 32-check / 6-primitive。
- **D1–D5 唯一质量标准**：禁用学术标准作判据。
