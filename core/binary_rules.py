"""Laghu/Guru rule engine for Telugu script."""

from __future__ import annotations

SHORT_VOWELS = {"అ", "ఇ", "ఉ", "ఋ", "ఎ", "ఒ"}
LONG_VOWELS = {"ఆ", "ఈ", "ఊ", "ౠ", "ఏ", "ఓ", "ఐ", "ఔ"}

SHORT_MATRAS = {"ి", "ు", "ృ", "ె", "ొ"}
LONG_MATRAS = {"ా", "ీ", "ూ", "ౄ", "ే", "ో", "ై", "ౌ"}

ANUSVARA = "ం"
VISARGA = "ః"
VIRAMA = "్"


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
