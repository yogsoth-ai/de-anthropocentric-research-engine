---
name: literature-survey
description: Autonomous Literature Survey Campaign — 5 research paradigms (scoping, systematic, deep, narrative, snowball) with quantitative budget enforcement. Selects and executes the right survey paradigm based on research intent.
execution: campaign
used-by: knowledge-acquisition
---

# Literature Survey

Autonomous literature survey engine. Five research paradigms, each a self-contained playbook with quantitative budget enforcement. You provide a research question — it searches, screens, reads, categorizes, identifies gaps, and produces a structured survey output.

## Strategy Routing

| Signal | Strategy |
|--------|----------|
| 新领域全景映射、broad overview、field mapping | → scoping-survey |
| 穷尽式覆盖、PRISMA、systematic review | → systematic-survey |
| 精确子问题、specific mechanism、deep dive | → deep-survey |
| 理论驱动、argument building、narrative | → narrative-review |
| 种子论文、citation chain、lineage tracing | → snowball |

## Manifest

### Strategies (5)
- scoping-survey
- systematic-survey
- deep-survey
- narrative-review
- snowball

### Tactics (3)
- prisma-screening
- citation-chaining (shared: patent-mining, baseline-establishment)
- narrative-framing

### Subagent SOPs (11)
- survey-synthesis
- define-search-protocol
- categorize-papers (shared: meta-analysis, baseline-establishment)
- extract-data
- quality-assessment
- seed-selection
- saturation-detection (shared: patent-mining, benchmark-archaeology)
- taxonomy-mapping
- prisma-flowchart
- thematic-coding
- gap-identification (shared: benchmark-archaeology, baseline-establishment)

### Import SOPs (5, shared across all campaigns)
- web-search
- web-research
- paper-overview
- paper-search
- paper-research

## Budget Table

| Strategy | web-search | web-research | paper-overview | paper-search | paper-research |
|----------|-----------|-------------|---------------|-------------|---------------|
| scoping-survey | 100 | 10 | 100 | 20 | 0 |
| systematic-survey | 50 | 5 | 60 | 40 | 30 |
| deep-survey | 30 | 5 | 40 | 40 | 20 |
| narrative-review | 80 | 15 | 50 | 40 | 20 |
| snowball | 20 | 3 | 30 | 30 | 20 |

All values ±10% flexibility. Deviations require explicit reasoning.

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries, read_files_from_github_repository |
| semantic-scholar | ss_paper, ss_paper_batch, ss_references, ss_citations, ss_recommendations, ss_relevance_search, ss_author, ss_author_papers |

## Context Management

- Campaign start: context-init
- After each strategy completes: context-checkpoint (append to literature-survey context file)
