# Skill Index

Total skills in this distribution: 823

## north-star-crystallization (33 skills)

| Skill | Description |
|-------|-------------|
| actor-profiling | Understand who the user is — background, resources, constraints, and deep motivations. Produces an ActorProfile that informs all downstream decisions. Use this tactic at the start of any crystallization process to build a model of the user's capabilities, limitations, and intent. |
| and-or-decompose | KAOS-style recursive goal decomposition. AND decomposition for sub-goals that must ALL be satisfied. OR decomposition for alternative paths where any one suffices. Produces a GoalTree (DAG structure). |
| ask-constraints | Understand hard boundaries on the user's research — target venues, methodology preferences, areas to avoid, advisor/team requirements. Not limited to ML/AI — works for any research domain. |
| ask-decomposition-validation | Present the GoalTree to the user for confirmation. Ask about reasonableness, missing elements, and priority ordering among sub-goals. |
| ask-intentionality | Deep WHY probing inspired by i* Intentionality modeling. Understand the user's motivation, success definition, risk tolerance, innovation preference, independence preference, time urgency, and learning willingness. The most important SOP in actor-profiling — understanding WHY drives everything downstream. |
| ask-obstacle-acceptance | Present obstacles with their severity assessments and proposed mitigations to the user. Ask whether they can accept these obstacles. If unacceptable after 2 rounds, return to present-candidates. |
| assess-obstacle-severity | Rate each identified obstacle's difficulty — overcomability, time cost, workaround existence. May optionally use search tools to validate assessments. |
| broad-paper-search | Paper landscape scan within selected field(s). Strict import of literature-engine/literature-overview skill. Hard constraint: at least 80 papers scanned. |
| broad-web-search | Quick web scanning for field landscape understanding. Strict import of web-browsing/web-search skill. Hard constraint: brave_web_search count=10 per call, at least 150 total search results before completing. |
| clarify-resources | Understand what resources the user has available for research — compute, timeline, collaboration, data access, experimental environment. Every item accepts 'TBD' as a valid answer. |
| cold-start | Full crystallization strategy for users who have no research direction at all. Covers actor profiling, landscape reconnaissance, direction narrowing, obstacle analysis, goal decomposition, and north-star synthesis. Use when the user's first message reveals zero specificity about what they want to research. |
| crystallize-north-star | "Fuse the GoalTree root node and user motivation into a single crystallized North Star statement. Format: '[verb] [specific goal], through [method/path], solving [what problem], ultimately [what impact]'. Quality checks: specific? ambitious? achievable?" |
| deep-web-search | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Spawns a subagent to read pages in isolated context. Hard constraint: at least 30 web pages read in full. |
| direction-narrowing | Focus within the user's chosen field(s). Identify specific sub-directions through deep paper and web research, then present ranked candidates. Use after landscape-reconnaissance has identified fields of interest. |
| explore-resume | Understand the user's background comprehensively — technical stack, project experience, research experience, publications, research directions. Allows user to express interest beyond their resume. Execute once only, never re-run. |
| feasibility-check | Cross-reference the GoalTree against ActorProfile (capabilities), ObstacleReport (known barriers), and timeline (deadline feasibility). Identify infeasible paths and suggest OR alternatives. |
| final-validation | Self-review the North Star + ResearchBrief for completeness, consistency, and clarity before presenting to user. If issues found, return to specific tactic/SOP for targeted fix. If passes, present final output to user for confirmation. |
| formulate-top-goal | "Express the user's chosen research direction as a formal goal statement in the format: 'Achieve [what], such that [effect], under [constraints]'. Confirm with user before proceeding to decomposition." |
| generate-candidate-fields | Propose 3-8 candidate research fields based on the full ActorProfile. When user wants to explore beyond their current stack, use other ActorProfile signals (intentionality, boundary) to determine exploration space. Free exploration within the boundary. |
| generate-research-brief | Aggregate all accumulated context from the crystallization process into a structured ResearchBrief document. This is the final output artifact alongside the North Star — a comprehensive requirement context document for downstream research strategies. |
| goal-decomposition | Structure the user's chosen direction into a formal goal tree using KAOS-style AND/OR decomposition. Validate feasibility against ActorProfile and ObstacleReport. Use after obstacle-analysis confirms the direction is viable. |
| hot-start | Minimal crystallization strategy for users who already have a specific research topic or problem (e.g., "I want to improve CoT faithfulness in LLMs") and need structuring into a formal North Star. Heavily simplifies or skips exploration tactics, focusing on obstacle analysis, goal decomposition, and synthesis. Use when the user's first message reveals a specific, actionable research direction. |
| identify-obstacles | Enumerate barriers to pursuing the chosen research direction — knowledge barriers, resource barriers, capability barriers, competition barriers. May optionally use search tools to discover obstacles the user hasn't mentioned. |
| landscape-reconnaissance | Broad, shallow exploration of candidate research fields. Understand what's out there before narrowing. Use when the user needs to discover which fields are available to them — especially in cold-start and warm-start scenarios. |
| landscape-synthesis | Evaluate each candidate research field on maturity, competition, entry barrier, and publication opportunity. Synthesizes broad-web-search results into a structured FieldPanorama. Must consider both niche approaches AND direct frontal competition in hot fields. |
| north-star-crystallization | Goal-Driven Requirement Refinement Engine for Research. Crystallize a user's fuzzy research intent into a North Star statement and structured ResearchBrief through adaptive dialogue and on-demand investigation. |
| north-star-synthesis | Converge all accumulated context into a crystallized North Star statement and structured ResearchBrief. Performs self-review before presenting to user. Use as the final tactic in any start mode — this is where everything comes together. |
| obstacle-analysis | Identify what blocks the user from pursuing their chosen direction, assess severity, propose mitigations with search-validated evidence, and get user acceptance. Use after direction-narrowing has identified a specific direction. |
| present-and-ask | Present the field panorama to the user and gather their preferences — which fields interest them, which they reject, and why. A dialogue SOP that bridges landscape-synthesis output to user decision. |
| present-candidates | Analyze sub-directions within the user's chosen field and present ranked candidates. Combines sub-direction identification, skill-gap matching, and presentation into a single SOP. Depth scales by start mode: cold-start shows broad sub-directions, warm-start shows specific sub-problems, hot-start shows granular technical details. |
| propose-mitigations | Propose concrete mitigation strategies for severe obstacles. MUST use search tools to validate that proposed mitigations are realistic — no armchair theorizing. Each mitigation must have evidence of feasibility. |
| validate-leaves | Quality check on leaf nodes of the GoalTree. Verify each leaf is specific enough, actionable, and that the set of leaves fully covers the top goal. Flag issues for further decomposition. |
| warm-start | Simplified crystallization strategy for users who have a general research direction (e.g., "I'm interested in LLM reasoning") but lack specificity. Simplifies actor profiling and landscape reconnaissance, then proceeds through direction narrowing, obstacle analysis, goal decomposition, and north-star synthesis. Use when the user's first message reveals a general area but not a specific problem. |

## knowledge-acquisition (100 skills)

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

## deep-insight (111 skills)

| Skill | Description |
|-------|-------------|
| abp-vulnerability-classification | Classify assumptions on 2 axes — load-bearing (how much conclusion depends on it) × vulnerable (how likely to be false). Focuses attention on High-Load × High-Vulnerable quadrant. |
| abstraction-laddering | Move between concrete and abstract framings — 3 levels up (Why?) and 3 levels down (How?) to find the most productive research level. |
| ahrq-reason-classification | Classify gap root causes using AHRQ 4-reason framework (insufficient info, biased info, inconsistent info, not yet integrated). |
| alternative-model-generation | Generate alternative model formulations by relaxing, replacing, or generalizing specific assumptions. |
| appreciative-discovery | Search for positive deviants and extract transferable principles using Appreciative Inquiry. |
| appreciative-reframing | Find positive deviants and reframe the problem from deficit-based to asset-based using Appreciative Inquiry. |
| assumption-audit | Surface all assumptions, classify by vulnerability (load-bearing × likely-false), validate causal logic. Focus on dangerous assumptions — high load-bearing + non-explicit. |
| assumption-criticality | Measure how much conclusions change when each assumption is negated. Ranks assumptions by their impact on the final result. |
| assumption-enumeration | Systematically identify all assumptions in a method/model — structural, parametric, distributional, and scope assumptions. |
| assumption-extraction | Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model. |
| assumption-perturbation | One-at-a-time assumption perturbation — extract assumptions, define negations, re-derive conclusions under each negation, measure sensitivity. Identifies which assumptions are load-bearing. |
| assumption-stress-test | Systematic stress testing of assumptions — surface, classify by vulnerability, attack, assess fragility. Combines assumption-surfacing (shared), abp-vulnerability-classification, and clr-validation SOPs. |
| assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| boundary-analysis | Boundary Analysis Campaign — probe where methods fail, map validity envelopes, test robustness, catalog failure modes, detect scaling limits. 5 strategies, 3 tactics, 11 subagent SOPs. |
| boundary-critique | Apply CSH boundary critique — what is included/excluded, who benefits/is harmed, what expertise is privileged/marginalized. Identifies opportunities at the boundaries. |
| boundary-synthesis | Compile all boundary analysis products into a coherent report — validity envelopes, robustness results, failure catalogs, scaling maps, safe operating conditions. |
| boundary-unfolding | Systematically expose hidden system boundaries — CSH 12-question is/ought comparison, identify excluded stakeholders, reveal blind spots. Combines csh-12-question, jtbd-mapping, and salience-classification SOPs. |
| catwoe-analysis | Apply Checkland's CATWOE analysis from a specific stakeholder perspective to reveal how the problem looks from that viewpoint. |
| causal-tree-building | Build logical causal trees from symptoms to root causes — list UDEs, connect causal chains, validate logic, locate root causes. Combines ishikawa-decomposition, current-reality-tree, and clr-validation SOPs. |
| clr-validation | Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity. |
| concept-matrix-construction | Build articles × concepts coverage matrix to visualize research landscape and identify empty cells as gap candidates. |
| conclusion-sensitivity-measurement | Quantify how much conclusions change across all assumption negations and produce a sensitivity ranking. |
| consequence-following | Follow a provocation's logical consequences step by step to extract viable insights and new research directions. |
| controlled-perturbation | Systematically vary parameters along defined axes, recording performance at each point to identify degradation thresholds. |
| convergence-assessment | Compare results across multiple model variants — quantitative agreement metrics and qualitative conclusion stability. |
| counter-assumption-generation | Generate dialectical opposites for governing variables — coherent alternative worldviews where the opposite is true. |
| critical-path-identification | Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization. |
| cross-database-verification | Verify gap existence across multiple databases (Semantic Scholar, Google Scholar, arXiv, domain-specific). Distinguishes database-specific gaps from universal gaps. |
| cross-validation | Multi-source cross-validation of gap authenticity — cross-database search, temporal sensitivity testing, false-gap filtering, stakeholder confirmation. |
| csh-12-question | Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions (motivation, control, expertise, legitimacy) comparing is vs ought. |
| current-reality-tree | Build TOC Current Reality Trees — connect Undesirable Effects via sufficient-cause logic to identify 1-3 root causes. |
| decision-sensitivity | Identify which uncertainties would actually change the research direction decision. Compute EVPI to prioritize uncertainty reduction. |
| dialectical-escalation | Double-loop learning escalation — surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists. |
| dialectical-reformulation | Surface Argyris governing variables and test whether the problem dissolves under alternative governing variables (double-loop learning). |
| dialectical-synthesis | Hegelian thesis-antithesis-synthesis cycle — propose position, generate opposition, structured debate, synthesize transcending insight. Combines evaporating-cloud and polarity-mapping SOPs. |
| distribution-assignment | Assign probability distributions to uncertain parameters based on available evidence and domain knowledge. |
| dominant-idea-escape | Identify dominant paradigms constraining the field and use de Bono lateral thinking provocations to escape them. |
| dominant-idea-identification | Identify dominant paradigms and assumptions constraining thinking in a research field. |
| edge-case-generation | Systematically generate boundary inputs — boundary values, adversarial constructions, distribution shifts, rare combinations, scale extremes. |
| egm-construction | Build structured Evidence Gap Maps — define axes (intervention × outcome or method × domain), place gaps in cells, annotate with evidence density and quality. |
| evaporating-cloud | Model conflicts as Goldratt's Evaporating Cloud — expose hidden assumptions behind opposing needs to dissolve the conflict. |
| evidence-grading | Assess evidence quality using GRADE/SOE framework. Rates certainty level and identifies downgrade reasons. |
| evidence-mapping | Systematic evidence map construction — search, classify, locate gaps, visualize. Combines concept-matrix-construction, gap-keyword-extraction, evidence-grading, and egm-construction SOPs. |
| evidence-synthesis | Synthesize multi-source evidence into structured argumentation. Weaves findings from literature, web, and analysis into coherent evidence maps with explicit strength ratings. |
| failure-clustering | Group observed failures by mechanism (not symptom), identify common triggers per cluster, estimate frequency and severity. |
| failure-mode-analysis | Systematically catalog failure modes — generate edge cases, observe failures, cluster by mechanism, identify triggers and frequency. |
| failure-mode-cataloging | Systematic failure mode cataloging — generate boundary inputs, observe failures, cluster by mechanism, identify triggers, estimate frequency. |
| false-gap-filtering | Detect false gaps — search failures, already-solved gaps, and inherently unanswerable questions masquerading as research gaps. |
| five-whys-drilling | Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon to actionable root cause. Each level verified against evidence. |
| fragility-flagging | Identify which specific assumption changes cause conclusion divergence. Rates fragility severity and plausibility of alternatives. |
| gap-analysis | Gap Analysis Campaign — identify, classify, validate, and prioritize research gaps via systematic evidence mapping. 5 strategies (gap-identification, gap-classification, gap-validation, gap-prioritization, gap-synthesis), 3 tactics, 12 subagent SOPs. |
| gap-classification | Classify identified gaps using Miles 7-type taxonomy and AHRQ 4-reason framework. Determines gap type (theoretical, methodological, empirical, etc.) and root cause of gap existence. |
| gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| gap-keyword-extraction | Extract gap-indicating sentences and phrases from papers/reviews. Identifies linguistic markers of research gaps (e.g., "remains unclear", "has not been explored", "limited understanding"). |
| gap-prioritization | Score and rank validated gaps on importance, feasibility, novelty, and urgency. Multi-criteria decision analysis with stakeholder confirmation. |
| gap-synthesis | Compile all gap analysis intermediate products into a coherent final report with executive summary, detailed findings, and research agenda. |
| gap-synthesis-strategy | Compile all gap analysis products into a coherent final report with evidence gap maps, research agenda, and concept matrices. |
| gap-typology-classification | Classify gaps using Miles 7-type taxonomy (theoretical, methodological, empirical, population, practical, knowledge void, evidence gap). |
| gap-validation | Validate gap authenticity via cross-database verification, temporal sensitivity testing, and false-gap filtering. Ensures gaps are genuine absences, not search artifacts. |
| governing-variable-surfacing | Apply Argyris framework to identify governing variables — the unstated rules driving behavior in a research field. |
| hmw-formulation | Generate "How Might We" questions at different scope levels (narrow, medium, broad). Ensures each is actionable without being prescriptive. |
| insight | Insight Campaign — deep root-cause analysis of why research gaps persist. 5 strategies (root-cause-drilling, stakeholder-mapping, tension-mining, question-reformulation, assumption-audit), 4 tactics, 13 subagent SOPs. |
| interaction-detection | Detect and characterize significant parameter interactions from Sobol decomposition results. |
| ishikawa-decomposition | Decompose problems into 6M categories (Methodology, Data, Theory, Measurement, Researchers, Environment) via fishbone diagram analysis. |
| jtbd-mapping | Map stakeholder Jobs-to-be-Done — functional, emotional, and social jobs for each affected party. Identifies unserved jobs as opportunity signals. |
| lateral-escape | de Bono lateral escape sequence — identify dominant idea, generate provocations (escape/reversal/exaggeration/distortion), follow consequences to extract new framings. Breaks paradigm lock-in. |
| monte-carlo-sampling | Design and execute Monte Carlo sampling strategy for uncertainty propagation through a model. |
| morris-screening | Morris method screening — compute elementary effects to quickly identify important vs unimportant parameters. |
| multi-criteria-scoring | Score gaps on multiple dimensions (importance, feasibility, novelty, urgency, impact) using weighted multi-criteria decision analysis. |
| multi-model-convergence | Wimsatt-style multi-method cross-validation — enumerate assumptions, generate alternative models, compare results, flag divergences. |
| multi-perspective-reframing | Apply CATWOE from multiple stakeholder viewpoints and reframing matrix to reveal aspects invisible from the dominant perspective. |
| multi-stakeholder-simulation | Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis. |
| multi-worldview-comparison | Multi-worldview comparison — CATWOE from multiple perspectives, reframing matrix across professional lenses, identify overlooked framings. Reveals what single-perspective analysis misses. |
| negation-definition | Define strongest plausible alternatives (negations) for each assumption to enable perturbation analysis. |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| parameter-screening | Quick Morris method screening to identify which parameters have large effects and which can be safely ignored. |
| polarity-mapping | Map unresolvable tensions as Johnson polarities — 4 quadrants (positive/negative of each pole), early warnings, action steps for managing rather than solving. |
| prioritization-scoring | Multi-dimensional gap scoring and ranking — define criteria, score, weight, rank, sensitivity-check. Combines multi-criteria-scoring, stakeholder-confirmation, and feasibility assessment. |
| problem-reformulation | Problem Reformulation Campaign — question the problem itself. Escape dominant ideas, reframe from multiple perspectives, apply dialectical inquiry, assess wickedness, discover appreciative alternatives. 5 strategies, 3 tactics, 10 subagent SOPs. |
| provocation-generation | Generate de Bono lateral thinking provocations to challenge dominant ideas using escape, reversal, exaggeration, and distortion. |
| question-reformulation | Reframe research questions using abstraction laddering, HMW formulation, and Socratic probing. Find the most productive level and framing for investigation. |
| re-derivation | Re-derive conclusions under a negated assumption, tracking where the derivation diverges from the original. |
| reformulation-synthesis | Compile all problem reformulation analyses into a coherent report with a recommended new problem definition. |
| reframing-matrix | Reframe the problem from 4 professional perspectives to reveal what each discipline would focus on. |
| robustness-testing | Test conclusion robustness via multi-model convergence — enumerate assumptions, generate alternatives, compare results, flag fragile conclusions. |
| root-cause-drilling | Drill from surface symptoms to root causes via 5 Whys, Ishikawa decomposition, and Current Reality Trees. Validates each causal link with literature evidence. |
| salience-classification | Classify stakeholders by Mitchell et al. framework (Power, Legitimacy, Urgency). Assigns salience category and identifies systematically excluded parties. |
| scaling-frontier | Analyze behavior across scales — detect regime changes, identify capacity limits, fit scaling laws within regimes. |
| scaling-regime-detection | Detect regime changes in scaling behavior — breakpoints where behavior qualitatively shifts, mechanisms behind transitions. |
| screening-then-decomposition | Two-phase sensitivity — Morris quick screening to eliminate unimportant factors, then Sobol precise decomposition on survivors. Efficient allocation of analytical effort. |
| sensitivity-analysis | Sensitivity Analysis Campaign — identify which assumptions are most critical by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition, assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics, 11 subagent SOPs. |
| sensitivity-synthesis | Synthesize all sensitivity analysis results into a coherent report with prioritized recommendations. |
| sobol-decomposition | Sobol variance decomposition — compute first-order and total-order sensitivity indices for precise variance attribution. |
| socratic-probing | Apply 6 types of Socratic questions to test claims and assumptions. Exposes weaknesses and strengthens reasoning. |
| stakeholder-confirmation | Simulate stakeholder perspectives to validate gap priorities. Assesses gap value from researcher, practitioner, funder, and end-user viewpoints. |
| stakeholder-mapping | Map all affected parties using CSH 12-question framework, identify jobs-to-be-done, classify by salience. Reveals whose perspective is systematically excluded. |
| systematic-perturbation | Multi-axis systematic perturbation — define variation axes, perturb along each, measure degradation, construct validity envelope. |
| temporal-sensitivity-testing | Test whether a gap persists across different time windows (2/5/10 years). Determines if gap is narrowing, widening, or stable over time. |
| tension-mining | Identify opposing forces that keep gaps open. Uses evaporating cloud to expose hidden assumptions behind conflicts and polarity mapping for unresolvable tensions. |
| uncertainty-cascade | Uncertainty cascade propagation — assign input distributions, sample via Monte Carlo, propagate through model, analyze output distribution, identify critical paths. Maps how input uncertainty flows to output uncertainty. |
| uncertainty-propagation | Propagate input uncertainties through the model via Monte Carlo sampling. Identifies which input uncertainties contribute most to output uncertainty. |
| validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| validity-envelope-mapping | Map multi-dimensional validity envelopes — define variation axes, perturb systematically, measure degradation, construct boundary surface. |
| variance-decomposition | Sobol variance decomposition — compute first-order and total-order sensitivity indices to quantify each parameter's contribution to output variance. |
| variation-axis-definition | Identify orthogonal axes along which a method's validity might vary. Ensures axes are independent, measurable, and span the relevant parameter space. |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| wickedness-assessment | Apply Rittel's 10 criteria to determine if the problem is tame, complex, or wicked, and adjust research strategy accordingly. |
| wickedness-scoring | Score a problem against Rittel's 10 criteria to determine if it is tame, complex, or wicked. |

## hypothesis-formation (72 skills)

| Skill | Description |
|-------|-------------|
| abductive-hypothesis-generation | "Strategy: 面对异常的最佳解释推理" |
| ahp-weighting | "SOP: 使用 AHP 层次分析法确定评分维度权重，输出权重向量" |
| ahrq-picme-assessment | "SOP: 使用 AHRQ PiCMe 框架对研究 gap 进行 6 维度系统评估" |
| anomaly-characterization | "SOP: 描述和分类无法被现有理论解释的异常现象" |
| anomaly-driven-abduction | "Tactic: 归纳/溯因路径——描述异常现象，生成候选解释，按可信度排序" |
| answering-sequence-design | "SOP: 设计子问题的最优回答顺序" |
| boundary-condition-specification | "SOP: 指定假设成立的边界条件" |
| comparative-formulation | "Strategy: 构建对比性研究问题 — A vs B 的系统化比较" |
| competing-hypothesis-construction | "Strategy: 为同一现象构建多个竞争假设" |
| competing-hypothesis-generation | "SOP: 为同一现象生成机制上不同的竞争假设" |
| competing-hypothesis-matrix | "Tactic: 多假设管理——生成竞争假设，设计区分性预测，构建结构化比较矩阵" |
| consistency-check | "SOP: 检验 pairwise 判断矩阵的传递一致性，识别不一致项并建议修正" |
| decomposition-formulation | "Strategy: 将复杂研究问题分解为可独立回答的子问题层级" |
| deductive-hypothesis-generation | "Strategy: 从现有理论演绎推导假设" |
| dependency-mapping | "SOP: 映射子问题间的依赖关系" |
| discriminating-prediction-design | "SOP: 设计能区分竞争假设的关键预测和观察方案" |
| eclipse-application | "SOP: 应用 ECLIPSE 框架结构化混合方法研究问题" |
| evidence-based-prioritization | "Strategy: 基于证据强度的 AHRQ PiCMe 评估——用文献证据质量驱动 gap 优先级" |
| explanation-generation | "SOP: 为异常现象生成候选解释列表" |
| falsifiability-audit | "Tactic: 假设质量保证——检验可证伪性，修复不合格假设，完成操作化与边界条件规范" |
| falsifiability-check | "SOP: 检验假设是否满足可证伪性标准" |
| feasibility-constrained-formulation | "Strategy: 在资源约束下重塑研究问题 — pragmatic 调整保持核心价值" |
| feasibility-scoring | "SOP: 评估研究 gap 的可攻击性，识别瓶颈并输出可行性评分" |
| finer-criteria-check | "SOP: FINER 5 项标准逐项检验研究问题质量" |
| framework-guided-formulation | "Strategy: 选择 RQ 框架（PICO/SPIDER/SPICE/ECLIPSE）并系统应用" |
| framework-matching | "SOP: 根据研究类型匹配最适合的 RQ 框架" |
| framework-selection-and-application | "Tactic: 选择最适合的 RQ 框架并系统应用" |
| gap-normalization | "SOP: 统一不同来源的 gap 格式为标准 GapRecord" |
| gap-pairwise-judgment | "SOP: 对两个 gap 进行逐标准相对优先级判断，输出偏好结果" |
| gap-prioritization | Score and rank validated gaps on importance, feasibility, novelty, and urgency. Multi-criteria decision analysis with stakeholder confirmation. |
| hypothesis-comparison-matrix | "SOP: 构建竞争假设的多维度对比矩阵" |
| hypothesis-formulation | "Campaign: 将 insight 和 gap 转化为结构化的可测试假设" |
| hypothesis-operationalization | "Strategy: 将 working hypothesis 精确化为可测试形式" |
| hypothesis-synthesis | "SOP: 综合所有中间产物，产出最终结构化假设集" |
| impact-scoring | "SOP: 评估研究 gap 的潜在影响力，识别受益方并输出影响力评分" |
| importance-scoring | "SOP: 评估研究 gap 的学术与实践重要性，输出 1-5 分及依据" |
| inductive-hypothesis-generation | "Strategy: 从数据/观察归纳提炼假设" |
| mechanism-extraction | "SOP: 从理论中提取因果机制链" |
| multi-criteria-ranking | "Strategy: 多维度加权评分排序——将 gap 分解为独立子问题后重组为优先级列表" |
| novelty-scoring | "SOP: 评估研究 gap 的新颖性潜力，识别差异化方向并输出评分" |
| operationalization | "SOP: 将抽象概念操作化为可测量的指标和方法" |
| pairwise-comparison | "Tactic: 通过相对比较而非绝对评分对 gaps 进行排序，适用于难以量化的场景" |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| pico-application | "SOP: 应用 PICO/PICOTS 框架结构化研究问题" |
| plausibility-ranking | "SOP: 对候选解释按合理性进行多维度加权排序" |
| portfolio-optimization | "Strategy: gap 组合视为投资组合——用风险/收益/多样性优化选出最优 gap 组合" |
| priority-sensitivity-testing | "Tactic: 扰动评分权重，检验 gap 排序对权重选择的稳健性" |
| priority-synthesis | "SOP: 综合所有评分数据产出最终 gap 优先级列表及攻击路径建议" |
| quality-gate-check | "Shared SOP: 通用质量门检查（格式完整性、逻辑一致性）" |
| question-refinement-loop | "Tactic: 迭代精化研究问题直到通过 FINER 5 项标准" |
| question-synthesis | "SOP: 综合所有中间产物产出最终研究问题集" |
| rapid-triage | "Strategy: 快速粗筛——两轮过滤将大量 gaps 压缩为可精排的候选集" |
| relationship-specification | "SOP: 指定变量间关系的方向与形式" |
| research-question | "Campaign: 将假设细化为精确的、框架化的研究问题" |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scope-assessment | "SOP: 评估研究问题的范围是否合适（太宽/合适/太窄）" |
| scope-calibration | "Strategy: 调整研究问题范围 — zoom in/out 直到范围合适" |
| scoring-matrix-construction | "Tactic: 编排多维度评分 SOP，为所有 gaps 构建综合评估矩阵" |
| spice-application | "SOP: 应用 SPICE 框架结构化评估研究问题" |
| spider-application | "SOP: 应用 SPIDER 框架结构化定性研究问题" |
| stakeholder-weighted-ranking | "Strategy: 按利益相关者视角加权——同一 gap 在不同视角下权重不同，最终取共识排序" |
| sub-question-decomposition | "Tactic: 将主问题分解为可独立回答的子问题层级" |
| sub-question-generation | "SOP: 将主研究问题分解为可独立回答的子问题" |
| success-criteria-definition | "SOP: 为研究问题定义可测量的成功标准" |
| theory-identification | "SOP: 识别与研究gap相关的理论框架" |
| theory-mechanism-extraction | "Tactic: 演绎路径核心——从理论出发提取机制、变量与关系，生成假设候选" |
| variable-identification | "SOP: 识别变量及其在假设中的角色" |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| weight-perturbation | "SOP: 扰动权重检验 gap 排序稳定性，输出稳定性判定" |

## creative-ideation (188 skills)

| Skill | Description |
|-------|-------------|
| ablation-brainstorm | Remove components one by one, observe system changes to reveal hidden dependencies and generate ideas from structural gaps. |
| ablation-execution | Remove components one by one from a system, record the response/impact of each removal. |
| abstraction-extraction | Extract abstract principles from concrete domain cases. Strips domain-specific details to reveal transferable mechanisms. |
| abstraction-ladder | Perform bisociation at multiple abstraction levels |
| abstraction-to-design | "Abstract biological principle to design principle. Bridge from biology to engineering." |
| alternatives-generation | Generate alternatives for every known approach — ensure no approach goes unchallenged. |
| analogical-transfer | Systematic structure-mapping from source to target domain (Gentner). Identify relational correspondences and transfer higher-order constraints. |
| analogy-chain | Chain analogies to deeper levels (3-5 layers). Each layer reveals new aspects and insights not visible at the surface. |
| analogy-extraction | Extract transferable structural principles from source domains. Orchestrates source identification → abstraction → structural mapping → transfer validation. |
| analogy-quality-assessment | Assess analogy depth (surface/structural/systemic). Determines whether an analogy warrants transfer investment. |
| anti-benchmark | Challenge industry best practices' hidden assumptions. Deconstruct benchmarks to reveal unexamined constraints. |
| assumption-destruction | Assumption Destruction Campaign — open new solution spaces by negating, reversing, and challenging fundamental assumptions. |
| assumption-enumeration | Systematically identify all assumptions in a method/model — structural, parametric, distributional, and scope assumptions. |
| assumption-perturbation | One-at-a-time assumption perturbation — extract assumptions, define negations, re-derive conclusions under each negation, measure sensitivity. Identifies which assumptions are load-bearing. |
| assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| axiom-negation | Identify and suspend fundamental assumptions via de Bono PO. Systematically negate axioms to reveal hidden solution spaces. |
| benchmark-challenge | Identify and negate benchmark assumptions. Deconstruct best practices to reveal hidden constraints and open new spaces. |
| benchmark-inventory | Identify and catalog all relevant benchmarks in target domain |
| benchmark-sweep | Systematically scan all known solutions, identify gaps in coverage and unexplored regions of the solution space. |
| biological-function-mapping | "Map technical functions to biological systems. Orchestrates problem-biologization → organism-discovery → functional-model-biology." |
| biological-strategy-extraction | "Extract strategy principles from organisms. Identify mechanism-level details of how biological systems achieve their function." |
| biologize-and-discover | "Biomimicry Design Spiral: Define→Biologize→Discover→Abstract→Emulate. Translate technical challenges into biological questions and find nature's solutions." |
| biomimicry | Biomimicry Campaign — discover transferable solutions from biological systems via Design Spiral, BioTRIZ, functional analogy, ecosystem patterns, and evolution strategies. |
| biomimicry-synthesis | "Synthesize all biomimicry outputs into a structured idea report. Integrate biological strategies, design principles, and technical solutions." |
| biotriz-principle-selection | "Select applicable BioTRIZ principles for a given contradiction. Map to biological cases." |
| biotriz-resolution | "BioTRIZ: biological 40 principles + bio contradiction matrix. Resolve technical contradictions using biological inventive principles." |
| bisociation-network-construction | Build multi-domain bridging concept network. Creates a network of collision points between multiple thinking matrices. |
| blend-completion | Complete blend with background knowledge |
| blend-composition | Compose new connections in blended space |
| blend-construction | Construct complete 4-space blends with emergent structure. Orchestrates input-space-construction → generic-space-extraction → blend-composition. |
| blend-elaboration | Run blend as mental simulation |
| bridge-validation | Validate analogy depth and transfer viability. Ensures only deep structural analogies (not surface-level similarities) proceed to transfer. |
| challenge-operation | "Non-threatening 'Why?' questioning of current practices (de Bono Challenge)" |
| challenge-questioning | "Non-threatening 'Why?' questioning of current practices to reveal historical accidents vs. genuine constraints." |
| combination-evaluation | Evaluate new combinations for feasibility and novelty |
| combination-mapping | Systematically enumerate parameter dimensions and generate viable combinations. Orchestrates parameter extraction → value enumeration → compatibility assessment → synthesis. |
| combinatorial-creativity | Combinatorial Creativity Campaign — produce emergent concepts via concept blending, multi-level bisociation, and function combination (Fauconnier-Turner) |
| combinatorial-synthesis | Synthesize all combinatorial creativity outputs |
| competitor-simulation | Competitor perspective — design strategies to defeat this solution, then use attack vectors to improve it. |
| component-decomposition | Decompose system into functional components, identify dependencies, and surface trimming candidates. |
| component-surgery | Component-level surgical operations (subtract/multiply/divide/unify/redirect) from Systematic Inventive Thinking (SIT). |
| compressed-conflict | Generate compressed conflicts (oxymorons) from problem contradictions and extract concrete idea directions from the symbolic tension. |
| concept-blending | "Fauconnier-Turner 4-space model: Generic + Input1 + Input2 → Blended Space" |
| concept-fan | "Expand from purpose to concepts to directions to ideas (de Bono Concept Fan)" |
| concept-fan-expansion | Expand concept fan from purpose through concepts to directions to ideas (de Bono Concept Fan). |
| concept-hierarchy | Build concept levels from purpose through concepts to ideas, with escape and fractionation at each level. |
| consistency-checking | Pairwise consistency evaluation to reduce solution space by identifying and removing inconsistent combinations. |
| consistency-pair-evaluation | Evaluate pairwise value consistency (logical/empirical/normative) |
| constraint-driven-ideation | Inject extreme constraints to force innovation — impossibility breeds creativity. |
| constraint-injection | Inject artificial constraints to force creative divergence. Generates and applies constraints (resource, time, material, audience, scale) to existing ideas to produce variants. |
| constraint-protocol | Inject constraints → force creative response → extract transferable principles. Orchestrates constraint injection, response generation, and principle extraction. |
| constraint-response | Generate creative solutions under extreme constraints — no "impossible" allowed, find a way. |
| constructive-rebellion | Build constructive alternatives from destructive negation. Transform violated assumptions into viable innovation directions. |
| contradiction-identification | Identify technical and physical contradictions in a system through functional modeling and matrix analysis. |
| contradiction-matrix-lookup | Query the 39x39 TRIZ contradiction matrix to find recommended inventive principles for a given technical contradiction. |
| coverage-analysis | Systematic coverage evaluation pipeline — benchmark inventory, method-problem crossing, and intersection evaluation to map explored vs unexplored solution space. |
| coverage-gap-detection | Detect uncovered regions in the solution space, producing a prioritized gap list. |
| cross-consistency-analysis | "CCA: pairwise consistency checking to reduce solution space 90-99%" |
| cross-domain-discovery | Cross-Domain Discovery Campaign — find transferable mechanisms from unrelated fields via bisociation, analogical transfer, random stimulus, and forced bridging |
| cross-domain-synthesis | Synthesize all cross-domain findings into a structured idea report. Integrates outputs from all strategies and SOPs. |
| dependency-identification | Identify critical dependencies from ablation results, producing a dependency graph and highlighting critical components. |
| design-by-analogy | "Complete DBA process: problem reframe → source search → map → transfer → adapt. Full Design-by-Analogy methodology for systematic analogical design." |
| design-space-exploration | Parametric variation + constraint satisfaction combinatorial search |
| design-space-mapping | Visualize explored/unexplored regions of solution space |
| design-space-visualization | Generate structured description of design space |
| destruction-synthesis | Synthesize all assumption destruction outputs into structured destructive innovation report. |
| direct-analogy | Find structurally similar systems in nature/technology/society. Map structural parallels to generate transferable solution principles. |
| direct-analogy-generation | Find direct analogies from nature/tech/society that share structural properties with the problem. Produces analogy list with structural mappings. |
| domain-divergence | Scan and select maximally diverse source domains. Ensures creative search covers genuinely unrelated fields with high transfer potential. |
| domain-scanning | Scan distant domains for transferable principles. Uses web-search and paper-overview to identify analogous solutions in unrelated fields. |
| ecosystem-pattern | "Extract ecosystem-level organization patterns (symbiosis, emergence, resilience) as design templates for complex systems." |
| ecosystem-pattern-extraction | "Extract ecosystem-level organization patterns (symbiosis, emergence, cycles, resilience)." |
| emergence-detection | Detect and validate emergent properties from combinations. Orchestrates emergent-property-identification → blend-elaboration. |
| emergent-property-hunting | Seek properties that emerge from combination (non-additive) |
| emergent-property-identification | Identify non-additive properties from combinations |
| emulation-generation | "Generate technical solutions emulating biological strategies. Bridge from design principle to concrete implementation." |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |
| escape-technique | Identify dominant thinking pattern and escape it via deliberate pattern-breaking. |
| evaluation-filtering | Multi-dimensional evaluation and tiered filtering of generated ideas. Orchestrates novelty assessment → feasibility check → ranking → selection. |
| evolution-mechanism-transfer | "Map evolution mechanisms to design operations. Translate selection, mutation, drift, radiation into design operators." |
| evolution-strategy | "Use evolution mechanisms (selection, mutation, radiation) as design operators for generating and refining solution populations." |
| excursion-departure | Leave the problem entirely and explore an unrelated domain. Produces excursion domain discoveries for later force-fitting. |
| excursion-method | Full 8-stage Gordon-Prince excursion process. Deliberate departure from the problem into unrelated domains, then force-fit discoveries back. |
| excursion-orchestration | Orchestrate the excursion sequence — departure into unrelated domain, force-fit discoveries back to problem, launch springboard ideas. |
| facet-bisociation | Bridge two unrelated thinking matrices via Koestler bisociation. Identify independent frames of reference and force collision to produce creative insight. |
| factorial-ideation | "DOE thinking: identify factors, define levels, and explore combinations to systematically cover the design space." |
| factor-level-design | Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration. |
| failure-driven-generation | Generate targeted solutions for each identified failure mode, ensuring every failure has at least one proposed mitigation. |
| failure-mode-cataloging | Systematic failure mode cataloging — generate boundary inputs, observe failures, cluster by mechanism, identify triggers, estimate frequency. |
| failure-taxonomy | Catalog all failure modes in a domain, classify them systematically, and generate targeted solutions for each failure type. |
| fantasy-analogy | Wish-fulfillment thinking — ignore physical laws for ideal solution. Use unconstrained imagination to reveal what the problem truly needs. |
| fantasy-wish | Unconstrained wish-fulfillment ideation. Ignore all physical laws to imagine the ideal solution, then identify realization directions. |
| forced-bridge-construction | Force connections between unrelated technologies. Deliberately construct bridges where none naturally exist to discover novel integration possibilities. |
| forced-connection | Force connection between two unrelated concepts. Deliberately construct bridging paths where no natural connection exists. |
| force-fit | Force-fit excursion discoveries back to the original problem. Deliberately create connections between unrelated findings and the challenge. |
| fractionation | Split concepts into smaller units and recombine them differently to produce novel structures. |
| functional-analogy | "Map technical functions to biological functions, find organisms solving equivalent problems. Deep functional matching across domains." |
| functional-model-biology | "Build biological system functional model. Map energy, matter, and information flows." |
| function-combination | "TRIZ function analysis: function-level recombination and redistribution" |
| function-model-construction | Build substance-field functional model of a system, annotating useful, harmful, insufficient, and excessive interactions. |
| function-redistribution | Redistribute functions across different components |
| function-trimming | Remove components while preserving function via TRIZ trimming methodology. Simplify systems by redistributing functions. |
| gap-driven-generation | Generate solutions targeting specific coverage gaps — detect gaps, generate failure-driven solutions, and design factor-level experiments. |
| general-morphological-analysis | "Ritchey GMA: complete iterative morphological process" |
| generic-space-extraction | Extract shared abstract structure from two input spaces |
| green-hat-session | Structured creative thinking in Six Hats Green Hat mode — pure creative output with judgment suspended. |
| idea-synthesis | Synthesize diverse ideas into coherent solution concepts. Combines fragments from multiple ideation passes into structured, actionable ideas with clear mechanism descriptions. |
| input-space-construction | Build input spaces for two source concepts |
| intersection-evaluation | Evaluate exploration status of each cell in a method×problem matrix, annotating as explored, partial, or unexplored. |
| inversion-extraction | Extract constructive insights from worst solutions. Transform failure analysis into innovation directions. |
| inversion-protocol | Reverse statements → extract insights → build constructive alternatives. Systematic inversion pipeline from negation to innovation. |
| lateral-synthesis | Synthesize all lateral thinking intermediate outputs into a structured idea report. |
| lateral-thinking | Lateral Thinking Campaign — escape logical thinking tracks via PO/movement, random entry, concept fan, challenge, and six hats (de Bono) |
| life-principles-application | "Apply life's principles as design constraints. Orchestrates ecosystem-pattern-extraction → evolution-mechanism-transfer → abstraction-to-design." |
| matrix-construction | Build n-dimensional morphological matrix |
| method-problem-crossing | Build method×problem cross-reference matrix showing which methods have been applied to which problems. |
| method-problem-matrix | Cross method×problem matrix, find unexplored intersections where known methods have not been applied to known problems. |
| morphological-exploration | Morphological Exploration Campaign — systematic dimension-combination enumeration to discover unexplored solution spaces via Zwicky box, CCA, and GMA |
| morphological-synthesis | Synthesize all morphological exploration outputs |
| movement-extraction | Extract constructive directions from provocations via 4 movement types (moment-to-moment, principle, focus difference, positive aspects). |
| movement-operation | Extract constructive directions from PO provocations using 4 movement types (moment-to-moment, principle, focus difference, positive aspects). |
| multi-level-bisociation | Simultaneous concept collision at multiple abstraction levels |
| novelty-scoring | "SOP: 评估研究 gap 的新颖性潜力，识别差异化方向并输出评分" |
| novice-perspective | Novice perspective — question the 'obvious' by adopting deliberate ignorance to reveal hidden complexity. |
| organism-discovery | "Find organisms solving similar problems. Search across kingdoms for biological champions." |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| parameter-identification | Identify the key parameters/dimensions of a problem space. Produces a structured parameter list with value ranges for morphological analysis. |
| parameter-variation | Systematic one-factor-at-a-time parameter sweep |
| path-generation | Generate combination paths through consistent space |
| personal-analogy | Empathic identification — become the system/component. First-person embodiment to discover hidden constraints and opportunities. |
| personal-identification | First-person empathic identification with a system or component. Produces experience description and design insights from embodiment. |
| perspective-forcing | Perspective Forcing Campaign — discover hidden solutions by systematically switching viewpoints via roles, six hats, temporal projection, and constraint injection |
| perspective-rotation | Rotate through reviewer/practitioner/theorist/time-machine/novice perspectives systematically. Ensures comprehensive viewpoint coverage. |
| perspective-synthesis | Synthesize all perspective outputs into a structured multi-perspective idea report. |
| po-provocation | Generate PO (Provocative Operation) statements per de Bono's lateral thinking. Creates deliberately illogical provocations to escape dominant thinking patterns. |
| practitioner-hat | Engineer perspective — assess buildability, cost, timeline, and integration challenges. |
| problem-biologization | "Restate technical problem as biological question. Translate engineering challenges into nature's language." |
| provocation-and-movement | "PO + Movement: generate provocations then extract useful directions (4 movement types)" |
| provocation-generation | Generate de Bono lateral thinking provocations to challenge dominant ideas using escape, reversal, exaggeration, and distortion. |
| random-entry | "Random word/concept as thinking entry point (de Bono Random Entry)" |
| random-paper-entry | Select random paper facet as creative stimulus. Uses genuine randomness in paper selection to break domain fixation. |
| random-stimulus-entry | Random word/paper/concept as thinking entry point. Use genuine randomness to escape fixation and open unexpected solution paths. |
| random-word-stimulus | Use random word/concept injection as creative stimulus. Selects random concepts and forces connection to the problem space, generating unexpected solution paths. |
| recombination-architecture | Reassemble decomposed fragments into novel structures through systematic recombination of components. |
| recombination-generation | Reassemble decomposed system fragments into novel structural arrangements that create emergent value. |
| reversal-generation | Systematically reverse positive statements to generate creative inversions. Produces reversed statements with initial associations. |
| reverse-brainstorming | How to make it worse? → reverse for solutions. Generate anti-solutions then invert to discover novel approaches. |
| reviewer2-hat | Hostile reviewer perspective — find fatal flaws, logical gaps, and missing evidence in a solution. |
| role-based-ideation | Role-play as reviewer/practitioner/theorist/novice/competitor to generate diverse perspectives on a solution. |
| sacred-cow-hunting | Find and challenge domain's unquestioned beliefs. Systematic identification and productive violation of dogma. |
| sacred-cow-identification | Find domain's unquestioned beliefs. Systematic identification of dogma that constrains innovation. |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scamper-divergence | Execute SCAMPER 7 operators on a target solution. Subagent self-selects best 2-3 operators for deepest exploration. |
| scamper-transformation | 7 operators (Substitute/Combine/Adapt/Modify/Put/Eliminate/Reverse) for systematic transformation of existing solutions. |
| separation-principle | Apply time/space/condition/scale separation to resolve physical contradictions where the same parameter must satisfy opposing requirements. |
| six-hats-ideation | "Green Hat focused creative thinking within Six Hats framework" |
| six-hats-rotation | Complete Six Hats rotation (White→Red→Black→Yellow→Green→Blue) to force systematic perspective diversity. |
| solution-space-reduction | Apply CCA to remove inconsistent combinations |
| springboard-launch | Convert analogy insights into concrete feasible solutions. Transform abstract connections into actionable mechanisms. |
| stakeholder-simulation | Simulate user/engineer/investor/regulator/society perspectives to surface hidden requirements and opportunities. |
| stepping-stone | Use impractical ideas as stepping stones to reach practical solutions (de Bono Stepping Stone technique). |
| structural-deconstruction | Decompose systems into components and reassemble via SCAMPER, SIT, TRIZ, and recombination. Campaign orchestrating 5 strategies for systematic structural transformation. |
| structural-mapping | Map source→target structural correspondences. Identifies corresponding, missing, and extra elements between domains. |
| structural-synthesis | Synthesize all structural transformation outputs into a coherent, ranked idea report with lineage tracking. |
| surgery-operation | Execute component surgery operations (subtract/multiply/divide/unify/redirect) from Systematic Inventive Thinking. |
| symbolic-analogy | Compress core contradiction into poetic imagery/oxymoron. Use compressed conflicts to reveal hidden solution directions. |
| symbolic-compression | Compress problem contradiction into 2-3 word oxymoron. Produces oxymorons with interpretation directions for each. |
| synectics | Synectics Campaign — systematic use of analogy and metaphor for breakthrough associations via Gordon's 4 analogy types and excursion method. |
| synectics-synthesis | Synthesize all synectics outputs into a structured idea report. Combines results from all analogy types and excursion processes. |
| systematic-enumeration | Systematic Enumeration Campaign — exhaustive coverage analysis to discover overlooked solution spaces via benchmark sweep, method-problem matrix, ablation, and failure taxonomy |
| temporal-projection | View problem from 5yr/50yr/500yr future, backcast to generate temporally-informed creative solutions. |
| theorist-hat | Theorist perspective — assess theoretical foundations, formal rigor, and formalization opportunities. |
| time-machine | Temporal projection — view a solution from future/past time horizons to generate temporally-informed insights. |
| transfer-adaptation | Adapt transferred principle to target problem constraints. Produces concrete adapted solutions from abstract principles. |
| trimming-execution | Progressively remove components from a system while verifying function preservation through redistribution. |
| triz-contradiction-resolution | Resolve technical and physical contradictions via TRIZ 40 inventive principles and separation methods. |
| triz-principle-application | Select inventive principles from the contradiction matrix and generate concrete solutions for identified contradictions. |
| value-enumeration | Enumerate 3-5 values per parameter including extremes |
| vital-relation-mapping | Map 15 vital relations between concepts |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| white-space-detection | Identify matrix regions not covered by existing methods |
| white-space-identification | Identify unexplored viable regions in the morphological matrix where no existing methods operate. |
| worst-case-design | Design the worst possible solution. Deliberate failure engineering to reveal hidden constraints and inversion opportunities. |
| worst-method-inversion | Design worst possible solution → extract insights → invert. Deliberate failure design as creative catalyst. |
| zwicky-box-construction | "Classic Zwicky box: parameter identification → value enumeration → matrix construction" |

## convergence (120 skills)

| Skill | Description |
|-------|-------------|
| adaptive-pair-selection | Iteratively select maximally informative pairs, execute comparisons, update ratings, and check convergence until ranking stabilizes. |
| adversarial-debate-protocol | Structured debate protocol that constructs an advocate, deploys critic attacks, and renders a judge verdict through iterative rounds. |
| advocate-construction | Construct the strongest possible case for a rejected candidate or counter-position. |
| aggregation-method | Aggregate multiple ranking ballots into a consensus ranking using a specified social choice method. |
| alternative-scoring | Score each candidate alternative against all criteria to produce a score matrix. |
| appropriateness-bounding | Establish acceptability standards through RAND/UCLA Appropriateness Method or Consensus Conference protocols. |
| argument-crystallization | Distill the strongest arguments from each perspective through Argument Delphi or Dialectical Delphi methods. |
| argument-extraction | Extract and steel-man the core arguments supporting a given opinion cluster. |
| assumption-challenge | Construct the strongest counter-argument against a specific assumption and propose alternatives. |
| assumption-excavation | Systematic extraction, challenge, and sensitivity analysis of assumptions underlying a decision to identify load-bearing beliefs. |
| assumption-extraction | Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model. |
| ballot-collection | Gather independent ranking ballots from multiple judges or perspectives for a given candidate set. |
| best-option-selection | Select the single best candidate from a set using WSM, TOPSIS, AHP, MAUT, or VIKOR methods. |
| bottleneck-identification | Identify bottleneck dimensions from radar data with severity ranking. |
| category-sorting | Classify candidates into predefined categories using ELECTRE-Tri, FlowSort, AHPSort, or DRSA methods. |
| cluster-analysis | Identify natural opinion clusters from collected judgments and characterize each cluster. |
| coherence-diagnosis | Strategy for auditing preference consistency using Consistency Ratio, cycle enumeration, and mElo to detect and resolve intransitivities. |
| collective-adjudication | Strategy for multi-judge ranking aggregation using Condorcet, Schulze, Borda, Kemeny-Young, and Copeland methods to produce consensus rankings from diverse perspectives. |
| comparative-feasibility-ranking | Compare feasibility across multiple candidates using multi-dimensional radar and weighted feasibility index. |
| comparison-executor | Execute a pairwise comparison between two candidates, producing a judgment with winner, confidence, and reasoning. |
| conclusion-sensitivity | Map which assumptions are load-bearing by assessing how the conclusion changes if each assumption fails. |
| conjunctive-filter | Apply conjunctive screening rules to eliminate candidates that fail any threshold. |
| consensus-classification | Classify items as consensus or dissensus at a given threshold. |
| consensus-measurement | Compute consensus score from collected judgments using the appropriate statistical method. |
| consensus-synthesis | Synthesize all rounds into a final consensus report documenting agreements, dissent, and process. |
| consistency-audit-loop | Detect preference cycles, localize inconsistent judgments, request corrections, and recompute ratings until consistency threshold is met. |
| constraint-classification | Classify constraints into hard constraints, soft constraints, and assumptions. |
| constraint-drilling | Identify constraints, classify them by type and severity, assess removability, and design removal paths for removable constraints. |
| constraint-identification | Find blockers and showstoppers using TOC, TRIZ contradiction analysis, and Pre-mortem techniques. |
| constraint-identification-sop | Identify constraints for a candidate using TOC, TRIZ, and Pre-mortem methods. |
| convergence-check | Evaluate whether the ranking has stabilized by analyzing rating history and computing stability metrics. |
| convergence-distillation | Iterative convergence to a single answer through Classic Delphi, Modified Delphi, or Nominal Group Technique rounds. |
| counter-thesis-construction | Construct the strongest possible counter-argument to the convergence decision using Dialectical Inquiry and Thesis-Antithesis-Synthesis methods. |
| coverage-scoring | Compute coverage completeness, redundancy, and gap severity scores from a coverage map. |
| criteria-interrogation | Challenge the evaluation criteria themselves using Assumption-based Planning, Critical Systems Heuristics, and Boundary Critique to ensure the framework is sound. |
| criterion-definition | Extract evaluation criteria from research goals and candidate alternatives. |
| critic-attack | Attack an advocate's case with multiple arguments rated by severity. |
| cycle-detection | Scan a pairwise comparison matrix for preference cycles and compute transitivity metrics. |
| deliberative-calibration | Strategy for small-N complete pairwise comparison using Bradley-Terry, Thurstone, AHP, and Borda methods to produce calibrated rankings. |
| dimension-assessment | Score a single readiness dimension for a candidate with evidence and gap analysis. |
| disagreement-cartography | Map the structure of disagreement across perspectives using Policy Delphi, Argument Delphi, or SAST methods. |
| disagreement-mapping | Map disagreement structure by collecting judgments, clustering opinions, extracting arguments per cluster, and visualizing fault lines. |
| disagreement-visualization | Produce a structured disagreement map showing clusters, arguments, and fault lines. |
| diversity-maximization | Maximize portfolio diversity and coverage using MAP-Elites, Niche coverage, Maximum dispersion, and Anti-clustering methods. |
| dominance-check | Identify dominated and non-dominated alternatives in a score matrix using Pareto dominance. |
| dynamic-tracking | Strategy for continuous rating updates using Elo, Glicko-2, TrueSkill 2, and Whole-History Rating for live ranking systems and A/B testing. |
| efficient-exploration | Strategy for large-N sparse pairwise comparison using TrueSkill, active learning, and rank centrality to rank 100+ candidates from limited comparisons. |
| feasibility-assessment | Feasibility Assessment Campaign — evaluate whether selected candidates can actually be implemented using TRL, NASSS, Stage-Gate, TRIZ, TOC, and parametric estimation methods. |
| feasibility-synthesis | Synthesize all assessments into a feasibility matrix, recommendation, and risk summary. |
| feedback-distribution | Create anonymized feedback report summarizing group judgment distribution for a given round. |
| full-ranking | Produce a complete ordering of all candidates using PROMETHEE I/II, ELECTRE III, or MAVT methods. |
| futures-calibration | Aggregate probability judgments across perspectives using Real-Time Delphi or prediction market mechanisms. |
| gate-criteria-definition | Define gate criteria and pass thresholds for a specific stage in the Stage-Gate process. |
| gate-judgment | Evaluate a candidate against gate criteria and render GO/KILL/RECYCLE verdict with evidence. |
| inconsistency-localization | Identify which specific comparison pairs are most responsible for preference cycles and inconsistencies. |
| iterative-convergence-round | Execute one full Delphi round — collect judgments, distribute anonymous feedback, measure consensus, decide whether to continue. |
| judge-verdict | Render an impartial verdict on advocate case vs critic attacks with explicit reasoning. |
| judgment-collection | Collect independent judgments from all perspectives on a given question. |
| maturation-pathway-design | Design path to readiness using Stage-Gate, Technology Roadmapping, and milestone planning methods. |
| maturity-diagnosis | Assess current readiness of candidates using TRL 9-level, NASSS 7-dimension, and Innovation Readiness Level frameworks. |
| method-sensitivity-report | Analyze how the choice of MCDA method affects final rankings and identify method-sensitive alternatives. |
| multi-criteria-scoring | Score gaps on multiple dimensions (importance, feasibility, novelty, urgency, impact) using weighted multi-criteria decision analysis. |
| multi-dimensional-readiness-scan | Assess readiness across multiple dimensions, synthesize into radar visualization, and identify bottleneck dimensions. |
| multi-judge-aggregation | Collect independent rankings from multiple judges, aggregate using social choice methods, and identify disagreement hotspots. |
| multi-method-triangulation | Apply 2-3 MCDA methods to the same candidates, compare rankings, and identify method-sensitive options. |
| multi-perspective-attack | Assign distinct perspectives to attack a decision from multiple angles, then synthesize findings into a unified assessment. |
| multi-stakeholder-simulation | Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis. |
| niche-coverage-analysis | Define niches within the solution space, map candidates to niches, score coverage completeness, and identify gaps requiring attention. |
| niche-definition | Define niches and capability areas that a portfolio should cover based on domain structure and objectives. |
| niche-mapping | Map each candidate to the niches it covers, indicating strength of coverage for each assignment. |
| non-compensatory-screening | Eliminate non-qualifying candidates using conjunctive rules, dominance filtering, lexicographic ordering, or veto thresholds. |
| normalization | Normalize a score matrix using a specified method to make scores comparable across criteria. |
| objective-definition | Define optimization objectives, constraints, and trade-off preferences from context and candidate information. |
| optimization-run | Execute multi-objective optimization on candidates to produce a Pareto front of non-dominated solutions. |
| pair-selector | Select the next comparison pairs that maximize information gain given current ratings and comparison history. |
| pairwise-ranking | Pairwise Ranking Campaign — produce global rankings through pairwise comparisons and voting aggregation using Bradley-Terry, Elo, TrueSkill, Condorcet, Borda, Schulze methods. |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| pareto-frontier-construction | Build the Pareto frontier from multi-objective optimization, visualize trade-offs, and select a portfolio from non-dominated solutions. |
| pareto-visualization | Create visual representation of the Pareto frontier showing trade-offs between objectives with narrative explanation. |
| perspective-assignment | Define distinct stakeholder or analytical perspectives with their values, concerns, and evaluation criteria. |
| perspective-attack | Attack a decision from a specific assigned perspective, producing rated arguments and constructive alternatives. |
| portfolio-evaluation-per-scenario | Evaluate a specific portfolio's performance metrics and vulnerabilities under a given scenario. |
| portfolio-optimization | "Strategy: gap 组合视为投资组合——用风险/收益/多样性优化选出最优 gap 组合" |
| portfolio-synthesis | Synthesize all per-scenario evaluations into a final portfolio recommendation with robustness score and actionable guidance. |
| radar-synthesis | Synthesize multiple dimension scores into radar chart data and compute overall readiness. |
| rank-comparison | Compare multiple ranking results to assess agreement and identify divergent items. |
| ranking-synthesis | Produce the final ranking artifact from converged ratings and consistency report. |
| rating-update | Incorporate a new judgment into the rating model and return updated ratings for all candidates. |
| removability-assessment | Assess how removable a constraint is with effort estimate and dependency analysis. |
| removal-path | Design concrete removal steps for a constraint with timeline and resource needs. |
| resource-envelope-estimation | Estimate resources, budget, and timeline using parametric, analogous, and three-point (PERT) estimation methods. |
| resurrection-advocacy | Argue for rejected candidates using Devil's Advocacy, Dialectical Inquiry, and Adversarial Collaboration to ensure elimination was justified. |
| risk-balancing | Balance portfolio risk and return using Markowitz mean-variance, CVaR, Risk parity, and Kelly criterion methods. |
| robustness-under-uncertainty | Select portfolios that perform well across multiple future scenarios using Minimax regret, Robust optimization, Scenario planning, and Info-gap methods. |
| round-decision | Decide whether to continue iterating or stop based on consensus score, round number, and stability. |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scenario-construction | Construct distinct future scenarios spanning key uncertainties for portfolio stress testing. |
| scenario-stress-testing | Construct distinct future scenarios, evaluate portfolio performance under each, and identify vulnerabilities and robustness characteristics. |
| scoring-matrix-construction | "Tactic: 编排多维度评分 SOP，为所有 gaps 构建综合评估矩阵" |
| scoring-synthesis | Synthesize score matrix, rankings, and sensitivity analysis into a final recommendation. |
| screening-then-scoring | First eliminate non-qualifying candidates with non-compensatory rules, then score survivors with full MCDA methods. |
| selection-from-frontier | Select the final portfolio from the Pareto front by applying stakeholder preferences and decision criteria. |
| sensitivity-analysis | Sensitivity Analysis Campaign — identify which assumptions are most critical by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition, assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics, 11 subagent SOPs. |
| staged-gate-evaluation | Define gate criteria for each stage, evaluate candidates at each gate, and render go/kill/recycle decisions with evidence. |
| stakeholder-objection-simulation | Simulate stakeholder objections through role-play and political feasibility analysis to test whether the decision survives real-world opposition. |
| steel-manning | Steel-Manning Campaign — adversarial verification of convergence decisions through resurrection advocacy, winner stress-testing, criteria interrogation, and multi-perspective attack using Devil's Advocacy, Pre-mortem, Red Teaming, Dialectical Inquiry methods. |
| steel-manning-synthesis | Synthesize all attacks and verdicts into a final unified assessment with surviving concerns and recommended modifications. |
| structured-consensus | Structured Consensus Campaign — converge multiple perspectives into shared agreement through iterative structured dialogue using Delphi variants, NGT, RAND/UCLA, Consensus Conference methods. |
| temporal-sequencing | Determine optimal ordering and phasing of portfolio investments using Real Options, Critical path, Dependency graph, and Staged investment methods. |
| threshold-calibration | Systematically sweep consensus thresholds to observe which items achieve consensus at what level, producing a threshold-consensus curve. |
| threshold-setting | Define minimum acceptable thresholds for each criterion based on context and constraints. |
| threshold-sweep | Compute consensus status at multiple threshold levels to produce a threshold-consensus curve. |
| value-maximization | Maximize total portfolio value within constraints using Knapsack, Linear programming, Cost-benefit analysis, and NPV ranking methods. |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| weight-elicitation | Determine criteria weights using AHP, Swing, BWM, MACBETH, or Simos methods. |
| weight-elicitation-sop | Compute criteria weights using a specified elicitation method (AHP, Swing, BWM, MACBETH, or Simos). |
| winner-stress-testing | Stress-test the winning candidate using Pre-mortem, Red Teaming, and Failure Mode Analysis to expose hidden weaknesses before commitment. |

## stress-test (103 skills)

| Skill | Description |
|-------|-------------|
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| adversarial-escalation | "Strategy: Progressive pressure escalation — starts with surface-level challenges and escalates to fundamental assumption attacks based on defender confidence decay." |
| adversarial-persona | "Strategy: Role-play attacks from hostile personas — competing lab researcher, hostile reviewer, funding skeptic, domain outsider — each with distinct attack motivations and blind spots." |
| adversarial-roleplay | "Tactic: Construct detailed hostile persona, attack artifact from that persona's perspective, record successful attack paths for aggregation." |
| adversarial-stress-testing | "Campaign: Logical extreme and boundary testing via reductio ad absurdum and edge-case analysis. Core question: Does this artifact collapse under logical limits and boundary conditions? Methods: Lakatos 1976, Dutilh Novaes 2016, BVA, Flyvbjerg Critical Case, Popper." |
| alternative-analysis | "Strategy: What-If Analysis, Alternative Futures, and Four Ways of Seeing — generate competing explanations and scenarios to challenge the dominant narrative." |
| alternative-futures | Generate 2-4 divergent scenarios from the same evidence base, each representing a plausible alternative to the artifact's conclusions. |
| assumption-cascade | "Tactic: Surface assumptions, sort by dependency, attack root assumptions first, then trace cascade failures through the dependency graph." |
| assumption-cascade-tracer | Build assumption dependency graphs and trace cascade failures when root assumptions are invalidated. |
| assumption-challenge | Construct the strongest counter-argument against a specific assumption and propose alternatives. |
| assumption-negation | "Classic reductio ad absurdum: negate the core claim, derive logical consequences, seek contradiction or absurdity." |
| attack-resilience-scoring | Compute overall resilience score (0.0-1.0) based on attack results, coverage, and vulnerability severity distribution. |
| attack-vector-generation | Generate specific attack strategies for a given threat surface, producing concrete probes that can be executed. |
| boundary-enumeration | "Systematic Boundary Value Analysis: identify parameter boundaries, test at and beyond limits, detect breakpoints." |
| boundary-probing | "Map parameter space, generate extreme values, test at boundaries, detect breakpoints, synthesize validity envelope." |
| breakpoint-detection | "Test a claim at extreme parameter values and detect the precise point where it breaks down." |
| causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| causal-necessity-testing | "Tactic: Extract causal claims, evaluate probability of necessity (PN) and sufficiency (PS) for each, classify into necessity-sufficiency quadrants." |
| claim-negation | "Formally negate the core claim, producing the logical complement for reductio testing." |
| claim-refinement | "Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation)." |
| closest-worlds | "Strategy: Lewis Possible Worlds — find the minimal change to reality that would flip the conclusion, measuring how close the nearest world where the conclusion fails." |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| contradiction-derivation | "Negate a claim, derive logical consequences step by step, detect whether a genuine contradiction or absurdity emerges." |
| contradiction-detection | "Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state." |
| counterexample-generation | "Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies." |
| counterexample-heuristics | "Generate counterexamples (monsters), attempt monster-barring, incorporate surviving counterexamples as lemma refinements (Lakatos method)." |
| counterfactual-probing | "Campaign: Counterfactual reasoning to identify load-bearing factors. Core question: If key factors were different, would the conclusion still hold? Methods: Pearl SCM Three-Step, Lewis Possible Worlds, Tetlock & Belkin, PNS/PS." |
| counterfactual-scenario-construction | Construct precise, internally consistent counterfactual scenarios where specified factors are altered, then reason about the resulting conclusion. |
| courtroom-structured | "Strategy: Legal adversarial structure — prosecution presents case, defense responds, evidence is cross-examined, judge delivers verdict. Emphasizes evidence quality and procedural rigor." |
| critical-case-design | "Flyvbjerg critical case methodology: select most-likely and least-likely cases to maximize inferential power." |
| critic-defender-judge | "Strategy: Classic triangular debate — Critic attacks, Defender responds, Judge adjudicates. Based on Irving AI Safety via Debate with Toulmin argumentation structure." |
| cross-examination | Probes defender responses for inconsistencies, logical gaps, and unsupported claims. Acts as follow-up interrogation after initial defense. |
| debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| debate-transcript-analysis | Extracts key turning points, patterns, and insights from completed debate transcripts. Produces structured summary for verdict synthesis. |
| deductive-chain | "Derive logical consequences step by step from a given premise, building a traceable derivation chain." |
| design-fmea | "Strategy: Research design-level FMEA — function analysis, failure mode identification, severity/occurrence/detection scoring per AIAG-VDA 2019." |
| detection-scoring | "Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact." |
| devils-advocacy | Construct the strongest possible counter-argument against a position, steelmanning the opposition before attacking. |
| dialectical-escalation | Double-loop learning escalation — surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists. |
| divergence-detection | Identifies agreement and disagreement patterns across multiple perspective evaluations. Maps consensus clusters and persistent divergence points. |
| evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |
| evidence-tournament | "Tactic: Evidence gathering, cross-examination, and quality judgment. External evidence is collected, presented, challenged, and scored for relevance and reliability." |
| extreme-value-generation | "Generate boundary and extreme test values for a given parameter dimension to stress-test claims." |
| factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| factor-removal | "Strategy: Systematic factor removal — remove factors one at a time and observe whether the conclusion remains stable, identifying which factors are load-bearing." |
| failure-anticipation | "Campaign: Forward-looking failure analysis combining pre-mortem rapid screening with systematic FMEA deep-dive. Core question: If this artifact fails, how will it fail? Methods: Klein Pre-Mortem 2007, AIAG-VDA FMEA 2019, IEC 60812." |
| failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| failure-chain-tracing | "Tactic: Trace upstream causes and downstream effects of each failure mode. Builds multi-level cause-mode-effect chains for systemic understanding." |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| flip-point-detection | Find the minimal change magnitude along a dimension that causes the conclusion to flip from true to false. |
| fragility-measurement | Compute a fragility index from flip-point distances and degradation scores, summarizing how robust the conclusion is. |
| function-analysis | "FMEA Step 3: Decompose artifact into function tree — identify what each component is supposed to do before analyzing how it can fail." |
| groupthink-mitigation | "Strategy: 10th Man Rule and Liberating Structures — institutionalized dissent to prevent premature consensus and expose suppressed objections." |
| key-assumptions-check | "Military ACT: systematically enumerate all assumptions, classify by type, and evaluate evidence strength supporting each." |
| lakatos-heuristics | "Proofs and Refutations method: generate counterexamples, attempt monster-barring, incorporate surviving counterexamples as lemma refinements." |
| load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |
| minimal-change-search | "Tactic: Generate candidate changes, detect flip-points where conclusion reverses, measure fragility as distance to nearest flip." |
| mitigation-design | "Strategy: Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasures validated via re-scoring." |
| mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| mitigation-proposal | Proposes concrete mitigation strategies for identified weaknesses. Generates prevention, detection, and response measures with feasibility assessment. |
| mitigation-validation | "Tactic: Run mini-FMEA on proposed mitigations to verify they do not introduce new failure modes. Prevents mitigation-induced risks." |
| monster-barring-attempt | "Attempt to exclude a counterexample as illegitimate by tightening definitions or preconditions (Lakatos monster-barring)." |
| multiagent-debate | "Campaign: Multi-agent structured debate for adversarial validation. Core question: Can this artifact survive structured adversarial debate? Methods: Irving AI Safety via Debate, Du Society of Mind, Liang MAD, Toulmin Argumentation, D3 framework." |
| multi-perspective-panel | "Strategy: Multi-stakeholder review panel — diverse expert perspectives evaluate artifact simultaneously, then synthesize through structured deliberation." |
| necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor — would the conclusion fail if this factor were absent? |
| necessity-sufficiency | "Strategy: Probability of Necessity and Sufficiency (PNS/PS) — systematically evaluate whether each factor is necessary, sufficient, both, or neither for the conclusion." |
| occurrence-scoring | Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution. |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| parameter-space-mapping | "Identify all parameter dimensions along which a claim's validity might vary." |
| persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| perspective-critic | Evaluates artifact from a specific assigned perspective. Produces assessment grounded in that viewpoint's values, priorities, and expertise. |
| perspective-rotation | Rotate through reviewer/practitioner/theorist/time-machine/novice perspectives systematically. Ensures comprehensive viewpoint coverage. |
| premortem-facilitation | Execute Klein pre-mortem protocol — assume failure has occurred, generate plausible failure scenarios through prospective hindsight. |
| premortem-to-fmea-pipeline | "Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis." |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |
| process-fmea | "Strategy: Research execution process FMEA — analyzes how the research process itself can fail during execution, distinct from design-level failures." |
| prospective-hindsight | "Strategy: Klein pre-mortem — assume the artifact has failed, then retrospect plausible causes. Generates rapid failure scenario catalog." |
| red-teaming | "Campaign: Systematic adversarial attack from military/intelligence/AI-safety traditions. Core question: Can systematic adversarial attacks find fatal flaws? Methods: UFMCS Red Team Handbook v9.0, CIA SAT, Anthropic Red Teaming, NIST AI RMF, Inie et al. 12-strategy taxonomy." |
| re-scoring | Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected. |
| risk-prioritization | "Strategy: Action Priority matrix — classifies failure modes into H/M/L priority using severity-weighted scoring per AIAG-VDA 2019 Action Priority tables." |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |
| single-factor-removal | Remove one specified factor from the artifact's support structure and reason about how the conclusion changes. |
| society-of-mind | "Strategy: Multi-agent collaborative debate based on Du et al. Society of Mind. Agents share perspectives iteratively until convergence or divergence is detected." |
| structural-counterfactual | "Strategy: Pearl Three-Step counterfactual — Abduction (fit model to evidence), Action (intervene on factor), Prediction (derive counterfactual outcome)." |
| structured-attack-campaign | "Tactic: Full attack lifecycle — threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces." |
| sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor — would this factor alone be enough to produce the conclusion? |
| systematic-factor-ablation | "Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance." |
| systematic-probing | "Strategy: AI-safety systematic probing — enumerate all threat surfaces, generate attack vectors per surface, execute probes, and aggregate findings across the full attack space." |
| thought-experiment | "Strategy: Williamson-style precise thought experiments — construct carefully specified counterfactual scenarios to test whether conclusions depend on contingent features." |
| threat-surface-mapping | Enumerate all attackable surfaces of an artifact — logical, empirical, methodological, social, and practical dimensions. |
| validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| validity-envelope-mapping | Map multi-dimensional validity envelopes — define variation axes, perturb systematically, measure degradation, construct boundary surface. |
| verdict-synthesis | Synthesizes findings from a completed campaign into typed verdict reports. Produces DebateVerdict, RedTeamReport, FailureAnticipationReport, CounterfactualMap, or AdversarialStressReport depending on campaign. Also supports cross-campaign StressTestSummary. |
| weakness-classification | Classifies discovered weaknesses into severity tiers (fatal/major/minor/cosmetic) with structured justification and exploitability assessment. |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |

## experiment-execution (88 skills)

| Skill | Description |
|-------|-------------|
| ablation-component-mapping | "Map system architecture to ablatable units for ablation studies" |
| ablation-design | "Design ablation studies to isolate component contributions in ML systems" |
| activity-listing | "Enumerate all implementation activities from an experiment design" |
| assumption-challenging | "Challenge each assumption's validity — shared cross-repo SOP" |
| assumption-constraint | "Which assumptions are most fragile? — Vulnerability ranking + impact assessment of experiment assumptions" |
| baseline-selection | "Select appropriate baselines for experimental comparison" |
| bottleneck-identification | Identify bottleneck dimensions from radar data with severity ranking. |
| budget-constrained-design | "Optimize experiment design under compute and time budget constraints" |
| buffer-sizing | "Calculate project, feeding, and resource buffers — shared with implementation-planning" |
| causal-chain-tracing | "Trace UDE to root cause via IF...THEN...BECAUSE logic chains" |
| checkpoint-and-recover | "Checkpoint state before risky operations, detect anomalies, and recover gracefully" |
| comparison-design | "Design fair comparison experiments against baselines and competing methods" |
| competitive-move-prediction | "Predict competitor progress, publications, and strategic moves" |
| competitive-scenario | "What will competitors do? — Competitive method progress prediction and time window analysis" |
| conflict-resolution | "How do constraints conflict with each other? — Evaporating Cloud + assumption challenging + injection to resolve constraint conflicts" |
| consistency-pair-evaluation | Evaluate pairwise value consistency (logical/empirical/normative) |
| constraint-analysis | "What limits us — identify bottlenecks, quantify constraints, analyze dependencies, resolve conflicts before experiment execution" |
| constraint-breaking | "Orchestrate the full constraint-breaking cycle: extract conflict, challenge assumptions, project resolution" |
| constraint-synthesis | "Synthesize constraint analysis into actionable report with priorities" |
| constraint-tree-building | "Build Current Reality Tree from UDEs through causal chains to core conflicts" |
| core-conflict-extraction | "Extract core conflict in Evaporating Cloud format (A-B-C-D-D')" |
| critical-chain-identification | "Identify the critical chain — longest path considering resource contention" |
| critical-path-calculation | "CPM forward/backward pass with float calculation to identify the critical path" |
| critical-path-planning | "Identify the shortest execution path via CPM forward/backward pass, resource leveling, and buffer insertion" |
| cross-consistency-filtering | "Orchestrates pairwise consistency evaluation and narrative construction to filter the morphological field" |
| dependency-constraint | "What must be completed first? — Dependency chain analysis + prerequisite graph construction" |
| dependency-graph-construction | "Build task dependency graph with predecessor/successor relationships" |
| dependency-sequencing | "Determine task dependencies and execution order" |
| design-matrix-construction | "Build the experiment design matrix with proper orthogonality and balance" |
| design-synthesis | "SOP: synthesize complete experiment design report" |
| duration-estimation | "Three-point PERT estimation for implementation activities" |
| environment-specification | "SOP: define complete experiment environment specification" |
| execution-monitoring | "Monitor execution progress, detect anomalies, and report status" |
| execution-synthesis | "Synthesize complete execution report from all results, tests, and reproducibility data" |
| experiment-config-generation | "SOP: generate executable experiment configuration files" |
| experiment-design | "Transform validated hypotheses into rigorous, executable experiment designs" |
| experiment-running | "Execute the plan by dispatching fresh subagents per task, monitoring status, and collecting results" |
| factor-identification | "Identify independent, dependent, and control variables for an experiment" |
| factor-level-design | Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration. |
| future-reality-projection | "Project solution effects using Future Reality Tree logic" |
| implementation-planning | "Plan execution path, produce executable plan, dispatch subagents, collect and analyze results" |
| implementer-dispatch | "Dispatch execution subagent — select model by complexity, construct prompt with full task context" |
| intermediate-objective-design | "Design intermediate objectives to overcome each identified obstacle" |
| level-specification | "Determine appropriate levels for each experimental factor" |
| metric-specification | "Define experiment metrics and significance standards" |
| morphological-scenario | "What are all possible combinations? — Zwicky Box construction with CCA consistency filtering for systematic scenario enumeration" |
| narrative-scenario | "What is the story of each future? — Shell method narrative construction for rich qualitative scenario understanding" |
| obstacle-identification | "TOC Prerequisite Tree — list obstacles preventing direct achievement of the objective" |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| parameter-enumeration | "Enumerate possible values for each uncertainty driver using MECE principles" |
| parameter-space-construction | "Orchestrates driver identification and parameter enumeration to build the complete morphological field" |
| plan-formatting | "Format task plan as bite-sized executable tasks following superpowers:writing-plans conventions" |
| plan-writing | "Format critical path and prerequisites into bite-sized executable plan following superpowers:writing-plans conventions" |
| prerequisite-planning | "Identify obstacles blocking direct achievement and design intermediate objectives to overcome each" |
| quality-gate-check | "Shared SOP: 通用质量门检查（格式完整性、逻辑一致性）" |
| reproducibility-protocol | "Ensure experiment reproducibility through systematic environment and seed control" |
| reproducibility-verification | "Verify result reproducibility via re-runs with different seeds and ICC comparison" |
| resource-constraint | "Are resources sufficient? — Quantify compute, data, time, human, and financial resource constraints" |
| resource-quantification | "Quantify resource demand vs supply vs gap for each resource category" |
| result-analysis | "Statistically analyze collected results, verify reproducibility, and synthesize findings" |
| result-collection | "Collect experiment outputs — metrics, logs, artifacts — into structured result set" |
| result-validation-loop | "Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis" |
| robustness-design | "Design experiments to identify failure boundaries and robustness limits" |
| robustness-scoring | "Compute robustness index across scenarios with sensitivity analysis" |
| sample-size-estimation | "SOP: power analysis and required experiment count estimation" |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scaling-design | "Design scaling experiments to characterize performance-resource relationships" |
| scenario-driver-identification | "Identify key uncertainty drivers using PESTEL framework scanning" |
| scenario-impact-assessment | "Assess each scenario's impact on the research approach across multiple dimensions" |
| scenario-narrative-construction | "Build rich narratives for surviving morphological configurations using Shell method" |
| scenario-planning | "What might the future look like — construct multiple future scenarios, assess research approach robustness under different assumptions" |
| scenario-synthesis | "Comprehensive scenario analysis report synthesizing all scenario work" |
| seed-protocol-design | "SOP: design random seed strategy for reproducibility" |
| sensitivity-ranking | "Rank constraints by sensitivity — which ones most impact the outcome if they shift" |
| statistical-method-selection | "Select appropriate statistical methods for experiment analysis" |
| statistical-testing | "Execute statistical tests — bootstrap, permutation, Bayesian ROPE — on experiment results" |
| strategy-robustness-testing | "Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios" |
| stress-scenario | "What is the worst case? — Extreme condition construction and failure mode enumeration for risk preparedness" |
| subagent-execution-loop | "Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection" |
| task-decomposition | "Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan" |
| temporal-scenario | "How does it evolve over time? — Short/medium/long-term timeline projection with technology maturity curves" |
| timeline-projection | "Extrapolate research landscape timelines using trend analysis and milestone projection" |
| undesirable-effect-listing | "List current Undesirable Effects (UDEs) — observable symptoms of system underperformance" |
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| worst-case-construction | "Construct extreme but plausible worst-case scenarios for stress testing" |

## web-browsing (2 skills)

| Skill | Description |
|-------|-------------|
| web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |

## literature-engine (3 skills)

| Skill | Description |
|-------|-------------|
| literature-overview | Quick landscape scan — discover papers on a topic without full-text reading |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |

## subagent-spawning (1 skills)

| Skill | Description |
|-------|-------------|
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

## context-management (2 skills)

| Skill | Description |
|-------|-------------|
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points — typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |

