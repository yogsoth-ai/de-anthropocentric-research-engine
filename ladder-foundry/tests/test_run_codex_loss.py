import json
import subprocess
import sys
from pathlib import Path

LF = Path(__file__).resolve().parents[1]
SCRIPT = LF / "skills" / "optimization-loop" / "scripts" / "run_codex_loss.py"
sys.path.insert(0, str(SCRIPT.parent))


def test_script_and_schemas_exist():
    assert SCRIPT.exists()
    assert (SCRIPT.parent / "loss1.schema.json").exists()
    assert (SCRIPT.parent / "loss2.schema.json").exists()


def test_schemas_are_byte_identical_copies():
    import run_codex_loss  # noqa
    s1a = (SCRIPT.parent / "loss1.schema.json").read_bytes()
    s1b = (LF / "skills" / "injection-fidelity" / "loss1.schema.json").read_bytes()
    assert s1a == s1b
    s2a = (SCRIPT.parent / "loss2.schema.json").read_bytes()
    s2b = (LF / "skills" / "ladder-quality-order" / "loss2.schema.json").read_bytes()
    assert s2a == s2b


def test_validate_minimal_ok():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    good = {"fidelity": True, "loss1": 1.0, "drift_flag": False,
            "per_axis_evidence": {ax: {"observed": 0.9, "expected_band": "L4",
                                       "pass": True, "quote": "q"}
                                  for ax in ("A1", "A2", "A3", "A4", "A5")}}
    M.validate(good, schema)  # no raise


def test_validate_missing_key_raises():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    bad = {"fidelity": True}  # missing loss1/per_axis_evidence/drift_flag
    try:
        M.validate(bad, schema)
        assert False, "should have raised"
    except M.CodexOutputError:
        pass


def test_validate_wrong_type_raises():
    import run_codex_loss as M
    schema = json.loads((SCRIPT.parent / "loss1.schema.json").read_text(encoding="utf-8"))
    bad = {"fidelity": "yes", "loss1": 1.0, "drift_flag": False,
           "per_axis_evidence": {}}
    try:
        M.validate(bad, schema)
        assert False
    except M.CodexOutputError:
        pass


def test_shuffle_unshuffle_reversible():
    import run_codex_loss as M
    ids = ["id0", "id1", "id2", "id3", "id4", "id5"]
    perm = M.shuffle_perm(len(ids), seed=42)        # list pos -> original index
    shuffled = [ids[perm[p]] for p in range(len(ids))]
    back = M.unshuffle(list(range(len(ids))), perm)  # induced positions -> orig idx
    assert sorted(back) == list(range(len(ids)))
    assert {shuffled[p] for p in range(6)} == set(ids)


def test_kendall_tau_perfect_and_reversed():
    import run_codex_loss as M
    # induced order identical to intended -> tau == 1
    assert M.kendall_tau([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]) == 1.0
    # fully reversed -> tau == -1
    assert M.kendall_tau([0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]) == -1.0


def test_copeland_from_pairwise():
    import run_codex_loss as M
    # 0 beats everyone, 5 loses to everyone -> induced order 0..5
    pairs = []
    for i in range(6):
        for j in range(i + 1, 6):
            pairs.append({"i": i, "j": j, "winner": i})  # lower index always wins
    order = M.copeland_order(pairs, n=6)
    assert order == [0, 1, 2, 3, 4, 5]


def test_endpoint_vote_count():
    import run_codex_loss as M
    # w0 = number of times the true-high endpoint (mapped winner) wins
    judgments = [{"winner": 0}, {"winner": 0}, {"winner": 5},
                 {"winner": 0}, {"winner": 0}]
    w0 = M.count_endpoint_wins(judgments, high_pos=0)
    assert w0 == 4
    assert M.endpoint_pass(w0) is True       # 4 >= 5 - 1
    assert M.endpoint_pass(2) is False


def _fake_loss1(payload, schema_path):
    return json.dumps({
        "fidelity": True, "loss1": 1.0, "drift_flag": False,
        "per_axis_evidence": {ax: {"observed": 0.9, "expected_band": "L4",
                                   "pass": True, "quote": "q"}
                              for ax in ("A1", "A2", "A3", "A4", "A5")}})


def test_loss1_landing(tmp_path, monkeypatch):
    import run_codex_loss as M
    rd = tmp_path / "runs" / "r0"
    (rd / "configs").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    (rd / "transcripts").mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    (rd / "transcripts" / "s.md").write_text("### user\n\nhi\n", encoding="utf-8")
    out = rd / "loss" / "s.loss1.json"
    M.run_loss1(transcript=str(rd / "transcripts" / "s.md"),
                config=str(rd / "configs" / "s.json"),
                skill_md=str(LF / "skills" / "injection-fidelity" / "SKILL.md"),
                out=str(out), codex_fn=_fake_loss1)
    got = json.loads(out.read_text(encoding="utf-8"))
    assert got["fidelity"] is True and got["loss1"] == 1.0


def test_loss2_plumbing_lands_and_validates(tmp_path):
    # Structure-only: fake rank + endpoint codex_fns exercise the run_loss2
    # composition (A/B->position map, perm.index, copeland->unshuffle, perm.json
    # + loss2.json write + schema validate). Asserts NOTHING about the verdict
    # values (no gate outcome from canned output -> stays clear of the no-fake-
    # stub forbidden line); only that the artifact lands well-formed.
    import run_codex_loss as M
    rd = tmp_path / "runs" / "r0"
    (rd / "triples").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    triples = []
    for k in range(6):
        p = rd / "triples" / f"id{k}.json"
        p.write_text(json.dumps({"research_config": {}, "research_graph": {},
                                 "research_result": {"title": f"id{k}"}}),
                     encoding="utf-8")
        triples.append(str(p))

    def fake_codex(payload, schema_path):
        if "pairwise" in Path(schema_path).read_text(encoding="utf-8"):
            pairs = [{"i": i, "j": j, "winner": i}
                     for i in range(6) for j in range(i + 1, 6)]
            return json.dumps({"pairwise": pairs})
        return json.dumps({"winner": "A"})        # endpoint A/B label

    out = rd / "loss" / "topic00.loss2.json"
    M.run_loss2(triples=triples, intended_order="id0,id1,id2,id3,id4,id5",
                skill_md=str(LF / "skills" / "ladder-quality-order" / "SKILL.md"),
                out=str(out), seed=7, codex_fn=fake_codex)
    art = json.loads(out.read_text(encoding="utf-8"))
    schema = json.loads((SCRIPT.parent / "loss2.schema.json").read_text(encoding="utf-8"))
    M.validate(art, schema)                       # lands schema-valid
    assert set(art) >= {"tau", "monotonicity_pass", "endpoint_separation_pass",
                        "rigor_floor_flag", "pairwise_log"}
    assert (out.with_suffix(".perm.json")).exists()      # permutation recorded
    assert len(art["pairwise_log"]) == 15                # all i<j pairs, unshuffled


def test_bad_json_degrades_and_exits_2(tmp_path):
    # subprocess: a codex edge returning junk -> degrade-to-disk + exit 2
    rd = tmp_path / "runs" / "r0"
    (rd / "configs").mkdir(parents=True)
    (rd / "loss").mkdir(parents=True)
    (rd / "transcripts").mkdir(parents=True)
    (rd / "configs" / "s.json").write_text('{"rung_id": 0}', encoding="utf-8")
    (rd / "transcripts" / "s.md").write_text("### user\n\nhi\n", encoding="utf-8")
    out = rd / "loss" / "s.loss1.json"
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "loss1",
         "--transcript", str(rd / "transcripts" / "s.md"),
         "--config", str(rd / "configs" / "s.json"),
         "--skill-md", str(LF / "skills" / "injection-fidelity" / "SKILL.md"),
         "--out", str(out), "--_test-bad-json"],
        capture_output=True, text=True)
    assert r.returncode == 2
    got = json.loads(out.read_text(encoding="utf-8"))
    assert got["pass"] is False and "parse_error" in got
