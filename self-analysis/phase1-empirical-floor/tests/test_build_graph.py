from build_graph import build_graph

def test_used_by_reverses_to_forward_edge():
    model = {"skills": [
        {"name": "child", "used_by": ["parent"], "dependencies": [], "tactics": [], "sops": [], "campaign": None},
        {"name": "parent", "used_by": [], "dependencies": [], "tactics": [], "sops": [], "campaign": None},
    ], "parse_errors": []}
    g = build_graph(model)
    assert ["parent", "child", "used-by"] in g["edges"]

def test_tactics_sops_campaign_edges():
    model = {"skills": [
        {"name": "strat", "used_by": [], "dependencies": [], "tactics": ["tac"], "sops": ["sop"], "campaign": "camp"},
    ], "parse_errors": []}
    g = build_graph(model)
    assert ["strat", "tac", "tactics"] in g["edges"]
    assert ["strat", "sop", "sops"] in g["edges"]
    assert ["camp", "strat", "campaign"] in g["edges"]

def test_dangling_target_flagged_not_dropped():
    model = {"skills": [
        {"name": "a", "used_by": [], "dependencies": ["ghost"], "tactics": [], "sops": [], "campaign": None},
    ], "parse_errors": []}
    g = build_graph(model)
    assert ["a", "ghost", "dependencies"] in g["edges"]
    assert "ghost" in g["dangling_targets"]

def test_nodes_include_every_parsed_skill():
    model = {"skills": [
        {"name": "x", "used_by": [], "dependencies": [], "tactics": [], "sops": [], "campaign": None},
    ], "parse_errors": []}
    g = build_graph(model)
    assert "x" in g["nodes"]
