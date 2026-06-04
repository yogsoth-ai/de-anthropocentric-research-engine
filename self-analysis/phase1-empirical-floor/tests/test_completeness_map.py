from completeness_map import build_completeness

GRAPH = {"nodes": ["a", "b", "c"],
         "edges": [["a", "b", "used-by"]],  # b has incoming; a,c do not
         "dangling_targets": []}
MODEL = {"skills": [{"name": n} for n in ["a", "b", "c"]], "parse_errors": []}

def test_incoming_edge_is_in_use():
    cm = build_completeness(MODEL, GRAPH, telemetry={"firing_counts": {}})
    assert cm["labels"]["b"] == "in-use"

def test_fired_is_in_use_even_without_edge():
    cm = build_completeness(MODEL, GRAPH, telemetry={"firing_counts": {"a": {"invocations": 3}}})
    assert cm["labels"]["a"] == "in-use"

def test_no_edge_not_fired_with_telemetry_is_suspect():
    cm = build_completeness(MODEL, GRAPH, telemetry={"firing_counts": {"a": {"invocations": 1}}})
    assert cm["labels"]["c"] == "suspect-redundant"

def test_no_telemetry_means_unknown_never_suspect():
    cm = build_completeness(MODEL, GRAPH, telemetry=None)
    assert cm["labels"]["a"] == "unknown"
    assert cm["labels"]["c"] == "unknown"
    assert "suspect-redundant" not in cm["labels"].values()
    assert cm["coverage"]["telemetry_present"] is False

def test_not_a_pruning_verdict_banner():
    cm = build_completeness(MODEL, GRAPH, telemetry={"firing_counts": {}})
    assert "not a pruning verdict" in cm["_disclaimer"].lower()
