---
name: Literature Overview
description: Quick landscape scan — discover papers on a topic without full-text reading
type: sop
layer: sop
agents: [alphaxiv, semantic-scholar]
tools:
  alphaxiv: [discover_papers]
  semantic-scholar: [relevanceSearch]
input: query (string)
output: PaperList[] with title, authors, year, citationCount, abstract snippet
---

# Literature Overview SOP

## Layer Rules
- **Layer**: sop — wraps MCP tools directly
- **Called by**: Any tactic or strategy requiring a quick literature landscape scan
- **Calls**: alphaxiv MCP tools, semantic-scholar MCP tools (never calls other SOPs)

## Purpose

Fast landscape scan. Understand what papers exist on a topic, who the key authors are, and rough citation counts. **No full-text reading.** This skill is for orientation — getting a bird's-eye view before committing to deeper reading.

Use this when you need to:
- Quickly assess how much literature exists on a topic
- Identify key papers and authors in a field
- Get citation counts to gauge paper impact
- Decide which papers deserve deeper reading (via literature-search or literature-research)

## Tools

| Tool | Purpose | Returns |
|------|---------|---------|
| `alphaxiv.discover_papers` | Semantic search for arXiv papers | Ranked paper list with title, abstract snippet, arXiv ID |
| `ss.relevanceSearch` | Keyword search across all venues | Title, abstract, authors, year, citationCount, paperId |

### Tool Roles
- **alphaxiv.discover_papers** = primary search for arXiv-covered fields (CS, math, physics, stats, EE, quant-bio/finance)
- **ss.relevanceSearch** = supplementary search for non-arXiv papers (biomedical, clinical, social science, humanities)

## HARD-GATE

<HARD-GATE>
**This skill returns abstracts and metadata ONLY.**

Do NOT draw conclusions about:
- Methodology details
- Experimental results
- Specific contributions or findings
- Comparative analysis between papers

Abstracts are for ORIENTATION — identifying what exists and what looks promising.

**For any substantive analysis, escalate to:**
- `literature-search` — read AI-summarized reports (medium depth)
- `literature-research` — read raw full text (deep)

**Treating abstracts as sufficient for research conclusions is PROHIBITED.**
</HARD-GATE>

## Workflow

### Step 1: Search arXiv via alphaxiv

```
alphaxiv.discover_papers(
  keywords: ["keyword1", "keyword2", "keyword3"],
  question: "Detailed semantic description of desired papers",
  difficulty: 3
)
```

**Parameters:**
- `keywords`: 3-4 concise terms (method names, acronyms, authors)
- `question`: Detailed description of what papers you're looking for
- `difficulty`: 1-10 (use 3 for overview, higher = more retrieval effort)

### Step 2: Supplement with semantic-scholar

```
ss.relevanceSearch(
  query: "search terms",
  limit: 20,
  year: "2022-2024",
  fields_of_study: "Computer Science"
)
```

**Parameters:**
- `query`: keyword search string
- `limit`: max results (default 10, max 100)
- `year`: year range filter (e.g., "2023-2024", "2020-")
- `fields_of_study`: field filter (optional)
- `min_citation_count`: citation threshold (optional)
- `open_access_only`: boolean (optional)

### Step 3: Merge and Deduplicate

- Combine results from both sources
- Deduplicate by title similarity or matching arXiv IDs
- Sort by citation count (descending) as default ranking

### Step 4: Return Structured Results

For each paper, present:
- **Title**
- **Authors** (first author + et al. for brevity)
- **Year**
- **Citation Count** (from ss if available)
- **Abstract Snippet** (first 2-3 sentences)
- **Source** (alphaxiv / semantic-scholar / both)

## Tool-Specific Notes

### alphaxiv.discover_papers
- Covers: computer science, mathematics, physics, statistics, quantitative biology/finance, electrical engineering
- Does NOT cover: biomedical, clinical, life science (PubMed, Cell, Nature)
- Returns: paper ID, title, authors, publication date, abstract snippet
- `difficulty` parameter: 1-3 for quick scans, 5-7 for thorough discovery, 8-10 for exhaustive

### ss.relevanceSearch
- Covers: all academic venues (broader than arXiv)
- Returns: title, abstract, authors, year, citationCount, paperId, externalIds
- ID formats in results: S2 ID, arXiv ID, DOI, PMID
- Rate limit: 1 req/s without API key, 100 req/s with SS_API_KEY

## Example

**Quick scan: "graph neural networks for drug discovery"**

```
# Step 1: arXiv search
alphaxiv.discover_papers(
  keywords: ["GNN", "drug discovery", "molecular"],
  question: "Papers applying graph neural networks to drug discovery and molecular property prediction",
  difficulty: 3
)

# Step 2: Supplement
ss.relevanceSearch(
  query: "graph neural network drug discovery",
  limit: 15,
  year: "2022-2024",
  min_citation_count: 50
)

# Step 3-4: Merge, deduplicate, return sorted list
```

**Expected output:** A list of 15-30 papers with titles, authors, years, and citation counts — enough to understand the landscape and pick papers for deeper reading.
