import json
import jsonschema
from optimizer.dataset_writer import write_sample, SCHEMA


def test_written_sample_validates_and_has_no_log_path(tmp_path):
    out = tmp_path / "train.jsonl"
    sample = {
        "sample_id": "batch0-topic01-id0", "batch_id": "batch0", "topic_id": "topic-01",
        "rung_id": 0, "research_config": {"label": "id0"},
        "label": {"A1": "L0", "A2": "L0", "A3": "L0", "A4": "C0", "A5": "G+", "B1": "F-neu", "ladder_composite": 0},
        "research_graph": {"nodes": [], "edges": []}, "research_result": {"document": "d"},
        "behavior_trace": {}, "injection_fidelity": {"fidelity": True, "per_axis_evidence": {}, "drift_flag": False},
        "completability": "ok", "gate_pass": True, "split": "train",
        "logs_dir": "/home/u/.claude/projects/secret",  # must be stripped
    }
    write_sample(out, sample)
    line = json.loads(out.read_text(encoding="utf-8").splitlines()[0])
    assert "logs_dir" not in line  # privacy red line
    jsonschema.validate(line, SCHEMA)
