from core.chandassu_validator import (
    get_meter_info,
    list_known_meters,
    suggest_meter_names,
    validate_line_meter,
    validate_meter_text,
)


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


def test_validate_kanda_padyam_sequence_order() -> None:
    text = "రామ సుఖం\nరామ ప్రేమ\n"
    result = validate_meter_text(text, "kanda_padyam")
    assert result["valid"] is False
    assert result["sequence_length_mismatch"] is False


def test_validate_line_meter_mismatch_details() -> None:
    result = validate_line_meter("రామ సుఖం", "utpalamala")
    assert result["valid"] is False
    assert result["difference_count"] >= 1
    assert "description" in result


def test_list_known_meters() -> None:
    meters = list_known_meters()
    assert any(item["meter_name"] == "utpalamala" for item in meters)


def test_get_meter_info() -> None:
    info = get_meter_info("champakamala")
    assert info["meter_name"] == "champakamala"
    assert "description" in info
    assert info["patterns"] == [[1, 0, 0, 1]]
