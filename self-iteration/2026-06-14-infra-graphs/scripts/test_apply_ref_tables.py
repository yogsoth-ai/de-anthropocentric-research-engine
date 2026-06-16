import json, re
from pathlib import Path
import lib_refactory as lib
import apply_ref_tables as art

NINE = {"north-star-crystallization", "knowledge-acquisition", "deep-insight",
        "hypothesis-formation", "creative-ideation", "convergence",
        "stress-test", "experiment-execution", "knowledge-structuring"}


def test_build_tables_targets_match_refactory():
    """Every built table's skill set must equal the ref/<pkg> out-edge target set
    from refactory_source (post-rename names)."""
    tabs = art.build_tables()       # {pkg: [(layer, skill, desc), ...]}
    assert set(tabs) == NINE
    total = sum(len(v) for v in tabs.values())
    assert total == 889, f"ref rows={total}"


def test_skill_names_are_post_rename():
    tabs = art.build_tables()
    names = {n["name"] for n in lib.load_source()["nodes"]}
    for pkg, rows in tabs.items():
        for layer, skill, desc in rows:
            assert skill in names, f"{pkg}: {skill} not a real node"


def test_descriptions_preserved_not_mojibake():
    """Renamed rows must keep the clean committed description text, never the
    mojibake HTML from refactory_source."""
    tabs = art.build_tables()
    conv = {s: d for _, s, d in tabs["convergence"]}
    # collision skill renamed but description kept clean (ASCII-readable)
    d = conv["convergence-saturation-detection"]
    assert d and "�" not in d, repr(d)
    assert "<b>" not in d and "&middot;" not in d, repr(d)


def test_per_pkg_counts():
    tabs = art.build_tables()
    counts = {p: len(r) for p, r in tabs.items()}
    assert counts["convergence"] == 120
    assert counts["creative-ideation"] == 189
    assert counts["north-star-crystallization"] == 33
