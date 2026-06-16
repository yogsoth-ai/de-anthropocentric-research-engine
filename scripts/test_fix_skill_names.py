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
