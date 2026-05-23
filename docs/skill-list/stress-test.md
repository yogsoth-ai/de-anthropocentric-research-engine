# stress-test

Used to adversarially test research plans, argument structures, and key conclusions, covering red teaming, counterfactual reasoning, boundary-value analysis, FMEA, and debate-style validation.

[Back to skill navigation](./skill-list.md)

Skill count: 103

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
