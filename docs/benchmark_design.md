# Chandas-Compile Benchmark Design

This document describes the benchmark dataset schema, evaluation metrics, and report format for the Chandas-Compile benchmarking system.

## Benchmark Dataset Schema

Each benchmark dataset is a JSON file with the following structure:

```json
{
  "entries": [
    {
      "name": "example_name",
      "text": "PALLAVI: ...\nCHARANAM: ...",
      "expected_patterns": {
        "PALLAVI": [[1,0,1,0]],
        "CHARANAM": [[1,0,0,1]]
      },
      "source": "source_name",
      "author": "author_name",
      "notes": "optional notes"
    }
  ]
}
```

### Fields

- `name`: unique entry identifier.
- `text`: the Kirtana or poetic text to validate.
- `expected_patterns`: mapping from section name to line-pattern arrays.
- `source`: origin of the example.
- `author`: poet or contributor.
- `notes`: optional author/annotation notes.

## Evaluation Metrics

Each benchmark entry should generate:

- `structure_valid`: whether the Kirtana section flow is valid.
- `fsm_state`: final FSM state after validation.
- `section_results`: line-level validation results.

Aggregate metrics include:

- `total_entries`
- `valid_entries`
- `invalid_entries`
- `valid_ratio`

## Report Format

The benchmark report is a JSON summary containing:

- `total_entries`
- `valid_entries`
- `invalid_entries`
- `valid_ratio`
- `reports`: array of per-entry results

Per-entry result fields:

- `name`
- `source`
- `structure_valid`
- `fsm_state`
- `sections`

## Future Extensions

- Add scoring for meter completeness and line-level margin.
- Add model name and generation timestamp metadata.
- Add human judgment fields for qualitative evaluation.
