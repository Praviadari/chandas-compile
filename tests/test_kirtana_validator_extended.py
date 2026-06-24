from core.kirtana_validator import validate_kirtana_text


def test_kirtana_with_anupallavi() -> None:
    sample = """PALLAVI: రామ ప్రేమ.
ANUPALLAVI: రామ శాంతి.
CHARANAM: రామ సుఖం.
"""
    expected_patterns = {
        "PALLAVI": [[1, 0, 1, 0]],
        "ANUPALLAVI": [[1, 0, 1, 0]],
        "CHARANAM": [[1, 0, 0, 1]],
    }
    result = validate_kirtana_text(sample, expected_patterns)
    assert result["structure_valid"] is True
    assert result["fsm_state"] == "END"


def test_kirtana_invalid_order() -> None:
    sample = """CHARANAM: రామ సుఖం.
PALLAVI: రామ ప్రేమ.
"""
    expected_patterns = {
        "PALLAVI": [[1, 0, 1, 0]],
        "CHARANAM": [[1, 0, 0, 1]],
    }
    result = validate_kirtana_text(sample, expected_patterns)
    assert result["structure_valid"] is False
    assert len(result["invalid_transitions"]) > 0
