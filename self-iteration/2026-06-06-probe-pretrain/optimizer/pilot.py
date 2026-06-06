def pilot_verdict(loss2, idN_completability):
    """PT5 go/no-go：id0 实质甩开 idN-1（端点分离）且 idN-1 产出可评判但差的文档。
    rigor_floor_flag 或 idN-1 不可评判 → NO-GO（RR-1 杀手风险，停、报用户）。"""
    if loss2.get("rigor_floor_flag"):
        return "NO-GO"
    if idN_completability != "ok":
        return "NO-GO"
    return "GO" if loss2.get("endpoint_separation_pass") else "NO-GO"
