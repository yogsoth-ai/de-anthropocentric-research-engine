import json
import jsonschema
from pathlib import Path

SCHEMA = json.loads(
    (Path(__file__).parent.parent / "schemas" / "provenance.schema.json").read_text(encoding="utf-8")
)
_ALLOWED = set(SCHEMA["properties"].keys())


def write_sample(out_path, sample: dict):
    """Persist one sample. Privacy red line: strip any field not in the schema allow-list
    (incl. logs_dir / any path), then schema-validate, then append."""
    clean = {k: v for k, v in sample.items() if k in _ALLOWED}
    jsonschema.validate(clean, SCHEMA)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(clean, ensure_ascii=False) + "\n")
