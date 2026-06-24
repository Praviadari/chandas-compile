"""Chandas-Compile Python package exports."""

from .binary_rules import analyze_syllable, analyze_syllable_with_trace, analyze_text_with_trace, encode_text, validate_pattern_with_trace
from .benchmark import BenchmarkEntry, evaluate_entry, load_benchmark_entries, summarize_reports
from .data_ingest import (
    load_csv_corpus,
    load_json_corpus,
    normalize_text,
    parse_labeled_text,
    save_normalized_dataset,
    save_versioned_dataset,
    build_versioned_dataset,
)
from .kirtana_fsm import KirtanaFSM
from .kirtana_validator import validate_kirtana_text, validate_kirtana_sections, parse_kirtana_text
from .meter_validator import analyze_text, format_bits, validate_pattern
from .chandassu_validator import get_known_meter_names, get_meter_patterns, suggest_meter_names, validate_line_meter, validate_meter_text

__all__ = [
    "analyze_syllable",
    "encode_text",
    "BenchmarkEntry",
    "evaluate_entry",
    "load_benchmark_entries",
    "summarize_reports",
    "load_csv_corpus",
    "load_json_corpus",
    "normalize_text",
    "parse_labeled_text",
    "save_normalized_dataset",
    "KirtanaFSM",
    "validate_kirtana_text",
    "validate_kirtana_sections",
    "parse_kirtana_text",
    "analyze_text",
    "format_bits",
    "validate_pattern",
    "get_known_meter_names",
    "get_meter_info",
    "list_known_meters",
]
