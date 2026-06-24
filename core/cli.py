"""Command-line interface for Chandas-Compile."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from core import analyze_text, validate_kirtana_text, validate_pattern
from core.benchmark import BenchmarkEntry, evaluate_entry, load_benchmark_entries
from core.chandassu_validator import suggest_meter_names, validate_line_meter, validate_meter_text
from core.data_ingest import (
    load_csv_corpus,
    load_json_corpus,
    parse_labeled_text,
    save_versioned_dataset,
)


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


def run_meter(args: argparse.Namespace) -> None:
    text = read_text(args.file, args.text)
    if args.meter == "suggest":
        result = {"suggestions": suggest_meter_names(text)}
    else:
        result = validate_meter_text(text, args.meter)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def run_ingest(args: argparse.Namespace) -> None:
    if args.format == "json":
        entries = load_json_corpus(args.file)
    elif args.format == "csv":
        entries = load_csv_corpus(
            args.file,
            text_column=args.text_column,
            source_column=args.source_column,
            author_column=args.author_column,
            metre_column=args.metre_column,
            section_column=args.section_column,
        )
    else:
        labels = [label.strip() for label in args.labels.split(",") if label.strip()]
        entries = parse_labeled_text(read_text(args.file, None), labels=labels)

    save_versioned_dataset(entries, args.output, args.version, args.source, notes=args.notes)
    print(json.dumps({"output": args.output, "entries": len(entries), "version": args.version}, ensure_ascii=False, indent=2))


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

    meter_parser = subparsers.add_parser("meter", help="Validate Telugu text against a named Chandassu meter")
    meter_parser.add_argument("--meter", required=True, help="Named meter to validate, e.g. utpalamala, champakamala, kanda_padyam")
    meter_parser.add_argument("--text", help="Telugu text to validate")
    meter_parser.add_argument("--file", help="Path to a text file containing Telugu text")
    meter_parser.set_defaults(func=run_meter)

    ingest_parser = subparsers.add_parser("ingest", help="Ingest a corpus and save a versioned normalized dataset")
    ingest_parser.add_argument("--file", required=True, help="Input file path")
    ingest_parser.add_argument("--format", choices=["json", "csv", "labeled"], default="json", help="Input file format")
    ingest_parser.add_argument("--output", required=True, help="Path to save normalized dataset JSON")
    ingest_parser.add_argument("--version", required=True, help="Dataset version")
    ingest_parser.add_argument("--source", required=True, help="Dataset source identifier")
    ingest_parser.add_argument("--notes", default="", help="Optional provenance notes")
    ingest_parser.add_argument("--text-column", default="text", help="CSV column name for text content")
    ingest_parser.add_argument("--source-column", default="source", help="CSV column name for source metadata")
    ingest_parser.add_argument("--author-column", default="author", help="CSV column name for author metadata")
    ingest_parser.add_argument("--metre-column", default="metre", help="CSV column name for metre metadata")
    ingest_parser.add_argument("--section-column", default="section", help="CSV column name for section metadata")
    ingest_parser.add_argument("--labels", default="PALLAVI:,CHARANAM:,ANUPALLAVI:", help="Comma-separated section labels for labeled text")
    ingest_parser.set_defaults(func=run_ingest)

    benchmark_parser = subparsers.add_parser("benchmark", help="Run benchmark evaluation from dataset JSON")
    benchmark_parser.add_argument("--file", required=True, help="Path to benchmark dataset JSON file")
    benchmark_parser.set_defaults(func=run_benchmark)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
