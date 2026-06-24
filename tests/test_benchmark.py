from core.benchmark import BenchmarkEntry, evaluate_entry, load_benchmark_entries, summarize_reports


def test_load_benchmark_entries() -> None:
    entries = load_benchmark_entries("datasets/sample_benchmark.json")
    assert len(entries) == 1
    assert entries[0].name == "simple_kirtana"


def test_evaluate_entry() -> None:
    entry = BenchmarkEntry(
        name="test",
        text="PALLAVI: రామ ప్రేమ\nCHARANAM: రామ సుఖం\n",
        expected_patterns={"PALLAVI": [[1, 0, 1, 0]], "CHARANAM": [[1, 0, 0, 1]]},
    )
    report = evaluate_entry(entry)
    assert report["structure_valid"] is True


def test_summarize_reports() -> None:
    reports = [
        {"structure_valid": True},
        {"structure_valid": False},
    ]
    summary = summarize_reports(reports)
    assert summary["total_entries"] == 2
    assert summary["valid_entries"] == 1
    assert summary["invalid_entries"] == 1
    assert summary["valid_ratio"] == 0.5
