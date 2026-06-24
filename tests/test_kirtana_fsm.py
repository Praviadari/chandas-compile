from core.kirtana_fsm import KirtanaFSM


def test_valid_pallavi_charanam_end_sequence() -> None:
    fsm = KirtanaFSM()
    assert fsm.transition("CHARANAM")
    assert fsm.transition("CHARANAM")
    assert fsm.transition("END")
    assert fsm.state == "END"


def test_invalid_transition_from_end() -> None:
    fsm = KirtanaFSM()
    assert fsm.transition("CHARANAM")
    assert fsm.transition("END")
    assert not fsm.transition("PALLAVI")


def test_validate_sequence_helper() -> None:
    fsm = KirtanaFSM()
    assert fsm.validate_sequence(["PALLAVI", "CHARANAM", "CHARANAM", "END"])
    assert not fsm.validate_sequence(["PALLAVI", "END", "CHARANAM"])
