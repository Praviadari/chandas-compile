"""Laghu/Guru rule engine for Telugu script."""

from __future__ import annotations

SHORT_VOWELS = {"అ", "ఇ", "ఉ", "ఋ", "ఎ", "ఒ"}
LONG_VOWELS = {"ఆ", "ఈ", "ఊ", "ౠ", "ఏ", "ఓ", "ఐ", "ఔ"}

SHORT_MATRAS = {"ి", "ు", "ృ", "ె", "ొ"}
LONG_MATRAS = {"ా", "ీ", "ూ", "ౄ", "ే", "ో", "ై", "ౌ"}

ANUSVARA = "ం"
VISARGA = "ః"
VIRAMA = "్"
YATI_MARKS = {"|", "॥", "।"}


def analyze_syllable(char: str, next_is_conjunct: bool = False) -> int:
    """Return 0 for Laghu and 1 for Guru for a Telugu akshara-like unit."""
    if not char:
        return 0

    # Full vowel letter or long vowel sign implies a Guru.
    if char in LONG_VOWELS or any(mark in char for mark in LONG_MATRAS):
        return 1

    # Consonant clusters and halant-bound units are heavy.
    if next_is_conjunct or char.endswith(VIRAMA):
        return 1

    # Anusvara/visarga make the syllable Guru.
    if ANUSVARA in char or VISARGA in char:
        return 1

    # Yati marks often increase weight or reset meter context.
    if any(mark in char for mark in YATI_MARKS):
        return 1

    # Short vowels and short matras are Laghu.
    if char in SHORT_VOWELS or any(mark in char for mark in SHORT_MATRAS):
        return 0

    # Consonant-only units are treated as Laghu by default.
    return 0


def encode_text(units: list[str]) -> list[int]:
    """Encode a list of Telugu orthographic units into Laghu/Guru bits."""
    bits: list[int] = []
    for idx, unit in enumerate(units):
        next_is_conjunct = False
        if idx + 1 < len(units):
            next_is_conjunct = units[idx + 1].startswith(VIRAMA)
        bits.append(analyze_syllable(unit, next_is_conjunct=next_is_conjunct))
    return bits


def analyze_syllable_with_trace(char: str, next_is_conjunct: bool = False) -> tuple[int, list[str]]:
    """Analyze a Telugu akshara and also return a reasoning trace."""
    reasons: list[str] = []
    result = analyze_syllable(char, next_is_conjunct=next_is_conjunct)

    if not char:
        reasons.append("Empty input produces Laghu by default.")
        return result, reasons

    if char in LONG_VOWELS or any(mark in char for mark in LONG_MATRAS):
        reasons.append("Long vowel or long matra detected -> Guru.")

    if next_is_conjunct:
        reasons.append("Next unit starts with virama, indicating a conjunct cluster -> Guru.")

    if ANUSVARA in char or VISARGA in char:
        reasons.append("Anusvara or visarga present -> Guru.")

    if char.endswith(VIRAMA):
        reasons.append("Ends with halant/virama -> Guru (closed/clipped syllable). ")

    if any(mark in char for mark in YATI_MARKS):
        reasons.append("Yati or punctuation marker present -> Guru-like extra weight.")

    if char in SHORT_VOWELS or any(mark in char for mark in SHORT_MATRAS):
        if result == 0:
            reasons.append("Short vowel or short matra detected -> Laghu.")

    if result == 0 and not reasons:
        reasons.append("Consonant-only or default short form -> Laghu.")

    if result == 1 and not reasons:
        reasons.append("Default weight rules cause Guru.")

    return result, reasons


def analyze_text_with_trace(text: str) -> list[dict[str, object]]:
    """Return traceable Laghu/Guru analysis for each Telugu akshara unit in a text."""
    from core.tokenizer import split_aksharas

    units = split_aksharas(text)
    traced: list[dict[str, object]] = []
    for idx, unit in enumerate(units):
        next_is_conjunct = idx + 1 < len(units) and units[idx + 1].startswith(VIRAMA)
        value, reasons = analyze_syllable_with_trace(unit, next_is_conjunct=next_is_conjunct)
        yati = any(mark in unit for mark in YATI_MARKS)

        entry = {
            "unit": unit,
            "value": value,
            "yati": yati,
            "reasons": reasons,
        }

        traced.append(entry)

        if yati and idx > 0:
            traced[idx - 1]["yati"] = True
            traced[idx - 1]["reasons"].append("Adjacent yati marker affects the previous syllable.")

    return traced


def validate_pattern_with_trace(text: str, expected_pattern: list[int]) -> dict[str, object]:
    """Validate a text line against expected pattern and include trace details."""
    from core.tokenizer import split_aksharas

    units = split_aksharas(text)
    actual_pattern = encode_text(units)
    trace = analyze_text_with_trace(text)
    valid = actual_pattern == expected_pattern
    return {
        "text": text,
        "units": units,
        "actual_pattern": actual_pattern,
        "expected_pattern": expected_pattern,
        "valid": valid,
        "trace": trace,
    }
