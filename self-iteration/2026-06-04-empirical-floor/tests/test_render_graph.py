from render_graph import build_nodes_edges, LAYER_COLORS, EXCLUDE_LAYERS

LAYERED = {
    "camp": {"layer": "campaign", "source": "declared-type", "phase": "p"},
    "strat": {"layer": "strategy", "source": "declared-type", "phase": "p"},
    "leaf": {"layer": "sop", "source": "leaf-default", "phase": "p"},
    "ref": {"layer": "reference", "source": "override", "phase": None},
}
GRAPH = {"nodes": ["camp", "strat", "leaf", "ref"],
         "edges": [["camp", "strat", "campaign"], ["strat", "leaf", "used-by"],
                   ["ref", "leaf", "used-by"]],
         "dangling_targets": []}

def test_reference_layer_excluded_from_nodes():
    nodes, edges = build_nodes_edges(GRAPH, LAYERED)
    ids = {n["id"] for n in nodes}
    assert "ref" not in ids
    assert {"camp", "strat", "leaf"} <= ids

def test_edges_touching_excluded_node_dropped():
    nodes, edges = build_nodes_edges(GRAPH, LAYERED)
    for e in edges:
        assert e["from"] != "ref" and e["to"] != "ref"
    # the two clean edges survive
    assert len(edges) == 2

def test_node_colored_by_layer():
    nodes, _ = build_nodes_edges(GRAPH, LAYERED)
    by_id = {n["id"]: n for n in nodes}
    assert by_id["camp"]["color"] == LAYER_COLORS["campaign"]
    assert by_id["leaf"]["color"] == LAYER_COLORS["sop"]

def test_inferred_node_marked_dashed_border():
    # leaf-default is inferred, not declared -> visually flagged
    nodes, _ = build_nodes_edges(GRAPH, LAYERED)
    by_id = {n["id"]: n for n in nodes}
    assert by_id["leaf"]["shapeProperties"]["borderDashes"] is True
    assert by_id["camp"]["shapeProperties"]["borderDashes"] is False

def test_reference_in_exclude_set():
    assert "reference" in EXCLUDE_LAYERS

def test_strip_external_cdn_removes_bootstrap():
    from render_graph import strip_external_cdn
    html = ('<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/'
            'dist/css/bootstrap.min.css" rel="stylesheet"/>'
            '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/'
            'dist/js/bootstrap.bundle.min.js"></script></head>'
            '<body><script>var x=1;</script></body>')
    out = strip_external_cdn(html)
    assert "jsdelivr" not in out
    assert "https://" not in out
    # the actual graph script survives
    assert "var x=1;" in out

