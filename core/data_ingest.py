"""Data ingestion and normalization utilities for Telugu poetry corpora."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


TELUGU_RANGE = (0x0C00, 0x0C7F)


def normalize_text(text: str) -> str:
    """Normalize Telugu text by removing non-Telugu characters and excess whitespace."""
    cleaned = re.sub(r"[^\u0C00-\u0C7F\s]", " ", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def normalize_entry(raw: dict[str, Any]) -> dict[str, Any]:
    """Create a normalized data entry from a raw metadata dictionary."""
    return {
        "text": normalize_text(str(raw.get("text", raw.get("verse", "")))),
        "source": raw.get("source") or raw.get("file") or "",
        "author": raw.get("author", ""),
        "metre": raw.get("metre", ""),
        "section": raw.get("section", ""),
    }


def load_json_corpus(path: str | Path) -> list[dict[str, Any]]:
    """Load a JSON corpus file and normalize each entry."""
    path_obj = Path(path)
    payload = json.loads(path_obj.read_text(encoding="utf-8"))
    raw_entries = payload.get("entries") if isinstance(payload, dict) else payload
    if not isinstance(raw_entries, list):
        raise ValueError("JSON corpus must be a list or contain an 'entries' list.")
    return [normalize_entry(item) for item in raw_entries]


def load_csv_corpus(
    path: str | Path,
    text_column: str = "text",
    source_column: str = "source",
    author_column: str | None = None,
    metre_column: str | None = None,
    section_column: str | None = None,
) -> list[dict[str, Any]]:
    """Load and normalize a corpus from a CSV file."""
    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        entries: list[dict[str, Any]] = []
        for row in reader:
            raw = {
                "text": row.get(text_column, ""),
                "source": row.get(source_column, ""),
                "author": row.get(author_column, "") if author_column else "",
                "metre": row.get(metre_column, "") if metre_column else "",
                "section": row.get(section_column, "") if section_column else "",
            }
            if raw["text"]:
                entries.append(normalize_entry(raw))
    return entries


def parse_labeled_text(text: str, labels: list[str] | None = None) -> list[dict[str, Any]]:
    """Parse labeled text with prefixed section markers into normalized entries."""
    entries: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    labels = [label.upper() for label in (labels or ["PALLAVI:", "CHARANAM:"])]

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        upper = line.upper()
        matching_label = next((label for label in labels if upper.startswith(label)), None)
        if matching_label:
            if current:
                entries.append(current)
            current = {
                "section": matching_label.rstrip(":"),
                "text": normalize_text(line[len(matching_label) :].strip()),
                "source": "labeled_text",
                "author": "",
                "metre": "",
            }
            continue

        if current is not None:
            current["text"] = normalize_text(f"{current['text']} {line}")

    if current:
        entries.append(current)
    return entries


def save_normalized_dataset(entries: list[dict[str, Any]], path: str | Path) -> None:
    """Save normalized entries to a JSON file."""
    path_obj = Path(path)
    payload = {"entries": entries}
    path_obj.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
