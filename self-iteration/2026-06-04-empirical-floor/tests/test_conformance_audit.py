from conformance_audit import audit_conformance, REQUIREMENTS

def test_counts_by_execution():
    model = {"skills": [
        {"name": "a", "execution": "subagent"},
        {"name": "b", "execution": "subagent"},
        {"name": "c", "execution": "strategy"},
        {"name": "d", "execution": None},
        {"name": "e", "execution": "weird-value"},
    ], "parse_errors": []}
    res = audit_conformance(model)
    assert res["counts"]["subagent"] == 2
    assert res["counts"]["strategy"] == 1
    assert res["counts"]["missing"] == 1
    assert res["counts"]["other"] == 1

def test_every_known_class_has_a_requirement():
    for cls in ["subagent", "tactic", "strategy", "campaign", "dialogue",
                "import", "sequential", "entry", "reference"]:
        assert cls in REQUIREMENTS and REQUIREMENTS[cls]

def test_markdown_render_lists_requirement():
    model = {"skills": [{"name": "a", "execution": "subagent"}], "parse_errors": []}
    md = audit_conformance(model)["markdown"]
    assert "subagent" in md
    assert REQUIREMENTS["subagent"] in md
