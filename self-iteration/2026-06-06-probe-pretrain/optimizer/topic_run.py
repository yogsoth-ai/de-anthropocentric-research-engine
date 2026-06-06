from tools.validate_pair import extract_blocks
from optimizer.gate import topic_passes


def run_topic_ladder(cards, topic_id, dialogue_fn, loss1_fn, loss2_fn,
                     emitter=None, batch_id=""):
    """跑一个 topic 的 n 档阶梯：forward 每档 → loss-1 每档 → loss-2 整条 → 判过闸。
    emitter 可选：埋 topic_start/rung_start/rung_done/topic_done 观测事件。"""
    if emitter:
        emitter.emit("topic_start", batch_id=batch_id, topic_id=topic_id,
                     intended_order=list(range(len(cards))))
    samples, fidelities = [], []
    for i, card in enumerate(cards):
        sid = f"{topic_id}-id{i}"
        if emitter:
            emitter.emit("rung_start", batch_id=batch_id, topic_id=topic_id,
                         rung_id=i, sample_id=sid, config_full=card,
                         axis_levels=card.get("axis_levels"))
        dr = _call_dialogue(dialogue_fn, card, topic_id, emitter, sid)
        graph, result = extract_blocks(dr.spec_text)
        f1 = loss1_fn(dr.transcript, card)
        ok = bool(f1["fidelity"]) and not f1.get("drift_flag", False)
        fidelities.append(ok)
        tpath = getattr(dr, "transcript_path", "")
        if emitter:
            emitter.emit("rung_done", batch_id=batch_id, topic_id=topic_id,
                         rung_id=i, sample_id=sid, fidelity=f1["fidelity"],
                         per_axis_evidence=f1.get("per_axis_evidence", {}),
                         drift_flag=f1.get("drift_flag", False),
                         transcript_path=tpath)
        samples.append({
            "sample_id": sid, "topic_id": topic_id, "rung_id": i,
            "research_config": card, "research_graph": graph,
            "research_result": result, "injection_fidelity": f1,
            "completability": dr.completability, "_transcript_path": tpath,
        })
    intended_order = list(range(len(cards)))
    f2 = loss2_fn([{"research_graph": s["research_graph"],
                    "research_result": s["research_result"]} for s in samples],
                  intended_order)
    fidelity_rate = sum(fidelities) / len(fidelities)
    tp = topic_passes(fidelity_rate, f2["monotonicity_pass"],
                      f2["endpoint_separation_pass"])
    for s in samples:
        s["gate_pass"] = tp
    if emitter:
        emitter.emit("topic_done", batch_id=batch_id, topic_id=topic_id,
                     tau=f2.get("tau"), monotonicity_pass=f2["monotonicity_pass"],
                     endpoint_separation_pass=f2["endpoint_separation_pass"],
                     rigor_floor_flag=f2.get("rigor_floor_flag", False),
                     topic_pass=tp, fidelity_rate=fidelity_rate)
    return {"samples": samples, "loss2": f2, "fidelity_rate": fidelity_rate,
            "topic_pass": tp, "rigor_floor_flag": f2.get("rigor_floor_flag", False)}


def _call_dialogue(dialogue_fn, card, topic_id, emitter, sid):
    """兼容两种签名：带/不带 emitter（旧 fake 不接受 emitter 关键字）。"""
    try:
        return dialogue_fn(card, topic_id, emitter=emitter, sample_id=sid)
    except TypeError:
        return dialogue_fn(card, topic_id)
