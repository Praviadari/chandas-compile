# Contributing to Chandas-Compile

Thank you for your interest in contributing to Chandas-Compile.

## Getting Started

1. Fork the repository.
2. Create a feature branch from `main`.
3. Install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. Run tests before opening a pull request:

```bash
python -m pytest -q
```

## Project Structure

- `core/`: implementation modules
- `tests/`: unit tests
- `datasets/`: sample datasets and benchmark entries
- `docs/`: planning and roadmap documentation

## How to Contribute

- Add tests for new features or bug fixes.
- Keep changes small and focused.
- Document behavior in `README.md` or `docs/` as needed.

## Reporting Issues

Please use the repository issue tracker to report bugs or request new features.

## Coding Guidelines

- Use `snake_case` for Python functions and variables.
- Keep line length under 100 characters when practical.
- Add clear docstrings for public functions.
