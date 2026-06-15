import json
from pathlib import Path
import lib_refactory as lib

HERE = Path(__file__).resolve().parent


def test_load_source():
    d = lib.load_source()
    assert d["meta"]["node_count"] == 915
    assert len(d["edges"]) == 3376


def test_rename_map_101():
    rm = lib.rename_map()      # {(pkg, old_bare): new_bare}
    assert len(rm) == 101      # 64 collision + 37 wrapper


def test_subkey_for_layer():
    # edge target layer -> dependencies sub-key
    assert lib.subkey_for_layer("campaign") == "campaigns"
    assert lib.subkey_for_layer("strategy") == "strategies"
    assert lib.subkey_for_layer("tactic") == "tactics"
    assert lib.subkey_for_layer("sop") == "sops"


def test_wrapper_source_map():
    ws = lib.wrapper_source_map()   # {new_wrapper_name: "skills/<body>/SKILL.md"}
    assert ws["north-star-crystallization-broad-web-search"] == "skills/web-search/SKILL.md"
    assert len(ws) == 37


def test_is_real_skill_node():
    nodes = {n["name"]: n for n in lib.load_source()["nodes"]}
    assert lib.is_real_skill_node("convergence-saturation-detection", nodes) is True
    assert lib.is_real_skill_node("ref/convergence", nodes) is False   # references layer
    assert lib.is_real_skill_node("timestamp.py", nodes) is False      # references layer
