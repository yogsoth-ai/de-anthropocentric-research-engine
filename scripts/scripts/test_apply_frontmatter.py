import json
from pathlib import Path
import lib_refactory as lib
import apply_frontmatter as af


def test_build_dep_index():
    idx = af.build_dep_index()      # node -> {subkey: [skill names]}
    mcs = idx["convergence-multi-criteria-scoring"]
    assert "pairwise-ranking" in mcs.get("campaigns", [])      # same-layer edge
    assert "convergence-saturation-detection" in mcs.get("sops", [])


def test_no_references_targets_in_index():
    idx = af.build_dep_index()
    flat = {t for subs in idx.values() for lst in subs.values() for t in lst}
    assert not any(t.startswith("ref/") for t in flat)
    assert "timestamp.py" not in flat


def test_subkeys_clipped_by_layer():
    idx = af.build_dep_index()
    nodes = {n["name"]: n for n in lib.load_source()["nodes"]}
    for name, subs in idx.items():
        layer = nodes[name]["layer"]
        if layer == "tactic":
            assert set(subs) <= {"tactics", "sops"}
        if layer == "sop":
            assert set(subs) <= {"sops"}


def test_total_dep_edges_is_2476():
    idx = af.build_dep_index()
    total = sum(len(v) for subs in idx.values() for v in subs.values())
    assert total == 2476, f"total dep edges={total}"
