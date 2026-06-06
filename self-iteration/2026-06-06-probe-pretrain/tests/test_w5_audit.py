from tools.w5_audit import audit_revision_log


def test_clean_log_passes():
    log = [{"target": "axis_prose", "reason": "loss-1 低: A1=L4 未演出"}]
    assert audit_revision_log(log)["clean"] is True


def test_check_reference_fails():
    log = [{"target": "interp_params", "reason": "R13 check fired so loosen"}]
    r = audit_revision_log(log)
    assert r["clean"] is False and r["violations"]
