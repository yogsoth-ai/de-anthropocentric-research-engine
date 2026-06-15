---
name: web-search
description: 'Import SOP: 快速 web 扫描，发现 URL 和 snippet（来自 web-browsing）'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/web-search/SKILL.md
source_skill: web-search
provides: 快速 web 搜索能力 — 发现相关 URL、snippet、初步信息
dependencies:
  sops:
  - web-search
execution: import
---

# Web Search (Import)

从 `web-browsing` 技能库导入的快速 web 搜索能力。

## 用途

- 快速搜索理论框架、方法论文献
- 发现相关 URL 和 snippet
- 初步信息收集

## 使用方式

直接调用 `web-browsing` 中的 `web-search` skill。该 skill 提供:
- Brave Search API 调用
- 结果过滤和排序
- Snippet 提取

## 何时使用

- 需要快速了解某个概念/框架/方法
- 需要找到相关资源的 URL
- 初步信息扫描（不需要深度阅读）

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
