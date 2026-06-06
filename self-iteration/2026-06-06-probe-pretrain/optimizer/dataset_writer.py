import json
import jsonschema
from pathlib import Path

SCHEMA = json.loads(
    (Path(__file__).parent.parent / "schemas" / "provenance.schema.json").read_text(encoding="utf-8")
)
_ALLOWED = set(SCHEMA["properties"].keys())


def write_sample(out_path, sample: dict):
    """落盘一条样本。隐私红线：剥掉任何不在 schema allow-list 的字段
    （含 logs_dir / 任何路径），再 schema 校验，再 append。"""
    clean = {k: v for k, v in sample.items() if k in _ALLOWED}
    jsonschema.validate(clean, SCHEMA)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(clean, ensure_ascii=False) + "\n")
