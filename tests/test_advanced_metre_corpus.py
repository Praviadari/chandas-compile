import json
from pathlib import Path

from core.chandassu_validator import validate_line_meter, validate_meter_text


def test_advanced_metre_corpus_entries_exist() -> None:
    path = Path("datasets/advanced_metre_corpus.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert len(payload["entries"]) == 3


def test_utpalamala_example() -> None:
    result = validate_line_meter("రామ ప్రేమ", "utpalamala")
    assert result["valid"] is True


def test_champakamala_example() -> None:
    result = validate_line_meter("రామ సుఖం", "champakamala")
    assert result["valid"] is True


def test_kanda_padyam_example() -> None:
    result = validate_meter_text("రామ ప్రేమ\nరామ సుఖం", "kanda_padyam")
    assert result["valid"] is True
