FIDELITY_BATCH_MIN = 0.90
TOPIC_PASS_RATIO_MIN = 0.80
CONVERGE_CONSECUTIVE = 3


def topic_passes(fidelity_rate, monotonicity_pass, endpoint_separation_pass):
    """某 topic 过闸 = 保真≥90% ∧ 单调 ∧ 端点分离（§4.3）。"""
    return (fidelity_rate >= FIDELITY_BATCH_MIN
            and monotonicity_pass and endpoint_separation_pass)


def batch_pass_ratio(topic_pass_flags):
    """一个 batch 内过闸 topic 占比。"""
    return sum(1 for x in topic_pass_flags if x) / len(topic_pass_flags)


def converged(recent_ratios):
    """连续 3 个 batch、每个 ≥0.8 → 收敛（§9）。无迭代上限。"""
    if len(recent_ratios) < CONVERGE_CONSECUTIVE:
        return False
    last = recent_ratios[-CONVERGE_CONSECUTIVE:]
    return all(r >= TOPIC_PASS_RATIO_MIN for r in last)
