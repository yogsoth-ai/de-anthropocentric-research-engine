from blast_radius import compute_blast_radius

def test_transitive_callers():
    # camp -> strat -> tac  (forward). Changing 'tac' affects strat and camp.
    graph = {"nodes": ["camp", "strat", "tac"],
             "edges": [["camp", "strat", "campaign"], ["strat", "tac", "tactics"]],
             "dangling_targets": []}
    br = compute_blast_radius(graph)
    assert set(br["tac"]["impacted"]) == {"strat", "camp"}
    assert br["tac"]["impact_size"] == 2
    assert br["camp"]["impact_size"] == 0  # nothing calls camp

def test_cycle_terminates():
    graph = {"nodes": ["a", "b"],
             "edges": [["a", "b", "dependencies"], ["b", "a", "dependencies"]],
             "dangling_targets": []}
    br = compute_blast_radius(graph)
    assert set(br["a"]["impacted"]) == {"b"}
    assert set(br["b"]["impacted"]) == {"a"}
