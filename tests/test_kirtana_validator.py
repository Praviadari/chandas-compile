from core.kirtana_validator import validate_kirtana_text


def test_validate_kirtana_text_valid() -> None:
    sample = """PALLAVI: రామ ప్రేమ.
CHARANAM: రామ సుఖం.
"""
    expected_patterns = {
        "PALLAVI": [[1, 0]],
        "CHARANAM": [[1, 0]],
    }
    result = validate_kirtana_text(sample, expected_patterns)
    assert result["structure_valid"] is True
    assert result["fsm_state"] == "END"
    assert result["sections"][0].valid is True


def test_validate_kirtana_text_invalid_structure() -> None:
    sample = """CHARANAM: రామ సుఖం.
PALLAVI: రామ ప్రేమ.
"""
    expected_patterns = {
        "PALLAVI": [[1, 0]],
        "CHARANAM": [[1, 0]],
    }
    result = validate_kirtana_text(sample, expected_patterns)
    assert result["structure_valid"] is False
    assert result["fsm_state"] == "CHARANAM"
