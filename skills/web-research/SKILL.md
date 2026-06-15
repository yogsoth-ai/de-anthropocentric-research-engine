---
name: Web Research
description: Deep web research — fetches full page content for analysis. Snippets
  alone are PROHIBITED for conclusions.
type: sop
layer: sop
tools:
  web-search-provider:
  - web_search
  - news_search
  apify:
  - rag-web-browser
input: query (string), depth (standard | thorough)
output: PageAnalysis[] with full markdown content + source URL
---

# Web Research SOP

## Layer Rules
- **Layer**: sop — wraps MCP tools directly
- **Called by**: Any tactic or strategy requiring deep web content analysis
- **Calls**: configured web-search MCP tools + apify MCP tools (never calls other SOPs)

## Purpose

Deep web research. Fetch full page content for selected URLs and analyze thoroughly. Suitable for specific topic investigation, competitive analysis, technical documentation reading, and any task requiring substantive understanding of web content.

Use this when you need to:
- Understand a topic thoroughly from web sources
- Read full documentation or articles
- Compare information across multiple sources
- Draw substantive conclusions backed by full content
- Investigate technical details from official docs

**This skill REQUIRES full-page content fetching.** Snippet-only analysis is prohibited.

## Provider Selection

For URL discovery (Step 1), use whichever web-search MCP is configured — check
availability yourself. If more than one is active, try them in the order listed
below. This order is just the writing order, not a hard priority — any active
provider is equally valid.

- Brave — see Provider Details (Discovery) § Brave
- Tavily — see Provider Details (Discovery) § Tavily

For full-page content fetching (Step 3), always use `apify/rag-web-browser`.
This is not configurable — apify is the only supported content fetcher.

## HARD-GATE

<HARD-GATE>
**Search snippets are NOT sufficient for research.**

For EVERY page selected for analysis, you MUST fetch full content via `apify/rag-web-browser`.

**PROHIBITED:**
- Completing a research task using only snippets
- Drawing conclusions without reading full page content
- Presenting snippet summaries as research findings
- Citing information not verified in full-page content

**REQUIRED:**
- Call `apify/rag-web-browser` for every page you analyze
- Minimum 3 pages fetched via apify for any research task
- Every analytical claim must be traceable to full-page content
- Cross-reference claims across multiple fetched pages
</HARD-GATE>

## Workflow

### Step 1: Discover

Find candidate URLs via the configured web-search provider (~10 results per call).
See Provider Details (Discovery) for exact tool name and parameters.

For time-sensitive topics, use news search if available.

Use snippets ONLY to assess relevance for URL selection — not for analysis.

### Step 2: Select

Choose 3-10 most relevant URLs based on:
- Title relevance to research question
- Snippet suggests substantive content (not just a landing page)
- Source authority (official docs, reputable publications, expert blogs)
- Recency (prefer recent for fast-moving topics)
- Diversity of perspectives (avoid single-source bias)

### Step 3: Fetch

For each selected URL, fetch full content:

```
apify/rag-web-browser(query="<URL>", maxResults=1, outputFormats=["markdown"])
```

**Parameters:**
- `query` (required): the URL to fetch (when fetching a specific page) or search terms
- `maxResults` (default 3): set to 1 when fetching a known URL, 3-5 when searching
- `outputFormats` (default ["markdown"]): always use `["markdown"]` for LLM consumption

**When fetching a known URL:** pass the full URL as `query`, set `maxResults=1`
**When doing broad discovery:** pass search terms as `query`, set `maxResults=3`

### Step 4: Analyze

Base ALL conclusions on full page content:
- Quote or paraphrase specific passages
- Cross-reference claims across multiple fetched pages
- Note contradictions between sources
- Identify gaps in coverage
- Cite the source URL for each claim

### Step 5: Follow (Optional)

If fetched pages contain links to deeper resources:
- Extract relevant URLs from the markdown content
- Repeat Steps 3-4 for high-value links
- Build a comprehensive picture from multiple layers
- Useful for: documentation trails, reference chains, related articles

## Provider Details (Discovery)

### Brave

Use for URL discovery only — not for content analysis.

| Tool | Role | Returns |
|------|------|---------|
| `brave_web_search` | General URL discovery | URL, title, snippet |
| `brave_news_search` | Recent news URL discovery | URL, title, snippet, date |

**Key parameters:**
- `query` (required): search terms, max 400 chars
- `count`: 1-20 results (default 10)
- `freshness`: `pd` (24h), `pw` (7d), `pm` (31d), `py` (365d)

**Examples:**

```
brave_web_search(query="model context protocol MCP server development guide 2025", count=10)
brave_news_search(query="GPT-5 announcement details capabilities", freshness="pw", count=10)
```

### Tavily

Use for URL discovery only — not for content analysis.

| Tool | Role | Returns |
|------|------|---------|
| `tavily_search` | General URL discovery | URL, title, content snippet, score |

**Key parameters:**
- `query` (required): search terms
- `max_results`: number of results (default 10)
- `search_depth`: `basic` or `advanced` (default basic)

**Examples:**

```
tavily_search(query="model context protocol MCP server development guide 2025", max_results=10)
```

## Tool-Specific Notes

### apify/rag-web-browser
- `query` (required): Google Search keywords OR a specific URL to fetch
- `maxResults` (default 3): number of pages to scrape
  - Use `1` when fetching a known URL
  - Use `3-5` when doing a broad search via query terms
- `outputFormats` (default ["markdown"]): always use `["markdown"]`
- Some pages may fail to fetch (paywalls, JS-heavy SPAs, anti-bot) — note failures and try alternatives
- Rate limiting: sequential fetches are fine, no special throttling needed
- Large pages may be truncated — check if content seems incomplete
