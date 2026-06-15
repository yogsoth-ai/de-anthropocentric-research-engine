---
name: paper-research
description: 'Import SOP: 深度文献研究，原始全文 + PDF 问答（来自 literature-engine）'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-research/SKILL.md
source_skill: paper-research
provides: 深度文献研究能力 — 全文获取、PDF 问答、深度分析
dependencies:
  sops:
  - literature-research
execution: import
---

# Paper Research (Import)

从 `literature-engine` 技能库导入的深度文献研究能力。

## 用途

- 获取论文全文（markdown 格式）
- 对论文 PDF 进行问答
- 深度分析论文方法和结果

## 使用方式

直接调用 `literature-engine` 中的 `paper-research` skill。该 skill 提供:
- 论文全文获取（多源 fallback）
- PDF 问答（AlphaXiv answer_pdf_queries）
- AI 三遍阅读法（Keshav method）

## 何时使用

- 需要深入理解论文的方法细节
- 需要从论文中提取特定信息
- 需要对论文进行深度分析

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |

<!-- END available-tables (generated) -->
