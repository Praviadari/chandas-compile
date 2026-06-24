from core.meter_validator import validate_pattern


def test_validate_pattern_exact_match() -> None:
    result = validate_pattern("రామ", [1, 0])
    assert result["valid"] is True
    assert result["mismatch_index"] == -1


def test_validate_pattern_mismatch() -> None:
    result = validate_pattern("రామ", [0, 0])
    assert result["valid"] is False
    assert result["mismatch_index"] == 0
