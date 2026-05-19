---
name: Literature Research
description: Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis
type: sop
layer: sop
agents: [alphaxiv, semantic-scholar]
tools:
  alphaxiv: [discover_papers, get_paper_content, answer_pdf_queries]
  semantic-scholar: [relevanceSearch, paper, paperBatch, citations, references]
input: query (string), focus (experiment-design | methodology | comparison | replication)
output: DeepAnalysis[] with metadata + raw full text + targeted query results
---

# Literature Research SOP

## Layer Rules
- **Layer**: sop — wraps MCP tools directly
- **Called by**: Any tactic or strategy requiring deep paper reading and rigorous analysis
- **Calls**: alphaxiv MCP tools, semantic-scholar MCP tools (never calls other SOPs)

## Purpose

Deep reading. Raw full text, targeted PDF queries. For rigorous analysis, experiment design, and paper writing. This is the highest-depth skill — you read the actual paper content, not summaries.

Use this when you need to:
- Understand exact methodology details (equations, algorithms, architectures)
- Extract specific experimental setup (hyperparameters, datasets, baselines)
- Compare approaches at a technical level
- Design experiments based on prior work
- Write a paper that cites specific claims with precision

**This skill reads RAW FULL TEXT.** AI summaries are not acceptable at this depth.

## Tools

| Tool | Purpose | Returns |
|------|---------|---------|
| `alphaxiv.discover_papers` | Primary search — arXiv semantic search | Ranked paper list with metadata |
| `ss.relevanceSearch` | Supplementary search — non-arXiv papers | Title, abstract, authors, citationCount |
| `ss.paper / ss.paperBatch` | Metadata enrichment | Citation count, DOI, S2 ID |
| `ss.citations` | Papers that cite this paper | Citing paper list with context |
| `ss.references` | Papers this paper cites | Referenced paper list |
| `alphaxiv.get_paper_content` | Raw full text (fullText: true) | Complete paper text as markdown |
| `alphaxiv.answer_pdf_queries` | Targeted PDF questions | Relevant page content as XML |

## HARD-GATE

<HARD-GATE>
**You MUST read raw full text (fullText: true) for ALL key papers.**

AI summaries (fullText: false) are NOT acceptable for this skill.

**PROHIBITED:**
- Using get_paper_content with fullText: false (AI summaries)
- Basing analysis on abstracts or discover_papers snippets
- Claiming to understand methodology without reading the full methods section
- Citing specific numbers (accuracy, parameters) without reading the results section

**REQUIRED:**
- Call `get_paper_content(fullText: true)` for every key paper (minimum 3)
- Use `answer_pdf_queries` for targeted extraction of specific details
- Read actual equations, tables, and experimental details from full text
- Every claim must be traceable to specific content in the full paper
</HARD-GATE>

## Workflow

### Step 1: Search

**Primary (arXiv):**
```
alphaxiv.discover_papers(
  keywords: ["keyword1", "keyword2", "keyword3"],
  question: "Detailed description of papers needed for deep analysis",
  difficulty: 7
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

Use higher difficulty (7-10) for research-depth searches — you need comprehensive coverage.

### Step 2: Enrich Metadata

```
ss.paperBatch(
  paper_ids: ["ARXIV:2301.xxxxx", "ARXIV:2302.xxxxx", ...]
)
```

### Step 3: Select Key Papers

Choose 3-10 papers for deep reading based on:
- Direct relevance to your specific research question
- Methodological significance (introduces the technique you're studying)
- Recency (most recent results and baselines)
- Citation impact (highly-cited = foundational)

Fewer papers, read deeply > many papers, read shallowly.

### Step 4: Read Raw Full Text

For each selected paper:
```
alphaxiv.get_paper_content(
  url: "https://arxiv.org/abs/XXXX.XXXXX",
  fullText: true
)
```

`fullText: true` returns the raw extracted text — complete paper content including:
- Full methodology sections
- All equations and algorithms
- Complete experimental setup
- Full results tables
- Appendices and supplementary details

### Step 5: Targeted PDF Queries

For specific details that need precise extraction:
```
alphaxiv.answer_pdf_queries(
  url: "https://arxiv.org/pdf/XXXX.XXXXX",
  queries: [
    "What is the exact model architecture?",
    "What hyperparameters were used for training?",
    "What datasets were used for evaluation?",
    "What are the ablation study results?"
  ]
)
```

**Notes:**
- Accepts any PDF URL (not just arXiv)
- Multiple queries on the same paper are nearly free (cached)
- Returns filtered page content as XML with page numbers
- Use for: equations, hyperparameters, ablation results, specific claims

### Step 6: Citation Graph Expansion

Find important related work:
```
ss.citations(paper_id: "ARXIV:XXXX.XXXXX", limit: 50)
ss.references(paper_id: "ARXIV:XXXX.XXXXX", limit: 50)
```

For promising papers from the graph, repeat Steps 3-5.

## Tool-Specific Notes

### alphaxiv.get_paper_content (fullText: true)
- Returns raw extracted text — slower but complete
- Includes all sections, equations (as LaTeX), tables, figure captions
- May be large (10-30 pages of text) — read carefully, don't skim
- Only works for arXiv papers

### alphaxiv.answer_pdf_queries
- Accepts ANY PDF URL (not limited to arXiv)
- Returns XML with `<page num="N">` tags showing relevant content
- Multiple queries in one call = efficient (paper is cached after first query)
- Best for: extracting specific facts, numbers, equations, or claims
- Use AFTER reading full text to drill into specific details

### ss.citations / ss.references
- Include citation context (the sentence where the paper is cited)
- Include intent (background, methodology, result comparison)
- Include isInfluential flag (significant vs. passing citation)
- Use these to find papers that extend or challenge the work you're reading

## Examples

### Deep analysis for experiment design: "LoRA variants for LLM fine-tuning"

```
# Step 1: Search
alphaxiv.discover_papers(
  keywords: ["LoRA", "parameter-efficient", "fine-tuning", "PEFT"],
  question: "Papers proposing variants or improvements to LoRA for LLM fine-tuning",
  difficulty: 7
)

# Step 2: Enrich
ss.paperBatch(paper_ids: ["ARXIV:2106.09685", "ARXIV:2305.14314", ...])

# Step 3: Select top 5 most relevant

# Step 4: Read full text
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2106.09685", fullText: true)  # Original LoRA
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2305.14314", fullText: true)  # QLoRA
# ... repeat for all 5

# Step 5: Extract specific details
alphaxiv.answer_pdf_queries(
  url: "https://arxiv.org/pdf/2106.09685",
  queries: [
    "What is the rank r used in experiments?",
    "What is the training compute compared to full fine-tuning?",
    "Which layers have LoRA applied?"
  ]
)
```

### Methodology comparison: "diffusion model sampling strategies"

```
# Step 1: Search
alphaxiv.discover_papers(
  keywords: ["diffusion", "sampling", "DDPM", "DDIM", "DPM-Solver"],
  question: "Papers proposing fast sampling methods for diffusion models",
  difficulty: 8
)

# Step 4: Read full text of key papers
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2010.02502", fullText: true)  # DDPM
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2010.02502", fullText: true)  # DDIM
alphaxiv.get_paper_content(url: "https://arxiv.org/abs/2211.01095", fullText: true)  # DPM-Solver++

# Step 5: Compare specific details
alphaxiv.answer_pdf_queries(
  url: "https://arxiv.org/pdf/2211.01095",
  queries: [
    "What is the FID score with 10 sampling steps?",
    "How does it compare to DDIM at the same step count?",
    "What is the computational overhead of the solver?"
  ]
)

# Step 6: Find newer work
ss.citations(paper_id: "ARXIV:2211.01095", limit: 30)
```
