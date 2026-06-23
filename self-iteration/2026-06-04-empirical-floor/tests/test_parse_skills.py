from parse_skills import parse_skill_file, parse_skills_dir, _norm_list
from pathlib import Path

FIX = Path(__file__).parent / "fixtures" / "skills"

def test_comma_scalar_used_by_splits_into_multiple():
    # Real body: 126 files write `used-by: a, b, c` as one comma-joined scalar.
    assert _norm_list("a, b, c") == ["a", "b", "c"]
    assert _norm_list("solo") == ["solo"]

def test_list_form_not_resplit_on_internal_comma():
    # A YAML block-list item is already a discrete name; never re-split it.
    assert _norm_list(["a", "b"]) == ["a", "b"]

def test_dict_form_dependencies_extracts_skills_key():
    # Real body: 65 files write `dependencies: {skills: [...], mcp: {...}}`.
    # Only the skills: entries are skill-graph edges; mcp: names external servers.
    FIXD = FIX / "dict-deps" / "SKILL.md"
    rec = parse_skill_file(FIXD)
    assert rec["parse_error"] is None
    assert rec["dependencies"] == ["context-management", "subagent-spawning"]


def test_scalar_used_by_normalized_to_list():
    rec = parse_skill_file(FIX / "scalar-ub" / "SKILL.md")
    assert rec["name"] == "scalar-ub"
    assert rec["used_by"] == ["parent-a"]

def test_list_used_by_and_layer_edges():
    rec = parse_skill_file(FIX / "list-ub" / "SKILL.md")
    assert rec["used_by"] == ["parent-a", "parent-b"]
    assert rec["tactics"] == ["tac-x"]
    assert rec["sops"] == ["sop-y"]

def test_bom_prefixed_frontmatter_still_parses():
    # Real body has 24 SKILL.md files that open with a UTF-8 BOM before '---'.
    rec = parse_skill_file(FIX / "bom-ub" / "SKILL.md")
    assert rec["parse_error"] is None
    assert rec["name"] == "bom-ub"
    assert rec["used_by"] == ["parent-a"]

def test_missing_frontmatter_recorded_not_crash():
    rec = parse_skill_file(FIX / "no-fm" / "SKILL.md")
    assert rec["parse_error"] == "no-frontmatter"

def test_malformed_yaml_recorded_not_crash():
    rec = parse_skill_file(FIX / "bad-fm" / "SKILL.md")
    assert rec["parse_error"] == "yaml-error"

def test_dir_scan_returns_all_and_collects_errors():
    model = parse_skills_dir(FIX)
    assert len(model["skills"]) == 6
    assert sorted(model["parse_errors"]) == ["bad-fm", "no-fm"]
