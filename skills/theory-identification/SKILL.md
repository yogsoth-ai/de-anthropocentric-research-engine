---
name: theory-identification
description: 'SOP: Identify theoretical frameworks relevant to a research gap'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Research gap description + domain tags
output: List of relevant theoretical frameworks [{name, source, core_claim, relevance, applicability}]
dependencies:
  sops:
  - hypothesis-formation-paper-overview
  - hypothesis-formation-paper-search
  - hypothesis-formation-web-search
---

# Theory Identification
Identify theoretical frameworks relevant to a research gap, providing a theoretical basis for mechanism extraction.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. A clear research gap description exists (including domain, phenomenon, unanswered question)
2. Domain tags are provided (used to direct the literature scan)

Not satisfied → stop, return error: missing gap description or domain tags.
</HARD-GATE>

## Pipeline
1. Precheck: verify completeness of the gap description and domain tags
2. Literature scan: search for theoretical literature relevant to the gap (literature-engine + web-browsing)
3. Theory screening: keep theories directly or indirectly relevant to the gap (≥3, remove purely methodological literature)
4. Core claim extraction: distill a 1-2 sentence core_claim for each theory
5. Applicability assessment: assess each theory's explanatory power for the current gap (high/medium/low)
6. Output a structured theory list

## Output Format
```json
[
  {
    "name": "Theory Name",
    "source": "Author (Year) or canonical reference",
    "core_claim": "One-sentence summary of what the theory claims",
    "relevance": "Why this theory relates to the gap",
    "applicability": "high | medium | low"
  }
]
```
Minimum 3 entries, maximum 8 (sorted by applicability descending).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| hypothesis-formation-paper-overview | Import SOP: 论文快速扫描，返回 abstract 和 metadata（来自 literature-engine） |
| hypothesis-formation-paper-search | Import SOP: 中深度文献搜索，AI 摘要报告（来自 literature-engine） |
| hypothesis-formation-web-search | Import SOP: 快速 web 扫描，发现 URL 和 snippet（来自 web-browsing） |

<!-- END available-tables (generated) -->
