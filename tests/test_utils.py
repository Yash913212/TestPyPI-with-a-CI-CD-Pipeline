"""Unit tests for yash913212_pyutil utility functions."""

import pytest
from yash913212_pyutil import (
    __version__,
    count_words,
    reverse_string,
    slugify,
    to_uppercase,
    truncate_text,
)


def test_version():
    """Ensure the package exports a valid version string."""
    assert __version__ == "0.0.1"


class TestSlugify:
    """Tests for the slugify function."""

    def test_basic_slugify(self):
        assert slugify("Hello World!") == "hello-world"

    def test_leading_and_trailing_spaces(self):
        assert slugify("  leading and trailing spaces  ") == "leading-and-trailing-spaces"

    def test_multiple_special_characters(self):
        assert slugify("Python 3.12 & Packaging -- Guide!!") == "python-312-packaging-guide"

    def test_underscores_and_dashes(self):
        assert slugify("hello_world_test-case") == "hello-world-test-case"

    def test_empty_string(self):
        assert slugify("") == ""


class TestCountWords:
    """Tests for the count_words function."""

    def test_multiple_words(self):
        assert count_words("one two three") == 3

    def test_empty_string(self):
        assert count_words("") == 0

    def test_whitespace_only(self):
        assert count_words("     \t\n  ") == 0

    def test_single_word(self):
        assert count_words("Antigravity") == 1

    def test_extra_spaces_between_words(self):
        assert count_words("hello    world   with   spaces") == 4


class TestToUppercase:
    """Tests for the to_uppercase function."""

    def test_standard_conversion(self):
        assert to_uppercase("hello world") == "HELLO WORLD"

    def test_already_uppercase(self):
        assert to_uppercase("HELLO") == "HELLO"

    def test_empty_string(self):
        assert to_uppercase("") == ""


class TestReverseString:
    """Tests for the reverse_string function."""

    def test_standard_reverse(self):
        assert reverse_string("Python") == "nohtyP"

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_empty_string(self):
        assert reverse_string("") == ""


class TestTruncateText:
    """Tests for the truncate_text function."""

    def test_no_truncation_needed(self):
        assert truncate_text("Short text", 20) == "Short text"

    def test_exact_length_no_truncation(self):
        assert truncate_text("Exact", 5) == "Exact"

    def test_truncation_with_default_suffix(self):
        assert truncate_text("This is a long sentence.", 10) == "This is..."

    def test_truncation_with_custom_suffix(self):
        assert truncate_text("Long text to shorten", 8, suffix="~") == "Long te~"

    def test_negative_max_length_raises_error(self):
        with pytest.raises(ValueError, match="max_length must be non-negative"):
            truncate_text("Hello", -1)

    def test_max_length_less_than_suffix_raises_error(self):
        with pytest.raises(ValueError, match="max_length cannot be less than suffix length"):
            truncate_text("Hello World", 2, suffix="...")
