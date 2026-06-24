from core.binary_rules import analyze_syllable_with_trace, analyze_text_with_trace, validate_pattern_with_trace
from core.tokenizer import split_aksharas


def test_analyze_syllable_with_trace_long_vowel() -> None:
    value, reasons = analyze_syllable_with_trace("రా")
    assert value == 1
    assert any("Guru" in reason for reason in reasons)


def test_analyze_text_with_trace() -> None:
    trace = analyze_text_with_trace("రామ")
    assert len(trace) == 2
    assert trace[0]["unit"] == "రా"
    assert trace[1]["unit"] == "మ"


def test_validate_pattern_with_trace() -> None:
    result = validate_pattern_with_trace("రామ", [1, 0])
    assert result["valid"] is True
    assert "trace" in result


def test_split_aksharas_conjunct() -> None:
    units = split_aksharas("కశ్చిత్")
    assert len(units) >= 3
    assert any("్" in unit for unit in units)
