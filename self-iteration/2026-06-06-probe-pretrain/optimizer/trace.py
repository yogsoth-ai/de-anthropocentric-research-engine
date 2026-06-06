import json
from pathlib import Path


class TraceEmitter:
    """Real-time observability stream. Each emit appends a jsonl line; full transcript saved separately as .md.
    Device-local, gitignored, never committed. Privacy red line: relative paths only."""

    def __init__(self, run_id, run_dir, clock=None):
        self.run_id = run_id
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / "transcripts").mkdir(exist_ok=True)
        self._trace = self.run_dir / "trace.jsonl"
        self._seq = 0
        # clock injectable (script env forbids argless Date); defaults to datetime
        self._clock = clock or self._default_clock

    @staticmethod
    def _default_clock():
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()

    def emit(self, event, **fields):
        rec = {"ts": self._clock(), "run_id": self.run_id, "event": event,
               "seq": self._seq}
        rec.update(fields)
        with open(self._trace, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self._seq += 1
        return rec

    def save_transcript(self, sample_id, text):
        """Save the full transcript; return a relative path (never absolute / never containing a log path)."""
        rel = f"transcripts/{sample_id}.md"
        (self.run_dir / rel).write_text(text, encoding="utf-8")
        return rel
