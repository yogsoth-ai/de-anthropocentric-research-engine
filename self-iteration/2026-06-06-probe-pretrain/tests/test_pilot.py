from optimizer.pilot import pilot_verdict


def test_go_when_endpoints_separate():
    loss2 = {"endpoint_separation_pass": True, "rigor_floor_flag": False}
    assert pilot_verdict(loss2, idN_completability="ok") == "GO"


def test_nogo_when_rigor_floor():
    loss2 = {"endpoint_separation_pass": False, "rigor_floor_flag": True}
    assert pilot_verdict(loss2, idN_completability="ok") == "NO-GO"


def test_nogo_when_idN_not_completable():
    loss2 = {"endpoint_separation_pass": True, "rigor_floor_flag": False}
    assert pilot_verdict(loss2, idN_completability="failed") == "NO-GO"
