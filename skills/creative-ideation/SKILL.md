---
name: creative-ideation
description: Creative Generation Engine — transforms research hypotheses into diverse
  solution spaces via 10 parallel creativity campaigns spanning structural, analogical,
  destructive, and combinatorial methods.
execution: entry
pre-conditions:
- north-star-crystallization (research intent crystallized)
- hypothesis-formation (at least 1 testable hypothesis or precise research question)
dependencies:
  campaigns:
  - assumption-destruction
  - biomimicry
  - combinatorial-creativity
  - cross-domain-discovery
  - lateral-thinking
  - morphological-exploration
  - perspective-forcing
  - structural-deconstruction
  - synectics
  - systematic-enumeration
  sops:
  - creative-ideation-paper-overview
  - creative-ideation-paper-research
  - creative-ideation-paper-search
  - creative-ideation-web-research
  - creative-ideation-web-search
---

# Creative Ideation

## Campaign Routing

| Signal Keywords | Route To |
|----------------|----------|
| SCAMPER, TRIZ, 组件手术, 结构变换, 功能裁剪 | → structural-deconstruction |
| 跨域, 类比迁移, bisociation, 随机刺激, 强制连接 | → cross-domain-discovery |
| 假设否定, 反向头脑风暴, 最差方法, 反 benchmark | → assumption-destruction |
| 仿生, 生物类比, 自然策略, BioTRIZ, 生态模式 | → biomimicry |
| 类比, 隐喻, 远足法, 个人类比, 符号压缩 | → synectics |
| 形态分析, Zwicky box, CCA, 维度组合, 设计空间 | → morphological-exploration |
| PO, 横向思维, 概念扇, 随机入口, 挑战操作 | → lateral-thinking |
| 概念融合, blending, 涌现, 多层组合, 功能重分配 | → combinatorial-creativity |
| 视角切换, 六帽, 角色扮演, 约束注入, 时间投射 | → perspective-forcing |
| 穷举, 覆盖分析, 方法矩阵, ablation, 失败分类 | → systematic-enumeration |

## Multi-Campaign Orchestration

When the research problem warrants broad creative exploration, CC may invoke multiple campaigns in parallel. Four natural cluster families:

| Cluster | Campaigns | When |
|---------|-----------|------|
| 类比族 (Analogy) | cross-domain-discovery + biomimicry + synectics | Problem benefits from external domain transfer |
| 组合族 (Combinatorial) | structural-deconstruction + morphological-exploration + combinatorial-creativity | Problem has decomposable structure |
| 颠覆族 (Disruptive) | assumption-destruction + lateral-thinking + perspective-forcing | Problem is stuck in dominant paradigm |
| 覆盖族 (Coverage) | systematic-enumeration + morphological-exploration | Need exhaustive space mapping |

**全面发散**: Invoke 3-5 campaigns based on problem characteristics. Each campaign executes independently with its own context file. Results aggregated at ENTRY level.

CC decides:
- Which campaigns to invoke (1 or many)
- Execution order (parallel or sequential)
- When to cross-pollinate between campaign outputs
- When to stop (saturation-detection signals)

## Four-Level Hierarchy

```
ENTRY.md (this file)
  └── Campaign (10) — self-contained creative activity domain
        └── Strategy (5 per campaign) — iterative framework with budget + state ledger
              └── Tactic (2-3 per campaign) — SOP combination principle
                    └── SOP — single operation (subagent or import)
```

## MCP Tools

| Server | Tools |
|--------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries |
| semantic-scholar | paper, paperBatch, references, citations, recommendations, relevanceSearch |

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research SOPs |
| literature-engine | paper-overview + paper-search + paper-research SOPs |
| subagent-spawning | Subagent dispatch conventions (spawn-agent skill) |
| context-management | Checkpoint protocol (context-init, context-checkpoint) |

## Context Management

- **Campaign start**: `context-init` — load or create campaign context file
- **After each strategy**: `context-checkpoint` — append strategy output to campaign file
- **CC discretion**: Additional checkpoints when information density warrants it

Context file naming: `context/creative-ideation-[campaign]-[topic].md`

## Execution Boundary

This engine STOPS at idea generation. Its output is a structured set of diverse ideas with:
- Description (what the idea is)
- Source method (which campaign/strategy/SOP produced it)
- Novelty assessment (BREAKTHROUGH / HIGH / MODERATE / INCREMENTAL)
- Feasibility initial judgment (not deep validation)

It does NOT:
- Converge or select (→ convergence repo)
- Validate or debate (→ validation repo)
- Design experiments (→ experiment-design repo)
- Implement or prototype

## Shared Components

### Import SOPs (5, all campaigns)

| SOP | Source | Quality Gate |
|-----|--------|-------------|
| web-search | web-browsing | Snippets only — no conclusions from snippets |
| web-research | web-browsing | Must fetch full page via apify |
| paper-overview | literature-engine | Abstract only — no methodology conclusions |
| paper-search | literature-engine | AI summary — sufficient for methodology understanding |
| paper-research | literature-engine | Full text — required for quoting results |

### Shared Subagent SOPs (9)

| SOP | Used By |
|-----|---------|
| saturation-detection | All 10 campaigns |
| novelty-scoring | All 10 campaigns |
| idea-synthesis | All 10 campaigns |
| domain-scanning | cross-domain, biomimicry, synectics, combinatorial |
| assumption-surfacing | assumption-destruction, lateral-thinking, perspective-forcing, structural-deconstruction |
| constraint-injection | perspective-forcing, lateral-thinking, structural-deconstruction, morphological-exploration |
| parameter-identification | structural-deconstruction, morphological-exploration, combinatorial-creativity, systematic-enumeration |
| po-provocation | assumption-destruction, lateral-thinking, perspective-forcing |
| random-word-stimulus | cross-domain-discovery, lateral-thinking, synectics |

### Shared Tactics (4)

| Tactic | Used By |
|--------|---------|
| analogy-extraction | cross-domain-discovery, synectics, biomimicry |
| combination-mapping | morphological-exploration, combinatorial-creativity, structural-deconstruction, systematic-enumeration |
| provocation-generation | lateral-thinking, assumption-destruction, perspective-forcing |
| evaluation-filtering | All 10 campaigns |
