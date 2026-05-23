# knowledge-acquisition

Used to systematically gather and organize the literature, patents, benchmarks, experimental conditions, and evidence materials needed for research. It works well as a main entry point when entering a new direction or building an evidence base.

[Back to skill navigation](./skill-list.md)

Skill count: 100

| Skill | Description |
|-------|-------------|
| artifact-detection | Detect annotation artifacts and shortcuts in benchmarks |
| assignee-normalization | Standardize assignee names and identify corporate group affiliations across patent offices |
| baseline-establishment | SOTA Performance Baseline Campaign — 5 strategies for systematically collecting, standardizing, and analyzing performance data across methods. Produces standardized comparison tables, progress curves, and headroom analysis. |
| baseline-synthesis | Produce final structured baseline report integrating all analysis results |
| benchmark-archaeology | Evaluation Methodology Archaeology Campaign — 5 strategies for systematic analysis of AI/ML benchmarks, metrics, and leaderboards. Reveals construct validity issues, saturation, data contamination, and evaluation protocol inconsistencies. |
| benchmark-audit | Systematic quality assessment using BetterBench 46-criterion framework — 5 benchmarks, 30 papers, 40 web searches |
| benchmark-inventory | Identify and catalog all relevant benchmarks in target domain |
| benchmark-synthesis | Produce final structured audit report |
| bias-detection | Assess systematic biases in the evidence body — publication bias, reporting bias, and selective outcome reporting. Budget: 40 studies, 40 effect sizes, 40 web searches. |
| capability-taxonomy-mapping | Build capability taxonomy, map existing benchmark coverage |
| categorize-papers | Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review. |
| citation-chaining | Forward and backward citation tracing tactic — expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation. |
| citation-network-analysis | Build and analyze patent citation networks — main path analysis, PageRank, cluster detection |
| claim-analysis | Deep claim scope analysis — decompose independent/dependent claims and assess protection scope breadth. Budget: 30 patent families, 30 claim parses, 20 web searches. |
| claim-decomposition | Independent/dependent claim parsing, element extraction, and feature mapping to technical domains |
| claim-parsing | Patent claim syntax parsing — independent/dependent relationships and element extraction |
| classification-navigation | IPC/CPC hierarchy drill-down and lateral expansion for patent discovery |
| competitive-intelligence | Analyze competitor IP portfolios — comparative patent portfolio reports with strategy inference. Budget: 120 patent families, 15 claim parses, 40 web searches. |
| compute-normalization | Normalize results by compute budget (Pareto analysis) |
| condition-cataloging | Record evaluation conditions (data splits, hyperparams, hardware, seeds) from a paper |
| condition-normalization | Compare and standardize experimental conditions across papers |
| condition-standardization | Standardize evaluation condition differences across papers — 20 methods, 60 data points, 30 web searches budget |
| construct-validity-assessment | Evaluate whether benchmark measures its claimed capability |
| contamination-audit | Detect train-test data leakage and memorization artifacts |
| coverage-mapping | Map evaluation coverage, identify untested capability dimensions — 20 benchmarks, 30 papers, 50 web searches |
| cumulative-tracking | Track evidence accumulation over time — cumulative meta-analysis protocol design. Budget: 40 studies, 40 effect sizes, 30 web searches. |
| data-extraction-form | Design structured data extraction form for systematic meta-analysis data collection |
| deep-survey | Precise, targeted investigation of a specific sub-problem — few papers, all read in full depth. High paper-research ratio (50% deep-read rate). Use when the user knows exactly what they need to understand and requires detailed technical analysis with equations, hyperparameters, and specific claims extracted. |
| define-search-protocol | Formalize search queries and inclusion/exclusion criteria for systematic surveys. Produces a reproducible search protocol document. Used by systematic-survey. |
| discrepancy-analysis | Identify discrepancies between reported and reproducible scores — 15 methods, 45 data points, 30 web searches budget |
| discrepancy-identification | Compare same-method scores across sources, flag significant deviations |
| documentation-audit | Assess documentation completeness against BetterBench/Datasheets standards |
| effect-size-extraction | Systematically extract effect sizes and conditions from papers for meta-analytic synthesis |
| effect-size-planning | Determine effect size types and calculation methods for meta-analytic synthesis |
| evaluation-protocol-comparison | Compare implementation differences of same benchmark across papers |
| evidence-network-construction | Build evidence network graph for network meta-analysis — nodes, edges, geometry assessment |
| evidence-synthesis-planning | Plan the statistical synthesis approach — model selection, heterogeneity strategy, and reporting |
| extract-data | Structured data extraction from deep-read papers — produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey. |
| gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| headroom-estimation | Estimate theoretical/practical ceiling vs current SOTA gap |
| heterogeneity-investigation | Explain why different studies reach different conclusions — heterogeneity investigation protocol. Budget: 30 studies, 30 effect sizes, 50 web searches. |
| heterogeneity-source-analysis | Identify and classify sources of between-study heterogeneity (clinical, methodological, statistical) |
| inclusion-criteria-design | Define inclusion/exclusion criteria for systematic study selection in meta-analysis |
| landscape-survey | Patent landscape full-scan — maps technology domain via assignee ranking, IPC/CPC classification, filing trends. Budget: 200 patent families, 0 claim parses, 80 web searches. |
| leaderboard-dynamics-analysis | Analyze leaderboard score distributions, compression, selective reporting |
| leaderboard-harvesting | Systematically collect performance data from platforms and papers |
| legal-status-assessment | Determine patent legal status — active, expired, pending, lapsed, or revoked |
| literature-survey | Autonomous Literature Survey Campaign — 5 research paradigms (scoping, systematic, deep, narrative, snowball) with quantitative budget enforcement. Selects and executes the right survey paradigm based on research intent. |
| meta-analysis | Cross-Study Statistical Synthesis Campaign — 5 strategies for systematic collection and methodological planning of multi-study evidence synthesis. Covers pairwise, network, cumulative meta-analysis, heterogeneity investigation, and bias detection. Stops at protocol design (no computation). |
| meta-analysis-synthesis | Produce final meta-analysis protocol document assembling all planning outputs into PRISMA-compliant protocol |
| method-discovery | Identify all relevant methods via literature, leaderboards, citation chains |
| method-inventory | Comprehensively identify all relevant methods for a task — 50 methods, 60 web searches budget |
| metric-decomposition | Decompose composite metrics into constituent signals, analyze polarity and ceiling effects |
| narrative-framing | Theory-driven reading tactic — define a theoretical framework first, then guide reading to fill it with evidence. Five stages (theme identification, argument construction, evidence collection, counter-evidence, synthesis). The most intellectually demanding tactic. |
| narrative-review | Theory-driven literature review for building arguments and frameworks. Flexible, subjective, and narrative-focused — selects evidence strategically to support a thesis. High web-research budget for blogs, opinion pieces, and industry perspectives. Use when the user is writing a position paper, survey introduction, or constructing a coherent narrative around a research theme. |
| network-comparison | Compare N methods simultaneously including indirect evidence — network meta-analysis protocol design. Budget: 50 studies, 80 effect sizes, 60 web searches. |
| pairwise-synthesis | Compare two methods across multiple studies — paired meta-analysis protocol design. Budget: 30 studies, 30 effect sizes, 40 web searches. |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| patent-categorization | Classify patents by tech subdomain, application scenario, and value chain position |
| patent-family-tracing | Forward/backward patent citation and priority tracing until saturation |
| patent-mining | Systematic Patent Analysis Campaign — 5 strategies for patent landscape analysis, prior art search, white space identification, competitive intelligence, and claim analysis. Produces structured patent intelligence reports. |
| patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |
| patent-synthesis | Produce final structured patent intelligence report from all analysis results |
| performance-extraction | Systematically extract performance data and conditions from papers — 30 methods, 150 data points, 40 web searches budget |
| performance-table-assembly | Assemble unified comparison table with confidence interval annotations |
| pico-formulation | Construct PICO/PECO framework for the meta-analysis research question |
| prior-art-search | Evaluate novelty of specific invention — find relevant prior art across patents, publications, and products. Budget: 80 patent families, 20 claim parses, 50 web searches. |
| prisma-flowchart | Generate PRISMA-compliant flow data documenting the screening funnel — counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic. |
| prisma-screening | Multi-stage PRISMA screening tactic — progressively filter papers from a large candidate pool to a focused set for deep reading. Four stages (identification, title/abstract screening, full-text screening, inclusion) with documented counts at each stage. |
| progress-curve-construction | Build performance-over-time progress curves with inflection detection |
| progress-curve-fitting | Construct performance-over-time visualization data |
| progress-quantification | Track performance progress over time, quantify remaining headroom — 30 methods, 100 data points, 40 web searches budget |
| protocol-element-extraction | Extract evaluation protocol parameters from papers |
| protocol-forensics | Analyze evaluation protocol differences across papers for same benchmark — 5 benchmarks, 60 papers, 30 web searches |
| publication-bias-assessment | Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection model analyses for publication bias |
| quality-assessment | Methodological rigor scoring for papers — evaluates bias risk, reproducibility, sample adequacy using established frameworks. Used by systematic-survey. |
| quality-assessment-protocol | Methodological quality and bias risk assessment of included studies using validated tools |
| quality-scoring | Multi-dimensional patent quality assessment — forward citations, family size, claim count, geographic breadth |
| reproducibility-checklist-audit | Assess paper completeness against ML Reproducibility Checklist |
| risk-of-bias-assessment | Assess methodological bias using RoB2, PROBAST, or QUADAS-2 validated tools |
| saturation-analysis | Track score trajectories, detect saturation/failure points — 15 benchmarks, 50 papers, 60 web searches |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scoping-survey | Broad landscape mapping strategy — quickly understand what exists in a field. Prioritizes breadth over depth with high paper-overview volume and minimal deep reading. Use when entering a new field or needing orientation before committing to deeper investigation. |
| score-extraction | Extract (Task, Dataset, Metric, Score, Conditions) tuples from a paper |
| score-trajectory-analysis | Collect historical scores, fit saturation curves, detect inflection points |
| seed-selection | Validate and prioritize starting papers for snowball surveys. Evaluates which seeds will yield the richest citation traces based on citation count, recency, and network position. |
| sensitivity-analysis-design | Design leave-one-out, influence diagnostics, subgroup analyses, and robustness checks |
| snowball | Citation-chain-driven literature survey starting from seed papers. Traces research lineage in both forward (who cited this) and backward (what this cited) directions until saturation. High deep-read ratio (67%). Use when the user already has key papers and wants to find everything connected to them — ancestors, descendants, and branch points. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |
| systematic-survey | Exhaustive PRISMA-style literature survey — comprehensive coverage of all related work on a specific question. Multi-stage screening, citation chaining, quality assessment, and structured data extraction. Use when the user needs to demonstrate complete literature coverage or conduct rigorous gap analysis. |
| taxonomy-mapping | Construct a hierarchical field map from paper collection — multi-level taxonomy with parent/child relationships, paper counts per node, and maturity indicators. Used by scoping-survey. |
| thematic-coding | Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review. |
| trend-analysis | Patent filing volume time-series, technology lifecycle stage, and S-curve analysis |
| validity-probing | Challenge construct validity — does benchmark measure claimed capability? — 3 benchmarks, 40 papers, 30 web searches |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| white-space-analysis | Identify patent coverage gaps — feature cross-matrix blank areas revealing unprotected technology combinations. Budget: 150 patent families, 10 claim parses, 60 web searches. |
| white-space-mapping | Feature cross-matrix construction and blank area identification for patent opportunity mapping |
