def pilot_verdict(loss2, idN_completability):
    """PT5 go/no-go: id0 substantively beats idN-1 (endpoint separation) and idN-1 yields a judgeable-but-poor doc.
    rigor_floor_flag or idN-1 not judgeable -> NO-GO (RR-1 killer risk; stop and report to user)."""
    if loss2.get("rigor_floor_flag"):
        return "NO-GO"
    if idN_completability != "ok":
        return "NO-GO"
    return "GO" if loss2.get("endpoint_separation_pass") else "NO-GO"
