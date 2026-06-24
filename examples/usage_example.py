from core.kirtana_validator import validate_kirtana_text
from core.meter_validator import validate_pattern
from core.benchmark import BenchmarkEntry, evaluate_entry

sample_text = """PALLAVI: రామ ప్రేమ
CHARANAM: రామ సుఖం
"""
expected_patterns = {
    "PALLAVI": [[1, 0, 1, 0]],
    "CHARANAM": [[1, 0, 0, 1]],
}

print("Kirtana validation example")
result = validate_kirtana_text(sample_text, expected_patterns)
print(result)

print("\nMeter validation example")
print(validate_pattern("రామ ప్రేమ", [1, 0, 1, 0]))

entry = BenchmarkEntry(
    name="example",
    text=sample_text,
    expected_patterns=expected_patterns,
    source="example",
)
print("\nBenchmark example")
print(evaluate_entry(entry))
