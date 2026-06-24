# Chandas-Compile

An open-source algorithmic engine that models Telugu prosody (Chandassu) and
kirtana structures as computational rules and finite-state transitions.

## Core Concept

- Binary syllables: Laghu maps to `0`, Guru maps to `1`.
- Rule engine: Convert Telugu akshara-like units into bit patterns.
- State machine: Represent Pallavi and Charanam progression as an FSM.

## MVP Status

- Telugu tokenizer skeleton: [x]
- Laghu-Guru parser: [x]
- Kirtana FSM skeleton: [x]
- Unit tests for base rules: [x]

## Project Structure

- `core/binary_rules.py`: Laghu-Guru evaluator.
- `core/tokenizer.py`: Basic akshara splitter (MVP quality).
- `core/kirtana_fsm.py`: Minimal kirtana finite-state machine.
- `core/kirtana_validator.py`: Section-based kirtana parser and validator.
- `core/meter_validator.py`: Meter pattern validation and text analysis.
- `core/benchmark.py`: Benchmark-loading and evaluation helpers.
- `core/data_ingest.py`: Data ingestion and corpus normalization utilities.
- `main.py`: CLI demo script.
- `examples/usage_example.py`: Example use cases for developers.
- `tests/test_binary_rules.py`: Initial tests.
- `tests/test_kirtana_fsm.py`: FSM sequence validation tests.
- `tests/test_meter_validator.py`: Meter validation tests.
- `tests/test_kirtana_validator.py`: Kirtana validator end-to-end tests.
- `tests/test_benchmark.py`: Benchmark evaluation tests.
- `tests/test_data_ingest.py`: Data ingestion tests.

## Package Usage

```python
from core import analyze_text, validate_pattern, validate_kirtana_text

text = "రామ ప్రేమ"
pattern = analyze_text(text)
print(pattern)

result = validate_pattern(text, [1, 0, 1, 0])
print(result)
```

## Examples

Run the usage example script:

```bash
python examples/usage_example.py
```

## Quick Start

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
pytest -q
```

## CLI Usage

Install the package locally:

```bash
pip install -e .
```

Then use the CLI:

```bash
chandas-compile analyze --text "రామ ప్రేమ"
chandas-compile validate --text "రామ ప్రేమ" --expected 1,0,1,0
chandas-compile benchmark --file datasets/sample_benchmark.json
```

## Roadmap

- Improve conjunct/vatthulu handling and true akshara segmentation.
- Add chandassu validators (Utpalamala, Champakamala, Kanda Padyam).
- Build dataset tooling and benchmark suite.

## Benchmarking

- `core/benchmark.py` loads JSON benchmark entries and evaluates kirtana validation results.
- `datasets/sample_benchmark.json` includes a sample benchmark entry.
- Use `python main.py` to exercise the benchmark demo and `pytest -q` to validate benchmark tests.
