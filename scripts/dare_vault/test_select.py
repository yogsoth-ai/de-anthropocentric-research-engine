from select import load, kept_names, kept_edges

def test_counts():
    nodes, edges = load()
    kept = kept_names(nodes)
    assert len(kept) == 847, len(kept)
    assert len(nodes) - len(kept) == 83
    assert len(kept_edges(edges, kept)) == 1851

def test_analytical_sop_kept():
    nodes, _ = load()
    kept = kept_names(nodes)
    assert 'condition-cataloging' in kept
    assert 'creative-ideation-failure-mode-cataloging' in kept

def test_research_catalog_pkg_excluded():
    nodes, _ = load()
    kept = kept_names(nodes)
    assert 'research-catalog' not in kept
