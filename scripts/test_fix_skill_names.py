import fix_skill_names as m


def test_name_field_from_frontmatter():
    t = '---\nname: web-search\ndescription: x\n---\n# body\nname: not-this\n'
    assert m.name_field(t) == "web-search"


def test_name_field_dequotes():
    assert m.name_field('---\nname: "Web Search"\n---\n') == "Web Search"
    assert m.name_field("---\nname: 'web-search'\n---\n") == "web-search"


def test_name_field_ignores_body():
    # name only in body, not frontmatter -> None
    assert m.name_field("---\ndescription: x\n---\nname: nope\n") is None


def test_name_field_none_when_no_frontmatter():
    assert m.name_field("no frontmatter here\n") is None


def test_needs_fix():
    assert m.needs_fix("convergence-web-search",
                       "---\nname: web-search\n---\n") is True
    assert m.needs_fix("web-search",
                       "---\nname: web-search\n---\n") is False
    assert m.needs_fix("x", "---\ndescription: y\n---\n") is False  # no name -> skip


def test_fix_name_line_prefix_case():
    t = "---\nname: web-search\ndescription: keep me\n---\n# body\n"
    out = m.fix_name_line(t, "convergence-web-search")
    assert "name: convergence-web-search\n" in out
    assert "description: keep me\n" in out  # other lines intact
    assert "name: web-search\n" not in out


def test_fix_name_line_titlecase_case():
    t = "---\nname: Web Search\n---\n"
    assert m.fix_name_line(t, "web-search") == "---\nname: web-search\n---\n"


def test_fix_name_line_idempotent():
    t = "---\nname: web-search\ndescription: x\n---\n"
    assert m.fix_name_line(t, "web-search") == t


def test_fix_name_line_only_touches_name():
    t = '---\nname: Web Search\ndescription: "a: b"\nversion: 1.0.0\n---\nbody\n'
    out = m.fix_name_line(t, "web-search")
    assert out == '---\nname: web-search\ndescription: "a: b"\nversion: 1.0.0\n---\nbody\n'


def _mk(flat, folder, name):
    d = flat / folder
    d.mkdir(parents=True)
    (d / "SKILL.md").write_text(f"---\nname: {name}\ndescription: x\n---\nbody\n",
                                encoding="utf-8")


def test_scan_lists_only_mismatches(tmp_path):
    flat = tmp_path / "skills"
    _mk(flat, "convergence-web-search", "web-search")   # mismatch
    _mk(flat, "ablation-design", "ablation-design")     # ok
    got = dict(m.scan(flat))
    assert got == {"convergence-web-search": "web-search"}


def test_apply_fixes_rewrites_and_is_idempotent(tmp_path):
    flat = tmp_path / "skills"
    _mk(flat, "convergence-web-search", "web-search")
    changed = m.apply_fixes(flat)
    assert changed == ["convergence-web-search"]
    txt = (flat / "convergence-web-search" / "SKILL.md").read_text(encoding="utf-8")
    assert "name: convergence-web-search\n" in txt
    assert "description: x\n" in txt
    # second run: nothing left to change
    assert m.apply_fixes(flat) == []
