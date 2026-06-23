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


def test_read_frontmatter_repairs_unquoted_colon_in_description(tmp_path):
    # source-repo defect: an unquoted ':' in the description value breaks YAML.
    # read_frontmatter must repair (quote the description) and still parse.
    md = tmp_path / "SKILL.md"
    md.write_text(
        "---\nname: spawn-agent\n"
        "description: Spawn a CC subagent. Used by SOPs that declare execution: subagent.\n"
        "execution: subagent\n---\nbody\n", encoding="utf-8")
    fm, body = lib.read_frontmatter(md)
    assert fm is not None, "repair failed: still unparseable"
    assert fm["name"] == "spawn-agent"
    assert "execution: subagent" in fm["description"]
    assert fm["execution"] == "subagent"


def test_read_frontmatter_repair_preserves_embedded_quotes(tmp_path):
    md = tmp_path / "SKILL.md"
    md.write_text(
        '---\nname: foo\n'
        'description: Reads "config.yaml": then runs. Budget: 5 calls.\n---\nbody\n',
        encoding="utf-8")
    fm, _ = lib.read_frontmatter(md)
    assert fm is not None
    assert "config.yaml" in fm["description"] and "Budget: 5" in fm["description"]
