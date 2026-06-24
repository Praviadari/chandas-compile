from core.binary_rules import analyze_syllable_with_trace, analyze_text_with_trace


def test_yati_mark_increases_weight() -> None:
    value, reasons = analyze_syllable_with_trace("రా|")
    assert value == 1
    assert any("Yati" in reason for reason in reasons)


def test_analyze_text_with_trace_yati_flag() -> None:
    trace = analyze_text_with_trace("రా| మ")
    assert trace[0]["yati"] is True
