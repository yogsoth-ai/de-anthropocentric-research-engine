from classify_layers import classify_node, LAYERS

# Minimal hand-built inputs exercising each signal source.
TYP = {"strat-a": "strategy", "notype-leaf": None, "camp-a": "campaign"}
DESC = {"camp-by-desc": "Foo Campaign — 5 strategies for bar.",
        "tac-by-desc": "A tactic that does X."}
ROLE = {"tac-x": {"tactic"}, "sop-y": {"sop"}, "strat-b": {"strategy"}}
PHASE = {"notype-leaf": "convergence", "camp-by-desc": "convergence",
         "tac-by-desc": "convergence", "tac-x": "convergence",
         "sop-y": "convergence", "strat-b": "convergence", "lonely": None}
OVERRIDES = {"de-anthropocentric-research-engine": "meta",
             "research-catalog": "reference", "writing-specs": "sop"}

def test_declared_type_wins():
    assert classify_node("strat-a", TYP, DESC, ROLE, PHASE, OVERRIDES)[0] == "strategy"

def test_override_beats_everything():
    # declared/desc absent, but override pins it
    assert classify_node("de-anthropocentric-research-engine", {}, {}, {}, {}, OVERRIDES) == ("meta", "override")
    assert classify_node("research-catalog", {}, {}, {}, {}, OVERRIDES)[0] == "reference"

def test_index_description_keyword():
    assert classify_node("camp-by-desc", TYP, DESC, ROLE, PHASE, OVERRIDES)[0] == "campaign"
    assert classify_node("tac-by-desc", TYP, DESC, ROLE, PHASE, OVERRIDES)[0] == "tactic"

def test_graph_role_when_no_type_or_desc():
    assert classify_node("tac-x", TYP, DESC, ROLE, PHASE, OVERRIDES)[0] == "tactic"
    assert classify_node("sop-y", TYP, DESC, ROLE, PHASE, OVERRIDES)[0] == "sop"

def test_leaf_default_sop_when_has_phase():
    # no type, no desc keyword, no graph role, but has a phase => leaf SOP
    assert classify_node("notype-leaf", TYP, DESC, ROLE, PHASE, OVERRIDES) == ("sop", "leaf-default")

def test_unresolved_when_nothing_known():
    assert classify_node("lonely", TYP, DESC, ROLE, PHASE, OVERRIDES) == (None, "unresolved")

def test_layers_constant_has_five_levels():
    assert LAYERS == ["campaign", "strategy", "tactic", "sop"]
