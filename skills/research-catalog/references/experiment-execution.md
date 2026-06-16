# experiment-execution — skill table

88 skills. Sorted by layer (campaign→strategy→tactic→sop), then name.

| Layer | Skill | Description |
| --- | --- | --- |
| campaign | constraint-analysis | What limits us — identify bottlenecks, quantify constraints, analyze dependencies, resolve conflicts before experiment execution |
| campaign | experiment-design | Transform validated hypotheses into rigorous, executable experiment designs |
| campaign | implementation-planning | Plan execution path, produce executable plan, dispatch subagents, collect and analyze results |
| campaign | scenario-planning | What might the future look like — construct multiple future scenarios, assess research approach robustness under different assumptions |
| strategy | ablation-design | Design ablation studies to isolate component contributions in ML systems |
| strategy | assumption-constraint | Which assumptions are most fragile? — Vulnerability ranking + impact assessment of experiment assumptions |
| strategy | experiment-execution-bottleneck-identification | Where is the system bottleneck? — TOC 5 Focusing Steps + Current Reality Tree to find the binding constraint |
| strategy | comparison-design | Design fair comparison experiments against baselines and competing methods |
| strategy | competitive-scenario | What will competitors do? — Competitive method progress prediction and time window analysis |
| strategy | conflict-resolution | How do constraints conflict with each other? — Evaporating Cloud + assumption challenging + injection to resolve constraint conflicts |
| strategy | critical-path-planning | Identify the shortest execution path via CPM forward/backward pass, resource leveling, and buffer insertion |
| strategy | dependency-constraint | What must be completed first? — Dependency chain analysis + prerequisite graph construction |
| strategy | experiment-running | Execute the plan by dispatching fresh subagents per task, monitoring status, and collecting results |
| strategy | experiment-execution-factor-level-design | Design factorial experiments to test how specific factors affect outcomes |
| strategy | morphological-scenario | What are all possible combinations? — Zwicky Box construction with CCA consistency filtering for systematic scenario enumeration |
| strategy | narrative-scenario | What is the story of each future? — Shell method narrative construction for rich qualitative scenario understanding |
| strategy | plan-writing | Format critical path and prerequisites into bite-sized executable plan following superpowers:writing-plans conventions |
| strategy | prerequisite-planning | Identify obstacles blocking direct achievement and design intermediate objectives to overcome each |
| strategy | resource-constraint | Are resources sufficient? — Quantify compute, data, time, human, and financial resource constraints |
| strategy | result-analysis | Statistically analyze collected results, verify reproducibility, and synthesize findings |
| strategy | robustness-design | Design experiments to identify failure boundaries and robustness limits |
| strategy | scaling-design | Design scaling experiments to characterize performance-resource relationships |
| strategy | stress-scenario | What is the worst case? — Extreme condition construction and failure mode enumeration for risk preparedness |
| strategy | temporal-scenario | How does it evolve over time? — Short/medium/long-term timeline projection with technology maturity curves |
| tactic | budget-constrained-design | Optimize experiment design under compute and time budget constraints |
| tactic | checkpoint-and-recover | Checkpoint state before risky operations, detect anomalies, and recover gracefully |
| tactic | constraint-breaking | Orchestrate the full constraint-breaking cycle: extract conflict, challenge assumptions, project resolution |
| tactic | constraint-tree-building | Build Current Reality Tree from UDEs through causal chains to core conflicts |
| tactic | cross-consistency-filtering | Orchestrates pairwise consistency evaluation and narrative construction to filter the morphological field |
| tactic | parameter-space-construction | Orchestrates driver identification and parameter enumeration to build the complete morphological field |
| tactic | reproducibility-protocol | Ensure experiment reproducibility through systematic environment and seed control |
| tactic | result-validation-loop | Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis |
| tactic | sensitivity-ranking | Rank constraints by sensitivity — which ones most impact the outcome if they shift |
| tactic | statistical-method-selection | Select appropriate statistical methods for experiment analysis |
| tactic | strategy-robustness-testing | Orchestrates impact assessment and robustness scoring to evaluate research approach resilience across scenarios |
| tactic | subagent-execution-loop | Orchestrate task execution via fresh subagents with dispatch, monitoring, and result collection |
| tactic | task-decomposition | Orchestrate the breakdown of experiment design into sequenced, estimated, and formatted task plan |
| sop | ablation-component-mapping | Map system architecture to ablatable units for ablation studies |
| sop | activity-listing | Enumerate all implementation activities from an experiment design |
| sop | assumption-challenging | Challenge each assumption's validity — shared cross-repo SOP |
| sop | baseline-selection | Select appropriate baselines for experimental comparison |
| sop | buffer-sizing | Calculate project, feeding, and resource buffers — shared with implementation-planning |
| sop | causal-chain-tracing | Trace UDE to root cause via IF...THEN...BECAUSE logic chains |
| sop | competitive-move-prediction | Predict competitor progress, publications, and strategic moves |
| sop | experiment-execution-consistency-pair-evaluation | Pairwise consistency assessment using Cross-Consistency Assessment (CCA) matrix |
| sop | constraint-synthesis | Synthesize constraint analysis into actionable report with priorities |
| sop | core-conflict-extraction | Extract core conflict in Evaporating Cloud format (A-B-C-D-D') |
| sop | critical-chain-identification | Identify the critical chain — longest path considering resource contention |
| sop | critical-path-calculation | CPM forward/backward pass with float calculation to identify the critical path |
| sop | dependency-graph-construction | Build task dependency graph with predecessor/successor relationships |
| sop | dependency-sequencing | Determine task dependencies and execution order |
| sop | design-matrix-construction | Build the experiment design matrix with proper orthogonality and balance |
| sop | design-synthesis | SOP: synthesize complete experiment design report |
| sop | duration-estimation | Three-point PERT estimation for implementation activities |
| sop | environment-specification | SOP: define complete experiment environment specification |
| sop | execution-monitoring | Monitor execution progress, detect anomalies, and report status |
| sop | execution-synthesis | Synthesize complete execution report from all results, tests, and reproducibility data |
| sop | experiment-config-generation | SOP: generate executable experiment configuration files |
| sop | factor-identification | Identify independent, dependent, and control variables for an experiment |
| sop | future-reality-projection | Project solution effects using Future Reality Tree logic |
| sop | implementer-dispatch | Dispatch execution subagent — select model by complexity, construct prompt with full task context |
| sop | intermediate-objective-design | Design intermediate objectives to overcome each identified obstacle |
| sop | level-specification | Determine appropriate levels for each experimental factor |
| sop | metric-specification | Define experiment metrics and significance standards |
| sop | obstacle-identification | TOC Prerequisite Tree — list obstacles preventing direct achievement of the objective |
| sop | experiment-execution-paper-overview | Import SOP: paper landscape scan (from literature-engine skill) |
| sop | experiment-execution-paper-research | Import SOP: paper full-text reading (from literature-engine skill) |
| sop | experiment-execution-paper-search | Import SOP: paper AI summary reading (from literature-engine skill) |
| sop | parameter-enumeration | Enumerate possible values for each uncertainty driver using MECE principles |
| sop | plan-formatting | Format task plan as bite-sized executable tasks following superpowers:writing-plans conventions |
| sop | experiment-execution-quality-gate-check | Shared SOP: verify quality gate criteria are met before proceeding |
| sop | reproducibility-verification | Verify result reproducibility via re-runs with different seeds and ICC comparison |
| sop | resource-quantification | Quantify resource demand vs supply vs gap for each resource category |
| sop | result-collection | Collect experiment outputs — metrics, logs, artifacts — into structured result set |
| sop | robustness-scoring | Compute robustness index across scenarios with sensitivity analysis |
| sop | sample-size-estimation | SOP: power analysis and required experiment count estimation |
| sop | experiment-execution-saturation-detection | Shared SOP: detect information saturation — know when to stop searching/analyzing |
| sop | scenario-driver-identification | Identify key uncertainty drivers using PESTEL framework scanning |
| sop | scenario-impact-assessment | Assess each scenario's impact on the research approach across multiple dimensions |
| sop | scenario-narrative-construction | Build rich narratives for surviving morphological configurations using Shell method |
| sop | scenario-synthesis | Comprehensive scenario analysis report synthesizing all scenario work |
| sop | seed-protocol-design | SOP: design random seed strategy for reproducibility |
| sop | statistical-testing | Execute statistical tests — bootstrap, permutation, Bayesian ROPE — on experiment results |
| sop | timeline-projection | Extrapolate research landscape timelines using trend analysis and milestone projection |
| sop | undesirable-effect-listing | List current Undesirable Effects (UDEs) — observable symptoms of system underperformance |
| sop | experiment-execution-web-research | Import SOP: deep full-page content analysis (from web-browsing skill) |
| sop | experiment-execution-web-search | Import SOP: quick web scan discovery (from web-browsing skill) |
| sop | worst-case-construction | Construct extreme but plausible worst-case scenarios for stress testing |
