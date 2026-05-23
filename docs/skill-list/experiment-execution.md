# experiment-execution

Used to turn research hypotheses into experiment designs and execution paths, covering task decomposition, constraint handling, scenario planning, reproducibility, and result validation.

[Back to skill navigation](./skill-list.md)

Skill count: 88

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
| quality-gate-check | "Shared SOP: General quality gate check (format completeness and logical consistency)." |
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
