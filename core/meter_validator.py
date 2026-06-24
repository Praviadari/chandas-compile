"""Meter validation helpers for Telugu Laghu/Guru sequences."""

from __future__ import annotations

from core.binary_rules import encode_text
from core.tokenizer import split_aksharas


def analyze_text(text: str) -> list[int]:
    """Convert a Telugu text string into a Laghu/Guru integer sequence."""
    units = split_aksharas(text)
    return encode_text(units)


def format_bits(bits: list[int]) -> str:
    """Format a binary sequence as a readable string."""
    return ",".join(str(bit) for bit in bits)


def validate_pattern(text: str, expected_pattern: list[int]) -> dict[str, object]:
    """Validate a text sequence against an expected Laghu/Guru pattern."""
    actual_pattern = analyze_text(text)
    is_valid = actual_pattern == expected_pattern
    mismatch_index = -1
    if not is_valid:
        for index, (actual, expected) in enumerate(zip(actual_pattern, expected_pattern)):
            if actual != expected:
                mismatch_index = index
                break
        if mismatch_index == -1 and len(actual_pattern) != len(expected_pattern):
            mismatch_index = min(len(actual_pattern), len(expected_pattern))

    return {
        "text": text,
        "units": split_aksharas(text),
        "actual_pattern": actual_pattern,
        "expected_pattern": expected_pattern,
        "valid": is_valid,
        "mismatch_index": mismatch_index,
    }
