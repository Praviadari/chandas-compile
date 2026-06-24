from core.data_ingest import build_versioned_dataset, save_versioned_dataset


def test_build_versioned_dataset() -> None:
    entries = [{"text": "రామ ప్రేమ", "source": "test"}]
    payload = build_versioned_dataset(entries, version="1.0", source="unit-test", notes="sample")
    assert payload["metadata"]["version"] == "1.0"
    assert payload["metadata"]["entry_count"] == 1


def test_save_versioned_dataset(tmp_path) -> None:
    entries = [{"text": "రామ ప్రేమ", "source": "test"}]
    output = tmp_path / "dataset.json"
    save_versioned_dataset(entries, output, version="1.0", source="unit-test", notes="sample")
    assert output.exists()
    loaded = output.read_text(encoding="utf-8")
    assert "metadata" in loaded
