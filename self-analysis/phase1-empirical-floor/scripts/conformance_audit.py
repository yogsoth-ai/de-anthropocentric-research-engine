"""Study 1a: static conformance contract from execution fields."""
import argparse, json
from collections import Counter
from pathlib import Path

REQUIREMENTS = {
    "subagent": "Runtime MUST spawn an isolated sub-agent and recover its structured output.",
    "tactic": "Runtime MUST sequence multiple SOPs and aggregate their outputs.",
    "strategy": "Runtime MUST orchestrate nested tactics with budget/gate tracking.",
    "campaign": "Runtime MUST drive an end-to-end multi-strategy pipeline with phase state.",
    "dialogue": "Runtime MUST support multi-turn interactive Q&A with the user.",
    "import": "Runtime MUST resolve and inline an external/source skill by reference.",
    "sequential": "Runtime MUST execute ordered steps in-process without sub-agent spawn.",
    "entry": "Runtime MUST treat this as a pipeline entry point / router.",
    "reference": "Runtime MUST treat this as read-only reference material, not executable.",
}
KNOWN = set(REQUIREMENTS)

def audit_conformance(model):
    counts = Counter()
    members = {k: [] for k in list(KNOWN) + ["other", "missing"]}
    for s in model["skills"]:
        if s.get("parse_error"): continue
        ex = s.get("execution")
        cls = "missing" if not ex else (ex if ex in KNOWN else "other")
        counts[cls] += 1
        members[cls].append(s["name"])
    lines = ["# DARE Conformance Contract (Study 1a)", "",
             "What any runtime must satisfy to execute the skill body.", ""]
    for cls in list(REQUIREMENTS) + ["other", "missing"]:
        req = REQUIREMENTS.get(cls, "(no runtime requirement — uncategorized / not declared)")
        lines.append(f"## `{cls}` — {counts[cls]} skills")
        lines.append(f"**Requirement:** {req}")
        lines.append("")
    return {"counts": dict(counts), "members": members, "markdown": "\n".join(lines)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    model = json.loads(Path(a.model).read_text(encoding="utf-8"))
    res = audit_conformance(model)
    Path(a.out).write_text(res["markdown"], encoding="utf-8")
    print("counts:", res["counts"])

if __name__ == "__main__":
    main()
