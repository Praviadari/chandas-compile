"""Chandassu-specific meter validators for classical Telugu metres."""

from __future__ import annotations

from core.meter_validator import analyze_text

KNOWN_PATTERNS: dict[str, list[list[int]]] = {
    "utpalamala": [[1, 0, 1, 0]],
    "champakamala": [[1, 0, 0, 1]],
    "kanda_padyam": [[1, 0, 1, 0], [1, 0, 0, 1]],
}

KNOWN_SEQUENCE_PATTERNS: dict[str, list[list[int]]] = {
    "kanda_padyam": [[1, 0, 1, 0], [1, 0, 0, 1]],
}

METER_DESCRIPTIONS: dict[str, str] = {
    "utpalamala": "Four-syllable pattern with alternating Guru-Laghu weights.",
    "champakamala": "Four-syllable pattern with a trailing Guru weight.",
    "kanda_padyam": "Two-line sequence with Utpalamala followed by Champakamala.",
}


def get_known_meter_names() -> list[str]:
    return sorted(KNOWN_PATTERNS)


def get_meter_patterns(meter_name: str) -> list[list[int]]:
    return KNOWN_PATTERNS[meter_name.lower()]


def get_meter_info(meter_name: str) -> dict[str, object]:
    meter = meter_name.lower()
    info = {
        "meter_name": meter,
        "description": METER_DESCRIPTIONS.get(meter, ""),
        "patterns": get_meter_patterns(meter),
    }
    if meter in KNOWN_SEQUENCE_PATTERNS:
        info["sequence_patterns"] = KNOWN_SEQUENCE_PATTERNS[meter]
    return info


def list_known_meters() -> list[dict[str, object]]:
    return [
        {
            "meter_name": name,
            "description": METER_DESCRIPTIONS.get(name, ""),
        }
        for name in get_known_meter_names()
    ]


def _match_pattern(actual: list[int], expected: list[int]) -> dict[str, object]:
    """Compare actual and expected patterns and report mismatches."""
    length_mismatch = len(actual) != len(expected)
    mismatch_index = -1
    diff_count = 0

    for index, (a, e) in enumerate(zip(actual, expected)):
        if a != e:
            diff_count += 1
            if mismatch_index == -1:
                mismatch_index = index

    if length_mismatch and mismatch_index == -1:
        mismatch_index = min(len(actual), len(expected))

    return {
        "valid": actual == expected,
        "difference_count": diff_count,
        "mismatch_index": mismatch_index,
        "length_mismatch": length_mismatch,
    }


def validate_line_meter(text: str, meter_name: str) -> dict[str, object]:
    """Validate a single line against a named Chandassu meter pattern."""
    meter = meter_name.lower()
    patterns = get_meter_patterns(meter)
    actual = analyze_text(text)
    best_result = None

    for pattern in patterns:
        result = _match_pattern(actual, pattern)
        if result["valid"]:
            best_result = result
            break
        if best_result is None or result["difference_count"] < best_result["difference_count"]:
            best_result = result

    return {
        "meter_name": meter,
        "text": text,
        "actual_pattern": actual,
        "valid": best_result["valid"],
        "expected_patterns": patterns,
        "difference_count": best_result["difference_count"],
        "mismatch_index": best_result["mismatch_index"],
        "length_mismatch": best_result["length_mismatch"],
        "description": METER_DESCRIPTIONS.get(meter, ""),
    }


def suggest_meter_names(text: str) -> list[str]:
    """Return known meter names sorted by proximity to the text pattern."""
    actual = analyze_text(text)
    candidates: list[tuple[int, str]] = []
    for name, patterns in KNOWN_PATTERNS.items():
        best_diff = min(
            _match_pattern(actual, pattern)["difference_count"] for pattern in patterns
        )
        candidates.append((best_diff, name))
    candidates.sort()
    return [name for _diff, name in candidates]


def validate_meter_text(text: str, meter_name: str) -> dict[str, object]:
    """Validate a multi-line text against a named meter scheme."""
    meter = meter_name.lower()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if meter in KNOWN_SEQUENCE_PATTERNS:
        expected_sequence = KNOWN_SEQUENCE_PATTERNS[meter]
        results = []
        valid = len(lines) == len(expected_sequence)

        for index, expected_pattern in enumerate(expected_sequence):
            if index < len(lines):
                line = lines[index]
                actual = analyze_text(line)
                match = _match_pattern(actual, expected_pattern)
                results.append(
                    {
                        "meter_name": meter,
                        "text": line,
                        "actual_pattern": actual,
                        "valid": match["valid"],
                        "expected_pattern": expected_pattern,
                        "difference_count": match["difference_count"],
                        "mismatch_index": match["mismatch_index"],
                        "length_mismatch": match["length_mismatch"],
                        "description": METER_DESCRIPTIONS.get(meter, ""),
                    }
                )
            else:
                results.append(
                    {
                        "meter_name": meter,
                        "text": "",
                        "actual_pattern": [],
                        "valid": False,
                        "expected_pattern": expected_pattern,
                        "difference_count": len(expected_pattern),
                        "mismatch_index": 0,
                        "length_mismatch": True,
                        "description": METER_DESCRIPTIONS.get(meter, ""),
                    }
                )

        if len(lines) > len(expected_sequence):
            extra_lines = lines[len(expected_sequence):]
            for extra in extra_lines:
                results.append(
                    {
                        "meter_name": meter,
                        "text": extra,
                        "actual_pattern": analyze_text(extra),
                        "valid": False,
                        "expected_pattern": [],
                        "difference_count": len(analyze_text(extra)),
                        "mismatch_index": 0,
                        "length_mismatch": True,
                        "description": METER_DESCRIPTIONS.get(meter, ""),
                    }
                )
            valid = False

        return {
            "meter_name": meter,
            "valid": valid and all(item["valid"] for item in results),
            "line_results": results,
            "expected_sequence": expected_sequence,
            "sequence_length_mismatch": len(lines) != len(expected_sequence),
        }

    results = []
    for line in lines:
        results.append(validate_line_meter(line, meter_name))
    valid = all(item["valid"] for item in results)
    return {
        "meter_name": meter,
        "valid": valid,
        "line_results": results,
    }
