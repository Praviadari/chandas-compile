"""Benchmarking support for Chandas-Compile evaluation tasks."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from core.kirtana_validator import validate_kirtana_text


@dataclass
class BenchmarkEntry:
    name: str
    text: str
    expected_patterns: dict[str, list[list[int]]]
    source: str | None = None


def load_benchmark_entries(path: str | Path) -> list[BenchmarkEntry]:
    """Load benchmark entries from a JSON dataset file."""
    path_obj = Path(path)
    payload = json.loads(path_obj.read_text(encoding="utf-8"))
    entries: list[BenchmarkEntry] = []

    if isinstance(payload, dict) and "entries" in payload:
        for raw in payload["entries"]:
            entries.append(
                BenchmarkEntry(
                    name=raw["name"],
                    text=raw["text"],
                    expected_patterns=raw["expected_patterns"],
                    source=raw.get("source"),
                )
            )
    else:
        raise ValueError("Benchmark JSON must contain an 'entries' list.")

    return entries


def evaluate_entry(entry: BenchmarkEntry) -> dict[str, Any]:
    """Evaluate a single benchmark entry and return its validation report."""
    report = validate_kirtana_text(entry.text, entry.expected_patterns)
    return {
        "name": entry.name,
        "source": entry.source,
        "structure_valid": report["structure_valid"],
        "fsm_state": report["fsm_state"],
        "sections": report["sections"],
    }


def summarize_reports(reports: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize benchmark results across multiple entries."""
    total = len(reports)
    valid = sum(1 for report in reports if report["structure_valid"])
    return {
        "total_entries": total,
        "valid_entries": valid,
        "invalid_entries": total - valid,
        "valid_ratio": valid / total if total else 0.0,
        "reports": reports,
    }
