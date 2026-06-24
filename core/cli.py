"""Command-line interface for Chandas-Compile."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from core import analyze_text, validate_kirtana_text, validate_pattern
from core.benchmark import BenchmarkEntry, evaluate_entry, load_benchmark_entries


def read_text(path: str | None, value: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    if value is not None:
        return value
    raise ValueError("Either --file or --text must be provided.")


def parse_pattern(pattern: str) -> list[int]:
    return [int(x) for x in pattern.split(",") if x.strip()]


def run_analyze(args: argparse.Namespace) -> None:
    text = read_text(args.file, args.text)
    result = analyze_text(text)
    print(json.dumps({"text": text, "pattern": result}, ensure_ascii=False, indent=2))


def run_validate(args: argparse.Namespace) -> None:
    text = read_text(args.file, args.text)
    pattern = parse_pattern(args.expected)
    result = validate_pattern(text, pattern)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def run_kirtana(args: argparse.Namespace) -> None:
    text = read_text(args.file, args.text)
    patterns = json.loads(Path(args.patterns).read_text(encoding="utf-8"))
    result = validate_kirtana_text(text, patterns)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def _serialize_report(report: dict[str, Any]) -> dict[str, Any]:
    serialized = report.copy()
    serialized["sections"] = [
        {
            "name": section.name,
            "lines": section.lines,
            "expected_patterns": section.expected_patterns,
            "line_results": section.line_results,
            "valid": section.valid,
        }
        for section in report["sections"]
    ]
    return serialized


def run_benchmark(args: argparse.Namespace) -> None:
    entries = load_benchmark_entries(args.file)
    reports: list[dict[str, Any]] = [evaluate_entry(entry) for entry in entries]
    summary = {
        "total_entries": len(reports),
        "valid_entries": sum(1 for report in reports if report["structure_valid"]),
        "invalid_entries": sum(1 for report in reports if not report["structure_valid"]),
        "reports": [_serialize_report(report) for report in reports],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Chandas-Compile CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze", help="Analyze Telugu text to Laghu/Guru pattern")
    analyze_parser.add_argument("--text", help="Telugu text to analyze")
    analyze_parser.add_argument("--file", help="Path to a text file containing Telugu text")
    analyze_parser.set_defaults(func=run_analyze)

    validate_parser = subparsers.add_parser("validate", help="Validate a text line against expected Laghu/Guru pattern")
    validate_parser.add_argument("--expected", required=True, help="Comma-separated expected pattern, e.g. 1,0,1")
    validate_parser.add_argument("--text", help="Telugu text to validate")
    validate_parser.add_argument("--file", help="Path to a text file containing Telugu text")
    validate_parser.set_defaults(func=run_validate)

    kirtana_parser = subparsers.add_parser("kirtana", help="Validate labeled kirtana text against expected patterns JSON")
    kirtana_parser.add_argument("--patterns", required=True, help="JSON file containing expected patterns")
    kirtana_parser.add_argument("--text", help="Telugu kirtana text to validate")
    kirtana_parser.add_argument("--file", help="Path to a text file containing kirtana text")
    kirtana_parser.set_defaults(func=run_kirtana)

    benchmark_parser = subparsers.add_parser("benchmark", help="Run benchmark evaluation from dataset JSON")
    benchmark_parser.add_argument("--file", required=True, help="Path to benchmark dataset JSON file")
    benchmark_parser.set_defaults(func=run_benchmark)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
