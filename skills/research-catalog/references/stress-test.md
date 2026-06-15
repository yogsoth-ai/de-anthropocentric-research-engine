# stress-test — skill table

103 skills. Sorted by layer (campaign→strategy→tactic→sop), then name.

| Layer | Skill | Description |
| --- | --- | --- |
| campaign | adversarial-stress-testing | "Campaign: Logical extreme and boundary testing via reductio ad absurdum and edge-case analysis. Core question: Does this artifact collapse under logical limits and boundary conditions? Methods: Lakatos 1976, Dutilh Novaes 2016, BVA, Flyvbjerg Critical Case, Popper." |
| campaign | counterfactual-probing | "Campaign: Counterfactual reasoning to identify load-bearing factors. Core question: If key factors were different, would the conclusion still hold? Methods: Pearl SCM Three-Step, Lewis Possible Worlds, Tetlock & Belkin, PNS/PS." |
| campaign | failure-anticipation | "Campaign: Forward-looking failure analysis combining pre-mortem rapid screening with systematic FMEA deep-dive. Core question: If this artifact fails, how will it fail? Methods: Klein Pre-Mortem 2007, AIAG-VDA FMEA 2019, IEC 60812." |
| campaign | multiagent-debate | "Campaign: Multi-agent structured debate for adversarial validation. Core question: Can this artifact survive structured adversarial debate? Methods: Irving AI Safety via Debate, Du Society of Mind, Liang MAD, Toulmin Argumentation, D3 framework." |
| campaign | red-teaming | "Campaign: Systematic adversarial attack from military/intelligence/AI-safety traditions. Core question: Can systematic adversarial attacks find fatal flaws? Methods: UFMCS Red Team Handbook v9.0, CIA SAT, Anthropic Red Teaming, NIST AI RMF, Inie et al. 12-strategy taxonomy." |
| strategy | adversarial-escalation | "Strategy: Progressive pressure escalation — starts with surface-level challenges and escalates to fundamental assumption attacks based on defender confidence decay." |
| strategy | adversarial-persona | "Strategy: Role-play attacks from hostile personas — competing lab researcher, hostile reviewer, funding skeptic, domain outsider — each with distinct attack motivations and blind spots." |
| strategy | alternative-analysis | "Strategy: What-If Analysis, Alternative Futures, and Four Ways of Seeing — generate competing explanations and scenarios to challenge the dominant narrative." |
| strategy | stress-test-assumption-challenge | Construct the strongest counter-argument against a specific assumption and propose alternatives. |
| strategy | assumption-negation | "Classic reductio ad absurdum: negate the core claim, derive logical consequences, seek contradiction or absurdity." |
| strategy | boundary-enumeration | "Systematic Boundary Value Analysis: identify parameter boundaries, test at and beyond limits, detect breakpoints." |
| strategy | closest-worlds | "Strategy: Lewis Possible Worlds — find the minimal change to reality that would flip the conclusion, measuring how close the nearest world where the conclusion fails." |
| strategy | courtroom-structured | "Strategy: Legal adversarial structure — prosecution presents case, defense responds, evidence is cross-examined, judge delivers verdict. Emphasizes evidence quality and procedural rigor." |
| strategy | critic-defender-judge | "Strategy: Classic triangular debate — Critic attacks, Defender responds, Judge adjudicates. Based on Irving AI Safety via Debate with Toulmin argumentation structure." |
| strategy | critical-case-design | "Flyvbjerg critical case methodology: select most-likely and least-likely cases to maximize inferential power." |
| strategy | design-fmea | "Strategy: Research design-level FMEA — function analysis, failure mode identification, severity/occurrence/detection scoring per AIAG-VDA 2019." |
| strategy | factor-removal | "Strategy: Systematic factor removal — remove factors one at a time and observe whether the conclusion remains stable, identifying which factors are load-bearing." |
| strategy | groupthink-mitigation | "Strategy: 10th Man Rule and Liberating Structures — institutionalized dissent to prevent premature consensus and expose suppressed objections." |
| strategy | lakatos-heuristics | "Proofs and Refutations method: generate counterexamples, attempt monster-barring, incorporate surviving counterexamples as lemma refinements." |
| strategy | mitigation-design | "Strategy: Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasures validated via re-scoring." |
| strategy | multi-perspective-panel | "Strategy: Multi-stakeholder review panel — diverse expert perspectives evaluate artifact simultaneously, then synthesize through structured deliberation." |
| strategy | necessity-sufficiency | "Strategy: Probability of Necessity and Sufficiency (PNS/PS) — systematically evaluate whether each factor is necessary, sufficient, both, or neither for the conclusion." |
| strategy | process-fmea | "Strategy: Research execution process FMEA — analyzes how the research process itself can fail during execution, distinct from design-level failures." |
| strategy | prospective-hindsight | "Strategy: Klein pre-mortem — assume the artifact has failed, then retrospect plausible causes. Generates rapid failure scenario catalog." |
| strategy | risk-prioritization | "Strategy: Action Priority matrix — classifies failure modes into H/M/L priority using severity-weighted scoring per AIAG-VDA 2019 Action Priority tables." |
| strategy | society-of-mind | "Strategy: Multi-agent collaborative debate based on Du et al. Society of Mind. Agents share perspectives iteratively until convergence or divergence is detected." |
| strategy | structural-counterfactual | "Strategy: Pearl Three-Step counterfactual — Abduction (fit model to evidence), Action (intervene on factor), Prediction (derive counterfactual outcome)." |
| strategy | systematic-probing | "Strategy: AI-safety systematic probing — enumerate all threat surfaces, generate attack vectors per surface, execute probes, and aggregate findings across the full attack space." |
| strategy | thought-experiment | "Strategy: Williamson-style precise thought experiments — construct carefully specified counterfactual scenarios to test whether conclusions depend on contingent features." |
| strategy | stress-test-validity-envelope-mapping | Map multi-dimensional validity envelopes — define variation axes, perturb systematically, measure degradation, construct boundary surface. |
| tactic | adversarial-roleplay | "Tactic: Construct detailed hostile persona, attack artifact from that persona's perspective, record successful attack paths for aggregation." |
| tactic | assumption-cascade | "Tactic: Surface assumptions, sort by dependency, attack root assumptions first, then trace cascade failures through the dependency graph." |
| tactic | boundary-probing | "Map parameter space, generate extreme values, test at boundaries, detect breakpoints, synthesize validity envelope." |
| tactic | causal-necessity-testing | "Tactic: Extract causal claims, evaluate probability of necessity (PN) and sufficiency (PS) for each, classify into necessity-sufficiency quadrants." |
| tactic | contradiction-derivation | "Negate a claim, derive logical consequences step by step, detect whether a genuine contradiction or absurdity emerges." |
| tactic | counterexample-heuristics | "Generate counterexamples (monsters), attempt monster-barring, incorporate surviving counterexamples as lemma refinements (Lakatos method)." |
| tactic | stress-test-dialectical-escalation | Double-loop learning escalation — surface governing variables, generate counter-assumptions, test if problem dissolves under alternatives, score wickedness if it persists. |
| tactic | evidence-tournament | "Tactic: Evidence gathering, cross-examination, and quality judgment. External evidence is collected, presented, challenged, and scored for relevance and reliability." |
| tactic | failure-chain-tracing | "Tactic: Trace upstream causes and downstream effects of each failure mode. Builds multi-level cause-mode-effect chains for systemic understanding." |
| tactic | minimal-change-search | "Tactic: Generate candidate changes, detect flip-points where conclusion reverses, measure fragility as distance to nearest flip." |
| tactic | mitigation-validation | "Tactic: Run mini-FMEA on proposed mitigations to verify they do not introduce new failure modes. Prevents mitigation-induced risks." |
| tactic | stress-test-perspective-rotation | Rotate through reviewer/practitioner/theorist/time-machine/novice perspectives systematically. Ensures comprehensive viewpoint coverage. |
| tactic | premortem-to-fmea-pipeline | "Tactic: Pre-mortem rapid screening feeds high-risk items into full FMEA analysis. Bridges fast intuitive generation with systematic structured analysis." |
| tactic | structured-attack-campaign | "Tactic: Full attack lifecycle — threat surface enumeration, attack vector generation, systematic probing, and finding aggregation across all surfaces." |
| tactic | systematic-factor-ablation | "Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance." |
| sop | action-priority-matrix | Compute Risk Priority Number (RPN = S x O x D), classify failure modes into H/M/L action priority per AIAG-VDA tables. |
| sop | alternative-futures | Generate 2-4 divergent scenarios from the same evidence base, each representing a plausible alternative to the artifact's conclusions. |
| sop | assumption-cascade-tracer | Build assumption dependency graphs and trace cascade failures when root assumptions are invalidated. |
| sop | attack-resilience-scoring | Compute overall resilience score (0.0-1.0) based on attack results, coverage, and vulnerability severity distribution. |
| sop | attack-vector-generation | Generate specific attack strategies for a given threat surface, producing concrete probes that can be executed. |
| sop | breakpoint-detection | "Test a claim at extreme parameter values and detect the precise point where it breaks down." |
| sop | causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| sop | claim-negation | "Formally negate the core claim, producing the logical complement for reductio testing." |
| sop | claim-refinement | "Propose a refined claim that survives counterexamples while preserving maximum explanatory power (Lakatos lemma-incorporation)." |
| sop | confidence-calibration | Calibrates confidence scores based on debate progression. Determines whether to escalate, continue, or terminate based on cumulative evidence. |
| sop | contradiction-detection | "Evaluate whether a derivation chain has reached a genuine contradiction, absurdity, or inconclusive state." |
| sop | counterexample-generation | "Systematically generate counterexamples (monsters) to a given claim using diverse heuristic strategies." |
| sop | counterfactual-scenario-construction | Construct precise, internally consistent counterfactual scenarios where specified factors are altered, then reason about the resulting conclusion. |
| sop | cross-examination | Probes defender responses for inconsistencies, logical gaps, and unsupported claims. Acts as follow-up interrogation after initial defense. |
| sop | debate-architect | Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters. |
| sop | debate-critic | Generates structured criticism from attack stance using Toulmin model. Produces claims, grounds, warrants, and rebuttals targeting artifact weaknesses. |
| sop | debate-defender | Responds to attacks with counter-evidence and counter-arguments. Defends artifact using evidence, clarification, and rebuttal while acknowledging valid criticisms. |
| sop | debate-judge | Evaluates debate exchanges, adjudicates argument quality, and produces round verdicts with confidence scores and reasoning. |
| sop | debate-transcript-analysis | Extracts key turning points, patterns, and insights from completed debate transcripts. Produces structured summary for verdict synthesis. |
| sop | deductive-chain | "Derive logical consequences step by step from a given premise, building a traceable derivation chain." |
| sop | detection-scoring | "Rate detectability 1-10 (inverted: 10 = hardest to detect). Estimates how likely current controls would catch the failure before impact." |
| sop | devils-advocacy | Construct the strongest possible counter-argument against a position, steelmanning the opposition before attacking. |
| sop | divergence-detection | Identifies agreement and disagreement patterns across multiple perspective evaluations. Maps consensus clusters and persistent divergence points. |
| sop | evidence-scout | Searches for external evidence supporting or opposing specific claims. Returns structured evidence with source assessment and relevance scoring. |
| sop | extreme-value-generation | "Generate boundary and extreme test values for a given parameter dimension to stress-test claims." |
| sop | factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| sop | failure-chain-construction | Build cause-mode-effect chains tracing upstream root causes and downstream cascading effects for each failure mode. |
| sop | failure-mode-extraction | Extract structured failure mode list from raw scenarios or artifact analysis. Produces standardized failure mode records. |
| sop | finding-aggregation | Aggregate, deduplicate, and classify findings from multiple probes into a coherent vulnerability report. |
| sop | flip-point-detection | Find the minimal change magnitude along a dimension that causes the conclusion to flip from true to false. |
| sop | fragility-measurement | Compute a fragility index from flip-point distances and degradation scores, summarizing how robust the conclusion is. |
| sop | function-analysis | "FMEA Step 3: Decompose artifact into function tree — identify what each component is supposed to do before analyzing how it can fail." |
| sop | key-assumptions-check | "Military ACT: systematically enumerate all assumptions, classify by type, and evaluate evidence strength supporting each." |
| sop | load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |
| sop | mitigation-design-sop | Design prevention, detection, and response measures for high-priority failure modes. Produces actionable countermeasure specifications. |
| sop | mitigation-proposal | Proposes concrete mitigation strategies for identified weaknesses. Generates prevention, detection, and response measures with feasibility assessment. |
| sop | monster-barring-attempt | "Attempt to exclude a counterexample as illegitimate by tightening definitions or preconditions (Lakatos monster-barring)." |
| sop | necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor — would the conclusion fail if this factor were absent? |
| sop | occurrence-scoring | Rate failure mode occurrence probability 1-10. Estimates how likely each failure mode is to manifest during research execution. |
| sop | stress-test-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| sop | stress-test-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| sop | stress-test-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| sop | parameter-space-mapping | "Identify all parameter dimensions along which a claim's validity might vary." |
| sop | persona-construction | Build a detailed adversarial persona with background, motivation, expertise, blind spots, and preferred attack patterns. |
| sop | perspective-critic | Evaluates artifact from a specific assigned perspective. Produces assessment grounded in that viewpoint's values, priorities, and expertise. |
| sop | premortem-facilitation | Execute Klein pre-mortem protocol — assume failure has occurred, generate plausible failure scenarios through prospective hindsight. |
| sop | probe-execution | Execute a single attack probe against an artifact, record the result with evidence and severity classification. |
| sop | re-scoring | Re-evaluate S/O/D scores after mitigation measures are in place. Validates that mitigations actually reduce risk as expected. |
| sop | stress-test-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| sop | severity-scoring | Rate failure mode severity 1-10 based on end-effect impact. Follows AIAG-VDA severity scale calibrated for research artifacts. |
| sop | single-factor-removal | Remove one specified factor from the artifact's support structure and reason about how the conclusion changes. |
| sop | sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor — would this factor alone be enough to produce the conclusion? |
| sop | threat-surface-mapping | Enumerate all attackable surfaces of an artifact — logical, empirical, methodological, social, and practical dimensions. |
| sop | stress-test-validity-envelope-construction | Combine multi-axis perturbation data into a multi-dimensional validity description with boundary conditions and interaction effects. |
| sop | verdict-synthesis | Synthesizes findings from a completed campaign into typed verdict reports. Produces DebateVerdict, RedTeamReport, FailureAnticipationReport, CounterfactualMap, or AdversarialStressReport depending on campaign. Also supports cross-campaign StressTestSummary. |
| sop | weakness-classification | Classifies discovered weaknesses into severity tiers (fatal/major/minor/cosmetic) with structured justification and exploitability assessment. |
| sop | stress-test-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| sop | stress-test-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
