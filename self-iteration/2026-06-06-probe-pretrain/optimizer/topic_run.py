from tools.validate_pair import extract_blocks
from optimizer.gate import topic_passes


def run_topic_ladder(cards, topic_id, dialogue_fn, loss1_fn, loss2_fn):
    """跑一个 topic 的 n 档阶梯：forward 每档 → loss-1 每档 → loss-2 整条 → 判过闸。"""
    samples, fidelities = [], []
    for i, card in enumerate(cards):
        dr = dialogue_fn(card, topic_id)
        graph, result = extract_blocks(dr.spec_text)
        f1 = loss1_fn(dr.transcript, card)
        fidelities.append(bool(f1["fidelity"]) and not f1.get("drift_flag", False))
        samples.append({
            "sample_id": f"{topic_id}-id{i}", "topic_id": topic_id, "rung_id": i,
            "research_config": card, "research_graph": graph, "research_result": result,
            "injection_fidelity": f1, "completability": dr.completability,
        })
    intended_order = list(range(len(cards)))
    f2 = loss2_fn([{"research_graph": s["research_graph"],
                    "research_result": s["research_result"]} for s in samples], intended_order)
    fidelity_rate = sum(fidelities) / len(fidelities)
    tp = topic_passes(fidelity_rate, f2["monotonicity_pass"], f2["endpoint_separation_pass"])
    for s in samples:
        s["gate_pass"] = tp
    return {"samples": samples, "loss2": f2, "fidelity_rate": fidelity_rate,
            "topic_pass": tp, "rigor_floor_flag": f2.get("rigor_floor_flag", False)}
