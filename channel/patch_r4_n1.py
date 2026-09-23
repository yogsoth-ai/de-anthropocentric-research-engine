import json
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parents[1]
ARCH = json.loads((BASE / "refactory/2026-08-23-22-16-dare-v4-architecture.json").read_text(encoding="utf-8"))
SOURCE = json.loads((BASE / "scripts/refactory_source.json").read_text(encoding="utf-8"))
META = {x["id"]: x for k in ("tactics", "sops") for x in ARCH[k]}
TACTICS = {x["id"] for x in ARCH["tactics"]}
SOURCE_NAMES = {x["name"] for x in SOURCE["nodes"]}
R4 = [
    "analyze-experiment-results", "analyze-future-scenarios", "build-domain-ontology",
    "construct-argument-map", "construct-causal-model", "decompose-research-question",
    "falsifiability-audit", "formulate-research-question", "pairwise-ranking",
    "portfolio-optimization", "structured-consensus", "construct-design-matrix",
    "design-randomness-protocol", "estimate-sample-size", "extract-core-conflict",
    "identify-critical-chain", "identify-scenario-drivers", "list-undesirable-effects",
    "map-ablation-components", "optimize-design-under-budget", "predict-competitive-move",
    "project-future-reality", "quantify-resource-gap", "select-experimental-baseline",
    "select-statistical-method", "specify-execution-environment", "specify-metrics",
    "specify-reproducibility-protocol", "statistical-testing", "verify-reproducibility",
]

SOP_STEPS = {
    "construct-design-matrix": [
        "Enumerate factors, levels, blocking variables, and the chosen design mode; reject levels that are not measurable.",
        "Allocate runs under balance, orthogonality, randomization, and the stated run budget; show the allocation table.",
        "Audit aliasing, coverage, and run-order bias, then return the matrix with diagnostics and unresolved compromises.",
    ],
    "design-randomness-protocol": [
        "Inventory every stochastic source, including sampling, initialization, augmentation, scheduling, and nondeterministic kernels.",
        "Assign seed ownership, propagation rules, repetition counts, and logging points for the declared reproducibility target.",
        "Walk one rerun through the protocol and flag any randomness that remains uncontrolled or only statistically reproducible.",
    ],
    "estimate-sample-size": [
        "State the estimand, detectable effect, variance or prior uncertainty, design structure, and whether the target is power or precision.",
        "Calculate the required observations or repetitions under power = 0.8, recording α = 0.05 and the formula or simulation used.",
        "Vary the uncertain inputs, report sensitivity and attrition allowance, and reject a plan whose feasible budget cannot meet the target.",
    ],
    "extract-core-conflict": [
        "List the observed undesirable effects and the two desired conditions that cannot be satisfied simultaneously.",
        "Trace each condition through its prerequisite assumptions and mark which links are empirical, inferred, or disputed.",
        "Return the typed conflict structure with candidate leverage points and the evidence needed to dissolve each assumption.",
    ],
    "identify-critical-chain": [
        "Normalize the dependency graph into tasks, durations, resources, and convergence points before calculating paths.",
        "Find the longest resource-feasible dependency path and distinguish true criticality from a merely long branch.",
        "Stress the path against contention and delay, then report bottlenecks, slack, and the evidence behind each risk.",
    ],
    "identify-scenario-drivers": [
        "Collect candidate drivers from the stated horizon and classify their impact direction, magnitude, and controllability.",
        "Score uncertainty independently from impact and rank the drivers by their contribution to scenario divergence.",
        "Select the smallest defensible driver set, explain exclusions, and expose dependencies or correlated drivers.",
    ],
    "list-undesirable-effects": [
        "Extract observable negative effects from the supplied system observations and attach a source or measurement to each.",
        "Separate symptoms, downstream consequences, and duplicate descriptions while preserving severity and affected conditions.",
        "Return a deduplicated UDE register with confidence, evidence links, and the effects requiring causal follow-up.",
    ],
    "map-ablation-components": [
        "Partition the system into removable or replaceable units and record interfaces, shared state, and legal ablation boundaries.",
        "For each unit, state the expected contribution, dependency risks, and the comparison needed to isolate its effect.",
        "Check that the proposed ablations preserve the target claim and return a matrix of units, operations, and hypotheses.",
    ],
    "optimize-design-under-budget": [
        "Translate the resource budget into per-run limits, fixed overhead, and validity constraints that no candidate may violate.",
        "Compare feasible designs by expected information per cost while preserving the essential contrast, randomization, and measurement plan.",
        "Select the dominant design or document the tradeoff when no candidate is strictly superior; include the budget ledger.",
    ],
    "predict-competitive-move": [
        "Separate observed competitor signals from assumptions about capability, intent, and timing.",
        "Construct plausible next moves and attach a timing range, enabling evidence, and preemption consequence to each.",
        "Rank priority risks under the declared horizon and identify what new evidence would reverse the forecast.",
    ],
    "project-future-reality": [
        "Insert the proposed intervention into the supplied causal or constraint model and state the expected immediate effects.",
        "Propagate consequences through downstream links, including new undesirable effects, side effects, and displaced bottlenecks.",
        "Return the projected tree with evidence status and a verdict on whether the intervention breaks the target constraint.",
    ],
    "quantify-resource-gap": [
        "Define the plan scope and units, then estimate demand for people, compute, data, time, and materials.",
        "Record available supply, committed allocations, and uncertainty bounds before subtracting supply from demand.",
        "Classify gap severity, identify the binding resource, and show which assumption or mitigation would change the result.",
    ],
    "select-experimental-baseline": [
        "Translate the experimental claim into the capabilities a fair baseline must share and the controls it must not receive.",
        "Inventory SOTA, simple, oracle, and control candidates with protocol, data, compute, and provenance comparability.",
        "Select the minimal baseline set that tests the claim and record exclusions, fairness risks, and rationale.",
    ],
    "select-statistical-method": [
        "Read the predeclared design, outcome scale, pairing, sample size, multiplicity plan, and decision objective.",
        "Compare eligible inferential or estimation procedures against distributional and dependence assumptions; preserve α = 0.05.",
        "Choose the method, state diagnostics and fallback boundaries, and explain why alternatives do not fit the design.",
    ],
    "specify-execution-environment": [
        "Capture hardware, software, data, configuration, and version variables that can change the experiment's interpretation.",
        "Mark which variables are fixed, sampled, or uncontrolled and connect each to a reproducibility or validity risk.",
        "Return a minimal environment record with identifiers, capture timing, and the omissions that remain material.",
    ],
    "specify-metrics": [
        "Name the primary and secondary estimands, measurement units, directionality, and population or comparison they describe.",
        "Set uncertainty reporting, missing-data handling, and decision thresholds before observing outcomes.",
        "Check metric validity against the claim and return the predeclared reporting and interpretation rules.",
    ],
    "specify-reproducibility-protocol": [
        "Choose the exact, statistical, or conceptual reproduction target and define what counts as agreement.",
        "Map seeds, environment capture, data versioning, rerun count, and comparison metrics to that target.",
        "Return acceptance criteria and known limits so a later verification can distinguish failure from target mismatch.",
    ],
    "statistical-testing": [
        "Lock the analysis to the predeclared test or estimator, outcome definition, comparison, and multiplicity rule.",
        "Compute effect size and uncertainty, including the α = 0.05 decision rule, model checks, and any ROPE or equivalence criterion.",
        "Interpret the result against the estimand and practical threshold without converting a non-significant result into evidence of no effect.",
    ],
    "verify-reproducibility": [
        "Align rerun and replication outputs to the declared reproducibility target and verify that environments and inputs are comparable.",
        "Compute suitable agreement, variance, or calibration metrics and report their uncertainty rather than a binary match alone.",
        "Judge the target-specific verdict, diagnose divergence sources, and state whether another run or a revised target is required.",
    ],
}

TACTIC_STEPS = {
    "analyze-experiment-results": ["Freeze the predeclared estimand and analysis plan before reading the outcome pattern.", "Run the statistical procedure and reproducibility check on the completed outputs, keeping effect size separate from decision significance.", "Calibrate the synthesis against uncertainty, model checks, and practical relevance before writing the interpretation."],
    "analyze-future-scenarios": ["Define the time horizon, scenario axes, and driver uncertainties that can change the research path.", "Construct internally compatible scenarios and compare impact, competitive timing, temporal trajectory, and robustness.", "Select the conclusions that survive scenario variation and mark the assumptions that make them fragile."],
    "build-domain-ontology": ["Fix the domain boundary and seed vocabulary, excluding entities that cannot be placed in the stated scope.", "Extract concepts, type relations, and build hierarchy while preserving evidence for each non-trivial edge.", "Audit consistency, coverage gaps, canonical identities, and confidence before returning the ontology."],
    "construct-argument-map": ["Atomize each claim and expose premises, assumptions, and counterclaims as typed nodes.", "Attach evidence and defeaters to relations, then score strength with the caller's rubric and visible uncertainty.", "Inspect contradictions and construct the final graph without averaging away unresolved disputes."],
    "construct-causal-model": ["Define measurable variables and candidate mechanisms with explicit direction and scope.", "Represent mechanism edges, evidence, feedback, interventions, and counterfactual dependencies in one inspectable graph.", "Validate causal links and update confidence while distinguishing correlation, mechanism, and intervention evidence."],
    "decompose-research-question": ["State the research question, scope, and answerability constraints that delimit decomposition.", "Generate MECE subquestions, map dependencies, and identify which subquestion each dependency enables.", "Sequence the work by prerequisite and information value, flagging overlaps and unanswerable branches."],
    "falsifiability-audit": ["State the hypothesis as a claim with an observable consequence and explicit boundary conditions.", "Operationalize constructs and evaluate whether an admissible observation could contradict the claim.", "Return the verdict, missing operational detail, and the smallest repair that preserves falsifiability."],
    "formulate-research-question": ["Select a framework that matches the hypothesis, population, comparison, and intended decision.", "Test question quality, scope, feasibility, criteria, and threshold against the available evidence and resources.", "Refine the abstraction level and emit one precise question with success criteria and documented exclusions."],
    "pairwise-ranking": ["Define the candidate set, comparison objective, and stopping rule before selecting a pair.", "Choose informative pairs, collect independent judgments, update ratings, and preserve disagreement rather than averaging it invisibly.", "Audit ranking coherence and stop only when the resolution criterion is met or the remaining uncertainty is explicit."],
    "portfolio-optimization": ["Formalize objectives, dependencies, resource limits, and scenario assumptions for the candidate portfolio.", "Construct the Pareto frontier, test impact and robustness across scenarios, and measure diversity and optionality.", "Select a feasible portfolio and sequence it with a traceable tradeoff and residual risk statement."],
    "structured-consensus": ["Map the judgment space into stable agreements, disagreements, evidence quality, and calibrated probabilities.", "Run bounded convergence rounds that revise arguments and confidence without erasing minority positions.", "Apply the stopping threshold and return consensus, unresolved disagreements, confidence, and stop rationale."],
}

def map_provenance(meta):
    out = []
    for old in meta.get("old", []):
        plain = re.sub(r"\s*\[[^]]*\]", "", old).strip()
        leaf = plain.rsplit("/", 1)[-1]
        if leaf in SOURCE_NAMES:
            out.append(f"- resolved: {leaf}")
        elif "[" in old and "]" in old:
            out.append(f"- intermediate: {old}")
        else:
            out.append(f"- concept: {old}")
    return out or ["- concept: v4 synthesis without a one-to-one v3 leaf"]

def delta_fields(produces):
    fields = ["findings"]
    text = " ".join(produces)
    for key, value in (("evidence", "evidence_updates"), ("hypothesis", "hypothesis_updates"),
                       ("assumption", "assumption_updates"), ("uncertainty", "uncertainties"),
                       ("decision", "decisions"), ("question", "open_questions")):
        if key in text and value not in fields:
            fields.append(value)
    return fields

def write(node_id):
    meta = META[node_id]
    if node_id in TACTICS:
        calls = ARCH["calls"].get(node_id, [])
        steps = [
            f"{i}. {TACTIC_STEPS[node_id][(i - 1) % len(TACTIC_STEPS[node_id])]} (`{call}`)"
            for i, call in enumerate(calls, 1)
        ]
        prod = {
            "analyze-experiment-results": ["effect_estimates", "uncertainty_summary", "reproducibility_assessment", "interpretation"],
            "analyze-future-scenarios": ["scenario_set", "impact_comparison", "robustness_assessment"],
            "build-domain-ontology": ["scoped_ontology", "typed_relations", "consistency_findings", "coverage_gaps"],
            "construct-argument-map": ["argument_graph", "evidence_links", "counterclaims", "strength_assessment"],
            "construct-causal-model": ["causal_graph", "mechanism_edges", "intervention_implications", "confidence_updates"],
            "decompose-research-question": ["subquestion_set", "dependency_map", "answering_sequence"],
            "falsifiability-audit": ["falsifiability_verdict", "operational_definition", "boundary_conditions"],
            "formulate-research-question": ["research_question", "success_criteria", "scope_decision"],
            "pairwise-ranking": ["updated_ratings", "ranking", "coherence_diagnostics"],
            "portfolio-optimization": ["pareto_frontier", "selected_portfolio", "scenario_risk_summary"],
            "structured-consensus": ["consensus_report", "unresolved_disagreements", "confidence_summary"],
        }[node_id]
        body = "\n".join([f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "", "```yaml", "required: [research_object, objective, constraints]", "optional: [evidence, assumptions, prior_results]", "constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]", "```", "", "## Execution protocol", "", *steps, "", "Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.", "", "## Output contract", "", "```yaml", f"produces: [{', '.join(prod)}]", f"delta_fields: [findings, {', '.join(x for x in ['evidence_updates','hypothesis_updates','assumption_updates','uncertainties','decisions','open_questions','recommended_jumps'] if any(k in ' '.join(prod) for k in x.split('_')))}]", "```", "", "## Thresholds and quality gates", "", "- Every output is traceable to a named input, called operation, and evidence reference.", "- Scope, assumptions, and unresolved alternatives remain explicit.", "- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.", "", "## Failure and counterexamples", "", "Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.", "", "## Provenance map", "", *map_provenance(meta), "", "## Preserved source criteria ledger", "", "| source | criterion | treatment |", "|---|---|---|", "| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |", "| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |", "| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |", "", "## Context checkpoint / Delta notes", "", "Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.", ""])
    else:
        steps = SOP_STEPS[node_id]
        stat = "constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]"
        body = "\n".join([f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "", "```yaml", "required: [research_object, operation_parameters]", "optional: [evidence, assumptions, constraints]", stat, "```", "", "## Procedure", "", *[f"{i}. {x}" for i, x in enumerate(steps, 1)], "", "## Output contract", "", "```yaml", "produces: [operation_result, evidence_trace, uncertainties]", "delta_fields: [findings, evidence_updates, uncertainties]", "```", "", "## Quality gates", "", f"- The {node_id.replace('-', ' ')} decision is tied to its declared scientific object and source evidence.", "- Missing values, assumptions, and boundary conditions remain visible.", "- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.", "", "## Failure and counterexamples", "", f"Reject {node_id.replace('-', ' ')} when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.", "", "## Provenance map", "", *map_provenance(meta), ""])
    body = body.replace("delta_fields: [findings, ]", "delta_fields: [findings, uncertainties]")
    body = body.replace("伪", chr(0x03B1))
    desc = meta["desc"].replace('"', '\\"')
    (BASE / "v4/skills" / node_id / "SKILL.md").write_text(f'---\nname: {node_id}\ndescription: "{desc}"\n---\n\n' + body, encoding="utf-8", newline="\n")

for node in R4:
    write(node)
print(f"patched {len(R4)} R4 skills")
