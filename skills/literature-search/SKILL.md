---
name: Literature Search
description: Medium-depth literature search — read AI-summarized reports for every paper analyzed
type: sop
layer: sop
agents: [alphaxiv, semantic-scholar]
tools:
  alphaxiv: [discover_papers, get_paper_content]
  semantic-scholar: [relevanceSearch, paper, paperBatch, citations, references]
input: query (string), scope (survey | gap-analysis | background)
output: PaperAnalysis[] with metadata + AI summary content
---

# Literature Search SOP

## Layer Rules
- **Layer**: sop — wraps MCP tools directly
- **Called by**: Any tactic or strategy requiring literature survey with paper content reading
- **Calls**: alphaxiv MCP tools, semantic-scholar MCP tools (never calls other SOPs)

## Purpose

Medium-depth reading. Understand methods, contributions, and findings via AI-generated summary reports. Suitable for literature surveys, gap analysis, and building background knowledge.

Use this when you need to:
- Conduct a literature survey on a topic
- Understand what methods exist and how they compare
- Identify gaps in current research
- Build background knowledge for a research project

**This skill reads AI-summarized reports** — not raw full text. For rigorous analysis requiring raw text, use `literature-research`.

## Tools

| Tool | Purpose | Returns |
|------|---------|---------|
| `alphaxiv.discover_papers` | Primary search — arXiv semantic search | Ranked paper list with metadata |
| `ss.relevanceSearch` | Supplementary search — non-arXiv papers | Title, abstract, authors, citationCount |
| `ss.paper / ss.paperBatch` | Metadata enrichment | Citation count, DOI, S2 ID, externalIds |
| `ss.citations` | Papers that cite this paper (incoming) | Citing paper list with context |
| `ss.references` | Papers this paper cites (outgoing) | Referenced paper list |
| `alphaxiv.get_paper_content` | AI summary report (fullText: false) | Structured AI-generated paper report |

## HARD-GATE

<HARD-GATE>
**Do NOT base analysis on abstracts or discover_papers snippets alone.**

For EVERY paper selected for analysis, you MUST call:
```
alphaxiv.get_paper_content(url: arxiv_url, fullText: false)
```

This returns an AI-generated summary report optimized for LLM consumption.

**PROHIBITED:**
- Completing a research task without reading paper content
- Using only abstracts from ss.relevanceSearch as your evidence
- Using only discover_papers snippets as your evidence
- Claiming to understand a paper's methodology from its abstract alone

**REQUIRED:**
- Call get_paper_content for every paper you analyze
- Base your analysis on the AI summary report content
- Minimum 5 papers read via get_paper_content for any survey task
</HARD-GATE>

## Workflow

### Step 1: Search

**Primary (arXiv):**
```
alphaxiv.discover_papers(
  keywords: ["keyword1", "keyword2", "keyword3"],
  question: "Detailed description of papers needed",
  difficulty: 5
)
```

**Supplementary (non-arXiv):**
```
ss.relevanceSearch(
  query: "search terms",
  limit: 20,
  year: "2022-2024"
)
```

### Step 2: Enrich Metadata

For papers found via alphaxiv, enrich with citation data:
```
ss.paperBatch(
  paper_ids: ["ARXIV:2301.xxxxx", "ARXIV:2302.xxxxx", ...]
)
```

Returns: citationCount, DOI, S2 ID for each paper.

### Step 3: Select Papers

Choose top N papers (typically 5-15) based on:
- Relevance to research question
- Citation count (impact indicator)
- Recency (for fast-moving fields)
- Diversity of approaches (avoid reading only one school of thought)

### Step 4: Read AI Summary Reports

For each selected paper:
```
alphaxiv.get_paper_content(
  url: "https://arxiv.org/abs/XXXX.XXXXX",
  fullText: false
)
```

`fullText: false` (default) returns an AI-generated intermediate report:
- Structured summary of contributions
- Key methods and techniques
- Main results and findings
- Optimized for LLM consumption (faster than raw text)

### Step 5: Citation Graph Expansion (Optional)

To find related work not caught by keyword search:
```
ss.citations(paper_id: "ARXIV:XXXX.XXXXX", limit: 50)
ss.references(paper_id: "ARXIV:XXXX.XXXXX", limit: 50)
```

Filter results by year and citation count, then repeat Steps 3-4 for promising papers.

## Tool-Specific Notes

### alphaxiv.get_paper_content
- `fullText: false` (default) — AI-generated report, faster, structured
- `fullText: true` — raw extracted text, slower, complete (use in literature-research, not here)
- Accepts: arXiv URL (`https://arxiv.org/abs/XXXX.XXXXX`), PDF URL, alphaXiv URL
- Only works for arXiv papers — non-arXiv papers cannot be read via this tool

### ss.paperBatch
- Max 500 papers per call
- Auto-prefixes bare arXiv IDs (e.g., `2301.12345` → `ARXIV:2301.12345`)
- Returns null for papers not found

### ss.citations / ss.references
- Max 1000 results per call
- Use `offset` and `limit` for pagination
- Includes citation context, intent, and influence flags

## Examples

### Literature survey: "attention mechanisms in vision transformers"

```
# Step 1: Search
alphaxiv.discover_papers(
  keywords: ["vision transformer", "attention", "ViT"],
  question: "Papers proposing or analyzing attention mechanisms in vision transformers",
  difficulty: 5
)
ss.relevanceSearch(query: "vision transformer attention mechanism", limit: 15, year: "2022-2024")

# Step 2: Enrich
ss.paperBatch(paper_ids: ["ARXIV:2010.11929", "ARXIV:2103.14030", ...])

# Step 3: Select top 8 by citation count + relevance

# Step 4: Read each
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2010.11929")  # ViT
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2103.14030")  # Swin
# ... repeat for all 8

# Step 5: Expand via citations of ViT
ss.citations(paper_id: "ARXIV:2010.11929", limit: 30)
```

### Gap analysis: "efficient inference for large language models"

```
# Step 1: Broad search
alphaxiv.discover_papers(
  keywords: ["LLM", "efficient inference", "quantization", "pruning"],
  question: "Methods for making large language model inference faster or cheaper",
  difficulty: 6
)

# Step 2-4: Enrich, select 10, read AI summaries

# Step 5: Check what recent papers cite the seminal works
ss.citations(paper_id: "ARXIV:2210.17323", limit: 50)  # GPTQ
ss.citations(paper_id: "ARXIV:2306.00978", limit: 50)  # AWQ
```
