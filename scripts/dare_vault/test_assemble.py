from select import load, kept_names
from assemble import orchestration, page
def test_orchestration_has_down_and_utils():
    nodes, edges = load(); kept = kept_names(nodes)
    s = orchestration('abductive-hypothesis-generation', nodes, edges, kept)
    assert '[[concepts/dare-' in s
    assert '依赖的 utils' in s
def test_page_has_frontmatter_and_tag():
    nodes, edges = load(); kept = kept_names(nodes)
    p = page('six-hats-rotation', nodes, '讲解正文', edges, kept)
    assert p.startswith('---')
    assert 'dare-method' in p
    assert 'skills/six-hats-rotation/SKILL.md' in p
