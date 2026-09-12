import json
import pathlib
import re
import shutil

BASE = pathlib.Path(__file__).resolve().parents[1]
V4 = BASE / "v4" / "skills"
ARCH = json.loads((BASE / "refactory/2026-08-23-22-16-dare-v4-architecture.json").read_text(encoding="utf-8"))
SOURCE = json.loads((BASE / "scripts/refactory_source.json").read_text(encoding="utf-8"))
META = {x["id"]: x for k in ("tactics", "sops") for x in ARCH[k]}
TACTICS = {x["id"] for x in ARCH["tactics"]}
PARTITION = json.loads((BASE / "channel/_partition.json").read_text(encoding="utf-8"))
IDS = []
for group in PARTITION.values():
    for item in group:
        if item[0] not in IDS:
            IDS.append(item[0])
for path in (BASE / "channel/deliverables/R5/pilot").glob("*/body.md"):
    if path.parent.name not in IDS:
        IDS.append(path.parent.name)
assert len(IDS) == 267, len(IDS)

R4_TACTICS = {
    "analyze-experiment-results", "analyze-future-scenarios", "build-domain-ontology",
    "construct-argument-map", "construct-causal-model", "decompose-research-question",
    "falsifiability-audit", "formulate-research-question", "pairwise-ranking",
    "portfolio-optimization", "structured-consensus",
}
R4_SOPS = {
    "construct-design-matrix", "design-randomness-protocol", "estimate-sample-size",
    "extract-core-conflict", "identify-critical-chain", "identify-scenario-drivers",
    "list-undesirable-effects", "map-ablation-components", "optimize-design-under-budget",
    "predict-competitive-move", "project-future-reality", "quantify-resource-gap",
    "select-experimental-baseline", "select-statistical-method", "specify-execution-environment",
    "specify-metrics", "specify-reproducibility-protocol", "statistical-testing",
    "verify-reproducibility",
}
R4 = R4_TACTICS | R4_SOPS

BODY = {}
for group in ("R1", "R2", "R3", "R5"):
    for path in (BASE / f"channel/deliverables/{group}").rglob("body.md"):
        BODY[path.parent.name] = path
for path in (BASE / "channel/deliverables/R5/pilot").glob("*/body.md"):
    BODY[path.parent.name] = path

def provenance(meta):
    names = {x["name"] for x in SOURCE["nodes"]}
    out = []
    for old in meta.get("old", []):
        plain = re.sub(r"\s*\[[^]]*\]", "", old).strip()
        normalized = plain.replace("/", "-")
        if normalized in names:
            out.append(f"- resolved: {normalized}")
        else:
            out.append(f"- intermediate: {old}")
    return out or ["- concept: v4 synthesis without a one-to-one v3 leaf"]

def delta(fields):
    text = " ".join(fields).lower()
    out = []
    for key, value in (("evidence", "evidence_updates"), ("hypothesis", "hypothesis_updates"),
                       ("assumption", "assumption_updates"), ("uncert", "uncertainties"),
                       ("decision", "decisions"), ("question", "open_questions"),
                       ("jump", "recommended_jumps")):
        if key in text and value not in out:
            out.append(value)
    return out or ["findings", "decisions"]

TACTIC_REQ = {
    "analyze-experiment-results": ["experiment_results", "predeclared_analysis_plan", "reproducibility_target"],
    "analyze-future-scenarios": ["research_path", "scenario_axes", "uncertainty_drivers"],
    "build-domain-ontology": ["domain_scope", "concept_records", "relation_evidence"],
    "construct-argument-map": ["claim_records", "premise_records", "evidence_records"],
    "construct-causal-model": ["variable_records", "mechanism_candidates", "evidence_records"],
    "decompose-research-question": ["research_question", "scope_constraints", "dependency_evidence"],
    "falsifiability-audit": ["hypothesis", "operational_definition", "boundary_conditions"],
    "formulate-research-question": ["hypothesis_or_gap", "candidate_frameworks", "feasibility_constraints"],
    "pairwise-ranking": ["candidate_set", "pairwise_judgments", "ranking_objective"],
    "portfolio-optimization": ["candidate_set", "objective_vector", "resource_constraints", "scenario_set"],
    "structured-consensus": ["judgment_records", "evidence_records", "stopping_rule"],
}
TACTIC_PROD = {
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
}

SOP_REQ = {
    "construct-design-matrix": ["factor_schema", "design_mode", "run_budget", "randomization_constraints"],
    "design-randomness-protocol": ["randomness_sources", "reproducibility_target", "run_plan"],
    "estimate-sample-size": ["effect_target", "uncertainty_model", "power_target", "design_structure"],
    "extract-core-conflict": ["undesirable_effects", "constraint_relations", "assumption_records"],
    "identify-critical-chain": ["dependency_graph", "resource_constraints", "convergence_points"],
    "identify-scenario-drivers": ["candidate_drivers", "impact_assessments", "uncertainty_assessments"],
    "list-undesirable-effects": ["system_observations", "effect_evidence", "severity_scale"],
    "map-ablation-components": ["system_structure", "component_dependencies", "removal_constraints"],
    "optimize-design-under-budget": ["candidate_designs", "run_costs", "resource_budget", "validity_constraints"],
    "predict-competitive-move": ["competitor_evidence", "research_path", "time_horizon"],
    "project-future-reality": ["intervention", "causal_model", "undesirable_effects"],
    "quantify-resource-gap": ["resource_demand", "resource_supply", "plan_scope"],
    "select-experimental-baseline": ["experimental_claim", "candidate_baselines", "protocol_context"],
    "select-statistical-method": ["design_structure", "outcome_type", "sample_size", "decision_objective"],
    "specify-execution-environment": ["hardware_context", "software_context", "data_context", "configuration_context"],
    "specify-metrics": ["estimand", "outcome_schema", "decision_thresholds"],
    "specify-reproducibility-protocol": ["reproducibility_target", "experiment_specification", "available_controls"],
    "statistical-testing": ["predeclared_analysis_plan", "observations", "comparison_structure"],
    "verify-reproducibility": ["reproducibility_target", "rerun_results", "replication_results"],
}
SOP_PROD = {k: [k.replace("-", "_") + "_result", "evidence_trace", "uncertainties"] for k in R4_SOPS}

def r4_body(node_id):
    meta = META[node_id]
    calls = ARCH["calls"].get(node_id, [])
    if node_id in R4_TACTICS:
        req = TACTIC_REQ[node_id]
        prod = TACTIC_PROD[node_id]
        steps = []
        for i, call in enumerate(calls, 1):
            steps.append(f"{i}. Use `{call}` on its named scientific object and record the evidence or decision it contributes.")
        return "\n".join([
            f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "",
            "```yaml", f"required: [{', '.join(req)}]", "optional: [assumptions, prior_findings, evidence_updates]",
            "constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]", "```", "",
            "## Execution protocol", "", *steps,
            "", "Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.", "",
            "## Output contract", "", "```yaml", f"produces: [{', '.join(prod)}]", f"delta_fields: [{', '.join(delta(prod))}]", "```", "",
            "## Thresholds and quality gates", "", "- Each output is traceable to an input object, operation, and evidence reference.",
            "- Scope, assumptions, and unresolved alternatives remain explicit.", "- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.", "",
            "## Failure and counterexamples", "", "Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.", "",
            "## Provenance map", "", *provenance(meta), "", "## Preserved source criteria ledger", "",
            "| source | criterion | treatment |", "|---|---|---|", "| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |",
            "| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |", "| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |", "",
            "## Context checkpoint / Delta notes", "", "Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.", ""
        ])
    req = SOP_REQ[node_id]
    prod = SOP_PROD[node_id]
    stat = "constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]"
    return "\n".join([
        f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "", "```yaml",
        f"required: [{', '.join(req)}]", "optional: [evidence, assumptions, prior_results]", stat, "```", "",
        "## Procedure", "", "1. Validate the typed inputs and state the decision this operation must support.",
        "2. Apply the declared operation to the named object; record intermediate values that affect interpretation.",
        "3. Check boundary conditions and counterexamples, then emit the result with uncertainty and source links.", "",
        "## Output contract", "", "```yaml", f"produces: [{', '.join(prod)}]", f"delta_fields: [{', '.join(delta(prod))}]", "```", "",
        "## Quality gates", "", "- Inputs are named scientific objects with compatible schemas.", "- Every material result has a derivation or source reference.", "- Fixed statistical criteria remain exact where applicable: α 0.05 and power 0.8.", "",
        "## Failure and counterexamples", "", "Return a failed operation with the violated precondition when inputs are incomplete, assumptions are unsupported, or a counterexample defeats the result.", "",
        "## Provenance map", "", *provenance(meta), ""
    ])

def generic_body(node_id):
    meta = META[node_id]
    if node_id in TACTICS:
        calls = ARCH["calls"].get(node_id, [])
        steps = [f"{i}. Prepare the `{call}` input and record the decision it contributes." for i, call in enumerate(calls[:8], 1)] or ["1. Establish the typed research object and admissible constraints.", "2. Apply the node-specific transformation and retain evidence links.", "3. Inspect uncertainty and counterexamples before selecting the result."]
        prod = ["structured_result", "evidence_trace", "uncertainties", "next_actions"]
        return "\n".join([f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "", "```yaml", "required: [research_object, objective, constraints]", "optional: [evidence, assumptions, prior_results]", "constraints: [use named research objects; preserve provenance; do not infer missing evidence]", "```", "", "## Execution protocol", "", *steps, "", "Deviation: skip or reorder a called operation only when its input is absent or already present; record the reason.", "", "## Output contract", "", "```yaml", f"produces: [{', '.join(prod)}]", f"delta_fields: [{', '.join(delta(prod))}]", "```", "", "## Thresholds and quality gates", "", "- Every transformation names the object consumed and its evidence.", "- Unresolved assumptions and boundary conditions remain explicit.", "- No conclusion is stronger than the supplied evidence.", "", "## Failure and counterexamples", "", "Reject the result when required objects are missing, criteria conflict, or a counterexample invalidates the claimed scope.", "", "## Provenance map", "", *provenance(meta), "", "## Preserved source criteria ledger", "", "| source | criterion | treatment |", "|---|---|---|", "| v3 provenance entries above | explicit source constraints | retained verbatim where resolved; otherwise marked unresolved |", "", "## Context checkpoint / Delta notes", "", "Record the selected result, evidence updates, uncertainty, decisions, open questions, and recommended jumps as the returned research-state delta.", ""])
    return "\n".join([f"# {node_id}", "", "## Purpose", "", meta["desc"], "", "## Input contract", "", "```yaml", "required: [research_object, operation_parameters]", "optional: [evidence, assumptions, constraints]", "constraints: [parameters name the scientific object being transformed; preserve provenance and missingness]", "```", "", "## Procedure", "", "1. Identify the typed target, decision question, and eligible evidence.", "2. Transform the target using the declared rule and attach each material choice to an input or source.", "3. Inspect scope, missingness, and counterexamples, then emit the typed result with uncertainty.", "", "## Output contract", "", "```yaml", "produces: [operation_result, evidence_trace, uncertainties]", "delta_fields: [findings, evidence_updates, uncertainties]", "```", "", "## Quality gates", "", "- The operation applies to a named scientific object, not a generic placeholder.", "- Every non-trivial value has a source, derivation, or explicit missing marker.", "- The output remains within scope and records uncertainty.", "", "## Failure and counterexamples", "", "Fail closed when the target schema is incomplete, evidence is incompatible, or a counterexample breaks the interpretation.", "", "## Provenance map", "", *provenance(meta), ""])

if V4.exists():
    for child in V4.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
for node_id in IDS:
    meta = META[node_id]
    if node_id in R4:
        body = r4_body(node_id)
    elif node_id in BODY:
        body = BODY[node_id].read_text(encoding="utf-8")
        body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S) if body.startswith("---") else body
    else:
        body = generic_body(node_id)
    description = meta["desc"].replace('"', '\\"')
    content = f'---\nname: {node_id}\ndescription: "{description}"\n---\n\n' + body.lstrip()
    path = V4 / node_id / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
print(f"generated {len(IDS)} skills; R4={len(R4)}; draft={len(BODY)}; synthesized={len(set(IDS)-set(BODY)-R4)}")
