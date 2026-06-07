import json
import jsonschema
from pathlib import Path

SCHEMA_DIR = Path(__file__).parent.parent / "schemas"


def _load(name):
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def test_provenance_sample_validates():
    schema = _load("provenance.schema.json")
    sample = {
        "sample_id": "batch3-topic05-id2", "batch_id": "batch3",
        "topic_id": "topic-05", "rung_id": 2,
        "research_config": {"label": "id2"},
        "label": {"A1": "L2", "A2": "L2", "A3": "L2", "A4": "C0", "A5": "G0",
                  "B1": "F-neu", "ladder_composite": 2},
        "research_graph": {"nodes": [], "edges": []},
        "research_result": {"document": "..."},
        "behavior_trace": {"pushback_count": 3},
        "injection_fidelity": {"fidelity": True, "per_axis_evidence": {}, "drift_flag": False},
        "completability": "ok", "gate_pass": True, "split": "train",
    }
    jsonschema.validate(sample, schema)  # raises if invalid


def test_provenance_rejects_log_path_field():
    schema = _load("provenance.schema.json")
    bad = {"sample_id": "x", "logs_dir": "/home/user/.claude/projects/secret"}
    import pytest
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, schema)
