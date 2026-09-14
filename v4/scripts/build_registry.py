"""Derive v4 registry artifacts from the read-only architecture source."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCH = Path(r"D:\YOGSOTH-AI\file-transfer\2026-08-23-22-16-dare-v4-architecture.json")
REG = ROOT / "v4" / "registry"
PROV_SUFFIX = re.compile(r"\s*(?:\([^)]*\)|\[[^]]*\])\s*$")
EXPLICIT_INTERMEDIATE = {
    "conceptual-blending [strategy]",
    "Pass3/merge-near-duplicate-concepts",
}
PROVENANCE_ALIASES = {
    "conceptual-blending/generic-space": "generic-space-extraction",
}
DESC_MODE_OVERRIDES = {
    "sensitivity-analysis": {
        "modes": ["Morris", "Sobol", "perturbation", "Monte-Carlo"],
        "modes_provenance": {
            "source": "architecture.desc",
            "reason": "Architecture desc declares four modes; R4 audit resolves each to v3 source nodes.",
            "v3_sources": {
                "Morris": ["parameter-screening (strategy):2384", "morris-screening (SOP):2853"],
                "Sobol": ["variance-decomposition (strategy):2391", "sobol-decomposition (SOP):2860"],
                "perturbation": ["systematic-perturbation (tactic):2510", "controlled-perturbation (SOP):2811"],
                "Monte-Carlo": ["uncertainty-propagation (strategy):2405", "monte-carlo-sampling (SOP):2909"],
            },
        },
    },
    "synthesize-literature-evidence": {
        "modes": ["scoping", "systematic", "deep", "narrative", "snowball"],
        "modes_provenance": {
            "source": "architecture.desc",
            "reason": "Architecture desc declares five execution modes; R4 audit resolves each to a v3 survey strategy.",
            "v3_sources": {
                "scoping": ["scoping-survey (strategy):4239"],
                "systematic": ["systematic-survey (strategy):4246"],
                "deep": ["deep-survey (strategy):4253"],
                "narrative": ["narrative-review (strategy):4260"],
                "snowball": ["snowball (strategy):4267"],
            },
        },
    },
    "synthesize-meta-analytic-evidence": {
        "modes": ["pairwise", "network", "cumulative", "heterogeneity", "bias"],
        "modes_provenance": {
            "source": "architecture.desc",
            "reason": "The authoritative desc explicitly declares these modes while the architecture modes field is absent.",
        },
    },
    "design-experiment": {
        "modes": ["factorial", "ablation", "comparison", "scaling", "robustness"],
        "modes_provenance": {
            "source": "architecture.desc",
            "reason": "Architecture desc declares five design modes; R4 audit resolves each to a v3 design strategy.",
            "v3_sources": {
                "factorial": ["experiment-execution-factor-level-design (strategy):3105"],
                "ablation": ["ablation-design (strategy):3112"],
                "comparison": ["comparison-design (strategy):3119"],
                "scaling": ["scaling-design (strategy):3126"],
                "robustness": ["robustness-design (strategy):3133"],
            },
        },
    },
}
R2_PROVENANCE_SOURCES = {
    "falsifiability-audit": {"falsifiability/audit <- architecture semantic consolidation": "falsifiability-audit"},
    "pairwise-ranking": {"pairwise/ranking <- architecture semantic consolidation": "pairwise-ranking"},
    "define-criteria": {"hypothesis-formation/scoring-matrix-construction (criteria-extraction core)": "hypothesis-formation-scoring-matrix-construction"},
    "elicit-weights": {"hypothesis-formation/ahp-weighting": "ahp-weighting", "convergence/weight-elicitation-sop": "weight-elicitation-sop"},
    "identify-variables": {"hypothesis-formation/variable-identification": "hypothesis-formation-variable-identification"},
    "generate-subquestions": {"hypothesis-formation/sub-question-generation": "sub-question-generation"},
    "sequence-work": {"hypothesis-formation/answering-sequence-design": "answering-sequence-design"},
    "verify-evidence-independence": {"deep-insight/cross-database-verification": "cross-database-verification"},
    "surface-assumptions": {"creative-ideation/assumption-surfacing": "creative-ideation-assumption-surfacing", "deep-insight/assumption-enumeration": "deep-insight-assumption-enumeration", "convergence/assumption-extraction": "convergence-assumption-extraction"},
    "challenge-assumption": {"convergence/assumption-challenge": "convergence-assumption-challenge"},
    "apply-perturbation": {"creative-ideation/assumption-perturbation": "creative-ideation-assumption-perturbation"},
    "detect-breakpoint": {"stress-test/breakpoint-detection": "breakpoint-detection", "deep-insight/controlled-perturbation (threshold detection output)": "controlled-perturbation"},
    "construct-validity-envelope": {"deep-insight/validity-envelope-construction": "deep-insight-validity-envelope-construction", "stress-test/validity-envelope-construction": "stress-test-validity-envelope-construction"},
    "construct-defense": {"stress-test/debate-defender": "debate-defender", "convergence/advocate-construction": "advocate-construction"},
    "adjudicate-exchange": {"stress-test/debate-judge": "debate-judge", "convergence/judge-verdict": "judge-verdict"},
    "derive-consequences": {"stress-test/deductive-chain": "deductive-chain", "deep-insight/consequence-following": "consequence-following"},
    "enumerate-combinations": {"creative-ideation/matrix-construction": "matrix-construction", "creative-ideation/recombination-generation": "recombination-generation"},
    "evaluate-compatibility": {"creative-ideation/consistency-pair-evaluation": "creative-ideation-consistency-pair-evaluation"},
    "generate-provocation": {"creative-ideation/po-provocation": "po-provocation", "deep-insight/provocation-generation": "deep-insight-provocation-generation", "creative-ideation/random-word-stimulus": "random-word-stimulus"},
    "identify-bottleneck": {"convergence/bottleneck-identification": "convergence-bottleneck-identification", "deep-insight/critical-path-identification (limiting-input interpretation)": "critical-path-identification"},
    "identify-obstacles": {"north-star-crystallization/identify-obstacles": "identify-obstacles", "experiment-execution/obstacle-identification": "obstacle-identification"},
    "trace-causal-chain": {"knowledge-structuring/causal-chain-query": "causal-chain-query", "experiment-execution/causal-chain-tracing": "causal-chain-tracing"},
    "design-mitigation": {"stress-test/mitigation-design-sop": "mitigation-design-sop", "stress-test/re-scoring": "re-scoring", "convergence/removal-path": "removal-path"},
    "evaluate-scenario-impact": {"convergence/portfolio-evaluation-per-scenario": "portfolio-evaluation-per-scenario", "experiment-execution/scenario-impact-assessment": "scenario-impact-assessment"},
    "map-coverage-space": {"creative-ideation/method-problem-crossing": "method-problem-crossing", "knowledge-acquisition/capability-taxonomy-mapping": "capability-taxonomy-mapping"},
    "normalize-comparison-scale": {"convergence/normalization": "normalization", "knowledge-acquisition/compute-normalization": "compute-normalization"},
    "score-object": {"hypothesis-formation/novelty-scoring": "hypothesis-formation-novelty-scoring", "deep-insight/multi-criteria-scoring": "deep-insight-multi-criteria-scoring", "knowledge-structuring/novelty-scoring": "knowledge-structuring-novelty-scoring", "knowledge-structuring/gap-prioritization [strategy]": "knowledge-structuring-gap-prioritization"},
    "inventory-reference-items": {"knowledge-acquisition/benchmark-inventory": "knowledge-acquisition-benchmark-inventory", "creative-ideation/benchmark-inventory": "creative-ideation-benchmark-inventory"},
    "measure-portfolio-diversity": {"convergence/diversity-maximization [strategy]": "diversity-maximization", "convergence/niche-coverage-analysis [tactic]": "niche-coverage-analysis"},
    "construct-perspective-set": {"multi-worldview-comparison [tactic]": "multi-worldview-comparison", "stakeholder-objection-simulation [strategy]": "stakeholder-objection-simulation"},
    "rotate-perspective": {"personal-analogy [synectics tactic]": "personal-analogy"},
    "evaluate-scenario-robustness": {"experiment-execution/robustness-scoring": "robustness-scoring", "experiment-execution/strategy-robustness-testing [tactic]": "strategy-robustness-testing", "convergence/portfolio-optimization/robustness-under-uncertainty [strategy]": "robustness-under-uncertainty"},
}
R4_RESOLVED_ALIASES = [
    {"v3_id": "anti-benchmark", "v4_id": "audit-benchmark-validity", "compression_type": "many-to-1", "notes": "R4 resolved alias; capability-audit chain continues through destructive-ideation and coverage-white-space-search."},
    {"v3_id": "seed-concept-search", "v4_id": "extract-concepts", "compression_type": "many-to-1", "notes": "R4 resolved alias; mapped to extract-concepts."},
    {"v3_id": "synectics", "v4_id": "analogical-discovery", "compression_type": "many-to-1", "notes": "R4 resolved alias; capability-audit chain also covers conceptual-blending and problem-reframing perspective-shift."},
    {"v3_id": "web-search", "v4_id": "map-research-landscape", "compression_type": "many-to-1", "notes": "R4 resolved alias; broad/deep web-search imports are covered by map-research-landscape."},
]


def provenance_variants(value: str) -> set[str]:
    value = value.strip()
    stripped = value
    while True:
        next_value = PROV_SUFFIX.sub("", stripped).strip()
        if next_value == stripped:
            break
        stripped = next_value
    basename = stripped.rsplit("/", 1)[-1]
    variants = {value, stripped, basename}
    if "/" in stripped:
        package, name = stripped.rsplit("/", 1)
        variants.add(f"{package}-{name}")
    alias = PROVENANCE_ALIASES.get(stripped)
    if alias:
        variants |= {alias, alias.rsplit("/", 1)[-1]}
    return {x for x in variants if x}


def provenance_statuses(nodes: list[dict]) -> None:
    source = ROOT / "scripts" / "refactory_source.json"
    try:
        source_names = {n.get("name", "") for n in json.loads(source.read_text(encoding="utf-8")).get("nodes", [])}
        source_names |= {x.rsplit("/", 1)[-1] for x in source_names}
    except (OSError, json.JSONDecodeError):
        source_names = set()
    for node in nodes:
        statuses = {}
        for old in node.get("old", []):
            clean = PROV_SUFFIX.sub("", old).strip()
            variants = provenance_variants(old)
            if old in EXPLICIT_INTERMEDIATE:
                statuses[old] = "intermediate"
            elif any(candidate in source_names for candidate in variants):
                statuses[old] = "resolved"
            elif clean.startswith("Pass") or re.search(r"\[(?:campaign|strategy)(?:/tactic)?\]", old):
                statuses[old] = "intermediate"
            else:
                statuses[old] = "concept"
        node["provenance_status"] = statuses
        sources = R2_PROVENANCE_SOURCES.get(node["id"])
        if sources:
            node["provenance_sources"] = sources
            for old in sources:
                if old in statuses:
                    statuses[old] = "resolved"


def main() -> None:
    source = json.loads(ARCH.read_text(encoding="utf-8"))
    nodes = []
    for kind in ("tactics", "sops"):
        for node in source[kind]:
            item = dict(node)
            if node.get("id") in DESC_MODE_OVERRIDES:
                item.update(DESC_MODE_OVERRIDES[node["id"]])
            item["type"] = "tactic" if kind == "tactics" else "sop"
            item["provenance"] = item.get("old", [])
            nodes.append(item)
    provenance_statuses(nodes)
    calls = [
        {"type": "calls", "source": src, "target": target}
        for src, targets in source["calls"].items()
        for target in targets
    ]
    jumps = [
        {"type": "jump", "source": edge[0], "target": edge[1]}
        for edge in source["jumps"]
    ]
    graph = {
        "schema": "dare-v4-graph-1",
        "source": str(ARCH),
        "node_model": source["node_model"],
        "edge_semantics": source["edge_semantics"],
        "stats": source["stats"],
        "nodes": nodes,
        "edges": calls + jumps,
        "calls": calls,
        "jumps": jumps,
        "provenance_aliases": R4_RESOLVED_ALIASES,
        "counts": {
            "nodes": len(nodes),
            "tactics": len(source["tactics"]),
            "sops": len(source["sops"]),
            "calls": len(calls),
            "jumps": len(jumps),
            "edges": len(calls) + len(jumps),
            "capability_contracts": len(source["capability_audit"]),
        },
    }
    capabilities = {
        "schema": "dare-v4-capabilities-1",
        "source": str(ARCH),
        "count": len(source["capability_audit"]),
        "contracts": source["capability_audit"],
    }
    REG.mkdir(parents=True, exist_ok=True)
    (REG / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REG / "capabilities.json").write_text(json.dumps(capabilities, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
