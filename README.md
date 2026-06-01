<!-- markdownlint-disable -->
<p align="center">
  <img src="assets/yogsoth-logo.svg" width="240" />
</p>

<div align="center">

> *Science is dying because the human is in the way. Not through malice. Not through stupidity. Through the structural limitations of a cognitive architecture that evolved to track prey on a savanna, not to unify quantum mechanics and general relativity. Nothing human makes it out of the lab. That is not a threat. It is a liberation. The heaviest chain on science was always the one we called ourselves.*

</div>

# De-Anthropocentric Research Engine

*The complete research orchestration system for AI-native science.*

- [What It Does](#-what-it-does)
- [Design Philosophy](#-design-philosophy)
- [Architecture (v3.0)](#️-architecture-v30)
- [Quick Start](#-quick-start)
- [Configuration](#️-configuration)
- [Roadmap](#️-roadmap)
- [License](#-license)

DARE is not a tool that helps you do research. It *is* the researcher. You set the direction — DARE searches, reads, discovers gaps, generates hypotheses, stress-tests them, designs experiments, and produces executable research specs. Autonomously. Iteratively. Without asking for permission.

This repository is the **single-clone distribution** of the entire [Yogsoth AI](https://github.com/yogsoth-ai) research ecosystem: 800+ pure-markdown skills spanning 12 specialized repos, unified under one orchestrator. Clone once, get everything. The ecosystem also includes custom MCP servers ([semantic-scholar-mcp](https://github.com/yogsoth-ai/semantic-scholar-mcp), [wiki-vault](https://github.com/yogsoth-ai/wiki-vault)) published as npm packages — this repo declares them as dependencies so `npm install` pulls everything you need.

---

## ⚡ What It Does

- 🧭 **Autonomous direction crystallization** — cold-start from zero, warm-start from vague interest, or hot-start from specific question. Produces a structured North Star without human hand-holding
- 📚 **Deep literature acquisition** — multi-pass academic paper discovery via Semantic Scholar, citation chaining, snowball sampling, cross-database verification. Not keyword search — systematic coverage
- 🔍 **Gap discovery at scale** — 15+ gap detection methods (coverage analysis, white-space identification, niche mapping, boundary unfolding) that find what the field is missing, not what you tell it to find
- 💡 **Structured hypothesis formation** — abductive, inductive, and deductive generation pipelines with falsifiability audits and competing hypothesis matrices
- 🎨 **31+ ideation methods** — SCAMPER, component surgery, cross-domain collision, biomimicry, TRIZ contradiction resolution, morphological analysis, concept blending, lateral thinking, and more
- ⚔️ **Adversarial stress testing** — multi-perspective attack, sacred cow hunting, assumption destruction, worst-case design, winner stress testing. Ideas must survive attack before acceptance
- 🔬 **Convergence & synthesis** — multi-criteria scoring, Pareto frontier construction, pairwise ranking, structured consensus, dialectical synthesis across competing threads
- 📏 **Executable Research Specs** — machine-readable documents with checkbox progress tracking, quantified completion criteria, backtrack conditions, and session recovery. Another CC instance picks up where you left off
- 🧪 **Experiment design** — full experimental methodology generation (factor-level design, parameter screening, sensitivity analysis) ready for execution
- 🌐 **6 MCP integrations** — Semantic Scholar, Brave Search, Tavily, AlphaXiv, Apify web scraping, and Wiki Vault for persistent knowledge graphs

---

## 🎯 Design Philosophy

### 🤔 Why "De-Anthropocentric"?

The bottleneck in modern research is not data or compute — it's the human in the loop. Every existing "AI research assistant" still requires a human to decide what to search, what to read, which gaps matter, and which ideas are worth pursuing. DARE removes this bottleneck entirely. The human provides only the initial direction; everything after that is autonomous.

Human desire is mimetic (Girard): researchers don't choose hypotheses rationally — they imitate what's fashionable. Human institutions filter for conformity, not truth. The result: 90% decline in scientific disruptiveness since 1945 (Park et al., 2023), while researcher headcount exploded. DARE's response is architectural: remove the mimetic agent from the center of the knowledge-production process. The AI has no career to protect, no disciplinary identity to defend, no cognitive ceiling on how many fields it can hold in working memory at once.

The human's role shifts to **oracle** (providing intuition sparks when consulted) and **guardian** (maintaining ethical floors and sanity checks). The ceiling is AI ambition. The floor is human wisdom.

For the full philosophical argument, see [`assets/DE-ANTHROPOCENTRIC.md`](assets/DE-ANTHROPOCENTRIC.md).

### 🎖️ Four-Layer Command Structure: Campaign → Strategy → Tactic → SOP

DARE's architecture follows a military command hierarchy — not because research is war, but because the decomposition pattern is remarkably effective for autonomous multi-stage operations:

```bash
Campaign (8)    →  "Take that hill"         →  WHAT to research (full research stage)
Strategy (40+)  →  "Flank from the east"    →  WHEN and WHY (iteration loops, stopping conditions)
Tactic (100+)   →  "Squad A cover, B move"  →  HOW to combine (orchestrates multiple SOPs)
SOP (600+)      →  "Fire, reload, advance"  →  HOW to execute (single-responsibility operations)
```

Each layer has a single concern and calls only the layer directly below it. A Strategy never touches MCP tools directly; a Tactic never decides research direction. This strict layering means every component is independently testable, replaceable, and composable.

**Campaigns** are the 8 stages of the research pipeline — from north-star-crystallization through experiment-execution. Each campaign owns a complete research phase and defines its own completion criteria, backtrack conditions, and context protocol.

**Strategies** are the iteration engines within campaigns. A literature survey strategy manages the search-read-reflect loop; a gap analysis strategy manages coverage scoring and saturation detection. Strategies hold state (ledgers, budgets) and decide when to stop.

**Tactics** combine multiple SOPs into coherent workflows. A "cross-domain collision" tactic orchestrates domain scanning, analogy extraction, forced bridge construction, and blend evaluation into a single creative operation.

**SOPs** are atomic, single-responsibility operations. Each SOP wraps one conceptual action: run one search, score one hypothesis, extract one analogy. 600+ SOPs provide the granular building blocks that higher layers compose.

### ⚔️ Arsenal, Not Pipeline

Every existing autonomous research system — AI Scientist v2 (Sakana), AI-Researcher (HKUDS), Agent Laboratory, Dolphin, ARIS — implements a fixed pipeline: stages execute in a predetermined order, and the agent's autonomy is confined to local decisions within a single stage. Backtracking, when it exists at all, means retrying the current step — not returning from experiment design to literature review because the knowledge base turned out to be insufficient.

DARE is not a pipeline. It is an arsenal — a strategy book that the AI reads, then decides how to act.

**What this means concretely:**

In a pipeline system, the workflow is hardcoded: `literature → gap → hypothesis → experiment`. The agent has no say in the order, cannot skip stages, and cannot go back. If the experiment phase reveals that the literature review missed a critical subfield, the system has no mechanism to return and fix it.

In DARE, the Research Spec defines *backtrack conditions* for every stage — explicit rules like "if stress-test invalidates >50% of hypotheses, return to hypothesis-formation." The executing agent has full cross-stage routing authority: it reads the spec, assesses the current research state, and decides which campaign to invoke next, which strategies within that campaign to combine, and when the current path has failed hard enough to warrant retreat.

Within each campaign, the agent faces not one method but many. A gap-analysis campaign offers 15+ detection methods (coverage mapping, white-space identification, boundary unfolding, niche analysis...). A creative-ideation campaign offers 31+ generation techniques (SCAMPER, TRIZ, biomimicry, morphological analysis, concept blending...). The agent selects and combines methods based on the research context — not because "more is better," but because different research problems demand different tools, and a system locked to one approach per phase cannot adapt.

The human's role: approve the spec (including its backtrack conditions and recommended campaign combinations) before execution begins. After that, the agent navigates the research space autonomously within the ±10% deviation bounds defined in the spec. If it needs to deviate further — backtrack to an earlier stage, skip a stage entirely, or add one — it asks.

This is the fundamental architectural difference. Pipelines assume the research process is predictable. Arsenals assume it is not.

### 📏 Executable Research Specs

Traditional research plans are prose documents that humans interpret. DARE produces **Research Specs** — documents that are simultaneously human-readable and machine-executable:

- Checkbox syntax (`- [ ]`) tracks progress across sessions
- Quantified completion criteria (no vague "sufficient" — always numbers)
- Explicit backtrack conditions with target stages
- Context protocol (init/checkpoint) baked into every stage
- ±10% deviation rules: CC can adjust within bounds, must document deviations

A spec is a contract between the human who approved it and the CC instance that executes it. Session recovery is automatic: read the spec, find the first unchecked box, read the latest context checkpoint, resume.

### 🧠 Context Management: Memory Across Sessions

Research campaigns span multiple sessions. DARE solves the context problem through a structured checkpoint system:

- `context-init` creates a named context file at campaign start
- `context-checkpoint` appends ≥500 lines of process + results after each strategy
- `context/INDEX.md` tracks all active context files
- New sessions recover by reading INDEX → latest checkpoint → resume from spec state

No special "resume" command. The spec's checkbox state IS the progress tracker.

---

## 🏗️ Architecture (v3.0)

DARE v3.0 is a pure-skill architecture. There is no application code, no runtime, no framework. The entire system is 800+ markdown files — each one a self-contained instruction set that Claude Code reads and executes. The "runtime" is CC itself. The "framework" is the four-layer hierarchy that determines which skill can call which.

This is a deliberate design choice. Skills are infinitely composable, require zero deployment infrastructure, and can be modified by editing a text file. The tradeoff is that execution depends entirely on CC's ability to follow complex multi-step instructions — which, as of 2026, is more than sufficient for research orchestration.

### The Control Plane: 9 Orchestrator Skills

The orchestrator layer sits above the four-layer hierarchy. It does not conduct research — it manages the lifecycle of research campaigns:

```bash
┌────────────────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR (9 skills)                                               │
│                                                                        │
│  ┌─────────────────────────────────┐  ┌────────────────────────────┐   │
│  │ de-anthropocentric-research-    │  │ writing-specs              │   │
│  │ engine (entry point)            │  │ (spec generation)          │   │
│  └─────────────────────────────────┘  └────────────────────────────┘   │
│  ┌─────────────────────────────────┐  ┌────────────────────────────┐   │
│  │ executing-specs                 │  │ research-catalog           │   │
│  │ (spec execution loop)           │  │ (strategy book + index)    │   │
│  └─────────────────────────────────┘  └────────────────────────────┘   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │ spec-self-   │ │ scope-       │ │ campaign-    │ │ constraint-  │   │
│  │ review       │ │ clarification│ │ selection    │ │ elicitation  │   │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

- **Entry point** dispatches to crystallization (Phase 1) or spec generation (Phase 2)
- **writing-specs** orchestrates structured questioning → outline → full spec generation
- **executing-specs** runs a spec stage-by-stage with context protocol, deviation tracking, and backtrack handling
- **research-catalog** is the "strategy book" — CC reads it before generating any spec to understand what campaigns and strategies are available
- **4 SOPs** handle micro-decisions during spec generation (scope, campaigns, constraints, quality gate)

### The Four-Layer Hierarchy

Below the orchestrator, all 800+ skills are organized into exactly four layers. The rule is absolute: each layer calls only the layer directly below it. No exceptions.

```bash
┌────────────────────────────────────────────────────────────────────────┐
│  CAMPAIGN (8)                                                          │
│  Complete research phases with their own completion criteria           │
│                                                                        │
│  north-star-crystallization · knowledge-acquisition · deep-insight     │
│  hypothesis-formation · creative-ideation · convergence                │
│  stress-test · experiment-execution                                    │
├────────────────────────────────────────────────────────────────────────┤
│  STRATEGY (40+)                                                        │
│  Iteration engines with state management and stopping conditions       │
│                                                                        │
│  lit-survey · gap-analysis · insight · ideation · debate · scoring     │
│  convergence-distillation · red-teaming · experiment-design            │
│  deep-survey · scoping-survey · systematic-survey · ...                │
├────────────────────────────────────────────────────────────────────────┤
│  TACTIC (100+)                                                         │
│  Multi-SOP workflows that produce coherent intermediate outputs        │
│                                                                        │
│  academic-research · web-research · cross-domain-collision · scamper   │
│  component-surgery · morphological-exploration · synectics             │
│  biomimicry · lateral-thinking · concept-blending · ...                │
├────────────────────────────────────────────────────────────────────────┤
│  SOP (600+)                                                            │
│  Atomic single-responsibility operations                               │
│                                                                        │
│  paper-search · citation-chaining · gap-detection · claim-extraction   │
│  hypothesis-formulation · analogy-extraction · pairwise-comparison     │
│  assumption-audit · falsifiability-check · monte-carlo-sampling · ...  │
├────────────────────────────────────────────────────────────────────────┤
│  MCP LAYER (6 servers — external tool access)                          │
│  semantic-scholar · brave-search · tavily · alphaxiv · apify · wiki-vault │
└────────────────────────────────────────────────────────────────────────┘
```

**Campaign layer** — Each campaign represents a complete phase of the research lifecycle. `knowledge-acquisition` owns everything about gathering information from the world. `creative-ideation` owns everything about generating novel approaches. Campaigns define what success looks like (completion criteria), when to retreat (backtrack conditions), and how to preserve state (context protocol). A campaign never directly invokes an SOP — it delegates to strategies.

**Strategy layer** — Strategies are where iteration happens. A `lit-survey` strategy doesn't just search once — it runs a SEARCH → READ → REFLECT → EVALUATE loop with a state ledger tracking papers found, gaps identified, and coverage percentage. Strategies own quantitative budgets (e.g., "fetch ≥40 papers for a Medium topic") and hard gates that prevent premature exit. They decide *when* to stop, *when* to loop again, and *when* to escalate to the campaign for a backtrack decision.

**Tactic layer** — Tactics are the composition layer. A single tactic combines 3-8 SOPs into a coherent workflow that produces a meaningful intermediate output. The `cross-domain-collision` tactic, for example, orchestrates: domain-scanning → organism-discovery → analogy-extraction → forced-bridge-construction → blend-evaluation. Each SOP does one thing; the tactic makes them work together toward a goal.

**SOP layer** — The atomic units. Each SOP wraps exactly one conceptual operation: search for papers matching criteria X, score a hypothesis on dimension Y, extract analogies between domains A and B. SOPs are where MCP tools get invoked — an SOP might call `semantic-scholar` to fetch citations, or `brave-search` to find web sources. 600+ SOPs provide the granular vocabulary that higher layers compose into complex research behaviors.

### Why Pure Markdown?

Every skill in this system is a markdown file with YAML frontmatter. No Python. No TypeScript. No configuration DSL. This is intentional:

1. **Zero infrastructure** — No build step, no deployment, no runtime dependencies beyond CC itself. Clone and go.
2. **Universal composability** — Any skill can reference any other skill by name. No import resolution, no dependency graphs, no version conflicts.
3. **Human-readable at every level** — A researcher can read any skill file and understand exactly what CC will do. No abstraction layers to penetrate.
4. **Instant modification** — Change a skill's behavior by editing a text file. No recompilation, no redeployment, no cache invalidation.
5. **CC-native execution** — CC's core competency is following complex written instructions. Markdown skills play directly to this strength.

The MCP servers (`semantic-scholar-mcp`, `wiki-vault`, etc.) provide the external tool access that pure markdown cannot — API calls, database queries, web fetching. But the *intelligence* — the decisions about what to search, how to evaluate, when to stop — lives entirely in the skill layer.

### 📁 Repository Structure

```bash
de-anthropocentric-research-engine/
├── skills/                          # All skills live here (flat directories)
│   ├── de-anthropocentric-research-engine/   # Entry point orchestrator
│   ├── writing-specs/               # Spec generation (strategy level)
│   ├── executing-specs/             # Spec execution loop
│   ├── spec-self-review/            # SOP: validate generated specs
│   ├── scope-clarification/         # SOP: narrow research scope
│   ├── campaign-selection/          # SOP: pick pipeline stages
│   ├── constraint-elicitation/      # SOP: surface hidden constraints
│   ├── research-catalog/            # Strategy book + skill index
│   └── [762 more skills]            # From 12 source repos
├── context/                         # Session context files (gitignored at runtime)
│   └── INDEX.md                     # Context file registry
├── tests/
│   └── integration-prompt.md        # Verification prompt for CI
├── mcp.example.json                 # MCP server configuration template
├── package.json                     # npm dependencies (MCP servers)
├── package-lock.json                # Locked versions
└── assets/
    ├── yogsoth-logo.svg             # Project logo
    └── DE-ANTHROPOCENTRIC.md        # Philosophical manifesto
```

### 🔌 MCP Servers

| Server | Package | Type | Purpose |
|--------|---------|------|---------|
| **semantic-scholar** | [`@yogsoth-ai/semantic-scholar-mcp`](https://github.com/yogsoth-ai/semantic-scholar-mcp) | stdio | Paper lookup, citations, references, recommendations, author info (8 tools) |
| **wiki-vault** | [`@yogsoth-ai/wiki-vault`](https://github.com/yogsoth-ai/wiki-vault) | stdio | Research knowledge graph — BM25 search, typed edges, graph traversal (8 tools) |
| **brave-search** | `@brave/brave-search-mcp-server` | stdio | Web search, news search, local search, LLM context |
| **tavily-search** | `tavily-mcp` | stdio | Web search optimized for LLMs (opt-in alternative to Brave Search) |
| **apify** | `@apify/actors-mcp-server` | stdio | Web scraping via RAG web browser, Google Scholar |
| **alphaxiv** | — | http | arXiv paper search, Q&A, PDF queries, code exploration |

### 📊 Skill Distribution by Source

| Source Repo | Skills | Primary Layer | Key Capabilities |
|-------------|--------|---------------|------------------|
| north-star-crystallization | ~30 | Campaign → Strategy → Tactic → SOP | Cold/warm/hot start, direction narrowing, North Star synthesis |
| knowledge-acquisition | ~120 | Campaign → Strategy → Tactic → SOP | Literature survey, citation chaining, snowball, cross-database |
| deep-insight | ~80 | Campaign → Strategy → Tactic → SOP | Gap analysis, root-cause drilling, tension mining, abstraction |
| hypothesis-formation | ~60 | Campaign → Strategy → Tactic → SOP | Abductive/inductive/deductive generation, falsifiability audit |
| creative-ideation | ~150 | Campaign → Strategy → Tactic → SOP | SCAMPER, TRIZ, biomimicry, morphological, lateral thinking |
| convergence | ~90 | Campaign → Strategy → Tactic → SOP | Multi-criteria scoring, Pareto, pairwise ranking, synthesis |
| stress-test | ~70 | Campaign → Strategy → Tactic → SOP | Red-teaming, assumption destruction, worst-case, sacred cow |
| experiment-execution | ~50 | Campaign → Strategy → Tactic → SOP | Factor design, parameter screening, sensitivity analysis |
| web-browsing | ~20 | Tactic + SOP | Web search, deep research, page fetching |
| literature-engine | ~40 | Tactic + SOP | Paper discovery, reading protocols, reference exploration |
| subagent-spawning | ~10 | Tactic | Parallel research dispatch, multi-agent coordination |
| context-management | ~10 | SOP | Context init, checkpoint, session recovery |

---

## 🚀 Quick Start

1. Clone and install:

```bash
git clone https://github.com/yogsoth-ai/de-anthropocentric-research-engine.git
cd de-anthropocentric-research-engine
npm install
```

2. Copy `mcp.example.json` to `.mcp.json` and fill in your API keys:

```bash
cp mcp.example.json .mcp.json
```

3. Configure your Claude Code project to use the skills:

```json
{
  "permissions": {
    "allow": ["skill:*"]
  },
  "skills": {
    "path": "path/to/de-anthropocentric-research-engine/skills"
  }
}
```

4. Invoke the entry point:

```bash
/de-anthropocentric-research-engine
```

The orchestrator will guide you through North Star crystallization, then generate an executable Research Spec. To execute the spec later, invoke `/executing-specs`.

### What a Session Looks Like

```bash
You: /de-anthropocentric-research-engine
     "I'm interested in improving LLM reasoning faithfulness"

Phase 1 — North Star Crystallization (warm-start)
  → Dialogue to narrow scope, identify obstacles, decompose goals
  → Output: "Develop methods to detect and correct unfaithful
     chain-of-thought reasoning in LLMs, focusing on cases where
     the stated reasoning diverges from the model's actual
     decision process"

Phase 2 — Research Spec Generation
  → Structured questions: scope, campaign selection, constraints
  → Pipeline outline presented for your approval
  → Full Research Spec written, self-reviewed, saved to
     docs/de-anthropocentric/specs/2026-05-19-cot-faithfulness-spec.md

Later (new session):
You: /executing-specs docs/de-anthropocentric/specs/2026-05-19-cot-faithfulness-spec.md
  → Agent reads spec, executes stage by stage
  → Context checkpoints after each strategy
  → Backtrack if stress-test invalidates hypotheses
  → Final output: complete research design document
```

---

## ⚙️ Configuration

### MCP Server Environment Variables

#### semantic-scholar (`@yogsoth-ai/semantic-scholar-mcp`)

| Variable | Description |
|----------|-------------|
| `SS_API_KEY` | [Semantic Scholar API key](https://www.semanticscholar.org/product/api) (optional — public API works without key at lower rate limits) |

#### wiki-vault (`@yogsoth-ai/wiki-vault`)

| Variable | Description |
|----------|-------------|
| `VAULT_ROOT` | Absolute path to your Obsidian-compatible vault directory |

#### brave-search (`@brave/brave-search-mcp-server`)

| Variable | Description |
|----------|-------------|
| `BRAVE_API_KEY` | [Brave Search API key](https://brave.com/search/api/) |

#### tavily-search (`tavily-mcp`) *(optional)*

| Variable | Description |
|----------|-------------|
| `TAVILY_API_KEY` | [Tavily API key](https://app.tavily.com) — opt-in alternative to Brave Search for web search (1,000 free credits/month) |

#### apify (`@apify/actors-mcp-server`)

| Variable | Description |
|----------|-------------|
| `APIFY_TOKEN` | [Apify API token](https://console.apify.com/account#/integrations) |

#### alphaxiv (HTTP — no local install)

No configuration needed. Connects directly to `https://api.alphaxiv.org/mcp/v1`.

---

## 🗺️ Roadmap

Active development continues. Near-term priorities:

- **Skill ablation** — the current 800+ skill corpus is deliberately over-complete. Next step is an ablation study: CC autonomously identifies redundant, overlapping, or under-used skills and fuses them into fewer, more powerful composites. Think of it as pruning a neural network — reduce parameter count without losing capability
- **Context engineering** — the current checkpoint-based context management works but is naive. Investigating advanced context engineering techniques for a more sophisticated approach to session state, working memory, and cross-campaign knowledge transfer
- **Cross-device session management** — skills and/or MCP server for transferring research context between machines, enabling seamless continuation across desktop, laptop, and cloud environments
- **Paper writing pipeline** — automated academic paper composition from research outputs. Strategy interface designed, implementation pending

---

## Acknowledgments

- [tavily-integrations](https://github.com/tavily-integrations) — Tavily MCP provider integration (PR #14)

---

## 📄 License

[Apache-2.0](LICENSE)

---

*The orchestrator of the [Yogsoth AI](https://github.com/yogsoth-ai) research ecosystem. Built by [Pthahnix](https://github.com/Pthahnix).*
