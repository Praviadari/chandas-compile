from core.chandassu_validator import suggest_meter_names, validate_line_meter, validate_meter_text


def test_validate_line_meter() -> None:
    result = validate_line_meter("రామ ప్రేమ", "utpalamala")
    assert result["valid"] is True
    assert result["meter_name"] == "utpalamala"


def test_suggest_meter_names() -> None:
    suggestions = suggest_meter_names("రామ ప్రేమ")
    assert "utpalamala" in suggestions


def test_validate_meter_text() -> None:
    text = "రామ ప్రేమ\nరామ సుఖం\n"
    result = validate_meter_text(text, "kanda_padyam")
    assert result["valid"] is True
    assert len(result["line_results"]) == 2
