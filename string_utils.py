#!/usr/bin/env python3
"""
String Utilities Module

Provides useful string manipulation functions.
"""


def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.

    This function reverses the order of words (not characters) in a sentence.
    Multiple spaces between words are collapsed to a single space.
    Leading and trailing spaces are removed.

    Args:
        sentence: The input sentence to reverse

    Returns:
        The sentence with words in reverse order, normalized to single spaces

    Examples:
        >>> reverse_words("hello world")
        'world hello'
        >>> reverse_words("the quick brown fox")
        'fox brown quick the'
        >>> reverse_words("  hello   world  ")
        'world hello'
        >>> reverse_words("")
        ''

    Note:
        - Words are defined as whitespace-separated tokens
        - All whitespace (spaces, tabs, newlines) are treated as word separators
        - Multiple consecutive spaces are collapsed to single spaces
        - Leading/trailing whitespace is removed
    """
    if not sentence or not sentence.strip():
        return ""

    # Split the sentence into words (handles multiple spaces automatically)
    words = sentence.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join back with single spaces
    return " ".join(reversed_words)


# Export all functions
__all__ = ['reverse_words']

