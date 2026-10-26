"""Utility functions for string manipulation and text processing."""

import re


def slugify(text: str) -> str:
    """Converts a string into a URL-friendly slug.

    Args:
        text: The input text to convert.

    Returns:
        A lowercased, hyphen-separated slug string.
    """
    cleaned = text.lower().strip()
    cleaned = re.sub(r"[^\w\s-]", "", cleaned)
    cleaned = re.sub(r"[\s_-]+", "-", cleaned)
    cleaned = re.sub(r"-+", "-", cleaned)
    return cleaned.strip("-")


def count_words(text: str) -> int:
    """Counts the number of words in a string.

    Args:
        text: The input text to analyze.

    Returns:
        The total count of whitespace-delimited words.
    """
    stripped = text.strip()
    if not stripped:
        return 0
    return len(stripped.split())


def to_uppercase(text: str) -> str:
    """Converts a string to uppercase.

    Args:
        text: The string to convert.

    Returns:
        The uppercase representation of the string.
    """
    return text.upper()


def reverse_string(text: str) -> str:
    """Reverses the order of characters in a string.

    Args:
        text: The input string.

    Returns:
        The reversed string.
    """
    return text[::-1]


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncates a string to a maximum length, appending a suffix if shortened.

    Args:
        text: The input text to truncate.
        max_length: The maximum allowed length of the resulting string.
        suffix: Suffix to append if the text is truncated (default "...").

    Returns:
        The truncated string, or the original string if it is within max_length.

    Raises:
        ValueError: If max_length is negative or smaller than the length of suffix.
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if len(text) <= max_length:
        return text

    if max_length < len(suffix):
        raise ValueError("max_length cannot be less than suffix length")

    return text[: max_length - len(suffix)] + suffix
