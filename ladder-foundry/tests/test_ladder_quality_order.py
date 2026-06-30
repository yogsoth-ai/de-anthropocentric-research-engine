import json
import sys
import subprocess
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SKILL = LF / "skills" / "ladder-quality-order" / "SKILL.md"
SCHEMA = LF / "skills" / "ladder-quality-order" / "loss2.schema.json"

sys.path.insert(0, str(LF))
from generator.leak_audit import leak_audit


def test_files_exist():
    assert SKILL.exists() and SCHEMA.exists()


def test_skill_and_schema_leak_clean():
    leak_audit(SKILL.read_text(encoding="utf-8"))
    leak_audit(SCHEMA.read_text(encoding="utf-8"))


def test_schema_required_keys_and_optional_fields_omitted():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert s.get("additionalProperties") is False
    req = set(s["required"])
    assert req == {"tau", "monotonicity_pass", "endpoint_separation_pass",
                   "rigor_floor_flag", "pairwise_log"}
    props = set(s["properties"])
    # ponytail must-fix: STAGE-5 optional fields are NOT in the schema
    assert "calibration_handoff" not in props
    assert "confound_flat_pass" not in props
    assert s["properties"]["tau"]["type"] == "number"
    assert s["properties"]["tau"]["minimum"] == -1
    assert s["properties"]["tau"]["maximum"] == 1
    for b in ("monotonicity_pass", "endpoint_separation_pass", "rigor_floor_flag"):
        assert s["properties"][b]["type"] == "boolean"


def test_pairwise_log_item_shape():
    s = json.loads(SCHEMA.read_text(encoding="utf-8"))
    item = s["properties"]["pairwise_log"]["items"]
    assert set(item["required"]) == {"i", "j", "winner", "reason"}
    assert item["properties"]["reason"]["minLength"] == 1
    assert item["properties"]["winner"]["type"] == "integer"


def test_downstream_gate_alignment():
    # the two bools, lower-cased, must be the exact strings gate_eval topic accepts
    r = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic",
                        "--fidelity-rate", "0.95", "--mono", "true",
                        "--endpoint", "true"],
                       cwd=str(LF), capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip() == "true"
    r2 = subprocess.run([sys.executable, "scripts/gate_eval.py", "topic",
                         "--fidelity-rate", "0.95", "--mono", "false",
                         "--endpoint", "true"],
                        cwd=str(LF), capture_output=True, text=True)
    assert r2.returncode == 0 and r2.stdout.strip() == "false"


def test_d1_d5_only_no_academic_criteria():
    txt = SKILL.read_text(encoding="utf-8").lower()
    for forbidden in ("novelty", "baseline", "citation", "publishab", "peer review"):
        assert forbidden not in txt, forbidden
    assert "d1" in txt and "d5" in txt
