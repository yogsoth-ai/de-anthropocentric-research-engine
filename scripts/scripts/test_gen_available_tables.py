import lib_refactory as lib
import gen_available_tables as gat


def test_layer_to_heading():
    assert gat.SUBKEY_HEADING["strategies"] == "Available Strategies"
    assert gat.SUBKEY_HEADING["tactics"] == "Available Tactics"
    assert gat.SUBKEY_HEADING["sops"] == "Available SOPs"
    assert gat.SUBKEY_HEADING["campaigns"] == "Available Campaigns"


def test_one_line_desc_strips_newlines_and_pipes():
    d = gat.one_line("Reads config.\nThen runs | fast")
    assert "\n" not in d and "|" not in d
    assert d == "Reads config. Then runs / fast"


def test_render_section_orders_and_labels(tmp_path):
    # a node with two sops -> one Available SOPs section, rows sorted by name
    descs = {"bar": "Do bar things", "baz": "Do baz things"}
    section = gat.render_section("sops", ["baz", "bar"], descs)
    assert "## Available SOPs" in section
    assert "| SOP | When to use |" in section
    # bar row precedes baz row (sorted)
    assert section.index("| bar |") < section.index("| baz |")
    assert "Do bar things" in section


def test_build_blocks_clips_by_layer(tmp_path):
    # construct a tiny skills tree: a strategy node depends on a tactic + sop
    skills = tmp_path / "skills"
    for nm, fm in [
        ("strat", "name: strat\ndependencies:\n  tactics:\n    - tac\n  sops:\n    - op\n"),
        ("tac", "name: tac\n"),
        ("op", "name: op\n"),
    ]:
        d = skills / nm
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\n{fm}---\nbody\n", encoding="utf-8")
    descs = gat.collect_descriptions(skills)
    block = gat.build_block("strat", skills, descs)
    assert "## Available Tactics" in block and "## Available SOPs" in block
    assert "Available Strategies" not in block       # strategy node has no strategies sub-key
