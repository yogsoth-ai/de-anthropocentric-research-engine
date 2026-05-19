---
name: baseline-establishment
description: SOTA Performance Baseline Campaign — 5 strategies for systematically collecting, standardizing, and analyzing performance data across methods. Produces standardized comparison tables, progress curves, and headroom analysis.
execution: campaign
used-by: knowledge-acquisition
---

# Baseline Establishment

## Strategy Routing

| User Intent | Route To |
|-------------|----------|
| Find all methods for a task | method-inventory |
| Extract scores from papers | performance-extraction |
| Normalize conditions across papers | condition-standardization |
| Check reproducibility / discrepancies | discrepancy-analysis |
| Track progress over time / headroom | progress-quantification |

## Manifest

### Strategies (5)

| Strategy | Purpose |
|----------|---------|
| method-inventory | Comprehensively identify all relevant methods for a task |
| performance-extraction | Systematically extract performance data and conditions from papers |
| condition-standardization | Standardize evaluation condition differences across papers |
| discrepancy-analysis | Identify discrepancies between reported and reproducible scores |
| progress-quantification | Track performance progress over time, quantify remaining headroom |

### Tactics (3)

| Tactic | Purpose |
|--------|---------|
| leaderboard-harvesting | Systematically collect performance data from platforms and papers |
| condition-normalization | Compare and standardize experimental conditions across papers |
| progress-curve-construction | Build performance-over-time progress curves |

### Subagent SOPs (10)

| SOP | Purpose |
|-----|---------|
| method-discovery | Identify methods via literature, leaderboards, citation chains |
| score-extraction | Extract (Task, Dataset, Metric, Score, Conditions) tuples |
| condition-cataloging | Record evaluation conditions per method |
| reproducibility-checklist-audit | Assess paper against ML Reproducibility Checklist |
| performance-table-assembly | Assemble unified comparison table |
| compute-normalization | Normalize results by compute budget |
| discrepancy-identification | Compare same-method scores across sources |
| headroom-estimation | Estimate ceiling vs current SOTA gap |
| progress-curve-fitting | Construct performance-over-time data |
| baseline-synthesis | Produce final structured baseline report |

## Budget Table

| Strategy | Methods | Data Points | Web Searches |
|----------|---------|-------------|--------------|
| method-inventory | 50 | 0 | 60 |
| performance-extraction | 30 | 150 | 40 |
| condition-standardization | 20 | 60 | 30 |
| discrepancy-analysis | 15 | 45 | 30 |
| progress-quantification | 30 | 100 | 40 |
| **TOTAL** | **145** | **355** | **200** |

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | get_paper_content, answer_pdf_queries |
| semantic-scholar | ss_paper, ss_relevance_search, ss_citations, ss_references |

## Context Management

Campaign outputs are accumulated in the calling knowledge-acquisition context:

- `methods_inventory.json` — All discovered methods with metadata
- `performance_data.json` — Extracted scores with provenance
- `conditions_matrix.json` — Standardized conditions per method
- `discrepancy_report.json` — Flagged score inconsistencies
- `progress_curves.json` — Time-series performance data
- `baseline_report.md` — Final synthesized baseline document
