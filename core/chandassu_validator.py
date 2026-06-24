"""Chandassu-specific meter validators for classical Telugu metres."""

from __future__ import annotations

from core.meter_validator import analyze_text

KNOWN_PATTERNS: dict[str, list[list[int]]] = {
    "utpalamala": [[1, 0, 1, 0]],
    "champakamala": [[1, 0, 0, 1]],
    "kanda_padyam": [[1, 0, 1, 0], [1, 0, 0, 1]],
}


def get_known_meter_names() -> list[str]:
    return sorted(KNOWN_PATTERNS)


def get_meter_patterns(meter_name: str) -> list[list[int]]:
    return KNOWN_PATTERNS[meter_name.lower()]


def validate_line_meter(text: str, meter_name: str) -> dict[str, object]:
    """Validate a single line against a named Chandassu meter pattern."""
    meter = meter_name.lower()
    patterns = get_meter_patterns(meter)
    actual = analyze_text(text)
    valid = actual in patterns
    return {
        "meter_name": meter,
        "text": text,
        "actual_pattern": actual,
        "valid": valid,
        "expected_patterns": patterns,
    }


def suggest_meter_names(text: str) -> list[str]:
    """Return all known meter names that match the given text."""
    actual = analyze_text(text)
    return [name for name, patterns in KNOWN_PATTERNS.items() if actual in patterns]


def validate_meter_text(text: str, meter_name: str) -> dict[str, object]:
    """Validate a multi-line text against a named meter scheme."""
    results = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        results.append(validate_line_meter(stripped, meter_name))
    valid = all(item["valid"] for item in results)
    return {
        "meter_name": meter_name.lower(),
        "valid": valid,
        "line_results": results,
    }
