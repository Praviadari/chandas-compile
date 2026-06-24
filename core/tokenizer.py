"""Very small tokenizer to split Telugu text into akshara-like units.

This module keeps dependent vowel signs, anusvara/visarga, and conjunct clusters
attached to the correct base consonant unit.
"""

from __future__ import annotations

VIRAMA = "్"
ZWJ = "\u200D"
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


def split_aksharas(text: str) -> list[str]:
    """Split Telugu text into rough akshara units.

    The tokenizer collects a base character and attaches subsequent dependent marks
    or consonant joiners until a natural break is reached.
    """
    units: list[str] = []
    current = ""

    for ch in text.strip():
        if ch.isspace():
            if current:
                units.append(current)
                current = ""
            continue

        if not current:
            current = ch
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
