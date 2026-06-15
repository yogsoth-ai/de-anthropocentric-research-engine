---
name: web-research
description: 'Import SOP: 深度 web 研究，全文抓取分析（来自 web-browsing）'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/web-research/SKILL.md
source_skill: web-research
provides: 深度 web 研究能力 — 全文抓取、内容分析、信息综合
dependencies:
  sops:
  - web-research
execution: import
---

# Web Research (Import)

从 `web-browsing` 技能库导入的深度 web 研究能力。

## 用途

- 深度研究某个理论框架的细节
- 全文抓取和分析网页内容
- 综合多个来源的信息

## 使用方式

直接调用 `web-browsing` 中的 `web-research` skill。该 skill 提供:
- Brave Search + Apify 全文抓取
- 内容分析和信息提取
- 多来源综合

## 何时使用

- 需要深入了解某个框架/方法的完整细节
- 需要从网页中提取结构化信息
- 需要综合多个来源形成完整理解
