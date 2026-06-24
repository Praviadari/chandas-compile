"""Very small tokenizer to split Telugu text into akshara-like units.

This module keeps dependent vowel signs, anusvara/visarga, and conjunct clusters
attached to the correct base consonant unit.
"""

from __future__ import annotations

VIRAMA = "్"
ZWJ = "\u200D"
TELUGU_START = 0x0C00
TELUGU_END = 0x0C7F
DEPENDENT_MARKS = {
    "ా",
    "ి",
    "ీ",
    "ు",
    "ూ",
    "ృ",
    "ౄ",
    "ె",
    "ే",
    "ై",
    "ొ",
    "ో",
    "ౌ",
    "ం",
    "ః",
}
YATI_MARKS = {"|", "॥", "।"}


def is_telugu_char(ch: str) -> bool:
    code = ord(ch)
    return (
        TELUGU_START <= code <= TELUGU_END
        or ch in DEPENDENT_MARKS
        or ch in YATI_MARKS
        or ch in {VIRAMA, ZWJ}
    )


def split_aksharas(text: str) -> list[str]:
    """Split Telugu text into rough akshara units.

    Non-Telugu punctuation and symbols are ignored when forming akshara units.
    """
    units: list[str] = []
    current = ""

    for ch in text.strip():
        if not is_telugu_char(ch):
            if current:
                units.append(current)
                current = ""
            continue

        if not current:
            current = ch
            continue

        if ch in YATI_MARKS:
            if current:
                units.append(current)
            units.append(ch)
            current = ""
            continue

        # Attach vowel signs and dependent marks to the current akshara.
        if ch in DEPENDENT_MARKS:
            current += ch
            continue

        # Attach zero-width joiner after a virama into the same cluster.
        if current.endswith(VIRAMA) or current.endswith(ZWJ):
            current += ch
            continue

        # If incoming char is virama or ZWJ, keep it in the current cluster.
        if ch == VIRAMA or ch == ZWJ:
            current += ch
            continue

        units.append(current)
        current = ch

    if current:
        units.append(current)

    return units
