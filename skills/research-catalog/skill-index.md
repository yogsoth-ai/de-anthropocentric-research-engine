# Skill Index

Total skills in this distribution: 823

## north-star-crystallization (33 skills)

| Skill | Description |
|-------|-------------|
| actor-profiling | Understand who the user is 鈥?background, resources, constraints, and deep motivations. Produces an ActorProfile that informs all downstream decisions. Use this tactic at the start of any crystallization process to build a model of the user's capabilities, limitations, and intent. |
| and-or-decompose | KAOS-style recursive goal decomposition. AND decomposition for sub-goals that must ALL be satisfied. OR decomposition for alternative paths where any one suffices. Produces a GoalTree (DAG structure). |
| ask-constraints | Understand hard boundaries on the user's research 鈥?target venues, methodology preferences, areas to avoid, advisor/team requirements. Not limited to ML/AI 鈥?works for any research domain. |
| ask-decomposition-validation | Present the GoalTree to the user for confirmation. Ask about reasonableness, missing elements, and priority ordering among sub-goals. |
| ask-intentionality | Deep WHY probing inspired by i* Intentionality modeling. Understand the user's motivation, success definition, risk tolerance, innovation preference, independence preference, time urgency, and learning willingness. The most important SOP in actor-profiling 鈥?understanding WHY drives everything downstream. |
| ask-obstacle-acceptance | Present obstacles with their severity assessments and proposed mitigations to the user. Ask whether they can accept these obstacles. If unacceptable after 2 rounds, return to present-candidates. |
| assess-obstacle-severity | Rate each identified obstacle's difficulty 鈥?overcomability, time cost, workaround existence. May optionally use search tools to validate assessments. |
| broad-paper-search | Paper landscape scan within selected field(s). Strict import of literature-engine/literature-overview skill. Hard constraint: at least 80 papers scanned. |
| broad-web-search | Quick web scanning for field landscape understanding. Strict import of web-browsing/web-search skill. Hard constraint: brave_web_search count=10 per call, at least 150 total search results before completing. |
| clarify-resources | Understand what resources the user has available for research 鈥?compute, timeline, collaboration, data access, experimental environment. Every item accepts 'TBD' as a valid answer. |
| cold-start | Full crystallization strategy for users who have no research direction at all. Covers actor profiling, landscape reconnaissance, direction narrowing, obstacle analysis, goal decomposition, and north-star synthesis. Use when the user's first message reveals zero specificity about what they want to research. |
| crystallize-north-star | "Fuse the GoalTree root node and user motivation into a single crystallized North Star statement. Format: '[verb] [specific goal], through [method/path], solving [what problem], ultimately [what impact]'. Quality checks: specific? ambitious? achievable?" |
| deep-web-search | Full-page web reading for non-academic perspectives 鈥?blogs, tech reports, product pages, industry analysis. Spawns a subagent to read pages in isolated context. Hard constraint: at least 30 web pages read in full. |
| direction-narrowing | Focus within the user's chosen field(s). Identify specific sub-directions through deep paper and web research, then present ranked candidates. Use after landscape-reconnaissance has identified fields of interest. |
| explore-resume | Understand the user's background comprehensively 鈥?technical stack, project experience, research experience, publications, research directions. Allows user to express interest beyond their resume. Execute once only, never re-run. |
| feasibility-check | Cross-reference the GoalTree against ActorProfile (capabilities), ObstacleReport (known barriers), and timeline (deadline feasibility). Identify infeasible paths and suggest OR alternatives. |
| final-validation | Self-review the North Star + ResearchBrief for completeness, consistency, and clarity before presenting to user. If issues found, return to specific tactic/SOP for targeted fix. If passes, present final output to user for confirmation. |
| formulate-top-goal | "Express the user's chosen research direction as a formal goal statement in the format: 'Achieve [what], such that [effect], under [constraints]'. Confirm with user before proceeding to decomposition." |
| generate-candidate-fields | Propose 3-8 candidate research fields based on the full ActorProfile. When user wants to explore beyond their current stack, use other ActorProfile signals (intentionality, boundary) to determine exploration space. Free exploration within the boundary. |
| generate-research-brief | Aggregate all accumulated context from the crystallization process into a structured ResearchBrief document. This is the final output artifact alongside the North Star 鈥?a comprehensive requirement context document for downstream research strategies. |
| goal-decomposition | Structure the user's chosen direction into a formal goal tree using KAOS-style AND/OR decomposition. Validate feasibility against ActorProfile and ObstacleReport. Use after obstacle-analysis confirms the direction is viable. |
| hot-start | Minimal crystallization strategy for users who already have a specific research topic or problem (e.g., "I want to improve CoT faithfulness in LLMs") and need structuring into a formal North Star. Heavily simplifies or skips exploration tactics, focusing on obstacle analysis, goal decomposition, and synthesis. Use when the user's first message reveals a specific, actionable research direction. |
| identify-obstacles | Enumerate barriers to pursuing the chosen research direction 鈥?knowledge barriers, resource barriers, capability barriers, competition barriers. May optionally use search tools to discover obstacles the user hasn't mentioned. |
| landscape-reconnaissance | Broad, shallow exploration of candidate research fields. Understand what's out there before narrowing. Use when the user needs to discover which fields are available to them 鈥?especially in cold-start and warm-start scenarios. |
| landscape-synthesis | Evaluate each candidate research field on maturity, competition, entry barrier, and publication opportunity. Synthesizes broad-web-search results into a structured FieldPanorama. Must consider both niche approaches AND direct frontal competition in hot fields. |
| north-star-crystallization | Goal-Driven Requirement Refinement Engine for Research. Crystallize a user's fuzzy research intent into a North Star statement and structured ResearchBrief through adaptive dialogue and on-demand investigation. |
| north-star-synthesis | Converge all accumulated context into a crystallized North Star statement and structured ResearchBrief. Performs self-review before presenting to user. Use as the final tactic in any start mode 鈥?this is where everything comes together. |
| obstacle-analysis | Identify what blocks the user from pursuing their chosen direction, assess severity, propose mitigations with search-validated evidence, and get user acceptance. Use after direction-narrowing has identified a specific direction. |
| present-and-ask | Present the field panorama to the user and gather their preferences 鈥?which fields interest them, which they reject, and why. A dialogue SOP that bridges landscape-synthesis output to user decision. |
| present-candidates | Analyze sub-directions within the user's chosen field and present ranked candidates. Combines sub-direction identification, skill-gap matching, and presentation into a single SOP. Depth scales by start mode: cold-start shows broad sub-directions, warm-start shows specific sub-problems, hot-start shows granular technical details. |
| propose-mitigations | Propose concrete mitigation strategies for severe obstacles. MUST use search tools to validate that proposed mitigations are realistic 鈥?no armchair theorizing. Each mitigation must have evidence of feasibility. |
| validate-leaves | Quality check on leaf nodes of the GoalTree. Verify each leaf is specific enough, actionable, and that the set of leaves fully covers the top goal. Flag issues for further decomposition. |
| warm-start | Simplified crystallization strategy for users who have a general research direction (e.g., "I'm interested in LLM reasoning") but lack specificity. Simplifies actor profiling and landscape reconnaissance, then proceeds through direction narrowing, obstacle analysis, goal decomposition, and north-star synthesis. Use when the user's first message reveals a general area but not a specific problem. |

## knowledge-acquisition (100 skills)

| Skill | Description |
|-------|-------------|
| artifact-detection | Detect annotation artifacts and shortcuts in benchmarks |
| assignee-normalization | Standardize assignee names and identify corporate group affiliations across patent offices |
| baseline-establishment | SOTA Performance Baseline Campaign 鈥?5 strategies for systematically collecting, standardizing, and analyzing performance data across methods. Produces standardized comparison tables, progress curves, and headroom analysis. |
| baseline-synthesis | Produce final structured baseline report integrating all analysis results |
| benchmark-archaeology | Evaluation Methodology Archaeology Campaign 鈥?5 strategies for systematic analysis of AI/ML benchmarks, metrics, and leaderboards. Reveals construct validity issues, saturation, data contamination, and evaluation protocol inconsistencies. |
| benchmark-audit | Systematic quality assessment using BetterBench 46-criterion framework 鈥?5 benchmarks, 30 papers, 40 web searches |
| benchmark-inventory | Identify and catalog all relevant benchmarks in target domain |
| benchmark-synthesis | Produce final structured audit report |
| bias-detection | Assess systematic biases in the evidence body 鈥?publication bias, reporting bias, and selective outcome reporting. Budget: 40 studies, 40 effect sizes, 40 web searches. |
| capability-taxonomy-mapping | Build capability taxonomy, map existing benchmark coverage |
| categorize-papers | Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review. |
| citation-chaining | Forward and backward citation tracing tactic 鈥?expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation. |
| citation-network-analysis | Build and analyze patent citation networks 鈥?main path analysis, PageRank, cluster detection |
| claim-analysis | Deep claim scope analysis 鈥?decompose independent/dependent claims and assess protection scope breadth. Budget: 30 patent families, 30 claim parses, 20 web searches. |
| claim-decomposition | Independent/dependent claim parsing, element extraction, and feature mapping to technical domains |
| claim-parsing | Patent claim syntax parsing 鈥?independent/dependent relationships and element extraction |
| classification-navigation | IPC/CPC hierarchy drill-down and lateral expansion for patent discovery |
| competitive-intelligence | Analyze competitor IP portfolios 鈥?comparative patent portfolio reports with strategy inference. Budget: 120 patent families, 15 claim parses, 40 web searches. |
| compute-normalization | Normalize results by compute budget (Pareto analysis) |
| condition-cataloging | Record evaluation conditions (data splits, hyperparams, hardware, seeds) from a paper |
| condition-normalization | Compare and standardize experimental conditions across papers |
| condition-standardization | Standardize evaluation condition differences across papers — 20 methods, 60 data points, 30 web searches budget |
| construct-validity-assessment | Evaluate whether benchmark measures its claimed capability |
| contamination-audit | Detect train-test data leakage and memorization artifacts |
| coverage-mapping | Map evaluation coverage, identify untested capability dimensions 鈥?20 benchmarks, 30 papers, 50 web searches |
| cumulative-tracking | Track evidence accumulation over time 鈥?cumulative meta-analysis protocol design. Budget: 40 studies, 40 effect sizes, 30 web searches. |
| data-extraction-form | Design structured data extraction form for systematic meta-analysis data collection |
| deep-survey | Precise, targeted investigation of a specific sub-problem 鈥?few papers, all read in full depth. High paper-research ratio (50% deep-read rate). Use when the user knows exactly what they need to understand and requires detailed technical analysis with equations, hyperparameters, and specific claims extracted. |
| define-search-protocol | Formalize search queries and inclusion/exclusion criteria for systematic surveys. Produces a reproducible search protocol document. Used by systematic-survey. |
| discrepancy-analysis | Identify discrepancies between reported and reproducible scores — 15 methods, 45 data points, 30 web searches budget |
| discrepancy-identification | Compare same-method scores across sources, flag significant deviations |
| documentation-audit | Assess documentation completeness against BetterBench/Datasheets standards |
| effect-size-extraction | Systematically extract effect sizes and conditions from papers for meta-analytic synthesis |
| effect-size-planning | Determine effect size types and calculation methods for meta-analytic synthesis |
| evaluation-protocol-comparison | Compare implementation differences of same benchmark across papers |
| evidence-network-construction | Build evidence network graph for network meta-analysis 鈥?nodes, edges, geometry assessment |
| evidence-synthesis-planning | Plan the statistical synthesis approach 鈥?model selection, heterogeneity strategy, and reporting |
| extract-data | Structured data extraction from deep-read papers 鈥?produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey. |
| gap-identification | Identify what the literature has NOT addressed 鈥?missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| headroom-estimation | Estimate theoretical/practical ceiling vs current SOTA gap |
| heterogeneity-investigation | Explain why different studies reach different conclusions 鈥?heterogeneity investigation protocol. Budget: 30 studies, 30 effect sizes, 50 web searches. |
| heterogeneity-source-analysis | Identify and classify sources of between-study heterogeneity (clinical, methodological, statistical) |
| inclusion-criteria-design | Define inclusion/exclusion criteria for systematic study selection in meta-analysis |
| landscape-survey | Patent landscape full-scan 鈥?maps technology domain via assignee ranking, IPC/CPC classification, filing trends. Budget: 200 patent families, 0 claim parses, 80 web searches. |
| leaderboard-dynamics-analysis | Analyze leaderboard score distributions, compression, selective reporting |
| leaderboard-harvesting | Systematically collect performance data from platforms and papers |
| legal-status-assessment | Determine patent legal status 鈥?active, expired, pending, lapsed, or revoked |
| literature-survey | Autonomous Literature Survey Campaign 鈥?5 research paradigms (scoping, systematic, deep, narrative, snowball) with quantitative budget enforcement. Selects and executes the right survey paradigm based on research intent. |
| meta-analysis | Cross-Study Statistical Synthesis Campaign 鈥?5 strategies for systematic collection and methodological planning of multi-study evidence synthesis. Covers pairwise, network, cumulative meta-analysis, heterogeneity investigation, and bias detection. Stops at protocol design (no computation). |
| meta-analysis-synthesis | Produce final meta-analysis protocol document assembling all planning outputs into PRISMA-compliant protocol |
| method-discovery | Identify all relevant methods via literature, leaderboards, citation chains |
| method-inventory | Comprehensively identify all relevant methods for a task — 50 methods, 60 web searches budget |
| metric-decomposition | Decompose composite metrics into constituent signals, analyze polarity and ceiling effects |
| narrative-framing | Theory-driven reading tactic 鈥?define a theoretical framework first, then guide reading to fill it with evidence. Five stages (theme identification, argument construction, evidence collection, counter-evidence, synthesis). The most intellectually demanding tactic. |
| narrative-review | Theory-driven literature review for building arguments and frameworks. Flexible, subjective, and narrative-focused 鈥?selects evidence strategically to support a thesis. High web-research budget for blogs, opinion pieces, and industry perspectives. Use when the user is writing a position paper, survey introduction, or constructing a coherent narrative around a research theme. |
| network-comparison | Compare N methods simultaneously including indirect evidence 鈥?network meta-analysis protocol design. Budget: 50 studies, 80 effect sizes, 60 web searches. |
| pairwise-synthesis | Compare two methods across multiple studies 鈥?paired meta-analysis protocol design. Budget: 30 studies, 30 effect sizes, 40 web searches. |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only 鈥?no methodology conclusions from abstracts. |
| paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) 鈥?equations, hyperparameters, specific claims extracted. |
| paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| patent-categorization | Classify patents by tech subdomain, application scenario, and value chain position |
| patent-family-tracing | Forward/backward patent citation and priority tracing until saturation |
| patent-mining | Systematic Patent Analysis Campaign 鈥?5 strategies for patent landscape analysis, prior art search, white space identification, competitive intelligence, and claim analysis. Produces structured patent intelligence reports. |
| patent-query-formulation | Construct keyword + IPC/CPC + assignee combination search strategies for patent databases |
| patent-synthesis | Produce final structured patent intelligence report from all analysis results |
| performance-extraction | Systematically extract performance data and conditions from papers — 30 methods, 150 data points, 40 web searches budget |
| performance-table-assembly | Assemble unified comparison table with confidence interval annotations |
| pico-formulation | Construct PICO/PECO framework for the meta-analysis research question |
| prior-art-search | Evaluate novelty of specific invention 鈥?find relevant prior art across patents, publications, and products. Budget: 80 patent families, 20 claim parses, 50 web searches. |
| prisma-flowchart | Generate PRISMA-compliant flow data documenting the screening funnel 鈥?counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic. |
| prisma-screening | Multi-stage PRISMA screening tactic 鈥?progressively filter papers from a large candidate pool to a focused set for deep reading. Four stages (identification, title/abstract screening, full-text screening, inclusion) with documented counts at each stage. |
| progress-curve-construction | Build performance-over-time progress curves with inflection detection |
| progress-curve-fitting | Construct performance-over-time visualization data |
| progress-quantification | Track performance progress over time, quantify remaining headroom — 30 methods, 100 data points, 40 web searches budget |
| protocol-element-extraction | Extract evaluation protocol parameters from papers |
| protocol-forensics | Analyze evaluation protocol differences across papers for same benchmark 鈥?5 benchmarks, 60 papers, 30 web searches |
| publication-bias-assessment | Plan funnel plots, Egger's test, trim-and-fill, p-curve, and selection model analyses for publication bias |
| quality-assessment | Methodological rigor scoring for papers 鈥?evaluates bias risk, reproducibility, sample adequacy using established frameworks. Used by systematic-survey. |
| quality-assessment-protocol | Methodological quality and bias risk assessment of included studies using validated tools |
| quality-scoring | Multi-dimensional patent quality assessment 鈥?forward citations, family size, claim count, geographic breadth |
| reproducibility-checklist-audit | Assess paper completeness against ML Reproducibility Checklist |
| risk-of-bias-assessment | Assess methodological bias using RoB2, PROBAST, or QUADAS-2 validated tools |
| saturation-analysis | Track score trajectories, detect saturation/failure points 鈥?15 benchmarks, 50 papers, 60 web searches |
| saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| scoping-survey | Broad landscape mapping strategy 鈥?quickly understand what exists in a field. Prioritizes breadth over depth with high paper-overview volume and minimal deep reading. Use when entering a new field or needing orientation before committing to deeper investigation. |
| score-extraction | Extract (Task, Dataset, Metric, Score, Conditions) tuples from a paper |
| score-trajectory-analysis | Collect historical scores, fit saturation curves, detect inflection points |
| seed-selection | Validate and prioritize starting papers for snowball surveys. Evaluates which seeds will yield the richest citation traces based on citation count, recency, and network position. |
| sensitivity-analysis-design | Design leave-one-out, influence diagnostics, subgroup analyses, and robustness checks |
| snowball | Citation-chain-driven literature survey starting from seed papers. Traces research lineage in both forward (who cited this) and backward (what this cited) directions until saturation. High deep-read ratio (67%). Use when the user already has key papers and wants to find everything connected to them 鈥?ancestors, descendants, and branch points. |
| survey-synthesis | Final synthesis step 鈥?weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |
| systematic-survey | Exhaustive PRISMA-style literature survey 鈥?comprehensive coverage of all related work on a specific question. Multi-stage screening, citation chaining, quality assessment, and structured data extraction. Use when the user needs to demonstrate complete literature coverage or conduct rigorous gap analysis. |
| taxonomy-mapping | Construct a hierarchical field map from paper collection 鈥?multi-level taxonomy with parent/child relationships, paper counts per node, and maturity indicators. Used by scoping-survey. |
| thematic-coding | Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review. |
| trend-analysis | Patent filing volume time-series, technology lifecycle stage, and S-curve analysis |
| validity-probing | Challenge construct validity 鈥?does benchmark measure claimed capability? 鈥?3 benchmarks, 40 papers, 30 web searches |
| web-research | Full-page web reading for non-academic perspectives 鈥?blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only 鈥?no conclusions from snippets alone. |
| white-space-analysis | Identify patent coverage gaps 鈥?feature cross-matrix blank areas revealing unprotected technology combinations. Budget: 150 patent families, 10 claim parses, 60 web searches. |
| white-space-mapping | Feature cross-matrix construction and blank area identification for patent opportunity mapping |

## deep-insight (111 skills)

| Skill | Description |
|-------|-------------|
| abp-vulnerability-classification | Classify assumptions on 2 axes 鈥?load-bearing (how much conclusion depends on it) 脳 vulnerable (how likely to be false). Focuses attention on High-Load 脳 High-Vulnerable quadrant. |
| abstraction-laddering | Move between concrete and abstract framings 鈥?3 levels up (Why?) and 3 levels down (How?) to find the most productive research level. |
| ahrq-reason-classification | Classify gap root causes using AHRQ 4-reason framework (insufficient info, biased info, inconsistent info, not yet integrated). |
| alternative-model-generation | Generate alternative model formulations by relaxing, replacing, or generalizing specific assumptions. |
| appreciative-discovery | Search for positive deviants and extract transferable principles using Appreciative Inquiry. |
| appreciative-reframing | Find positive deviants and reframe the problem from deficit-based to asset-based using Appreciative Inquiry. |
| assumption-audit | Surface all assumptions, classify by vulnerability (load-bearing 脳 likely-false), validate causal logic. Focus on dangerous assumptions 鈥?high load-bearing + non-explicit. |
| assumption-criticality | Measure how much conclusions change when each assumption is negated. Ranks assumptions by their impact on the final result. |
| assumption-enumeration | Systematically identify all assumptions in a method/model 鈥?structural, parametric, distributional, and scope assumptions. |
| assumption-extraction | Systematically extract all assumptions (stated, implicit, boundary, mathematical, practical) from a method or model. |
| assumption-perturbation | One-at-a-time assumption perturbation 鈥?extract assumptions, define negations, re-derive conclusions under each negation, measure sensitivity. Identifies which assumptions are load-bearing. |
| assumption-stress-test | Systematic stress testing of assumptions 鈥?surface, classify by vulnerability, attack, assess fragility. Combines assumption-surfacing (shared), abp-vulnerability-classification, and clr-validation SOPs. |
| assumption-surfacing | Systematically extract implicit assumptions from methods, frameworks, or arguments. Identifies what is taken for granted without explicit justification. |
| boundary-analysis | Boundary Analysis Campaign 鈥?probe where methods fail, map validity envelopes, test robustness, catalog failure modes, detect scaling limits. 5 strategies, 3 tactics, 11 subagent SOPs. |
| boundary-critique | Apply CSH boundary critique 鈥?what is included/excluded, who benefits/is harmed, what expertise is privileged/marginalized. Identifies opportunities at the boundaries. |
| boundary-synthesis | Compile all boundary analysis products into a coherent report 鈥?validity envelopes, robustness results, failure catalogs, scaling maps, safe operating conditions. |
| boundary-unfolding | Systematically expose hidden system boundaries 鈥?CSH 12-question is/ought comparison, identify excluded stakeholders, reveal blind spots. Combines csh-12-question, jtbd-mapping, and salience-classification SOPs. |
| catwoe-analysis | Apply Checkland's CATWOE analysis from a specific stakeholder perspective to reveal how the problem looks from that viewpoint. |
| causal-tree-building | Build logical causal trees from symptoms to root causes 鈥?list UDEs, connect causal chains, validate logic, locate root causes. Combines ishikawa-decomposition, current-reality-tree, and clr-validation SOPs. |
| clr-validation | Apply Goldratt's 8 Categories of Legitimate Reservation to validate causal claims. Tests clarity, existence, sufficiency, and logical integrity. |
| concept-matrix-construction | Build articles 脳 concepts coverage matrix to visualize research landscape and identify empty cells as gap candidates. |
| conclusion-sensitivity-measurement | Quantify how much conclusions change across all assumption negations and produce a sensitivity ranking. |
| consequence-following | Follow a provocation's logical consequences step by step to extract viable insights and new research directions. |
| controlled-perturbation | Systematically vary parameters along defined axes, recording performance at each point to identify degradation thresholds. |
| convergence-assessment | Compare results across multiple model variants 鈥?quantitative agreement metrics and qualitative conclusion stability. |
| counter-assumption-generation | Generate dialectical opposites for governing variables 鈥?coherent alternative worldviews where the opposite is true. |
| critical-path-identification | Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization. |
| cross-database-verification | Verify gap existence across multiple databases (Semantic Scholar, Google Scholar, arXiv, domain-specific). Distinguishes database-specific gaps from universal gaps. |
| cross-validation | Multi-source cross-validation of gap authenticity 鈥?cross-database search, temporal sensitivity testing, false-gap filtering, stakeholder confirmation. |
| csh-12-question | Apply Ulrich's Critical Systems Heuristics 12 questions across 4 dimensions (motivation, control, expertise, legitimacy) comparing is vs ought. |
| current-reality-tree | Build TOC Current Reality Trees 鈥?connect Undesirable Effects via sufficient-cause logic to identify 1-3 root causes. |
| decision-sensitivity | Identify which uncertainties would actually change the research direction decision. Compute EVPI to prioritize uncertainty reduction. |
| dialectical-escalation | Double-loop learning escalation 鈥?surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists. |
| dialectical-reformulation | Surface Argyris governing variables and test whether the problem dissolves under alternative governing variables (double-loop learning). |
| dialectical-synthesis | Hegelian thesis-antithesis-synthesis cycle 鈥?propose position, generate opposition, structured debate, synthesize transcending insight. Combines evaporating-cloud and polarity-mapping SOPs. |
| distribution-assignment | Assign probability distributions to uncertain parameters based on available evidence and domain knowledge. |
| dominant-idea-escape | Identify dominant paradigms constraining the field and use de Bono lateral thinking provocations to escape them. |
| dominant-idea-identification | Identify dominant paradigms and assumptions constraining thinking in a research field. |
| edge-case-generation | Systematically generate boundary inputs 鈥?boundary values, adversarial constructions, distribution shifts, rare combinations, scale extremes. |
| egm-construction | Build structured Evidence Gap Maps 鈥?define axes (intervention 脳 outcome or method 脳 domain), place gaps in cells, annotate with evidence density and quality. |
| evaporating-cloud | Model conflicts as Goldratt's Evaporating Cloud 鈥?expose hidden assumptions behind opposing needs to dissolve the conflict. |
| evidence-grading | Assess evidence quality using GRADE/SOE framework. Rates certainty level and identifies downgrade reasons. |
| evidence-mapping | Systematic evidence map construction 鈥?search, classify, locate gaps, visualize. Combines concept-matrix-construction, gap-keyword-extraction, evidence-grading, and egm-construction SOPs. |
| evidence-synthesis | Synthesize multi-source evidence into structured argumentation. Weaves findings from literature, web, and analysis into coherent evidence maps with explicit strength ratings. |
| failure-clustering | Group observed failures by mechanism (not symptom), identify common triggers per cluster, estimate frequency and severity. |
| failure-mode-analysis | Systematically catalog failure modes 鈥?generate edge cases, observe failures, cluster by mechanism, identify triggers and frequency. |
| failure-mode-cataloging | Systematic failure mode cataloging 鈥?generate boundary inputs, observe failures, cluster by mechanism, identify triggers, estimate frequency. |
| false-gap-filtering | Detect false gaps 鈥?search failures, already-solved gaps, and inherently unanswerable questions masquerading as research gaps. |
| five-whys-drilling | Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon to actionable root cause. Each level verified against evidence. |
| fragility-flagging | Identify which specific assumption changes cause conclusion divergence. Rates fragility severity and plausibility of alternatives. |
| gap-analysis | Gap Analysis Campaign 鈥?identify, classify, validate, and prioritize research gaps via systematic evidence mapping. 5 strategies (gap-identification, gap-classification, gap-validation, gap-prioritization, gap-synthesis), 3 tactics, 12 subagent SOPs. |
| gap-classification | Classify identified gaps using Miles 7-type taxonomy and AHRQ 4-reason framework. Determines gap type (theoretical, methodological, empirical, etc.) and root cause of gap existence. |
| gap-identification | Identify research gaps via PICOS frameworks, concept matrices, evidence gap maps, keyword extraction, citation analysis, and topic modeling. Systematic discovery of what is missing in the literature. |
| gap-keyword-extraction | Extract gap-indicating sentences and phrases from papers/reviews. Identifies linguistic markers of research gaps (e.g., "remains unclear", "has not been explored", "limited understanding"). |
| gap-prioritization | Score and rank validated gaps on importance, feasibility, novelty, and urgency. Multi-criteria decision analysis with stakeholder confirmation. |
| gap-synthesis | Compile all gap analysis intermediate products into a coherent final report with executive summary, detailed findings, and research agenda. |
| gap-synthesis-strategy | Compile all gap analysis products into a coherent final report with evidence gap maps, research agenda, and concept matrices. |
| gap-typology-classification | Classify gaps using Miles 7-type taxonomy (theoretical, methodological, empirical, population, practical, knowledge void, evidence gap). |
| gap-validation | Validate gap authenticity via cross-database verification, temporal sensitivity testing, and false-gap filtering. Ensures gaps are genuine absences, not search artifacts. |
| governing-variable-surfacing | Apply Argyris framework to identify governing variables 鈥?the unstated rules driving behavior in a research field. |
| hmw-formulation | Generate "How Might We" questions at different scope levels (narrow, medium, broad). Ensures each is actionable without being prescriptive. |
| insight | Insight Campaign 鈥?deep root-cause analysis of why research gaps persist. 5 strategies (root-cause-drilling, stakeholder-mapping, tension-mining, question-reformulation, assumption-audit), 4 tactics, 13 subagent SOPs. |
| interaction-detection | Detect and characterize significant parameter interactions from Sobol decomposition results. |
| ishikawa-decomposition | Decompose problems into 6M categories (Methodology, Data, Theory, Measurement, Researchers, Environment) via fishbone diagram analysis. |
| jtbd-mapping | Map stakeholder Jobs-to-be-Done 鈥?functional, emotional, and social jobs for each affected party. Identifies unserved jobs as opportunity signals. |
| lateral-escape | de Bono lateral escape sequence 鈥?identify dominant idea, generate provocations (escape/reversal/exaggeration/distortion), follow consequences to extract new framings. Breaks paradigm lock-in. |
| monte-carlo-sampling | Design and execute Monte Carlo sampling strategy for uncertainty propagation through a model. |
| morris-screening | Morris method screening 鈥?compute elementary effects to quickly identify important vs unimportant parameters. |
| multi-criteria-scoring | Score gaps on multiple dimensions (importance, feasibility, novelty, urgency, impact) using weighted multi-criteria decision analysis. |
| multi-model-convergence | Wimsatt-style multi-method cross-validation 鈥?enumerate assumptions, generate alternative models, compare results, flag divergences. |
| multi-perspective-reframing | Apply CATWOE from multiple stakeholder viewpoints and reframing matrix to reveal aspects invisible from the dominant perspective. |
| multi-stakeholder-simulation | Simulate multiple stakeholder perspectives evaluating a research gap, method, or proposal. Identifies blind spots from single-perspective analysis. |
| multi-worldview-comparison | Multi-worldview comparison 鈥?CATWOE from multiple perspectives, reframing matrix across professional lenses, identify overlooked framings. Reveals what single-perspective analysis misses. |
| negation-definition | Define strongest plausible alternatives (negations) for each assumption to enable perturbation analysis. |
| paper-overview | Paper metadata and abstract-level overview. Import of literature-engine/literature-overview skill. Abstracts only 鈥?no substantive claims without deeper reading. |
| paper-research | Full-text paper reading via three-pass Keshav method. Import of literature-engine/literature-research skill. Authoritative source for claims about paper content. |
| paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level 鈥?cite as "AI-extracted" not "paper states". |
| parameter-screening | Quick Morris method screening to identify which parameters have large effects and which can be safely ignored. |
| polarity-mapping | Map unresolvable tensions as Johnson polarities 鈥?4 quadrants (positive/negative of each pole), early warnings, action steps for managing rather than solving. |
| prioritization-scoring | Multi-dimensional gap scoring and ranking 鈥?define criteria, score, weight, rank, sensitivity-check. Combines multi-criteria-scoring, stakeholder-confirmation, and feasibility assessment. |
| problem-reformulation | Problem Reformulation Campaign 鈥?question the problem itself. Escape dominant ideas, reframe from multiple perspectives, apply dialectical inquiry, assess wickedness, discover appreciative alternatives. 5 strategies, 3 tactics, 10 subagent SOPs. |
| provocation-generation | Generate de Bono lateral thinking provocations to challenge dominant ideas using escape, reversal, exaggeration, and distortion. |
| question-reformulation | Reframe research questions using abstraction laddering, HMW formulation, and Socratic probing. Find the most productive level and framing for investigation. |
| re-derivation | Re-derive conclusions under a negated assumption, tracking where the derivation diverges from the original. |
| reformulation-synthesis | Compile all problem reformulation analyses into a coherent report with a recommended new problem definition. |
| reframing-matrix | Reframe the problem from 4 professional perspectives to reveal what each discipline would focus on. |
| robustness-testing | Test conclusion robustness via multi-model convergence 鈥?enumerate assumptions, generate alternatives, compare results, flag fragile conclusions. |
| root-cause-drilling | Drill from surface symptoms to root causes via 5 Whys, Ishikawa decomposition, and Current Reality Trees. Validates each causal link with literature evidence. |
| salience-classification | Classify stakeholders by Mitchell et al. framework (Power, Legitimacy, Urgency). Assigns salience category and identifies systematically excluded parties. |
| scaling-frontier | Analyze behavior across scales 鈥?detect regime changes, identify capacity limits, fit scaling laws within regimes. |
| scaling-regime-detection | Detect regime changes in scaling behavior 鈥?breakpoints where behavior qualitatively shifts, mechanisms behind transitions. |
| screening-then-decomposition | Two-phase sensitivity 鈥?Morris quick screening to eliminate unimportant factors, then Sobol precise decomposition on survivors. Efficient allocation of analytical effort. |
| sensitivity-analysis | Sensitivity Analysis Campaign 鈥?identify which assumptions are most critical by measuring their impact on conclusions. 5 strategies (parameter-screening, variance-decomposition, assumption-criticality, uncertainty-propagation, decision-sensitivity), 3 tactics, 11 subagent SOPs. |
| sensitivity-synthesis | Synthesize all sensitivity analysis results into a coherent report with prioritized recommendations. |
| sobol-decomposition | Sobol variance decomposition 鈥?compute first-order and total-order sensitivity indices for precise variance attribution. |
| socratic-probing | Apply 6 types of Socratic questions to test claims and assumptions. Exposes weaknesses and strengthens reasoning. |
| stakeholder-confirmation | Simulate stakeholder perspectives to validate gap priorities. Assesses gap value from researcher, practitioner, funder, and end-user viewpoints. |
| stakeholder-mapping | Map all affected parties using CSH 12-question framework, identify jobs-to-be-done, classify by salience. Reveals whose perspective is systematically excluded. |
| systematic-perturbation | Multi-axis systematic perturbation 鈥?define variation axes, perturb along each, measure degradation, construct validity envelope. |
| temporal-sensitivity-testing | Test whether a gap persists across different time windows (2/5/10 years). Determines if gap is narrowing, widening, or stable over time. |
| tension-mining | Identify opposing forces that keep gaps open. Uses evaporating cloud to expose hidden assumptions behind conflicts and polarity mapping for unresolvable tensions. |
| uncertainty-cascade | Uncertainty cascade propagation 鈥?assign input distributions, sample via Monte Carlo, propagate through model, analyze output distribution, identify critical paths. Maps how input uncertainty flows to output uncertainty. |
| uncertainty-propagation | Propagate input uncertainties through the model via Monte Carlo sampling. Identifies which input uncertainties contribute most to output uncertainty. |
| validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| validity-envelope-mapping | Map multi-dimensional validity envelopes 鈥?define variation axes, perturb systematically, measure degradation, construct boundary surface. |
| variance-decomposition | Sobol variance decomposition 鈥?compute first-order and total-order sensitivity indices to quantify each parameter's contribution to output variance. |
| variation-axis-definition | Identify orthogonal axes along which a method's validity might vary. Ensures axes are independent, measurable, and span the relevant parameter space. |
| web-research | Deep web research with full page fetching via Apify. Import of web-browsing/web-research skill. Must fetch full page 鈥?no conclusions from previews. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only 鈥?no conclusions from snippets alone. |
| wickedness-assessment | Apply Rittel's 10 criteria to determine if the problem is tame, complex, or wicked, and adjust research strategy accordingly. |
| wickedness-scoring | Score a problem against Rittel's 10 criteria to determine if it is tame, complex, or wicked. |

## hypothesis-formation (72 skills)

| Skill | Description |
|-------|-------------|
| abductive-hypothesis-generation | "Strategy: 闈㈠寮傚父鐨勬渶浣宠В閲婃帹鐞? |
| ahp-weighting | "SOP: 浣跨敤 AHP 灞傛鍒嗘瀽娉曠‘瀹氳瘎鍒嗙淮搴︽潈閲嶏紝杈撳嚭鏉冮噸鍚戦噺" |
| ahrq-picme-assessment | "SOP: 浣跨敤 AHRQ PiCMe 妗嗘灦瀵圭爺绌?gap 杩涜 6 缁村害绯荤粺璇勪及" |
| anomaly-characterization | "SOP: 鎻忚堪鍜屽垎绫绘棤娉曡鐜版湁鐞嗚瑙ｉ噴鐨勫紓甯哥幇璞? |
| anomaly-driven-abduction | "Tactic: 褰掔撼/婧洜璺緞鈥斺€旀弿杩板紓甯哥幇璞★紝鐢熸垚鍊欓€夎В閲婏紝鎸夊彲淇″害鎺掑簭" |
| answering-sequence-design | "SOP: 璁捐瀛愰棶棰樼殑鏈€浼樺洖绛旈『搴? |
| boundary-condition-specification | "SOP: 鎸囧畾鍋囪鎴愮珛鐨勮竟鐣屾潯浠? |
| comparative-formulation | "Strategy: 鏋勫缓瀵规瘮鎬х爺绌堕棶棰?鈥?A vs B 鐨勭郴缁熷寲姣旇緝" |
| competing-hypothesis-construction | "Strategy: 涓哄悓涓€鐜拌薄鏋勫缓澶氫釜绔炰簤鍋囪" |
| competing-hypothesis-generation | "SOP: 涓哄悓涓€鐜拌薄鐢熸垚鏈哄埗涓婁笉鍚岀殑绔炰簤鍋囪" |
| competing-hypothesis-matrix | "Tactic: 澶氬亣璁剧鐞嗏€斺€旂敓鎴愮珵浜夊亣璁撅紝璁捐鍖哄垎鎬ч娴嬶紝鏋勫缓缁撴瀯鍖栨瘮杈冪煩闃? |
| consistency-check | "SOP: 妫€楠?pairwise 鍒ゆ柇鐭╅樀鐨勪紶閫掍竴鑷存€э紝璇嗗埆涓嶄竴鑷撮」骞跺缓璁慨姝? |
| decomposition-formulation | "Strategy: 灏嗗鏉傜爺绌堕棶棰樺垎瑙ｄ负鍙嫭绔嬪洖绛旂殑瀛愰棶棰樺眰绾? |
| deductive-hypothesis-generation | "Strategy: 浠庣幇鏈夌悊璁烘紨缁庢帹瀵煎亣璁? |
| dependency-mapping | "SOP: 鏄犲皠瀛愰棶棰橀棿鐨勪緷璧栧叧绯? |
| discriminating-prediction-design | "SOP: 璁捐鑳藉尯鍒嗙珵浜夊亣璁剧殑鍏抽敭棰勬祴鍜岃瀵熸柟妗? |
| eclipse-application | "SOP: 搴旂敤 ECLIPSE 妗嗘灦缁撴瀯鍖栨贩鍚堟柟娉曠爺绌堕棶棰? |
| evidence-based-prioritization | "Strategy: 鍩轰簬璇佹嵁寮哄害鐨?AHRQ PiCMe 璇勪及鈥斺€旂敤鏂囩尞璇佹嵁璐ㄩ噺椹卞姩 gap 浼樺厛绾? |
| explanation-generation | "SOP: 涓哄紓甯哥幇璞＄敓鎴愬€欓€夎В閲婂垪琛? |
| falsifiability-audit | "Tactic: 鍋囪璐ㄩ噺淇濊瘉鈥斺€旀楠屽彲璇佷吉鎬э紝淇涓嶅悎鏍煎亣璁撅紝瀹屾垚鎿嶄綔鍖栦笌杈圭晫鏉′欢瑙勮寖" |
| falsifiability-check | "SOP: 妫€楠屽亣璁炬槸鍚︽弧瓒冲彲璇佷吉鎬ф爣鍑? |
| feasibility-constrained-formulation | "Strategy: 鍦ㄨ祫婧愮害鏉熶笅閲嶅鐮旂┒闂 鈥?pragmatic 璋冩暣淇濇寔鏍稿績浠峰€? |
| feasibility-scoring | "SOP: 璇勪及鐮旂┒ gap 鐨勫彲鏀诲嚮鎬э紝璇嗗埆鐡堕骞惰緭鍑哄彲琛屾€ц瘎鍒? |
| finer-criteria-check | "SOP: FINER 5 椤规爣鍑嗛€愰」妫€楠岀爺绌堕棶棰樿川閲? |
| framework-guided-formulation | "Strategy: 閫夋嫨 RQ 妗嗘灦锛圥ICO/SPIDER/SPICE/ECLIPSE锛夊苟绯荤粺搴旂敤" |
| framework-matching | "SOP: 鏍规嵁鐮旂┒绫诲瀷鍖归厤鏈€閫傚悎鐨?RQ 妗嗘灦" |
| framework-selection-and-application | "Tactic: 閫夋嫨鏈€閫傚悎鐨?RQ 妗嗘灦骞剁郴缁熷簲鐢? |
| gap-normalization | "SOP: 缁熶竴涓嶅悓鏉ユ簮鐨?gap 鏍煎紡涓烘爣鍑?GapRecord" |
| gap-pairwise-judgment | "SOP: 瀵逛袱涓?gap 杩涜閫愭爣鍑嗙浉瀵逛紭鍏堢骇鍒ゆ柇锛岃緭鍑哄亸濂界粨鏋? |
| gap-prioritization | "Campaign: 绯荤粺鍖栬瘎浼板拰鎺掑簭鐮旂┒ gaps锛岀‘瀹氭渶鍊煎緱鏀诲嚮鐨勭洰鏍? |
| hypothesis-comparison-matrix | "SOP: 鏋勫缓绔炰簤鍋囪鐨勫缁村害瀵规瘮鐭╅樀" |
| hypothesis-formulation | "Campaign: 灏?insight 鍜?gap 杞寲涓虹粨鏋勫寲鐨勫彲娴嬭瘯鍋囪" |
| hypothesis-operationalization | "Strategy: 灏?working hypothesis 绮剧‘鍖栦负鍙祴璇曞舰寮? |
| hypothesis-synthesis | "SOP: 缁煎悎鎵€鏈変腑闂翠骇鐗╋紝浜у嚭鏈€缁堢粨鏋勫寲鍋囪闆? |
| impact-scoring | "SOP: 璇勪及鐮旂┒ gap 鐨勬綔鍦ㄥ奖鍝嶅姏锛岃瘑鍒彈鐩婃柟骞惰緭鍑哄奖鍝嶅姏璇勫垎" |
| importance-scoring | "SOP: 璇勪及鐮旂┒ gap 鐨勫鏈笌瀹炶返閲嶈鎬э紝杈撳嚭 1-5 鍒嗗強渚濇嵁" |
| inductive-hypothesis-generation | "Strategy: 浠庢暟鎹?瑙傚療褰掔撼鎻愮偧鍋囪" |
| mechanism-extraction | "SOP: 浠庣悊璁轰腑鎻愬彇鍥犳灉鏈哄埗閾? |
| multi-criteria-ranking | "Strategy: 澶氱淮搴﹀姞鏉冭瘎鍒嗘帓搴忊€斺€斿皢 gap 鍒嗚В涓虹嫭绔嬪瓙闂鍚庨噸缁勪负浼樺厛绾у垪琛? |
| novelty-scoring | "SOP: 璇勪及鐮旂┒ gap 鐨勬柊棰栨€ф綔鍔涳紝璇嗗埆宸紓鍖栨柟鍚戝苟杈撳嚭璇勫垎" |
| operationalization | "SOP: 灏嗘娊璞℃蹇垫搷浣滃寲涓哄彲娴嬮噺鐨勬寚鏍囧拰鏂规硶" |
| pairwise-comparison | "Tactic: 閫氳繃鐩稿姣旇緝鑰岄潪缁濆璇勫垎瀵?gaps 杩涜鎺掑簭锛岄€傜敤浜庨毦浠ラ噺鍖栫殑鍦烘櫙" |
| paper-overview | "Import SOP: 璁烘枃蹇€熸壂鎻忥紝杩斿洖 abstract 鍜?metadata锛堟潵鑷?literature-engine锛? |
| paper-research | "Import SOP: 娣卞害鏂囩尞鐮旂┒锛屽師濮嬪叏鏂?+ PDF 闂瓟锛堟潵鑷?literature-engine锛? |
| paper-search | "Import SOP: 涓繁搴︽枃鐚悳绱紝AI 鎽樿鎶ュ憡锛堟潵鑷?literature-engine锛? |
| pico-application | "SOP: 搴旂敤 PICO/PICOTS 妗嗘灦缁撴瀯鍖栫爺绌堕棶棰? |
| plausibility-ranking | "SOP: 瀵瑰€欓€夎В閲婃寜鍚堢悊鎬ц繘琛屽缁村害鍔犳潈鎺掑簭" |
| portfolio-optimization | "Strategy: gap 缁勫悎瑙嗕负鎶曡祫缁勫悎鈥斺€旂敤椋庨櫓/鏀剁泭/澶氭牱鎬т紭鍖栭€夊嚭鏈€浼?gap 缁勫悎" |
| priority-sensitivity-testing | "Tactic: 鎵板姩璇勫垎鏉冮噸锛屾楠?gap 鎺掑簭瀵规潈閲嶉€夋嫨鐨勭ǔ鍋ユ€? |
| priority-synthesis | "SOP: 缁煎悎鎵€鏈夎瘎鍒嗘暟鎹骇鍑烘渶缁?gap 浼樺厛绾у垪琛ㄥ強鏀诲嚮璺緞寤鸿" |
| quality-gate-check | "Shared SOP: 閫氱敤璐ㄩ噺闂ㄦ鏌ワ紙鏍煎紡瀹屾暣鎬с€侀€昏緫涓€鑷存€э級" |
| question-refinement-loop | "Tactic: 杩唬绮惧寲鐮旂┒闂鐩村埌閫氳繃 FINER 5 椤规爣鍑? |
| question-synthesis | "SOP: 缁煎悎鎵€鏈変腑闂翠骇鐗╀骇鍑烘渶缁堢爺绌堕棶棰橀泦" |
| rapid-triage | "Strategy: 蹇€熺矖绛涒€斺€斾袱杞繃婊ゅ皢澶ч噺 gaps 鍘嬬缉涓哄彲绮炬帓鐨勫€欓€夐泦" |
| relationship-specification | "SOP: 鎸囧畾鍙橀噺闂村叧绯荤殑鏂瑰悜涓庡舰寮? |
| research-question | "Campaign: 灏嗗亣璁剧粏鍖栦负绮剧‘鐨勩€佹鏋跺寲鐨勭爺绌堕棶棰? |
| saturation-detection | "Shared SOP: 鍒ゆ柇褰撳墠娲诲姩鏄惁宸茶揪淇℃伅楗卞拰" |
| scope-assessment | "SOP: 璇勪及鐮旂┒闂鐨勮寖鍥存槸鍚﹀悎閫傦紙澶/鍚堥€?澶獎锛? |
| scope-calibration | "Strategy: 璋冩暣鐮旂┒闂鑼冨洿 鈥?zoom in/out 鐩村埌鑼冨洿鍚堥€? |
| scoring-matrix-construction | "Tactic: 缂栨帓澶氱淮搴﹁瘎鍒?SOP锛屼负鎵€鏈?gaps 鏋勫缓缁煎悎璇勪及鐭╅樀" |
| spice-application | "SOP: 搴旂敤 SPICE 妗嗘灦缁撴瀯鍖栬瘎浼扮爺绌堕棶棰? |
| spider-application | "SOP: 搴旂敤 SPIDER 妗嗘灦缁撴瀯鍖栧畾鎬х爺绌堕棶棰? |
| stakeholder-weighted-ranking | "Strategy: 鎸夊埄鐩婄浉鍏宠€呰瑙掑姞鏉冣€斺€斿悓涓€ gap 鍦ㄤ笉鍚岃瑙掍笅鏉冮噸涓嶅悓锛屾渶缁堝彇鍏辫瘑鎺掑簭" |
| sub-question-decomposition | "Tactic: 灏嗕富闂鍒嗚В涓哄彲鐙珛鍥炵瓟鐨勫瓙闂灞傜骇" |
| sub-question-generation | "SOP: 灏嗕富鐮旂┒闂鍒嗚В涓哄彲鐙珛鍥炵瓟鐨勫瓙闂" |
| success-criteria-definition | "SOP: 涓虹爺绌堕棶棰樺畾涔夊彲娴嬮噺鐨勬垚鍔熸爣鍑? |
| theory-identification | "SOP: 璇嗗埆涓庣爺绌秅ap鐩稿叧鐨勭悊璁烘鏋? |
| theory-mechanism-extraction | "Tactic: 婕旂粠璺緞鏍稿績鈥斺€斾粠鐞嗚鍑哄彂鎻愬彇鏈哄埗銆佸彉閲忎笌鍏崇郴锛岀敓鎴愬亣璁惧€欓€? |
| variable-identification | "SOP: 璇嗗埆鍙橀噺鍙婂叾鍦ㄥ亣璁句腑鐨勮鑹? |
| web-research | "Import SOP: 娣卞害 web 鐮旂┒锛屽叏鏂囨姄鍙栧垎鏋愶紙鏉ヨ嚜 web-browsing锛? |
| web-search | "Import SOP: 蹇€?web 鎵弿锛屽彂鐜?URL 鍜?snippet锛堟潵鑷?web-browsing锛? |
| weight-perturbation | "SOP: 鎵板姩鏉冮噸妫€楠?gap 鎺掑簭绋冲畾鎬э紝杈撳嚭绋冲畾鎬у垽瀹? |

## creative-ideation (188 skills)

| Skill | Description |
|-------|-------------|
| ablation-brainstorm | Remove components one by one, observe system changes to reveal hidden dependencies and generate ideas from structural gaps. |
| ablation-execution | Remove components one by one from a system, record the response/impact of each removal. |
| abstraction-extraction | Extract abstract principles from concrete domain cases. Strips domain-specific details to reveal transferable mechanisms. |
| abstraction-ladder | Perform bisociation at multiple abstraction levels |
| abstraction-to-design | "Abstract biological principle to design principle. Bridge from biology to engineering." |
| alternatives-generation | Generate alternatives for every known approach 鈥?ensure no approach goes unchallenged. |
| analogical-transfer | Systematic structure-mapping from source to target domain (Gentner). Identify relational correspondences and transfer higher-order constraints. |
| analogy-chain | Chain analogies to deeper levels (3-5 layers). Each layer reveals new aspects and insights not visible at the surface. |
| analogy-extraction | Extract transferable structural principles from source domains. Orchestrates source identification 鈫?abstraction 鈫?structural mapping 鈫?transfer validation. |
| analogy-quality-assessment | Assess analogy depth (surface/structural/systemic). Determines whether an analogy warrants transfer investment. |
| anti-benchmark | Challenge industry best practices' hidden assumptions. Deconstruct benchmarks to reveal unexamined constraints. |
| assumption-destruction | Assumption Destruction Campaign 鈥?open new solution spaces by negating, reversing, and challenging fundamental assumptions. |
| assumption-enumeration | Surface, perturb, and prioritize assumptions by disruption potential. Orchestrates assumption surfacing 鈫?perturbation 鈫?sacred cow identification 鈫?prioritization. |
| assumption-perturbation | Perturb each assumption, observe system response. Systematic stress-testing of assumptions to reveal fragility and opportunity. |
| assumption-surfacing | Enumerate implicit assumptions in a problem statement or existing solution. Produces categorized assumption inventory (physical, social, temporal, economic, technical). |
| axiom-negation | Identify and suspend fundamental assumptions via de Bono PO. Systematically negate axioms to reveal hidden solution spaces. |
| benchmark-challenge | Identify and negate benchmark assumptions. Deconstruct best practices to reveal hidden constraints and open new spaces. |
| benchmark-inventory | Catalog all known solutions/methods in a domain with performance, applicability, and limitations. |
| benchmark-sweep | Systematically scan all known solutions, identify gaps in coverage and unexplored regions of the solution space. |
| biological-function-mapping | "Map technical functions to biological systems. Orchestrates problem-biologization 鈫?organism-discovery 鈫?functional-model-biology." |
| biological-strategy-extraction | "Extract strategy principles from organisms. Identify mechanism-level details of how biological systems achieve their function." |
| biologize-and-discover | "Biomimicry Design Spiral: Define鈫払iologize鈫扗iscover鈫扐bstract鈫扙mulate. Translate technical challenges into biological questions and find nature's solutions." |
| biomimicry | Biomimicry Campaign 鈥?discover transferable solutions from biological systems via Design Spiral, BioTRIZ, functional analogy, ecosystem patterns, and evolution strategies. |
| biomimicry-synthesis | "Synthesize all biomimicry outputs into a structured idea report. Integrate biological strategies, design principles, and technical solutions." |
| biotriz-principle-selection | "Select applicable BioTRIZ principles for a given contradiction. Map to biological cases." |
| biotriz-resolution | "BioTRIZ: biological 40 principles + bio contradiction matrix. Resolve technical contradictions using biological inventive principles." |
| bisociation-network-construction | Build multi-domain bridging concept network. Creates a network of collision points between multiple thinking matrices. |
| blend-completion | Complete blend with background knowledge |
| blend-composition | Compose new connections in blended space |
| blend-construction | Construct complete 4-space blends with emergent structure. Orchestrates input-space-construction 鈫?generic-space-extraction 鈫?blend-composition. |
| blend-elaboration | Run blend as mental simulation |
| bridge-validation | Validate analogy depth and transfer viability. Ensures only deep structural analogies (not surface-level similarities) proceed to transfer. |
| challenge-operation | "Non-threatening 'Why?' questioning of current practices (de Bono Challenge)" |
| challenge-questioning | "Non-threatening 'Why?' questioning of current practices to reveal historical accidents vs. genuine constraints." |
| combination-evaluation | Evaluate new combinations for feasibility and novelty |
| combination-mapping | Systematically enumerate parameter dimensions and generate viable combinations. Orchestrates parameter extraction 鈫?value enumeration 鈫?compatibility assessment 鈫?synthesis. |
| combinatorial-creativity | Combinatorial Creativity Campaign 鈥?produce emergent concepts via concept blending, multi-level bisociation, and function combination (Fauconnier-Turner) |
| combinatorial-synthesis | Synthesize all combinatorial creativity outputs |
| competitor-simulation | Competitor perspective 鈥?design strategies to defeat this solution, then use attack vectors to improve it. |
| component-decomposition | Decompose system into functional components, identify dependencies, and surface trimming candidates. |
| component-surgery | Component-level surgical operations (subtract/multiply/divide/unify/redirect) from Systematic Inventive Thinking (SIT). |
| compressed-conflict | Generate compressed conflicts (oxymorons) from problem contradictions and extract concrete idea directions from the symbolic tension. |
| concept-blending | "Fauconnier-Turner 4-space model: Generic + Input1 + Input2 鈫?Blended Space" |
| concept-fan | "Expand from purpose to concepts to directions to ideas (de Bono Concept Fan)" |
| concept-fan-expansion | Expand concept fan from purpose through concepts to directions to ideas (de Bono Concept Fan). |
| concept-hierarchy | Build concept levels from purpose through concepts to ideas, with escape and fractionation at each level. |
| consistency-checking | Pairwise consistency evaluation to reduce solution space by identifying and removing inconsistent combinations. |
| consistency-pair-evaluation | Evaluate pairwise value consistency (logical/empirical/normative) |
| constraint-driven-ideation | Inject extreme constraints to force innovation 鈥?impossibility breeds creativity. |
| constraint-injection | Inject artificial constraints to force creative divergence. Generates and applies constraints (resource, time, material, audience, scale) to existing ideas to produce variants. |
| constraint-protocol | Inject constraints 鈫?force creative response 鈫?extract transferable principles. Orchestrates constraint injection, response generation, and principle extraction. |
| constraint-response | Generate creative solutions under extreme constraints 鈥?no "impossible" allowed, find a way. |
| constructive-rebellion | Build constructive alternatives from destructive negation. Transform violated assumptions into viable innovation directions. |
| contradiction-identification | Identify technical and physical contradictions in a system through functional modeling and matrix analysis. |
| contradiction-matrix-lookup | Query the 39x39 TRIZ contradiction matrix to find recommended inventive principles for a given technical contradiction. |
| coverage-analysis | Systematic coverage evaluation pipeline 鈥?benchmark inventory, method-problem crossing, and intersection evaluation to map explored vs unexplored solution space. |
| coverage-gap-detection | Detect uncovered regions in the solution space, producing a prioritized gap list. |
| cross-consistency-analysis | "CCA: pairwise consistency checking to reduce solution space 90-99%" |
| cross-domain-discovery | Cross-Domain Discovery Campaign 鈥?find transferable mechanisms from unrelated fields via bisociation, analogical transfer, random stimulus, and forced bridging |
| cross-domain-synthesis | Synthesize all cross-domain findings into a structured idea report. Integrates outputs from all strategies and SOPs. |
| dependency-identification | Identify critical dependencies from ablation results, producing a dependency graph and highlighting critical components. |
| design-by-analogy | "Complete DBA process: problem reframe 鈫?source search 鈫?map 鈫?transfer 鈫?adapt. Full Design-by-Analogy methodology for systematic analogical design." |
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
| emergence-detection | Detect and validate emergent properties from combinations. Orchestrates emergent-property-identification 鈫?blend-elaboration. |
| emergent-property-hunting | Seek properties that emerge from combination (non-additive) |
| emergent-property-identification | Identify non-additive properties from combinations |
| emulation-generation | "Generate technical solutions emulating biological strategies. Bridge from design principle to concrete implementation." |
| enumeration-synthesis | Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations. |
| escape-technique | Identify dominant thinking pattern and escape it via deliberate pattern-breaking. |
| evaluation-filtering | Multi-dimensional evaluation and tiered filtering of generated ideas. Orchestrates novelty assessment 鈫?feasibility check 鈫?ranking 鈫?selection. |
| evolution-mechanism-transfer | "Map evolution mechanisms to design operations. Translate selection, mutation, drift, radiation into design operators." |
| evolution-strategy | "Use evolution mechanisms (selection, mutation, radiation) as design operators for generating and refining solution populations." |
| excursion-departure | Leave the problem entirely and explore an unrelated domain. Produces excursion domain discoveries for later force-fitting. |
| excursion-method | Full 8-stage Gordon-Prince excursion process. Deliberate departure from the problem into unrelated domains, then force-fit discoveries back. |
| excursion-orchestration | Orchestrate the excursion sequence 鈥?departure into unrelated domain, force-fit discoveries back to problem, launch springboard ideas. |
| facet-bisociation | Bridge two unrelated thinking matrices via Koestler bisociation. Identify independent frames of reference and force collision to produce creative insight. |
| factorial-ideation | "DOE thinking: identify factors, define levels, and explore combinations to systematically cover the design space." |
| factor-level-design | Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration. |
| failure-driven-generation | Generate targeted solutions for each identified failure mode, ensuring every failure has at least one proposed mitigation. |
| failure-mode-cataloging | Systematically catalog all failure modes in a domain or method, producing a classified failure taxonomy. |
| failure-taxonomy | Catalog all failure modes in a domain, classify them systematically, and generate targeted solutions for each failure type. |
| fantasy-analogy | Wish-fulfillment thinking 鈥?ignore physical laws for ideal solution. Use unconstrained imagination to reveal what the problem truly needs. |
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
| gap-driven-generation | Generate solutions targeting specific coverage gaps 鈥?detect gaps, generate failure-driven solutions, and design factor-level experiments. |
| general-morphological-analysis | "Ritchey GMA: complete iterative morphological process" |
| generic-space-extraction | Extract shared abstract structure from two input spaces |
| green-hat-session | Structured creative thinking in Six Hats Green Hat mode 鈥?pure creative output with judgment suspended. |
| idea-synthesis | Synthesize diverse ideas into coherent solution concepts. Combines fragments from multiple ideation passes into structured, actionable ideas with clear mechanism descriptions. |
| input-space-construction | Build input spaces for two source concepts |
| intersection-evaluation | Evaluate exploration status of each cell in a method脳problem matrix, annotating as explored, partial, or unexplored. |
| inversion-extraction | Extract constructive insights from worst solutions. Transform failure analysis into innovation directions. |
| inversion-protocol | Reverse statements 鈫?extract insights 鈫?build constructive alternatives. Systematic inversion pipeline from negation to innovation. |
| lateral-synthesis | Synthesize all lateral thinking intermediate outputs into a structured idea report. |
| lateral-thinking | Lateral Thinking Campaign 鈥?escape logical thinking tracks via PO/movement, random entry, concept fan, challenge, and six hats (de Bono) |
| life-principles-application | "Apply life's principles as design constraints. Orchestrates ecosystem-pattern-extraction 鈫?evolution-mechanism-transfer 鈫?abstraction-to-design." |
| matrix-construction | Build n-dimensional morphological matrix |
| method-problem-crossing | Build method脳problem cross-reference matrix showing which methods have been applied to which problems. |
| method-problem-matrix | Cross method脳problem matrix, find unexplored intersections where known methods have not been applied to known problems. |
| morphological-exploration | Morphological Exploration Campaign 鈥?systematic dimension-combination enumeration to discover unexplored solution spaces via Zwicky box, CCA, and GMA |
| morphological-synthesis | Synthesize all morphological exploration outputs |
| movement-extraction | Extract constructive directions from provocations via 4 movement types (moment-to-moment, principle, focus difference, positive aspects). |
| movement-operation | Extract constructive directions from PO provocations using 4 movement types (moment-to-moment, principle, focus difference, positive aspects). |
| multi-level-bisociation | Simultaneous concept collision at multiple abstraction levels |
| novelty-scoring | Score ideas on novelty dimensions 鈥?structural distance from known solutions, conceptual surprise, domain-crossing depth. Produces ranked novelty assessment. |
| novice-perspective | Novice perspective 鈥?question the 'obvious' by adopting deliberate ignorance to reveal hidden complexity. |
| organism-discovery | "Find organisms solving similar problems. Search across kingdoms for biological champions." |
| paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only 鈥?no methodology conclusions from abstracts. |
| paper-research | Deep paper analysis with full text reading. Import of literature-engine/literature-research skill. Full text access 鈥?required for quoting results, verifying claims, extracting detailed methodology. |
| paper-search | Mid-depth paper analysis via AI-generated summaries. Import of literature-engine/literature-search skill. Reads AI summary 鈥?sufficient for methodology understanding but not for quoting specific results. |
| parameter-identification | Identify the key parameters/dimensions of a problem space. Produces a structured parameter list with value ranges for morphological analysis. |
| parameter-variation | Systematic one-factor-at-a-time parameter sweep |
| path-generation | Generate combination paths through consistent space |
| personal-analogy | Empathic identification 鈥?become the system/component. First-person embodiment to discover hidden constraints and opportunities. |
| personal-identification | First-person empathic identification with a system or component. Produces experience description and design insights from embodiment. |
| perspective-forcing | Perspective Forcing Campaign 鈥?discover hidden solutions by systematically switching viewpoints via roles, six hats, temporal projection, and constraint injection |
| perspective-rotation | Rotate through reviewer/practitioner/theorist/time-machine/novice perspectives systematically. Ensures comprehensive viewpoint coverage. |
| perspective-synthesis | Synthesize all perspective outputs into a structured multi-perspective idea report. |
| po-provocation | Generate PO (Provocative Operation) statements per de Bono's lateral thinking. Creates deliberately illogical provocations to escape dominant thinking patterns. |
| practitioner-hat | Engineer perspective 鈥?assess buildability, cost, timeline, and integration challenges. |
| problem-biologization | "Restate technical problem as biological question. Translate engineering challenges into nature's language." |
| provocation-and-movement | "PO + Movement: generate provocations then extract useful directions (4 movement types)" |
| provocation-generation | Generate PO provocations and extract constructive movement. Orchestrates assumption surfacing 鈫?provocation creation 鈫?movement extraction 鈫?idea formation. |
| random-entry | "Random word/concept as thinking entry point (de Bono Random Entry)" |
| random-paper-entry | Select random paper facet as creative stimulus. Uses genuine randomness in paper selection to break domain fixation. |
| random-stimulus-entry | Random word/paper/concept as thinking entry point. Use genuine randomness to escape fixation and open unexpected solution paths. |
| random-word-stimulus | Use random word/concept injection as creative stimulus. Selects random concepts and forces connection to the problem space, generating unexpected solution paths. |
| recombination-architecture | Reassemble decomposed fragments into novel structures through systematic recombination of components. |
| recombination-generation | Reassemble decomposed system fragments into novel structural arrangements that create emergent value. |
| reversal-generation | Systematically reverse positive statements to generate creative inversions. Produces reversed statements with initial associations. |
| reverse-brainstorming | How to make it worse? 鈫?reverse for solutions. Generate anti-solutions then invert to discover novel approaches. |
| reviewer2-hat | Hostile reviewer perspective 鈥?find fatal flaws, logical gaps, and missing evidence in a solution. |
| role-based-ideation | Role-play as reviewer/practitioner/theorist/novice/competitor to generate diverse perspectives on a solution. |
| sacred-cow-hunting | Find and challenge domain's unquestioned beliefs. Systematic identification and productive violation of dogma. |
| sacred-cow-identification | Find domain's unquestioned beliefs. Systematic identification of dogma that constrains innovation. |
| saturation-detection | Determine when additional ideation yields diminishing returns. Analyzes latest idea batch against existing corpus to judge continue/near-saturation/saturated. |
| scamper-divergence | Execute SCAMPER 7 operators on a target solution. Subagent self-selects best 2-3 operators for deepest exploration. |
| scamper-transformation | 7 operators (Substitute/Combine/Adapt/Modify/Put/Eliminate/Reverse) for systematic transformation of existing solutions. |
| separation-principle | Apply time/space/condition/scale separation to resolve physical contradictions where the same parameter must satisfy opposing requirements. |
| six-hats-ideation | "Green Hat focused creative thinking within Six Hats framework" |
| six-hats-rotation | Complete Six Hats rotation (White鈫扲ed鈫払lack鈫扽ellow鈫扜reen鈫払lue) to force systematic perspective diversity. |
| solution-space-reduction | Apply CCA to remove inconsistent combinations |
| springboard-launch | Convert analogy insights into concrete feasible solutions. Transform abstract connections into actionable mechanisms. |
| stakeholder-simulation | Simulate user/engineer/investor/regulator/society perspectives to surface hidden requirements and opportunities. |
| stepping-stone | Use impractical ideas as stepping stones to reach practical solutions (de Bono Stepping Stone technique). |
| structural-deconstruction | Decompose systems into components and reassemble via SCAMPER, SIT, TRIZ, and recombination. Campaign orchestrating 5 strategies for systematic structural transformation. |
| structural-mapping | Map source鈫抰arget structural correspondences. Identifies corresponding, missing, and extra elements between domains. |
| structural-synthesis | Synthesize all structural transformation outputs into a coherent, ranked idea report with lineage tracking. |
| surgery-operation | Execute component surgery operations (subtract/multiply/divide/unify/redirect) from Systematic Inventive Thinking. |
| symbolic-analogy | Compress core contradiction into poetic imagery/oxymoron. Use compressed conflicts to reveal hidden solution directions. |
| symbolic-compression | Compress problem contradiction into 2-3 word oxymoron. Produces oxymorons with interpretation directions for each. |
| synectics | Synectics Campaign 鈥?systematic use of analogy and metaphor for breakthrough associations via Gordon's 4 analogy types and excursion method. |
| synectics-synthesis | Synthesize all synectics outputs into a structured idea report. Combines results from all analogy types and excursion processes. |
| systematic-enumeration | Systematic Enumeration Campaign 鈥?exhaustive coverage analysis to discover overlooked solution spaces via benchmark sweep, method-problem matrix, ablation, and failure taxonomy |
| temporal-projection | View problem from 5yr/50yr/500yr future, backcast to generate temporally-informed creative solutions. |
| theorist-hat | Theorist perspective 鈥?assess theoretical foundations, formal rigor, and formalization opportunities. |
| time-machine | Temporal projection 鈥?view a solution from future/past time horizons to generate temporally-informed insights. |
| transfer-adaptation | Adapt transferred principle to target problem constraints. Produces concrete adapted solutions from abstract principles. |
| trimming-execution | Progressively remove components from a system while verifying function preservation through redistribution. |
| triz-contradiction-resolution | Resolve technical and physical contradictions via TRIZ 40 inventive principles and separation methods. |
| triz-principle-application | Select inventive principles from the contradiction matrix and generate concrete solutions for identified contradictions. |
| value-enumeration | Enumerate 3-5 values per parameter including extremes |
| vital-relation-mapping | Map 15 vital relations between concepts |
| web-research | Deep web page analysis with full content extraction. Import of web-browsing/web-research skill. Must fetch full page via apify 鈥?no shortcuts. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only 鈥?no conclusions from snippets alone. |
| white-space-detection | Identify matrix regions not covered by existing methods |
| white-space-identification | Identify unexplored viable regions in the morphological matrix where no existing methods operate. |
| worst-case-design | Design the worst possible solution. Deliberate failure engineering to reveal hidden constraints and inversion opportunities. |
| worst-method-inversion | Design worst possible solution 鈫?extract insights 鈫?invert. Deliberate failure design as creative catalyst. |
| zwicky-box-construction | "Classic Zwicky box: parameter identification 鈫?value enumeration 鈫?matrix construction" |

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
| assumption-extraction | Systematically surface hidden assumptions underlying a decision with confidence levels. |
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
| feasibility-assessment | Feasibility Assessment Campaign 鈥?evaluate whether selected candidates can actually be implemented using TRL, NASSS, Stage-Gate, TRIZ, TOC, and parametric estimation methods. |
| feasibility-synthesis | Synthesize all assessments into a feasibility matrix, recommendation, and risk summary. |
| feedback-distribution | Create anonymized feedback report summarizing group judgment distribution for a given round. |
| full-ranking | Produce a complete ordering of all candidates using PROMETHEE I/II, ELECTRE III, or MAVT methods. |
| futures-calibration | Aggregate probability judgments across perspectives using Real-Time Delphi or prediction market mechanisms. |
| gate-criteria-definition | Define gate criteria and pass thresholds for a specific stage in the Stage-Gate process. |
| gate-judgment | Evaluate a candidate against gate criteria and render GO/KILL/RECYCLE verdict with evidence. |
| inconsistency-localization | Identify which specific comparison pairs are most responsible for preference cycles and inconsistencies. |
| iterative-convergence-round | Execute one full Delphi round 鈥?collect judgments, distribute anonymous feedback, measure consensus, decide whether to continue. |
| judge-verdict | Render an impartial verdict on advocate case vs critic attacks with explicit reasoning. |
| judgment-collection | Collect independent judgments from all perspectives on a given question. |
| maturation-pathway-design | Design path to readiness using Stage-Gate, Technology Roadmapping, and milestone planning methods. |
| maturity-diagnosis | Assess current readiness of candidates using TRL 9-level, NASSS 7-dimension, and Innovation Readiness Level frameworks. |
| method-sensitivity-report | Analyze how the choice of MCDA method affects final rankings and identify method-sensitive alternatives. |
| multi-criteria-scoring | Multi-Criteria Scoring Campaign 鈥?evaluate and rank candidates against multiple weighted criteria using AHP, BWM, TOPSIS, VIKOR, ELECTRE, PROMETHEE, MAUT methods. |
| multi-dimensional-readiness-scan | Assess readiness across multiple dimensions, synthesize into radar visualization, and identify bottleneck dimensions. |
| multi-judge-aggregation | Collect independent rankings from multiple judges, aggregate using social choice methods, and identify disagreement hotspots. |
| multi-method-triangulation | Apply 2-3 MCDA methods to the same candidates, compare rankings, and identify method-sensitive options. |
| multi-perspective-attack | Assign distinct perspectives to attack a decision from multiple angles, then synthesize findings into a unified assessment. |
| multi-stakeholder-simulation | Simulates diverse stakeholder perspectives and their strongest objections/support arguments. Shared across steel-manning and consensus campaigns. |
| niche-coverage-analysis | Define niches within the solution space, map candidates to niches, score coverage completeness, and identify gaps requiring attention. |
| niche-definition | Define niches and capability areas that a portfolio should cover based on domain structure and objectives. |
| niche-mapping | Map each candidate to the niches it covers, indicating strength of coverage for each assignment. |
| non-compensatory-screening | Eliminate non-qualifying candidates using conjunctive rules, dominance filtering, lexicographic ordering, or veto thresholds. |
| normalization | Normalize a score matrix using a specified method to make scores comparable across criteria. |
| objective-definition | Define optimization objectives, constraints, and trade-off preferences from context and candidate information. |
| optimization-run | Execute multi-objective optimization on candidates to produce a Pareto front of non-dominated solutions. |
| pair-selector | Select the next comparison pairs that maximize information gain given current ratings and comparison history. |
| pairwise-ranking | Pairwise Ranking Campaign 鈥?produce global rankings through pairwise comparisons and voting aggregation using Bradley-Terry, Elo, TrueSkill, Condorcet, Borda, Schulze methods. |
| paper-overview | Paper landscape scan at abstract level 鈥?discover MCDA, voting theory, Delphi, and optimization methodology papers. |
| paper-research | Full-text deep reading of methodology papers 鈥?complete understanding of algorithms, proofs, and implementation details. |
| paper-search | Paper AI summary reading 鈥?deeper understanding of specific methodology papers without full-text commitment. |
| pareto-frontier-construction | Build the Pareto frontier from multi-objective optimization, visualize trade-offs, and select a portfolio from non-dominated solutions. |
| pareto-visualization | Create visual representation of the Pareto frontier showing trade-offs between objectives with narrative explanation. |
| perspective-assignment | Define distinct stakeholder or analytical perspectives with their values, concerns, and evaluation criteria. |
| perspective-attack | Attack a decision from a specific assigned perspective, producing rated arguments and constructive alternatives. |
| portfolio-evaluation-per-scenario | Evaluate a specific portfolio's performance metrics and vulnerabilities under a given scenario. |
| portfolio-optimization | Portfolio Optimization Campaign 鈥?select balanced combinations from candidate sets optimizing value, diversity, risk, and robustness using Markowitz, Knapsack, Pareto, Real Options, MAP-Elites, and minimax regret methods. |
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
| saturation-detection | Determines when to stop iterating 鈥?coverage threshold met or marginal returns diminishing. Shared across all campaigns. |
| scenario-construction | Construct distinct future scenarios spanning key uncertainties for portfolio stress testing. |
| scenario-stress-testing | Construct distinct future scenarios, evaluate portfolio performance under each, and identify vulnerabilities and robustness characteristics. |
| scoring-matrix-construction | Build a complete scoring matrix through criterion definition, weighting, scoring, normalization, and sensitivity testing. |
| scoring-synthesis | Synthesize score matrix, rankings, and sensitivity analysis into a final recommendation. |
| screening-then-scoring | First eliminate non-qualifying candidates with non-compensatory rules, then score survivors with full MCDA methods. |
| selection-from-frontier | Select the final portfolio from the Pareto front by applying stakeholder preferences and decision criteria. |
| sensitivity-analysis | Tests conclusion robustness by perturbing parameters and observing rank changes. Shared across scoring, portfolio, and steel-manning campaigns. |
| staged-gate-evaluation | Define gate criteria for each stage, evaluate candidates at each gate, and render go/kill/recycle decisions with evidence. |
| stakeholder-objection-simulation | Simulate stakeholder objections through role-play and political feasibility analysis to test whether the decision survives real-world opposition. |
| steel-manning | Steel-Manning Campaign 鈥?adversarial verification of convergence decisions through resurrection advocacy, winner stress-testing, criteria interrogation, and multi-perspective attack using Devil's Advocacy, Pre-mortem, Red Teaming, Dialectical Inquiry methods. |
| steel-manning-synthesis | Synthesize all attacks and verdicts into a final unified assessment with surviving concerns and recommended modifications. |
| structured-consensus | Structured Consensus Campaign 鈥?converge multiple perspectives into shared agreement through iterative structured dialogue using Delphi variants, NGT, RAND/UCLA, Consensus Conference methods. |
| temporal-sequencing | Determine optimal ordering and phasing of portfolio investments using Real Options, Critical path, Dependency graph, and Staged investment methods. |
| threshold-calibration | Systematically sweep consensus thresholds to observe which items achieve consensus at what level, producing a threshold-consensus curve. |
| threshold-setting | Define minimum acceptable thresholds for each criterion based on context and constraints. |
| threshold-sweep | Compute consensus status at multiple threshold levels to produce a threshold-consensus curve. |
| value-maximization | Maximize total portfolio value within constraints using Knapsack, Linear programming, Cost-benefit analysis, and NPV ranking methods. |
| web-research | Deep web research with full-page extraction 鈥?detailed methodology guides, tutorials, implementation references. |
| web-search | Quick web scan to discover relevant pages 鈥?methodology references, case studies, best practices for convergence methods. |
| weight-elicitation | Determine criteria weights using AHP, Swing, BWM, MACBETH, or Simos methods. |
| weight-elicitation-sop | Compute criteria weights using a specified elicitation method (AHP, Swing, BWM, MACBETH, or Simos). |
| winner-stress-testing | Stress-test the winning candidate using Pre-mortem, Red Teaming, and Failure Mode Analysis to expose hidden weaknesses before commitment. |

## stress-test (103 skills)

| Skill | Description |
|-------|-------------|
| action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| adversarial-escalation | "Strategy: Progressive pressure escalation 鈥?starts with surface-level challenges and escalates to fundamental assumption attacks based on defender confidence decay." |
| adversarial-persona | "Strategy: Role-play attacks from hostile personas 鈥?competing lab researcher, hostile reviewer, funding skeptic, domain outsider 鈥?each with distinct attack motivations and blind spots." |
| adversarial-roleplay | "Tactic: Construct detailed hostile persona, attack artifact from that persona's perspective, record successful attack paths for aggregation." |
| adversarial-stress-testing | "Campaign: Logical extreme and boundary testing via reductio ad absurdum and edge-case analysis. Core question: Does this artifact collapse under logical limits and boundary conditions? Methods: Lakatos 1976, Dutilh Novaes 2016, BVA, Flyvbjerg Critical Case, Popper." |
| alternative-analysis | "Strategy: What-If Analysis, Alternative Futures, and Four Ways of Seeing 鈥?generate competing explanations and scenarios to challenge the dominant narrative." |
| alternative-futures | Generate 2-4 divergent scenarios from the same evidence base, each representing a plausible alternative to the artifact's conclusions. |
| assumption-cascade | "Tactic: Surface assumptions, sort by dependency, attack root assumptions first, then trace cascade failures through the dependency graph." |
| assumption-cascade-tracer | Build assumption dependency graphs and trace cascade failures when root assumptions are invalidated. |
| assumption-challenge | "Strategy: Military-grade assumption testing 鈥?Key Assumptions Check, Devil's Advocacy, Team A/B analysis to expose hidden dependencies and unexamined beliefs." |
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
| closest-worlds | "Strategy: Lewis Possible Worlds 鈥?find the minimal change to reality that would flip the conclusion, measuring how close the nearest world where the conclusion fails." |
| confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| contradiction-derivation | "Negate a claim, derive logical consequences step by step, detect whether a genuine contradiction or absurdity emerges." |
| contradiction-detection | "Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state." |
| counterexample-generation | "Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies." |
| counterexample-heuristics | "Generate counterexamples (monsters), attempt monster-barring, incorporate surviving counterexamples as lemma refinements (Lakatos method)." |
| counterfactual-probing | "Campaign: Counterfactual reasoning to identify load-bearing factors. Core question: If key factors were different, would the conclusion still hold? Methods: Pearl SCM Three-Step, Lewis Possible Worlds, Tetlock & Belkin, PNS/PS." |
| counterfactual-scenario-construction | Construct precise, internally consistent counterfactual scenarios where specified factors are altered, then reason about the resulting conclusion. |
| courtroom-structured | "Strategy: Legal adversarial structure 鈥?prosecution presents case, defense responds, evidence is cross-examined, judge delivers verdict. Emphasizes evidence quality and procedural rigor." |
| critical-case-design | "Flyvbjerg critical case methodology: select most-likely and least-likely cases to maximize inferential power." |
| critic-defender-judge | "Strategy: Classic triangular debate 鈥?Critic attacks, Defender responds, Judge adjudicates. Based on Irving AI Safety via Debate with Toulmin argumentation structure." |
| cross-examination | Probes defender responses for inconsistencies, logical gaps, and unsupported claims. Acts as follow-up interrogation after initial defense. |
| debate-architect | Designs debate structure based on artifact type 鈥?selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| debate-transcript-analysis | Extracts key turning points, patterns, and insights from completed debate transcripts. Produces structured summary for verdict synthesis. |
| deductive-chain | "Derive logical consequences step by step from a given premise, building a traceable derivation chain." |
| design-fmea | "Strategy: Research design-level FMEA 鈥?function analysis, failure mode identification, severity/occurrence/detection scoring per AIAG-VDA 2019." |
| detection-scoring | "Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact." |
| devils-advocacy | Construct the strongest possible counter-argument against a position, steelmanning the opposition before attacking. |
| dialectical-escalation | "Tactic: Progressive debate escalation based on confidence thresholds. Each round increases attack sophistication until defender collapses or proves resilient." |
| divergence-detection | Identifies agreement and disagreement patterns across multiple perspective evaluations. Maps consensus clusters and persistent divergence points. |
| evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |
| evidence-tournament | "Tactic: Evidence gathering, cross-examination, and quality judgment. External evidence is collected, presented, challenged, and scored for relevance and reliability." |
| extreme-value-generation | "Generate boundary and extreme test values for a given parameter dimension to stress-test claims." |
| factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| factor-removal | "Strategy: Systematic factor removal 鈥?remove factors one at a time and observe whether the conclusion remains stable, identifying which factors are load-bearing." |
| failure-anticipation | "Campaign: Forward-looking failure analysis combining pre-mortem rapid screening with systematic FMEA deep-dive. Core question: If this artifact fails, how will it fail? Methods: Klein Pre-Mortem 2007, AIAG-VDA FMEA 2019, IEC 60812." |
| failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| failure-chain-tracing | "Tactic: Trace upstream causes and downstream effects of each failure mode. Builds multi-level cause-mode-effect chains for systemic understanding." |
| failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| flip-point-detection | Find the minimal change magnitude along a dimension that causes the conclusion to flip from true to false. |
| fragility-measurement | Compute a fragility index from flip-point distances and degradation scores, summarizing how robust the conclusion is. |
| function-analysis | "FMEA Step 3: Decompose artifact into function tree 鈥?identify what each component is supposed to do before analyzing how it can fail." |
| groupthink-mitigation | "Strategy: 10th Man Rule and Liberating Structures 鈥?institutionalized dissent to prevent premature consensus and expose suppressed objections." |
| key-assumptions-check | "Military ACT: systematically enumerate all assumptions, classify by type, and evaluate evidence strength supporting each." |
| lakatos-heuristics | "Proofs and Refutations method: generate counterexamples, attempt monster-barring, incorporate surviving counterexamples as lemma refinements." |
| load-bearing-identification | Identify which factors are "load-bearing walls" 鈥?factors whose removal would collapse the conclusion. |
| minimal-change-search | "Tactic: Generate candidate changes, detect flip-points where conclusion reverses, measure fragility as distance to nearest flip." |
| mitigation-design | "Strategy: Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasures validated via re-scoring." |
| mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| mitigation-proposal | Proposes concrete mitigation strategies for identified weaknesses. Generates prevention, detection, and response measures with feasibility assessment. |
| mitigation-validation | "Tactic: Run mini-FMEA on proposed mitigations to verify they do not introduce new failure modes. Prevents mitigation-induced risks." |
| monster-barring-attempt | "Attempt to exclude a counterexample as illegitimate by tightening definitions or preconditions (Lakatos monster-barring)." |
| multiagent-debate | "Campaign: Multi-agent structured debate for adversarial validation. Core question: Can this artifact survive structured adversarial debate? Methods: Irving AI Safety via Debate, Du Society of Mind, Liang MAD, Toulmin Argumentation, D3 framework." |
| multi-perspective-panel | "Strategy: Multi-stakeholder review panel 鈥?diverse expert perspectives evaluate artifact simultaneously, then synthesize through structured deliberation." |
| necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor 鈥?would the conclusion fail if this factor were absent? |
| necessity-sufficiency | "Strategy: Probability of Necessity and Sufficiency (PNS/PS) 鈥?systematically evaluate whether each factor is necessary, sufficient, both, or neither for the conclusion." |
| occurrence-scoring | Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution. |
| paper-overview | Paper landscape scan returning abstracts and metadata. Import of literature-engine/paper-overview skill. Abstracts only 鈥?no conclusions from abstracts. |
| paper-research | Paper full text access via alphaxiv answer_pdf_queries or get_paper_content(fullText=true). Import of literature-engine/paper-research skill. Raw extracted text for precise claims. |
| paper-search | Paper AI summary report via alphaxiv get_paper_content. Import of literature-engine/paper-search skill. Structured AI-generated intermediate report. |
| parameter-space-mapping | "Identify all parameter dimensions along which a claim's validity might vary." |
| persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| perspective-critic | Evaluates artifact from a specific assigned perspective. Produces assessment grounded in that viewpoint's values, priorities, and expertise. |
| perspective-rotation | "Tactic: Sequential perspective evaluation with divergence aggregation. Each agent evaluates from a distinct viewpoint, then disagreements are surfaced and resolved." |
| premortem-facilitation | Execute Klein pre-mortem protocol 鈥?assume failure has occurred, generate plausible failure scenarios through prospective hindsight. |
| premortem-to-fmea-pipeline | "Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis." |
| probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |
| process-fmea | "Strategy: Research execution process FMEA 鈥?analyzes how the research process itself can fail during execution, distinct from design-level failures." |
| prospective-hindsight | "Strategy: Klein pre-mortem 鈥?assume the artifact has failed, then retrospect plausible causes. Generates rapid failure scenario catalog." |
| red-teaming | "Campaign: Systematic adversarial attack from military/intelligence/AI-safety traditions. Core question: Can systematic adversarial attacks find fatal flaws? Methods: UFMCS Red Team Handbook v9.0, CIA SAT, Anthropic Red Teaming, NIST AI RMF, Inie et al. 12-strategy taxonomy." |
| re-scoring | Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected. |
| risk-prioritization | "Strategy: Action Priority matrix 鈥?classifies failure modes into H/M/L priority using severity-weighted scoring per AIAG-VDA 2019 Action Priority tables." |
| saturation-detection | Determines whether validation has reached saturation 鈥?no new weaknesses or failure modes being discovered. Used by all 5 campaigns as termination signal. |
| severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |
| single-factor-removal | Remove one specified factor from the artifact's support structure and reason about how the conclusion changes. |
| society-of-mind | "Strategy: Multi-agent collaborative debate based on Du et al. Society of Mind. Agents share perspectives iteratively until convergence or divergence is detected." |
| structural-counterfactual | "Strategy: Pearl Three-Step counterfactual 鈥?Abduction (fit model to evidence), Action (intervene on factor), Prediction (derive counterfactual outcome)." |
| structured-attack-campaign | "Tactic: Full attack lifecycle 鈥?threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces." |
| sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor 鈥?would this factor alone be enough to produce the conclusion? |
| systematic-factor-ablation | "Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance." |
| systematic-probing | "Strategy: AI-safety systematic probing 鈥?enumerate all threat surfaces, generate attack vectors per surface, execute probes, and aggregate findings across the full attack space." |
| thought-experiment | "Strategy: Williamson-style precise thought experiments 鈥?construct carefully specified counterfactual scenarios to test whether conclusions depend on contingent features." |
| threat-surface-mapping | Enumerate all attackable surfaces of an artifact 鈥?logical, empirical, methodological, social, and practical dimensions. |
| validity-envelope-construction | "Synthesize breakpoints across dimensions into a coherent validity envelope for a claim." |
| validity-envelope-mapping | "Map the complete validity envelope of a claim across all relevant dimensions, synthesizing breakpoints into a bounded region." |
| verdict-synthesis | Synthesizes findings from a completed campaign into typed verdict reports. Produces DebateVerdict, RedTeamReport, FailureAnticipationReport, CounterfactualMap, or AdversarialStressReport depending on campaign. Also supports cross-campaign StressTestSummary. |
| weakness-classification | Classifies discovered weaknesses into severity tiers (fatal/major/minor/cosmetic) with structured justification and exploitability assessment. |
| web-research | Deep web full-text retrieval via Apify RAG browser. Import of web-browsing/web-research skill. Full page content for substantive analysis. |
| web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only 鈥?no conclusions from snippets alone. |

## experiment-execution (88 skills)

| Skill | Description |
|-------|-------------|
| ablation-component-mapping | "Map system architecture to ablatable units for ablation studies" |
| ablation-design | "Design ablation studies to isolate component contributions in ML systems" |
| activity-listing | "Enumerate all implementation activities from an experiment design" |
| assumption-challenging | "Challenge each assumption's validity 鈥?shared cross-repo SOP" |
| assumption-constraint | "Which assumptions are most fragile? 鈥?Vulnerability ranking + impact assessment of experiment assumptions" |
| baseline-selection | "Select appropriate baselines for experimental comparison" |
| bottleneck-identification | "Where is the system bottleneck? 鈥?TOC 5 Focusing Steps + Current Reality Tree to find the binding constraint" |
| budget-constrained-design | "Optimize experiment design under compute and time budget constraints" |
| buffer-sizing | "Calculate project, feeding, and resource buffers 鈥?shared with implementation-planning" |
| causal-chain-tracing | "Trace UDE to root cause via IF...THEN...BECAUSE logic chains" |
| checkpoint-and-recover | "Checkpoint state before risky operations, detect anomalies, and recover gracefully" |
| comparison-design | "Design fair comparison experiments against baselines and competing methods" |
| competitive-move-prediction | "Predict competitor progress, publications, and strategic moves" |
| competitive-scenario | "What will competitors do? 鈥?Competitive method progress prediction and time window analysis" |
| conflict-resolution | "How do constraints conflict with each other? 鈥?Evaporating Cloud + assumption challenging + injection to resolve constraint conflicts" |
| consistency-pair-evaluation | "Pairwise consistency assessment using Cross-Consistency Assessment (CCA) matrix" |
| constraint-analysis | "What limits us 鈥?identify bottlenecks, quantify constraints, analyze dependencies, resolve conflicts before experiment execution" |
| constraint-breaking | "Orchestrate the full constraint-breaking cycle: extract conflict, challenge assumptions, project resolution" |
| constraint-synthesis | "Synthesize constraint analysis into actionable report with priorities" |
| constraint-tree-building | "Build Current Reality Tree from UDEs through causal chains to core conflicts" |
| core-conflict-extraction | "Extract core conflict in Evaporating Cloud format (A-B-C-D-D')" |
| critical-chain-identification | "Identify the critical chain 鈥?longest path considering resource contention" |
| critical-path-calculation | "CPM forward/backward pass with float calculation to identify the critical path" |
| critical-path-planning | "Identify the shortest execution path via CPM forward/backward pass, resource leveling, and buffer insertion" |
| cross-consistency-filtering | "Orchestrates pairwise consistency evaluation and narrative construction to filter the morphological field" |
| dependency-constraint | "What must be completed first? 鈥?Dependency chain analysis + prerequisite graph construction" |
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
| factor-level-design | "Design factorial experiments to test how specific factors affect outcomes" |
| future-reality-projection | "Project solution effects using Future Reality Tree logic" |
| implementation-planning | "Plan execution path, produce executable plan, dispatch subagents, collect and analyze results" |
| implementer-dispatch | "Dispatch execution subagent 鈥?select model by complexity, construct prompt with full task context" |
| intermediate-objective-design | "Design intermediate objectives to overcome each identified obstacle" |
| level-specification | "Determine appropriate levels for each experimental factor" |
| metric-specification | "Define experiment metrics and significance standards" |
| morphological-scenario | "What are all possible combinations? 鈥?Zwicky Box construction with CCA consistency filtering for systematic scenario enumeration" |
| narrative-scenario | "What is the story of each future? 鈥?Shell method narrative construction for rich qualitative scenario understanding" |
| obstacle-identification | "TOC Prerequisite Tree 鈥?list obstacles preventing direct achievement of the objective" |
| paper-overview | "Import SOP: paper landscape scan (from literature-engine skill)" |
| paper-research | "Import SOP: paper full-text reading (from literature-engine skill)" |
| paper-search | "Import SOP: paper AI summary reading (from literature-engine skill)" |
| parameter-enumeration | "Enumerate possible values for each uncertainty driver using MECE principles" |
| parameter-space-construction | "Orchestrates driver identification and parameter enumeration to build the complete morphological field" |
| plan-formatting | "Format task plan as bite-sized executable tasks following superpowers:writing-plans conventions" |
| plan-writing | "Format critical path and prerequisites into bite-sized executable plan following superpowers:writing-plans conventions" |
| prerequisite-planning | "Identify obstacles blocking direct achievement and design intermediate objectives to overcome each" |
| quality-gate-check | "Shared SOP: verify quality gate criteria are met before proceeding" |
| reproducibility-protocol | "Ensure experiment reproducibility through systematic environment and seed control" |
| reproducibility-verification | "Verify result reproducibility via re-runs with different seeds and ICC comparison" |
| resource-constraint | "Are resources sufficient? 鈥?Quantify compute, data, time, human, and financial resource constraints" |
| resource-quantification | "Quantify resource demand vs supply vs gap for each resource category" |
| result-analysis | "Statistically analyze collected results, verify reproducibility, and synthesize findings" |
| result-collection | "Collect experiment outputs — metrics, logs, artifacts — into structured result set" |
| result-validation-loop | "Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis" |
| robustness-design | "Design experiments to identify failure boundaries and robustness limits" |
| robustness-scoring | "Compute robustness index across scenarios with sensitivity analysis" |
| sample-size-estimation | "SOP: power analysis and required experiment count estimation" |
| saturation-detection | "Shared SOP: detect information saturation 鈥?know when to stop searching/analyzing" |
| scaling-design | "Design scaling experiments to characterize performance-resource relationships" |
| scenario-driver-identification | "Identify key uncertainty drivers using PESTEL framework scanning" |
| scenario-impact-assessment | "Assess each scenario's impact on the research approach across multiple dimensions" |
| scenario-narrative-construction | "Build rich narratives for surviving morphological configurations using Shell method" |
| scenario-planning | "What might the future look like 鈥?construct multiple future scenarios, assess research approach robustness under different assumptions" |
| scenario-synthesis | "Comprehensive scenario analysis report synthesizing all scenario work" |
| seed-protocol-design | "SOP: design random seed strategy for reproducibility" |
| sensitivity-ranking | "Rank constraints by sensitivity 鈥?which ones most impact the outcome if they shift" |
| statistical-method-selection | "Select appropriate statistical methods for experiment analysis" |
| statistical-testing | "Execute statistical tests — bootstrap, permutation, Bayesian ROPE — on experiment results" |
| strategy-robustness-testing | "Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios" |
| stress-scenario | "What is the worst case? 鈥?Extreme condition construction and failure mode enumeration for risk preparedness" |
| subagent-execution-loop | "Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection" |
| task-decomposition | "Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan" |
| temporal-scenario | "How does it evolve over time? 鈥?Short/medium/long-term timeline projection with technology maturity curves" |
| timeline-projection | "Extrapolate research landscape timelines using trend analysis and milestone projection" |
| undesirable-effect-listing | "List current Undesirable Effects (UDEs) 鈥?observable symptoms of system underperformance" |
| web-research | "Import SOP: deep full-page content analysis (from web-browsing skill)" |
| web-search | "Import SOP: quick web scan discovery (from web-browsing skill)" |
| worst-case-construction | "Construct extreme but plausible worst-case scenarios for stress testing" |

## web-browsing (2 skills)

| Skill | Description |
|-------|-------------|
| web-research | Deep web research 鈥?fetches full page content for analysis. Snippets alone are PROHIBITED for conclusions. |
| web-search | Quick web scanning 鈥?discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

## literature-engine (3 skills)

| Skill | Description |
|-------|-------------|
| literature-overview | Quick landscape scan 鈥?discover papers on a topic without full-text reading |
| literature-research | Deep literature research 鈥?raw full text reading and targeted PDF queries for rigorous analysis |
| literature-search | Medium-depth literature search 鈥?read AI-summarized reports for every paper analyzed |

## subagent-spawning (1 skills)

| Skill | Description |
|-------|-------------|
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

## context-management (2 skills)

| Skill | Description |
|-------|-------------|
| context-checkpoint | Append research process and results to the current Phase's context file. Each append MUST contain >=500 lines of markdown covering both process and results. Use this skill at plan-designated checkpoint points 鈥?typically after each strategy completes or at key decision nodes within a research Phase. |
| context-init | Create a new context file for a research Phase. Called once at Phase start to initialize the file that subsequent context-checkpoint calls will append to. Use this skill whenever a new research Phase begins and a fresh context file is needed. |

