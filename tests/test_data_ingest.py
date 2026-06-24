from core.data_ingest import load_json_corpus, load_csv_corpus, normalize_text, parse_labeled_text


def test_normalize_text_removes_non_telugu() -> None:
    normalized = normalize_text("Telugu రామ ప్రేమ! 123")
    assert "Telugu" not in normalized
    assert "రామ" in normalized


def test_load_json_corpus() -> None:
    entries = load_json_corpus("datasets/sample_corpus.json")
    assert len(entries) == 1
    assert entries[0]["source"] == "sample"


def test_parse_labeled_text() -> None:
    text = "PALLAVI: రామ ప్రేమ\nCHARANAM: రామ సుఖం"
    entries = parse_labeled_text(text)
    assert len(entries) == 2
    assert entries[0]["section"] == "PALLAVI"
    assert "రామ ప్రేమ" in entries[0]["text"]
