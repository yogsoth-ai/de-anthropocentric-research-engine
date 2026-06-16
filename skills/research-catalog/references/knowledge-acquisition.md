# knowledge-acquisition — skill table

101 skills. Sorted by layer (campaign→strategy→tactic→sop), then name.

| Layer | Skill | Description |
| --- | --- | --- |
| campaign | baseline-establishment | SOTA Performance Baseline Campaign — 5 strategies for systematically collecting, standardizing, and analyzing performance data across methods. Produces standardized comparison tables, progress curves, and headroom analysis. |
| campaign | benchmark-archaeology | Evaluation Methodology Archaeology Campaign — 5 strategies for systematic analysis of AI/ML benchmarks, metrics, and leaderboards. Reveals construct validity issues, saturation, data contamination, and evaluation protocol inconsistencies. |
| campaign | knowledge-acquisition | Research Knowledge Acquisition Engine with 5 campaigns (literature-survey, patent-mining, benchmark-archaeology, meta-analysis, baseline-establishment). Use this skill whenever a user needs to systematically acquire research knowledge — academic literature, patent landscapes, benchmark evaluations, cross-study statistical synthesis, or SOTA performance baselines. Pre-condition: north-star-crystallization must be complete. |
| campaign | literature-survey | Autonomous Literature Survey Campaign — 5 research paradigms (scoping, systematic, deep, narrative, snowball) with quantitative budget enforcement. Selects and executes the right survey paradigm based on research intent. |
| campaign | meta-analysis | Cross-Study Statistical Synthesis Campaign — 5 strategies for systematic collection and methodological planning of multi-study evidence synthesis. Covers pairwise, network, cumulative meta-analysis, heterogeneity investigation, and bias detection. Stops at protocol design (no computation). |
| campaign | patent-mining | Systematic Patent Analysis Campaign — 5 strategies for patent landscape analysis, prior art search, white space identification, competitive intelligence, and claim analysis. Produces structured patent intelligence reports. |
| strategy | benchmark-audit | Systematic quality assessment using BetterBench 46-criterion framework — 5 benchmarks, 30 papers, 40 web searches |
| strategy | bias-detection | Assess systematic biases in the evidence body — publication bias, reporting bias, and selective outcome reporting. Budget: 40 studies, 40 effect sizes, 40 web searches. |
| strategy | claim-analysis | Deep claim scope analysis — decompose independent/dependent claims and assess protection scope breadth. Budget: 30 patent families, 30 claim parses, 20 web searches. |
| strategy | competitive-intelligence | Analyze competitor IP portfolios — comparative patent portfolio reports with strategy inference. Budget: 120 patent families, 15 claim parses, 40 web searches. |
| strategy | condition-standardization | Standardize evaluation condition differences across papers — 20 methods, 60 data points, 30 web searches budget |
| strategy | coverage-mapping | Map evaluation coverage, identify untested capability dimensions — 20 benchmarks, 30 papers, 50 web searches |
| strategy | cumulative-tracking | Track evidence accumulation over time — cumulative meta-analysis protocol design. Budget: 40 studies, 40 effect sizes, 30 web searches. |
| strategy | deep-survey | Precise, targeted investigation of a specific sub-problem — few papers, all read in full depth. High paper-research ratio (50% deep-read rate). Use when the user knows exactly what they need to understand and requires detailed technical analysis with equations, hyperparameters, and specific claims extracted. |
| strategy | discrepancy-analysis | Identify discrepancies between reported and reproducible scores — 15 methods, 45 data points, 30 web searches budget |
| strategy | heterogeneity-investigation | Explain why different studies reach different conclusions — heterogeneity investigation protocol. Budget: 30 studies, 30 effect sizes, 50 web searches. |
| strategy | landscape-survey | Patent landscape full-scan — maps technology domain via assignee ranking, IPC/CPC classification, filing trends. Budget: 200 patent families, 0 claim parses, 80 web searches. |
| strategy | method-inventory | Comprehensively identify all relevant methods for a task — 50 methods, 60 web searches budget |
| strategy | narrative-review | Theory-driven literature review for building arguments and frameworks. Flexible, subjective, and narrative-focused — selects evidence strategically to support a thesis. High web-research budget for blogs, opinion pieces, and industry perspectives. Use when the user is writing a position paper, survey introduction, or constructing a coherent narrative around a research theme. |
| strategy | network-comparison | Compare N methods simultaneously including indirect evidence — network meta-analysis protocol design. Budget: 50 studies, 80 effect sizes, 60 web searches. |
| strategy | pairwise-synthesis | Compare two methods across multiple studies — paired meta-analysis protocol design. Budget: 30 studies, 30 effect sizes, 40 web searches. |
| strategy | performance-extraction | Systematically extract performance data and conditions from papers — 30 methods, 150 data points, 40 web searches budget |
| strategy | prior-art-search | Evaluate novelty of specific invention — find relevant prior art across patents, publications, and products. Budget: 80 patent families, 20 claim parses, 50 web searches. |
| strategy | progress-quantification | Track performance progress over time, quantify remaining headroom — 30 methods, 100 data points, 40 web searches budget |
| strategy | protocol-forensics | Analyze evaluation protocol differences across papers for same benchmark — 5 benchmarks, 60 papers, 30 web searches |
| strategy | saturation-analysis | Track score trajectories, detect saturation/failure points — 15 benchmarks, 50 papers, 60 web searches |
| strategy | scoping-survey | Broad landscape mapping strategy — quickly understand what exists in a field. Prioritizes breadth over depth with high paper-overview volume and minimal deep reading. Use when entering a new field or needing orientation before committing to deeper investigation. |
| strategy | snowball | Citation-chain-driven literature survey starting from seed papers. Traces research lineage in both forward (who cited this) and backward (what this cited) directions until saturation. High deep-read ratio (67%). Use when the user already has key papers and wants to find everything connected to them — ancestors, descendants, and branch points. |
| strategy | systematic-survey | Exhaustive PRISMA-style literature survey — comprehensive coverage of all related work on a specific question. Multi-stage screening, citation chaining, quality assessment, and structured data extraction. Use when the user needs to demonstrate complete literature coverage or conduct rigorous gap analysis. |
| strategy | validity-probing | Challenge construct validity — does benchmark measure claimed capability? — 3 benchmarks, 40 papers, 30 web searches |
| strategy | white-space-analysis | Identify patent coverage gaps — feature cross-matrix blank areas revealing unprotected technology combinations. Budget: 150 patent families, 10 claim parses, 60 web searches. |
| tactic | artifact-detection | Detect annotation artifacts and shortcuts in benchmarks |
| tactic | citation-chaining | Forward and backward citation tracing tactic — expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation. |
| tactic | knowledge-acquisition-claim-decomposition | Independent/dependent claim parsing, element extraction, and feature mapping to technical domains |
| tactic | classification-navigation | IPC/CPC hierarchy drill-down and lateral expansion for patent discovery |
| tactic | condition-normalization | Compare and standardize experimental conditions across papers |
| tactic | effect-size-extraction | Systematically extract effect sizes and conditions from papers for meta-analytic synthesis |
| tactic | evaluation-protocol-comparison | Compare implementation differences of same benchmark across papers |
| tactic | evidence-synthesis-planning | Plan the statistical synthesis approach — model selection, heterogeneity strategy, and reporting |
| tactic | leaderboard-harvesting | Systematically collect performance data from platforms and papers |
| tactic | narrative-framing | Theory-driven reading tactic — define a theoretical framework first, then guide reading to fill it with evidence. Five stages (theme identification, argument construction, evidence collection, counter-evidence, synthesis). The most intellectually demanding tactic. |
| tactic | patent-family-tracing | Forward/backward patent citation and priority tracing until saturation |
| tactic | prisma-screening | Multi-stage PRISMA screening tactic — progressively filter papers from a large candidate pool to a focused set for deep reading. Four stages (identification, title/abstract screening, full-text screening, inclusion) with documented counts at each stage. |
| tactic | progress-curve-construction | Build performance-over-time progress curves with inflection detection |
| tactic | quality-assessment-protocol | Methodological quality and bias risk assessment of included studies using validated tools |
| tactic | score-trajectory-analysis | Collect historical scores, fit saturation curves, detect inflection points |
| sop | assignee-normalization | Standardize assignee names and identify corporate group affiliations across patent offices |
| sop | baseline-synthesis | Produce final structured baseline report integrating all analysis results |
| sop | knowledge-acquisition-benchmark-inventory | Identify and catalog all relevant benchmarks in target domain |
| sop | benchmark-synthesis | Produce final structured audit report |
| sop | capability-taxonomy-mapping | Build capability taxonomy, map existing benchmark coverage |
| sop | categorize-papers | Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review. |
| sop | citation-network-analysis | Build and analyze patent citation networks — main path analysis, PageRank, cluster detection |
| sop | claim-parsing | Patent claim syntax parsing — independent/dependent relationships and element extraction |
| sop | compute-normalization | Normalize results by compute budget (Pareto analysis) |
| sop | condition-cataloging | Record evaluation conditions (data splits, hyperparams, hardware, seeds) from a paper |
| sop | construct-validity-assessment | Evaluate whether benchmark measures its claimed capability |
| sop | contamination-audit | Detect train-test data leakage and memorization artifacts |
| sop | data-extraction-form | Design structured data extraction form for systematic meta-analysis data collection |
| sop | define-search-protocol | Formalize search queries and inclusion/exclusion criteria for systematic surveys. Produces a reproducible search protocol document. Used by systematic-survey. |
| sop | discrepancy-identification | Compare same-method scores across sources, flag significant deviations |
| sop | documentation-audit | Assess documentation completeness against BetterBench/Datasheets standards |
| sop | effect-size-planning | Determine effect size types and calculation methods for meta-analytic synthesis |
| sop | evidence-network-construction | Build evidence network graph for network meta-analysis — nodes, edges, geometry assessment |
| sop | extract-data | Structured data extraction from deep-read papers — produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey. |
| sop | knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| sop | headroom-estimation | Estimate theoretical/practical ceiling vs current SOTA gap |
| sop | heterogeneity-source-analysis | Identify and classify sources of between-study heterogeneity (clinical, methodological, statistical) |
| sop | inclusion-criteria-design | Define inclusion/exclusion criteria for systematic study selection in meta-analysis |
| sop | leaderboard-dynamics-analysis | Analyze leaderboard score distributions, compression, selective reporting |
| sop | legal-status-assessment | Determine patent legal status — active, expired, pending, lapsed, or revoked |
| sop | meta-analysis-synthesis | Produce final meta-analysis protocol document assembling all planning outputs into PRISMA-compliant protocol |
| sop | method-discovery | Identify all relevant methods via literature, leaderboards, citation chains |
| sop | metric-decomposition | Decompose composite metrics into constituent signals, analyze polarity and ceiling effects |
| sop | knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| sop | knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| sop | knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| sop | patent-categorization | Classify patents by tech subdomain, application scenario, and value chain position |
| sop | patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |
| sop | patent-synthesis | Produce final structured patent intelligence report from all analysis results |
| sop | performance-table-assembly | Assemble unified comparison table with confidence interval annotations |
| sop | pico-formulation | Construct PICO/PECO framework for the meta-analysis research question |
| sop | prisma-flowchart | Generate PRISMA-compliant flow data documenting the screening funnel — counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic. |
| sop | progress-curve-fitting | Construct performance-over-time visualization data |
| sop | protocol-element-extraction | Extract evaluation protocol parameters from papers |
| sop | publication-bias-assessment | Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection model analyses for publication bias |
| sop | quality-assessment | Methodological rigor scoring for papers — evaluates bias risk, reproducibility, sample adequacy using established frameworks. Used by systematic-survey. |
| sop | quality-scoring | Multi-dimensional patent quality assessment — forward citations, family size, claim count, geographic breadth |
| sop | reproducibility-checklist-audit | Assess paper completeness against ML Reproducibility Checklist |
| sop | risk-of-bias-assessment | Assess methodological bias using RoB2, PROBAST, or QUADAS-2 validated tools |
| sop | knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| sop | score-extraction | Extract (Task, Dataset, Metric, Score, Conditions) tuples from a paper |
| sop | seed-selection | Validate and prioritize starting papers for snowball surveys. Evaluates which seeds will yield the richest citation traces based on citation count, recency, and network position. |
| sop | sensitivity-analysis-design | Design leave-one-out, influence diagnostics, subgroup analyses, and robustness checks |
| sop | survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |
| sop | taxonomy-mapping | Construct a hierarchical field map from paper collection — multi-level taxonomy with parent/child relationships, paper counts per node, and maturity indicators. Used by scoping-survey. |
| sop | thematic-coding | Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review. |
| sop | trend-analysis | Patent filing volume time-series, technology lifecycle stage, and S-curve analysis |
| sop | knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| sop | knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| sop | white-space-mapping | Feature cross-matrix construction and blank area identification for patent opportunity mapping |
