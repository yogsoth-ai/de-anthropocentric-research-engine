import json
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "injection-fidelity" / "SKILL.md"
SCHEMA = LF / "skills" / "injection-fidelity" / "loss1.schema.json"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit
from generator.weights import _COORD_TABLE


def test_files_exist():
    assert SKILL.exists() and SCHEMA.exists()


def test_skill_and_schema_leak_clean():
    leak_audit(SKILL.read_text(encoding="utf-8"))
    leak_audit(SCHEMA.read_text(encoding="utf-8"))


def test_schema_is_valid_json_with_required_keys():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert s.get("additionalProperties") is False
    req = set(s["required"])
    assert {"fidelity", "loss1", "per_axis_evidence", "drift_flag"} <= req
    props = s["properties"]
    assert props["fidelity"]["type"] == "boolean"
    assert props["loss1"]["type"] == "number"
    assert props["drift_flag"]["type"] == "boolean"


def test_six_rung_expected_matrix_matches_coord_table():
    # A1 increases with rung quality: rung 0 -> L4 band, rung 5 -> L0 band
    assert _COORD_TABLE["0"]["A1"] == "L4"
    assert _COORD_TABLE["5"]["A1"] == "L0"
    # the SKILL.md must state the same monotone direction; assert it names A1 + pushback
    txt = SKILL.read_text(encoding="utf-8")
    assert "A1" in txt and "pushback" in txt.lower()


def test_consistency_rule_documented():
    # loss1 == count(pass)/5 and fidelity == all(pass) and not drift -- must be in prose
    txt = SKILL.read_text(encoding="utf-8")
    assert "/5" in txt or "/ 5" in txt
    assert "drift" in txt.lower()
