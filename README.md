# yash913212-pyutil

A modern Python utility package for string operations and text processing, published to **TestPyPI** via an automated GitHub Actions CI/CD release pipeline.

[![CI/CD Pipeline](https://github.com/Yash913212/TestPyPI-with-a-CI-CD-Pipeline/actions/workflows/publish.yml/badge.svg)](https://github.com/Yash913212/TestPyPI-with-a-CI-CD-Pipeline/actions/workflows/publish.yml)

---

## Features

- **`slugify(text: str) -> str`**: Converts strings into URL-friendly, lowercased slugs.
- **`count_words(text: str) -> int`**: Safely counts whitespace-separated words.
- **`to_uppercase(text: str) -> str`**: Converts text to uppercase.
- **`reverse_string(text: str) -> str`**: Reverses the character sequence of text.
- **`truncate_text(text: str, max_length: int, suffix: str = "...") -> str`**: Gracefully shortens strings with custom suffixes.

---

## Installation

### From TestPyPI

To install the package from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ yash913212-pyutil
```

### From Local Source

```bash
pip install .
```

---

## Quickstart

```python
from yash913212_pyutil import slugify, count_words, to_uppercase, reverse_string, truncate_text

# Convert text into a clean URL slug
slug = slugify("Hello World! This is Python 3")
print(slug)  # Output: hello-world-this-is-python-3

# Count words
words = count_words("Fast and automated CI/CD pipeline")
print(words)  # Output: 5

# Uppercase text
upper = to_uppercase("hello antigravity")
print(upper)  # Output: HELLO ANTIGRAVITY

# Reverse text
reversed_str = reverse_string("Python")
print(reversed_str)  # Output: nohtyP

# Truncate text
short = truncate_text("DeepMind Advanced Agentic Coding", 15)
print(short)  # Output: DeepMind Adv...
```

---

## Development & Testing

### 1. Install Development Dependencies

```bash
pip install build pytest pytest-cov twine
```

### 2. Run Test Suite with Coverage

```bash
pytest --cov=src --cov-fail-under=90 tests/
```

### 3. Build Distribution Packages

Build both the wheel (`.whl`) and source distribution (`.tar.gz`):

```bash
python -m build
```

This creates the distribution files under `dist/`:
- `dist/yash913212_pyutil-0.0.1-py3-none-any.whl`
- `dist/yash913212_pyutil-0.0.1.tar.gz`

### 4. Verify Built Artifacts

```bash
twine check dist/*
```

---

## CI/CD Pipeline Architecture

This repository uses GitHub Actions (`.github/workflows/publish.yml`) to enforce high quality and safe releases:

1. **`test` job**:
   - Triggers on every `pull_request` to `main` and every `push` to `main`.
   - Runs `pytest` and verifies code coverage meets or exceeds 90%.
2. **`publish` job**:
   - Gated behind `needs: test`.
   - Executes **only** when a git tag matching `v*` (e.g. `v0.0.1`) is pushed.
   - Builds distribution packages with `python -m build`.
   - Verifies package validity using `twine check`.
   - Securely authenticates with TestPyPI using `secrets.TEST_PYPI_API_TOKEN` and publishes the distribution via `twine`.

---

## License

This project is licensed under the MIT License.
