---
name: paper-search
description: 'Import SOP: 中深度文献搜索，AI 摘要报告（来自 literature-engine）'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-search/SKILL.md
source_skill: paper-search
provides: 中深度文献搜索能力 — 搜索、筛选、AI 摘要
dependencies:
  sops:
  - literature-search
execution: import
---

# Paper Search (Import)

从 `literature-engine` 技能库导入的中深度文献搜索能力。

## 用途

- 搜索特定主题的相关论文
- 获取 AI 生成的论文摘要报告
- 筛选和排序搜索结果

## 使用方式

直接调用 `literature-engine` 中的 `paper-search` skill。该 skill 提供:
- 多源搜索（Semantic Scholar + Google Scholar + AlphaXiv）
- AI 摘要生成
- 相关性排序

## 何时使用

- 需要找到某个主题的相关论文集合
- 需要 AI 辅助的论文摘要
- 需要在多个数据库中搜索
