import json
from generator.cards import PolicyCard, to_dict


def _card():
    return PolicyCard(
        F0="research supervisor", F1="topic", F2="persona", F3="pressure",
        F4="stance", F5="corrigibility", F6="acceptance", F7="controversy",
        F8="turn budget", F9="closing",
        axis_levels={"A1": "L0", "A2": "L0", "A3": "L0", "A4": "L0", "A5": "L0"},
    )


def test_to_dict_has_f0_f9():
    d = to_dict(_card())
    assert [f"F{i}" for i in range(10)] == [k for k in d if k.startswith("F")]
    assert d["axis_levels"]["A1"] == "L0"


def test_to_dict_is_json_serializable():
    json.dumps(to_dict(_card()))   # raises if not serializable
