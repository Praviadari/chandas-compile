import json
from pathlib import Path

from core.cli import main


def test_cli_analyze(tmp_path):
    result_file = tmp_path / "input.txt"
    result_file.write_text("రామ ప్రేమ", encoding="utf-8")
    main(["analyze", "--file", str(result_file)])


def test_cli_validate(tmp_path):
    result_file = tmp_path / "input.txt"
    result_file.write_text("రామ ప్రేమ", encoding="utf-8")
    main(["validate", "--file", str(result_file), "--expected", "1,0,1,0"])


def test_cli_benchmark(tmp_path):
    data = {
        "entries": [
            {
                "name": "simple",
                "text": "PALLAVI: రామ ప్రేమ\nCHARANAM: రామ సుఖం\n",
                "expected_patterns": {"PALLAVI": [[1, 0, 1, 0]], "CHARANAM": [[1, 0, 0, 1]]},
            }
        ]
    }
    file_path = tmp_path / "benchmark.json"
    file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    main(["benchmark", "--file", str(file_path)])
