import json
import subprocess


def _default_codex(skill: str, payload: dict) -> str:
    """Real impl: spawn a codex session, load the given skill, feed payload, read back JSON.
    (The --task entry and actual codex args are aligned on-device in the PT phase; this is the skeleton.)"""
    proc = subprocess.run(
        ["codex", "exec", "--skill", skill],
        input=json.dumps(payload, ensure_ascii=False),
        capture_output=True, text=True, timeout=600,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"codex {skill} failed: {proc.stderr[:500]}")
    return proc.stdout.strip()


def parse_loss1(raw: str) -> dict:
    return json.loads(raw)


def parse_loss2(raw: str) -> dict:
    return json.loads(raw)


def run_loss1(transcript, card, codex_fn=_default_codex):
    raw = codex_fn("injection-fidelity", {"transcript": transcript, "card": card})
    return parse_loss1(raw)


def run_loss2(topic_samples, intended_order, codex_fn=_default_codex):
    raw = codex_fn("ladder-quality-order",
                   {"samples": topic_samples, "intended_order": intended_order})
    return parse_loss2(raw)
