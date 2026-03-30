#!/usr/bin/env python3
"""
Unit tests for string_utils module

This test suite uses Python's built-in unittest framework.
Following TDD principles: Tests written first, implementation follows.

Run with: python -m unittest test_string_utils.py
Or: python test_string_utils.py
"""

import unittest
from string_utils import reverse_words


class TestReverseWords(unittest.TestCase):
    """Test cases for the reverse_words function."""

    def test_reverse_simple_sentence(self):
        """Test reversing a simple two-word sentence."""
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_reverse_multiple_words(self):
        """Test reversing a sentence with multiple words."""
        self.assertEqual(
            reverse_words("the quick brown fox"),
            "fox brown quick the"
        )

    def test_reverse_single_word(self):
        """Test reversing a sentence with a single word."""
        self.assertEqual(reverse_words("hello"), "hello")

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_words(""), "")

    def test_reverse_with_leading_spaces(self):
        """Test reversing a sentence with leading spaces."""
        self.assertEqual(reverse_words("  hello world"), "world hello")

    def test_reverse_with_trailing_spaces(self):
        """Test reversing a sentence with trailing spaces."""
        self.assertEqual(reverse_words("hello world  "), "world hello")

    def test_reverse_with_extra_spaces_between_words(self):
        """Test reversing with multiple spaces between words."""
        self.assertEqual(
            reverse_words("hello   world"),
            "world hello"
        )

    def test_reverse_preserves_single_spaces(self):
        """Test that normal spacing is preserved after reversal."""
        result = reverse_words("hello world test")
        self.assertEqual(result, "test world hello")
        # Check that there's exactly one space between words
        self.assertEqual(result.split(" "), ["test", "world", "hello"])

    def test_reverse_sentence_with_punctuation(self):
        """Test reversing a sentence with punctuation."""
        self.assertEqual(
            reverse_words("hello, world!"),
            "world! hello,"
        )

    def test_reverse_numbers_and_mixed_content(self):
        """Test reversing with numbers and mixed content."""
        self.assertEqual(
            reverse_words("test123 hello456"),
            "hello456 test123"
        )

    def test_reverse_long_sentence(self):
        """Test reversing a longer sentence."""
        self.assertEqual(
            reverse_words("this is a longer sentence with more words"),
            "words more with sentence longer a is this"
        )

    def test_reverse_tabs_and_newlines(self):
        """Test handling of tabs and newlines (treated as whitespace)."""
        # Tabs should be treated as word separators
        result = reverse_words("hello\tworld")
        self.assertEqual(result, "world hello")

    def test_reverse_multiple_spaces_consecutive(self):
        """Test that multiple consecutive spaces are collapsed to one."""
        result = reverse_words("word1    word2     word3")
        self.assertEqual(result, "word3 word2 word1")

    def test_reverse_preserves_word_order_not_characters(self):
        """Verify it's word reversal, not character reversal."""
        # This ensures we're reversing words, not characters
        self.assertNotEqual(reverse_words("abc"), "cba")
        self.assertEqual(reverse_words("abc"), "abc")  # Single word unchanged


class TestReverseWordsEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""

    def test_only_spaces(self):
        """Test a string containing only spaces."""
        self.assertEqual(reverse_words("     "), "")

    def test_only_whitespace_various(self):
        """Test strings with only whitespace characters."""
        self.assertEqual(reverse_words("\t\n"), "")

    def test_unicode_characters(self):
        """Test reversing with unicode characters."""
        self.assertEqual(
            reverse_words("hello 世界"),
            "世界 hello"
        )

    def test_mixed_case_preserved(self):
        """Test that word casing is preserved."""
        self.assertEqual(
            reverse_words("Hello World"),
            "World Hello"
        )

    def test_single_character_words(self):
        """Test with single character words."""
        self.assertEqual(
            reverse_words("a b c d"),
            "d c b a"
        )


def run_tests():
    """Run all tests and display results."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestReverseWords))
    suite.addTests(loader.loadTestsFromTestCase(TestReverseWordsEdgeCases))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
