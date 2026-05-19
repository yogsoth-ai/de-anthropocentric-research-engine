---
name: benchmark-archaeology
description: Evaluation Methodology Archaeology Campaign — 5 strategies for systematic analysis of AI/ML benchmarks, metrics, and leaderboards. Reveals construct validity issues, saturation, data contamination, and evaluation protocol inconsistencies.
execution: campaign
used-by: knowledge-acquisition
---

# Benchmark Archaeology

Systematic excavation and critical analysis of AI/ML evaluation methodology. Treats benchmarks as historical artifacts requiring forensic examination — uncovering hidden assumptions, methodological drift, validity decay, and coverage gaps that accumulate over time.

## Strategy Routing

| Signal | Route To |
|--------|----------|
| "audit this benchmark", "benchmark quality", "BetterBench" | benchmark-audit |
| "saturation", "ceiling", "score plateau", "when will X be solved" | saturation-analysis |
| "does it actually measure", "construct validity", "what does score mean" | validity-probing |
| "what's not tested", "coverage gaps", "missing capabilities" | coverage-mapping |
| "different papers get different scores", "protocol differences" | protocol-forensics |

## Manifest

### Strategies (5)

| Strategy | Purpose |
|----------|---------|
| benchmark-audit | Systematic quality assessment using BetterBench 46-criterion framework |
| saturation-analysis | Track score trajectories, detect saturation and failure points |
| validity-probing | Challenge construct validity — does benchmark measure claimed capability? |
| coverage-mapping | Map evaluation coverage, identify untested capability dimensions |
| protocol-forensics | Analyze evaluation protocol differences across papers for same benchmark |

### Tactics (3)

| Tactic | Purpose |
|--------|---------|
| score-trajectory-analysis | Collect historical scores, fit saturation curves, detect inflection points |
| artifact-detection | Detect annotation artifacts and shortcuts in benchmarks |
| evaluation-protocol-comparison | Compare implementation differences of same benchmark across papers |

### Subagent SOPs (9 + 1 shared)

| SOP | Purpose |
|-----|---------|
| benchmark-inventory | Identify and catalog all relevant benchmarks in target domain |
| metric-decomposition | Decompose composite metrics into constituent signals |
| contamination-audit | Detect train-test data leakage and memorization artifacts |
| construct-validity-assessment | Evaluate whether benchmark measures its claimed capability |
| documentation-audit | Assess documentation completeness against BetterBench/Datasheets standards |
| capability-taxonomy-mapping | Build capability taxonomy, map existing benchmark coverage |
| leaderboard-dynamics-analysis | Analyze leaderboard score distributions, compression, selective reporting |
| protocol-element-extraction | Extract evaluation protocol parameters from papers |
| benchmark-synthesis | Produce final structured audit report |
| saturation-detection (shared) | Detect saturation signals in score trajectories (from literature-survey) |

## Budget Table

| Strategy | Benchmarks | Papers | Web Searches |
|----------|-----------|--------|--------------|
| benchmark-audit | 5 | 30 | 40 |
| saturation-analysis | 15 | 50 | 60 |
| validity-probing | 3 | 40 | 30 |
| coverage-mapping | 20 | 30 | 50 |
| protocol-forensics | 5 | 60 | 30 |
| **Total** | **48** | **210** | **210** |

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | get_paper_content, answer_pdf_queries |
| semantic-scholar | ss_paper, ss_relevance_search, ss_citations, ss_references |

## Context Management

All outputs write to `context/benchmark-archaeology/`:

```
context/benchmark-archaeology/
  audit/              # benchmark-audit outputs
  saturation/         # saturation-analysis outputs
  validity/           # validity-probing outputs
  coverage/           # coverage-mapping outputs
  forensics/          # protocol-forensics outputs
  synthesis/          # Final cross-strategy synthesis
```

Each strategy maintains its own state ledger within its output directory.
