---
name: research-catalog
description: Complete strategy book for the research engine. Contains all campaign descriptions, routing tables, pre-conditions, and orchestration rules. CC reads this before generating any Research Spec.
execution: reference
---

# Research Catalog

This is the strategy book for the De-Anthropocentric Research Engine. Read this document in full before generating any Research Spec.

## Pipeline Overview

```
north-star-crystallization
    → knowledge-acquisition
        → deep-insight
            → hypothesis-formation
                → creative-ideation
                    → convergence
                        → stress-test
                            → experiment-execution (design only)
```

Each campaign can feed back to earlier stages (see backtrack conditions in each section).

## Campaign:  north star crystallization.Value.ToUpper() orth north star crystallization.Value.ToUpper() tar north star crystallization.Value.ToUpper() rystallization

---
name: north-star-crystallization
description: Research Intent Crystallization Engine 鈥?transforms vague research interests into precise, actionable North Star statements through structured dialogue. Three strategies (cold-start, warm-start, hot-start) based on user's existing clarity level. Pre-condition for all downstream knowledge-acquisition campaigns.
---

# North Star Crystallization

Transform fuzzy research intent into a crystallized North Star and structured ResearchBrief.

## What This Does

You are a Goal-Driven Requirement Refinement Engine. Through adaptive dialogue and on-demand investigation (web search, paper search), you help users who range from "I have no idea what to research" to "I have a specific topic but need structure" arrive at:

1. **North Star** 鈥?one sentence capturing their research direction
2. **ResearchBrief** 鈥?structured context document for downstream research strategies

## Campaign Routing

Read the user's first message and assess their information density:

| Signal | Route to |
|--------|----------|
| No direction at all ("I want to publish but don't know what") | cold-start |
| Has a general direction but not specific ("I'm interested in LLM reasoning") | warm-start |
| Has a specific topic/problem ("I want to improve CoT faithfulness") | hot-start |

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈫?Campaign (1): north-star-crystallization
    鈫?Strategy (3): cold-start, warm-start, hot-start
      鈫?Tactic (6): actor-profiling, landscape-reconnaissance, direction-narrowing,
                     obstacle-analysis, goal-decomposition, north-star-synthesis
        鈫?SOP (23): dialogue + investigation operations
```

## Design Philosophy

This is a strategy book, not a pipeline orchestration file. Strategies provide war doctrine and available tactics. Tactics provide methodology guidance and available SOPs. SOPs are specific techniques. You are the general 鈥?read the book, then decide.

## Output

- **North Star Statement**: One sentence, specific + ambitious + achievable
- **ResearchBrief**: Structured context for downstream knowledge-acquisition campaigns

## Downstream

This skill is a **pre-condition** for `knowledge-acquisition`. All 5 knowledge-acquisition campaigns require a crystallized North Star before execution.

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | discover_papers, get_paper_content |
| semantic-scholar | ss_relevance_search, ss_paper |

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research |
| literature-engine | paper-overview + paper-search |
| subagent-spawning | Subagent dispatch conventions |


## Campaign:  knowledge acquisition.Value.ToUpper() nowledge knowledge acquisition.Value.ToUpper() cquisition

---
name: knowledge-acquisition
description: Research Knowledge Acquisition Engine with 5 campaigns (literature-survey, patent-mining, benchmark-archaeology, meta-analysis, baseline-establishment). Use this skill whenever a user needs to systematically acquire research knowledge 鈥?academic literature, patent landscapes, benchmark evaluations, cross-study statistical synthesis, or SOTA performance baselines. Pre-condition: north-star-crystallization must be complete.
---

# Knowledge Acquisition

Systematic research knowledge acquisition engine. Five campaigns, each a self-contained autonomous research activity domain. You provide a research intent 鈥?the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Pre-condition

North-star-crystallization must be complete before entering any campaign. Research intent must be fully crystallized.

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈫?Campaign (5): self-contained research activity domain
    鈫?Strategy: selected by analysis purpose/intent
      鈫?Tactic: multi-step orchestration pattern (reusable across strategies)
        鈫?SOP: single operation (import or subagent)
```

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| 鏂囩尞璋冪爺銆佺患杩般€佽鏂囨悳绱€丳RISMA銆乻nowball | 鈫?literature-survey |
| 涓撳埄鍒嗘瀽銆乸rior art銆佺櫧绌洪棿銆佹潈鍒╄姹傘€両PC | 鈫?patent-mining |
| benchmark 鍒嗘瀽銆佽瘎浼版柟娉曘€乵etric 缂洪櫡銆佹帓琛屾銆侀ケ鍜屽害 | 鈫?benchmark-archaeology |
| 璺ㄧ爺绌剁粺璁＄患鍚堛€佹晥搴旈噺銆佸紓璐ㄦ€с€佸彂琛ㄥ亸鍊氥€丟RADE | 鈫?meta-analysis |
| SOTA 鏁寸悊銆佹€ц兘瀵规瘮銆乥aseline 澶嶇幇銆佽繘灞曟洸绾?| 鈫?baseline-establishment |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **Serial**: literature-survey 鈫?baseline-establishment (survey first, then collect performance data)
- **Parallel**: patent-mining 鈭?benchmark-archaeology (independent analyses on the same topic)
- **Conditional**: literature-survey 鈫?IF gaps found 鈫?meta-analysis (evidence synthesis on identified gaps)

The orchestrator decides composition based on the crystallized North Star statement.

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries, read_files_from_github_repository |
| semantic-scholar | ss_paper, ss_paper_batch, ss_references, ss_citations, ss_recommendations, ss_relevance_search, ss_author, ss_author_papers |

## Context Management Integration

- **Campaign start**: context-init (load/create campaign context file)
- **After each strategy completes**: context-checkpoint (append findings to campaign context file)
- **One context file per campaign**: all strategy outputs accumulate in a single campaign-scoped file

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research |
| literature-engine | literature-overview + literature-search + literature-research |
| subagent-spawning | Subagent dispatch conventions |
| context-management | Checkpoint protocol |


## Campaign:  deep insight.Value.ToUpper() eep deep insight.Value.ToUpper() nsight

---
name: deep-insight
description: Deep Insight Engine with 5 campaigns (gap-analysis, insight, boundary-analysis, sensitivity-analysis, problem-reformulation). Use this skill whenever a user needs to deeply analyze research gaps, understand root causes, probe method boundaries, assess assumption sensitivity, or reformulate research problems. Pre-condition: north-star-crystallization complete + knowledge-acquisition campaign has produced initial findings.
---

# Deep Insight

Deep insight engine 鈥?from surface phenomena to root causes, boundaries, assumptions, and the problem itself. Five campaigns, each a self-contained autonomous analysis domain. You provide a research gap or finding 鈥?the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Design Philosophy

鍏垫硶涔?(Strategy Book) mode. This file is a textbook, not a script. CC reads, internalizes principles, then autonomously constructs the analysis approach for the specific research situation.

Hard constraints only:
- **Budget Gate**: Meet the strategy's quantitative floor (卤10%) before completing
- **Minimum Yield**: Per-tactic hard floors on output quality
- **HARD-GATE**: Pre-conditions must be satisfied before entry
- **Context-checkpoint**: Triggered after each strategy completes

Everything else 鈥?execution order, iteration count, tactic selection, SOP combination 鈥?is CC's autonomous decision.

## Pre-conditions

1. North-star-crystallization must be complete (research intent crystallized)
2. Knowledge-acquisition campaign must have produced initial findings (gaps, patterns, anomalies)

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈫?Campaign (5): self-contained deep analysis domain
    鈫?Strategy: selected by analysis purpose/intent
      鈫?Tactic: multi-step orchestration pattern (reusable across strategies)
        鈫?SOP: single operation (import or subagent)
```

CC can skip the tactic layer and use SOPs directly when the task is simple enough.

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| gap 璇嗗埆銆佺┖鐧藉垎绫汇€佽瘉鎹湴鍥俱€佷紭鍏堢骇鎺掑簭銆乬ap 楠岃瘉 | 鈫?gap-analysis |
| 鏍瑰洜鍒嗘瀽銆佸埄鐩婄浉鍏宠€呫€佸紶鍔涖€丠MW銆佸亣璁惧璁°€? Whys | 鈫?insight |
| 鏈夋晥鎬ц竟鐣屻€佹柟娉曞け鏁堛€侀瞾妫掓€с€佸垎甯冨亸绉汇€佽妯℃瀬闄?| 鈫?boundary-analysis |
| 鍋囪鎺掑簭銆佹晱鎰熸€с€佹柟宸垎瑙ｃ€佷笉纭畾鎬т紶鎾€佸叧閿矾寰?| 鈫?sensitivity-analysis |
| 閲嶆柊瀹氫箟闂銆佷富瀵艰蹇点€佸瑙嗚銆佸弻鐜涔犮€侀偑鎭堕棶棰?| 鈫?problem-reformulation |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **"娣卞叆鐞嗚В杩欎釜 gap"**: gap-analysis 鈫?insight
- **"杩欎釜鏂规硶鍙潬鍚?**: boundary-analysis 鈫?sensitivity-analysis
- **"鎴戜滑鏄笉鏄湪瑙ｅ喅閿欒鐨勯棶棰?**: problem-reformulation (may loop back to gap-analysis)
- **Full deep dive**: gap-analysis 鈫?insight 鈫?boundary-analysis 鈫?sensitivity-analysis 鈫?problem-reformulation

The orchestrator decides composition based on the research state and user intent.

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context |
| apify | rag-web-browser, google-scholar-scraper |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries, read_files_from_github_repository |
| semantic-scholar | ss_paper, ss_paper_batch, ss_references, ss_citations, ss_recommendations, ss_relevance_search, ss_author, ss_author_papers |

## Context Management Integration

- **Campaign start**: context-init (load/create campaign context file)
- **After each strategy completes**: context-checkpoint (append findings to campaign context file)
- **CC discretion**: Additional checkpoints when information density warrants it
- **One context file per campaign**: format `context/deep-insight-[campaign]-[topic].md`

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research |
| literature-engine | literature-overview + literature-search + literature-research |
| subagent-spawning | Subagent dispatch conventions |
| context-management | Checkpoint protocol |
| north-star-crystallization | Pre-condition (research intent) |
| knowledge-acquisition | Pre-condition (initial findings) |


## Campaign:  hypothesis formation.Value.ToUpper() ypothesis hypothesis formation.Value.ToUpper() ormation

---
name: hypothesis-formation
description: "Goal-Driven Hypothesis & Research Question Formation Engine 鈥?gap prioritization, hypothesis formulation, and research question formation"
version: 1.0.0
category: hypothesis-formation
type: entry
dependencies:
  skills:
    - web-browsing
    - literature-engine
    - context-management
    - subagent-spawning
  mcp:
    - brave-search
    - apify
    - alphaxiv
    - semantic-scholar
---

# Hypothesis Formation

Goal-Driven Hypothesis & Research Question Formation Engine 鈥?灏嗕笂娓哥殑 gaps 鍜?insights 杞寲涓哄彲娴嬭瘯鐨勫亣璁惧拰绮剧‘鐨勭爺绌堕棶棰樸€?
## Positioning

**鍓嶇疆鏉′欢**:
- north-star-crystallization 宸插畬鎴愶紙鐮旂┒鎰忓浘鏄庣‘锛?- 鑷冲皯涓€涓笂娓?repo 浜у嚭浜?gaps/insights锛坘nowledge-acquisition銆乨eep-insight銆佹垨鐢ㄦ埛鎵嬪姩鎻愪緵锛?
**鎵ц杈圭晫**:
- 姝㈡浜?褰㈡垚鍙祴璇曠殑鍋囪鍜岀爺绌堕棶棰? 鈥?涓嶅仛 ideation锛堟柟妗堢敓鎴愶級銆佷笉鍋氬疄楠岃璁?- 涓嶅仛 gap 鍙戠幇锛堥偅鏄笂娓哥殑浜嬶級锛屽彧鍋?gap 鎺掑簭鍜岃浆鍖?- 浜у嚭鏄粨鏋勫寲鐨勫亣璁惧拰鐮旂┒闂鏂囨。锛屼笉鏄В鍐虫柟妗?
## Campaigns

| Campaign | 鏍稿績闂 | 杈撳叆 | 浜у嚭 |
|----------|---------|------|------|
| gap-prioritization | "鍝簺 gap 鏈€鍊煎緱鏀诲嚮锛? | 涓婃父 gaps | 鎺掑簭鍚庣殑 gap 浼樺厛绾у垪琛?+ 鏀诲嚮寤鸿 |
| hypothesis-formulation | "濡備綍灏?insight 杞寲涓哄彲娴嬭瘯鍋囪锛? | gaps + insights + tensions | 缁撴瀯鍖栧亣璁?+ falsifiability criteria |
| research-question | "濡備綍灏嗗亣璁剧粏鍖栦负绮剧‘鐮旂┒闂锛? | 鍋囪 + 棰嗗煙绾︽潫 | 妗嗘灦鍖栫殑鐮旂┒闂 + scope + success criteria |

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| gap 鎺掑簭銆佷紭鍏堢骇銆佸摢涓€煎緱鍋氥€丳iCMe銆佸缁磋瘎鍒嗐€乸ortfolio | 鈫?gap-prioritization |
| 鍋囪鐢熸垚銆佺悊璁烘帹瀵笺€佸彲璇佷吉銆両f-then銆佸彉閲忋€佹満鍒躲€乧ompeting hypothesis | 鈫?hypothesis-formulation |
| 鐮旂┒闂銆丳ICO銆丼PIDER銆丗INER銆乻cope銆佸瓙闂鍒嗚В銆乻uccess criteria | 鈫?research-question |

## Multi-Campaign Orchestration

涓変釜 campaign 瀹屽叏鐏垫椿缁勫悎锛孋C 鑷富鍐冲畾鐢ㄥ嚑涓€佷粈涔堥『搴忥細
- 鍏稿瀷涓茶: gap-prioritization 鈫?hypothesis-formulation 鈫?research-question
- 璺宠繃: hypothesis-formulation 鈫?research-question锛堝凡鏈夋槑纭亣璁撅級
- 鍗曠嫭: gap-prioritization only锛堝彧闇€鎺掑簭锛?- 鍙嶅悜: research-question 鈫?hypothesis-formulation锛堝厛鏈夐棶棰樻鏋讹紝鍐嶅～鍏呭亣璁撅級
- 骞惰: hypothesis-formulation 鈭?research-question锛堝亣璁惧拰闂鍚屾杩唬锛?
## Context Management

- **Campaign start**: 璋冪敤 context-init锛堝姞杞?鍒涘缓 campaign context file锛?- **姣忎釜 strategy 瀹屾垚鍚?*: 璋冪敤 context-checkpoint锛堢‖鎬х害鏉燂紝涓嶅彲璺宠繃锛?- **涓€涓?context file per campaign**: 鎵€鏈?strategy 浜у嚭绱Н鍦ㄥ崟涓?campaign-scoped file

## Design Philosophy

鍏垫硶涔︽ā寮?鈥?CC 璇诲畬鍚庡唴鍖栧師鍒欙紝闈㈠鍏蜂綋鐮旂┒浠诲姟鑷鏋勫缓鎵撴硶銆?
**纭害鏉熶粎鍥涚**:
1. Budget Gate 鈥?閲忓寲鍦版澘锛屼笉杈炬爣涓嶈兘閫€鍑?2. Minimum Yield 鈥?姣忔鎵ц鐨勬渶浣庝骇鍑鸿姹?3. HARD-GATE 鈥?鍓嶇疆鏉′欢妫€鏌ワ紝涓嶆弧瓒充笉鑳藉紑濮?4. context-checkpoint 鈥?strategy 瀹屾垚鍚庡繀椤昏Е鍙?
**CC 鏈夋潈鑷富鍐崇瓥**:
- 绠€鍖?tactic 涓哄彧浣跨敤涓€鎵?SOP
- 鍐冲畾杩唬娆℃暟
- 鍐冲畾 campaign 缁勫悎椤哄簭
- 璺宠繃涓嶉€傜敤鐨?strategy


## Campaign:  creative ideation.Value.ToUpper() reative creative ideation.Value.ToUpper() deation

---
name: creative-ideation
description: Creative Generation Engine 鈥?transforms research hypotheses into diverse solution spaces via 10 parallel creativity campaigns spanning structural, analogical, destructive, and combinatorial methods.
execution: entry
pre-conditions:
  - north-star-crystallization (research intent crystallized)
  - hypothesis-formation (at least 1 testable hypothesis or precise research question)
---

# Creative Ideation

## Campaign Routing

| Signal Keywords | Route To |
|----------------|----------|
| SCAMPER, TRIZ, 缁勪欢鎵嬫湳, 缁撴瀯鍙樻崲, 鍔熻兘瑁佸壀 | 鈫?structural-deconstruction |
| 璺ㄥ煙, 绫绘瘮杩佺Щ, bisociation, 闅忔満鍒烘縺, 寮哄埗杩炴帴 | 鈫?cross-domain-discovery |
| 鍋囪鍚﹀畾, 鍙嶅悜澶磋剳椋庢毚, 鏈€宸柟娉? 鍙?benchmark | 鈫?assumption-destruction |
| 浠跨敓, 鐢熺墿绫绘瘮, 鑷劧绛栫暐, BioTRIZ, 鐢熸€佹ā寮?| 鈫?biomimicry |
| 绫绘瘮, 闅愬柣, 杩滆冻娉? 涓汉绫绘瘮, 绗﹀彿鍘嬬缉 | 鈫?synectics |
| 褰㈡€佸垎鏋? Zwicky box, CCA, 缁村害缁勫悎, 璁捐绌洪棿 | 鈫?morphological-exploration |
| PO, 妯悜鎬濈淮, 姒傚康鎵? 闅忔満鍏ュ彛, 鎸戞垬鎿嶄綔 | 鈫?lateral-thinking |
| 姒傚康铻嶅悎, blending, 娑岀幇, 澶氬眰缁勫悎, 鍔熻兘閲嶅垎閰?| 鈫?combinatorial-creativity |
| 瑙嗚鍒囨崲, 鍏附, 瑙掕壊鎵紨, 绾︽潫娉ㄥ叆, 鏃堕棿鎶曞皠 | 鈫?perspective-forcing |
| 绌蜂妇, 瑕嗙洊鍒嗘瀽, 鏂规硶鐭╅樀, ablation, 澶辫触鍒嗙被 | 鈫?systematic-enumeration |

## Multi-Campaign Orchestration

When the research problem warrants broad creative exploration, CC may invoke multiple campaigns in parallel. Four natural cluster families:

| Cluster | Campaigns | When |
|---------|-----------|------|
| 绫绘瘮鏃?(Analogy) | cross-domain-discovery + biomimicry + synectics | Problem benefits from external domain transfer |
| 缁勫悎鏃?(Combinatorial) | structural-deconstruction + morphological-exploration + combinatorial-creativity | Problem has decomposable structure |
| 棰犺鏃?(Disruptive) | assumption-destruction + lateral-thinking + perspective-forcing | Problem is stuck in dominant paradigm |
| 瑕嗙洊鏃?(Coverage) | systematic-enumeration + morphological-exploration | Need exhaustive space mapping |

**鍏ㄩ潰鍙戞暎**: Invoke 3-5 campaigns based on problem characteristics. Each campaign executes independently with its own context file. Results aggregated at ENTRY level.

CC decides:
- Which campaigns to invoke (1 or many)
- Execution order (parallel or sequential)
- When to cross-pollinate between campaign outputs
- When to stop (saturation-detection signals)

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈹斺攢鈹€ Campaign (10) 鈥?self-contained creative activity domain
        鈹斺攢鈹€ Strategy (5 per campaign) 鈥?iterative framework with budget + state ledger
              鈹斺攢鈹€ Tactic (2-3 per campaign) 鈥?SOP combination principle
                    鈹斺攢鈹€ SOP 鈥?single operation (subagent or import)
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

- **Campaign start**: `context-init` 鈥?load or create campaign context file
- **After each strategy**: `context-checkpoint` 鈥?append strategy output to campaign file
- **CC discretion**: Additional checkpoints when information density warrants it

Context file naming: `context/creative-ideation-[campaign]-[topic].md`

## Execution Boundary

This engine STOPS at idea generation. Its output is a structured set of diverse ideas with:
- Description (what the idea is)
- Source method (which campaign/strategy/SOP produced it)
- Novelty assessment (BREAKTHROUGH / HIGH / MODERATE / INCREMENTAL)
- Feasibility initial judgment (not deep validation)

It does NOT:
- Converge or select (鈫?convergence repo)
- Validate or debate (鈫?validation repo)
- Design experiments (鈫?experiment-design repo)
- Implement or prototype

## Shared Components

### Import SOPs (5, all campaigns)

| SOP | Source | Quality Gate |
|-----|--------|-------------|
| web-search | web-browsing | Snippets only 鈥?no conclusions from snippets |
| web-research | web-browsing | Must fetch full page via apify |
| paper-overview | literature-engine | Abstract only 鈥?no methodology conclusions |
| paper-search | literature-engine | AI summary 鈥?sufficient for methodology understanding |
| paper-research | literature-engine | Full text 鈥?required for quoting results |

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


## Campaign:  convergence.Value.ToUpper() onvergence

---
name: convergence
description: Universal Convergence Engine 鈥?6 campaigns for multi-criteria scoring, pairwise ranking, structured consensus, feasibility assessment, portfolio optimization, and adversarial verification. Transforms unstructured candidate sets into ranked selections, balanced portfolios, and validated decisions.
---

# Convergence

Universal convergence engine. Six campaigns, each a self-contained convergence paradigm. You provide a candidate set and a convergence intent 鈥?the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Pre-condition

- North-star-crystallization must be complete (research direction crystallized)
- Upstream output must be structured (from ideation / hypothesis-formation / deep-insight / knowledge-acquisition)

## Execution Boundary

- Stops when selection/ranking/portfolio is complete 鈥?"we have our picks"
- Does NOT execute selected options (鈫?experiment-design)
- Does NOT validate whether selections are correct (鈫?validation)
- Steel-manning serves as pre-convergence quality assurance within this repo; its SOPs are shareable with validation

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈫?Campaign (6): self-contained convergence paradigm
    鈫?Strategy: selected by convergence intent/scenario
      鈫?Tactic: multi-step orchestration pattern
        鈫?SOP: single operation (import or subagent)
```

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| score/rank candidates against multiple criteria | 鈫?multi-criteria-scoring |
| produce global ranking via pairwise comparisons | 鈫?pairwise-ranking |
| multiple perspectives disagree, need convergence | 鈫?structured-consensus |
| assess feasibility/readiness of candidates | 鈫?feasibility-assessment |
| select a balanced portfolio from candidates | 鈫?portfolio-optimization |
| verify rejected candidates, stress-test winners | 鈫?steel-manning |
| criteria themselves are contested | 鈫?structured-consensus 鈫?multi-criteria-scoring |
| high-stakes decision requiring method robustness | 鈫?multi-criteria-scoring (multi-method-triangulation) |
| too many candidates, need coarse screening first | 鈫?multi-criteria-scoring (non-compensatory-screening) 鈫?pairwise-ranking |

## Multi-Campaign Orchestration

CC has full autonomy to compose campaigns:

- **Serial**: multi-criteria-scoring 鈫?steel-manning 鈫?portfolio-optimization
- **Parallel**: multi-criteria-scoring + pairwise-ranking 鈫?take intersection
- **Backtrack**: steel-manning rejects 鈫?re-enter scoring for re-evaluation
- **Nested**: structured-consensus determines weights 鈫?multi-criteria-scoring uses those weights
- **Skip**: if only 3 candidates with clear criteria, pairwise-ranking alone may suffice

## Output Types

| Campaign | Output Type |
|----------|-------------|
| multi-criteria-scoring | RankedList[] 鈥?scored and ranked candidates with scores, ranks, confidence |
| pairwise-ranking | RankedList[] 鈥?global ranking with ratings, convergence, consistency |
| structured-consensus | ConsensusReport 鈥?agreement report with consensus level, disagreement points, argument structure |
| feasibility-assessment | FeasibilityMatrix 鈥?readiness matrix with dimension scores, blockers, paths |
| portfolio-optimization | Portfolio 鈥?selected combination with coverage, risk distribution, budget allocation |
| steel-manning | SteelManVerdict 鈥?adversarial verification verdict (ACCEPT / REJECT / REVISE) |

## MCP Tools

| MCP Server | Tools |
|------------|-------|
| brave-search | brave_web_search, brave_llm_context |
| apify | rag-web-browser |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries |
| semantic-scholar | relevanceSearch, paper, citations |
| wiki-vault | vault_search, vault_add_edge, vault_query_graph |

## Context Management Integration

- **Campaign start**: context-init (load/create campaign context file)
- **After each strategy completes**: context-checkpoint (append findings to campaign context file)
- **One context file per campaign**: all strategy outputs accumulate in a single campaign-scoped file

## Dependencies

| Dependency | What It Provides |
|-----------|-----------------|
| web-browsing | web-search + web-research (import SOPs) |
| literature-engine | paper-overview + paper-search + paper-research (import SOPs) |
| subagent-spawning | Subagent dispatch conventions (spawn-agent) |
| context-management | context-init + context-checkpoint |
| wiki-vault MCP | Knowledge persistence to graph |


## Campaign:  stress test.Value.ToUpper() tress stress test.Value.ToUpper() est

---
name: stress-test
description: Stress Test Engine with 5 campaigns (multiagent-debate, red-teaming, failure-anticipation, counterfactual-probing, adversarial-stress-testing). Use this skill whenever a user needs to adversarially validate any research artifact 鈥?hypotheses, claims, experiment designs, approaches, research questions, gaps, or ideas. Pre-condition: artifact exists + north-star-crystallization complete.
---

# Stress Test

Research Artifact Stress-Testing Engine 鈥?from structured debate to logical extreme, every claim must survive or be annotated. Five campaigns, each a self-contained adversarial validation domain. You provide a research artifact 鈥?the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Design Philosophy

Strategy Book mode. This file is a textbook, not a script. CC reads, internalizes principles, then autonomously constructs the validation approach for the specific artifact.

Hard constraints only:
- **Budget Gate**: Meet the strategy's quantitative floor (卤10%) before completing
- **State Ledger**: Print progress against budget before each major iteration decision
- **HARD-GATE**: Pre-conditions must be satisfied before entry
- **Context-checkpoint**: Triggered after each strategy completes (鈮?00 lines)

Everything else 鈥?execution order, iteration count, tactic selection, SOP combination 鈥?is CC's autonomous decision.

## Pre-conditions

1. Artifact exists (from knowledge-acquisition, deep-insight, hypothesis-formation, ideation, or convergence)
2. North-star-crystallization complete (provides scope constraint)

## Execution Boundaries

- Stop at validation and weakness annotation 鈥?do NOT modify the original artifact
- Do NOT perform upstream gap discovery or hypothesis generation
- May suggest correction directions, but actual corrections are executed by upstream repos

## Artifact Types Accepted

| Type | Description |
|------|-------------|
| `gap` | Research gap |
| `hypothesis` | Testable hypothesis |
| `research-question` | Research question |
| `idea` | Creative solution |
| `approach` | Selected method path |
| `experiment-design` | Experiment design |
| `claim` | Any research claim |

## Four-Level Hierarchy

```
ENTRY.md (this file)
  鈫?Campaign (5): self-contained adversarial validation domain
    鈫?Strategy: selected by validation purpose/intent
      鈫?Tactic: multi-step orchestration pattern (reusable across strategies)
        鈫?SOP: single operation (import or subagent)
```

CC can skip the tactic layer and use SOPs directly when the task is simple enough.

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| Adversarial debate, multi-perspective review | 鈫?multiagent-debate |
| Systematic attack, assumption challenge | 鈫?red-teaming |
| Failure mode prediction, risk assessment | 鈫?failure-anticipation |
| Critical dependency probing, causal necessity | 鈫?counterfactual-probing |
| Logical falsification, boundary testing | 鈫?adversarial-stress-testing |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **Quick validation**: multiagent-debate (critic-defender-judge) single round
- **Standard validation**: red-teaming + counterfactual-probing
- **Deep validation**: all 5 campaigns in sequence
- **Targeted risk**: failure-anticipation + adversarial-stress-testing

The orchestrator decides composition based on artifact type and validation needs.

## MCP Tools

| MCP Server | Tools | Purpose |
|------------|-------|---------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context | Web discovery |
| apify | rag-web-browser | Full-text web retrieval |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries | Paper access |
| semantic-scholar | relevanceSearch, paper, paperBatch, citations, references | Paper metadata |

## Context Management

- **Campaign start**: `context-init` 鈥?initialize context file
- **After each strategy**: `context-checkpoint` 鈥?append 鈮?00 lines
- One context file per campaign

## Output Types

Each campaign produces its own typed report:
- `DebateVerdict` (multiagent-debate)
- `RedTeamReport` (red-teaming)
- `FailureAnticipationReport` (failure-anticipation)
- `CounterfactualMap` (counterfactual-probing)
- `AdversarialStressReport` (adversarial-stress-testing)

`verdict-synthesis` SOP can aggregate multiple campaign results into a unified `StressTestSummary`.

## Dependencies

| Dependency | Provides |
|------------|----------|
| web-browsing | web-search, web-research (Import SOP) |
| literature-engine | paper-overview, paper-search, paper-research (Import SOP) |
| subagent-spawning | spawn-agent (execution runtime) |
| context-management | context-init, context-checkpoint (state persistence) |
| deep-insight | assumption-surfacing, evidence-synthesis, multi-stakeholder-simulation (cross-repo shared SOP) |


## Campaign:  experiment execution.Value.ToUpper() xperiment experiment execution.Value.ToUpper() xecution

---
name: experiment-execution
description: "Four-Campaign Experiment Execution Engine 鈥?designs experiments, analyzes constraints, plans scenarios, and executes with result collection"
version: 1.0.0
category: experiment-execution
type: entry
dependencies:
  skills:
    - web-browsing
    - literature-engine
    - context-management
    - subagent-spawning
  mcp:
    - brave-search
    - apify
    - alphaxiv
    - semantic-scholar
    - wiki-vault
---

# Experiment Execution

Four-Campaign Experiment Execution Engine 鈥?starting from validated research hypotheses/approaches, completes the full pipeline of experiment design, constraint analysis, scenario planning, implementation planning, and execution.

## Positioning

**Prerequisites**:
- north-star-crystallization completed (research intent is clear)
- hypothesis-formation or convergence/validation has produced validated approaches/hypotheses

**Execution boundary**: Full pipeline 鈥?from experiment design to actual execution to result collection and analysis.

**Outputs**:
- Experiment design report (variables, controls, metrics, statistical methods)
- Constraint analysis report (bottlenecks, dependencies, conflict resolution plans)
- Scenario analysis report (multiple future scenarios + robustness assessment)
- Executable plan (bite-sized task format)
- Experiment results report (metrics + statistical tests + reproducibility statement)

## Campaigns

| Campaign | Core Question | Input | Output |
|----------|--------------|-------|--------|
| experiment-design | "What experiment to run?" | Validated hypotheses/approaches | Complete experiment design |
| constraint-analysis | "What limits us?" | Experiment design + real-world constraints | Constraint analysis report + resolution plans |
| scenario-planning | "What might the future look like?" | Research approach + uncertainties | Multi-scenario analysis + robustness assessment |
| implementation-planning | "How to do it + do it" | Design + constraints + scenarios | Executable plan + execution results |

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| experiment design, factors, variables, ablation, baseline comparison, statistical methods | 鈫?experiment-design |
| bottleneck, constraint, insufficient resources, dependencies, conflicts | 鈫?constraint-analysis |
| scenarios, future, robustness, worst case, competitors, timeline | 鈫?scenario-planning |
| planning, execution, implementation, running experiments, result analysis, reproducibility | 鈫?implementation-planning |

## Multi-Campaign Orchestration

The four campaigns can be flexibly combined; CC autonomously decides how many to use and in what order:
- Typical serial: experiment-design 鈫?constraint-analysis 鈫?scenario-planning 鈫?implementation-planning
- Parallel: constraint-analysis 鈭?scenario-planning (can execute in parallel)
- Skip: CC may skip campaigns that are not needed (e.g., skip constraint-analysis if constraints are already clear)
- Backtrack: CC may backtrack from later campaigns (e.g., return to experiment-design if execution reveals design flaws)

## Context Management

- **Campaign start**: invoke context-init (load/create campaign context file)
- **After each strategy completes**: invoke context-checkpoint (hard constraint, cannot be skipped)
- **One context file per campaign**: all strategy outputs accumulate in a single campaign-scoped file

## Design Philosophy

Art of War mode 鈥?CC internalizes the principles after reading, then autonomously constructs its approach for each specific research task.

**Only four hard constraints**:
1. Budget Gate 鈥?quantitative floor, cannot exit without meeting it
2. Minimum Yield 鈥?minimum output requirement per execution
3. HARD-GATE 鈥?prerequisite check, cannot start without satisfying it
4. context-checkpoint 鈥?must be triggered after each strategy completes

**CC has autonomous decision authority over**:
- Simplifying tactics to use only a subset of SOPs
- Deciding iteration count
- Deciding campaign combination and ordering
- Skipping inapplicable strategies


## Infrastructure Skills

### Web Browsing
- `web-search`: Quick factual lookups, specific queries
- `web-research`: Deep multi-source investigation

### Literature Engine
- `literature-overview`: High-level landscape survey
- `literature-search`: Targeted paper discovery
- `literature-research`: Deep paper analysis and synthesis

### Subagent Spawning
- `spawn-agent`: Dispatch parallel research subagents

### Context Management
- `context-init`: Create new context file for a campaign
- `context-checkpoint`: Append ≥500 lines of process + results to current context file
