import json
from pathlib import Path
from usage_telemetry import collect_telemetry

FIX = Path(__file__).parent / "fixtures" / "logs"
GRAPH = {"nodes": ["warm-start", "context-init"],
         "edges": [["warm-start", "context-init", "dependencies"]],
         "dangling_targets": []}

def test_scope_filter_excludes_other_projects():
    t = collect_telemetry(FIX, GRAPH, scope_substr="YOGSOTH-AI")
    # warm-start fired once (dare.jsonl), NOT twice — other.jsonl excluded
    assert t["firing_counts"]["warm-start"]["invocations"] == 1

def test_cooccurrence_same_session():
    t = collect_telemetry(FIX, GRAPH, scope_substr="YOGSOTH-AI")
    pairs = {tuple(p[:2]): p[2] for p in t["cooccurrence"]}
    assert pairs[("context-init", "warm-start")] == 1  # sorted pair

def test_centrality_present_from_graph():
    t = collect_telemetry(FIX, GRAPH, scope_substr="YOGSOTH-AI")
    assert "context-init" in t["centrality"]

def test_output_has_no_identifiers():
    t = collect_telemetry(FIX, GRAPH, scope_substr="YOGSOTH-AI")
    blob = json.dumps(t)
    for leak in ["sessionId", "s1", "cwd", "C:\\\\", "YOGSOTH-AI", "Japanese"]:
        assert leak not in blob
