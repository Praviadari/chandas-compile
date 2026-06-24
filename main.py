"""Command-line entrypoint for Chandas Compile MVP."""

from __future__ import annotations

from core.benchmark import BenchmarkEntry, evaluate_entry, load_benchmark_entries
from core.binary_rules import analyze_syllable, encode_text
from core.kirtana_validator import validate_kirtana_text
from core.meter_validator import validate_pattern
from core.tokenizer import split_aksharas


def main() -> None:
    print("--- Chandas-Compile MVP ---")

    sample_word = "రామ"
    units = split_aksharas(sample_word)
    bits = encode_text(units)

    print(f"Input: {sample_word}")
    print(f"Units: {units}")
    print(f"Laghu/Guru bits: {bits}")

    sample_char = "రా"
    result = analyze_syllable(sample_char)
    state = "Guru (1)" if result == 1 else "Laghu (0)"
    print(f"Character: {sample_char} -> Operational State: {state}")

    pattern_check = validate_pattern(sample_word, [1, 0])
    print("\nMeter validation example:")
    print(f"Expected: {pattern_check['expected_pattern']}")
    print(f"Actual:   {pattern_check['actual_pattern']}")
    print(f"Valid:    {pattern_check['valid']}")

    kirtana_text = """PALLAVI: రామ సుఖం
CHARANAM: రామ ప్రేమ
"""
    expected_patterns = {
        "PALLAVI": [[1, 0, 0, 1]],
        "CHARANAM": [[1, 0, 1, 0]],
    }
    kirtana_result = validate_kirtana_text(kirtana_text, expected_patterns)
    print("\nKirtana validation example:")
    print(f"Structure valid: {kirtana_result['structure_valid']}")
    print(f"FSM state: {kirtana_result['fsm_state']}")

    benchmark_entries = load_benchmark_entries("datasets/sample_benchmark.json")
    benchmark_results = [evaluate_entry(entry) for entry in benchmark_entries]
    print("\nBenchmark example results:")
    for report in benchmark_results:
        print(
            f"- {report['name']}: valid={report['structure_valid']} state={report['fsm_state']}"
        )


if __name__ == "__main__":
    main()
