---
name: paper-overview
description: 'Import SOP: 论文快速扫描，返回 abstract 和 metadata（来自 literature-engine）'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-overview/SKILL.md
source_skill: paper-overview
provides: 论文快速扫描能力 — abstract、metadata、基本信息
dependencies:
  sops:
  - literature-overview
execution: import
---

# Paper Overview (Import)

从 `literature-engine` 技能库导入的论文快速扫描能力。

## 用途

- 快速了解一篇论文的主题和贡献
- 获取论文 metadata（作者、年份、引用数）
- 判断论文是否值得深入阅读

## 使用方式

直接调用 `literature-engine` 中的 `paper-overview` skill。该 skill 提供:
- Semantic Scholar / AlphaXiv 元数据获取
- Abstract 提取
- 基本相关性判断

## 何时使用

- 需要快速判断一篇论文是否相关
- 需要获取论文的基本信息
- 批量扫描多篇论文时

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-overview | Quick landscape scan — discover papers on a topic without full-text reading |

<!-- END available-tables (generated) -->
