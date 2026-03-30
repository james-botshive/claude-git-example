#!/usr/bin/env python3
"""
Unit tests for the calculator module

This test suite uses Python's built-in unittest framework.
Run with: python -m unittest test_calculator.py
Or: python test_calculator.py
"""

import unittest
import math
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    percentage
)


class TestAddition(unittest.TestCase):
    """Test cases for the add function."""

    def test_add_positive_integers(self):
        """Test adding positive integers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

    def test_add_negative_integers(self):
        """Test adding negative integers."""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(-10, 3), -7)

    def test_add_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0)

    def test_add_mixed_types(self):
        """Test adding int and float."""
        self.assertEqual(add(2, 3.5), 5.5)
        self.assertEqual(add(-1, 2.5), 1.5)


class TestSubtraction(unittest.TestCase):
    """Test cases for the subtract function."""

    def test_subtract_positive_integers(self):
        """Test subtracting positive integers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_negative_integers(self):
        """Test subtracting negative integers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-3, -5), 2)

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        self.assertAlmostEqual(subtract(5.5, 3.5), 2.0)
        self.assertAlmostEqual(subtract(3.0, 1.5), 1.5)


class TestMultiplication(unittest.TestCase):
    """Test cases for the multiply function."""

    def test_multiply_positive_integers(self):
        """Test multiplying positive integers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1, 100), 100)

    def test_multiply_negative_integers(self):
        """Test multiplying negative integers."""
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)


class TestDivision(unittest.TestCase):
    """Test cases for the divide function."""

    def test_divide_integers(self):
        """Test dividing integers."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide(1.0, 4.0), 0.25)

    def test_divide_by_zero(self):
        """Test that division by zero raises an error."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)


class TestPower(unittest.TestCase):
    """Test cases for the power function."""

    def test_power_positive_exponent(self):
        """Test raising numbers to positive powers."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)

    def test_power_negative_exponent(self):
        """Test raising numbers to negative powers."""
        self.assertAlmostEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(10, -2), 0.01)

    def test_power_fractional_exponent(self):
        """Test raising numbers to fractional powers (roots)."""
        self.assertAlmostEqual(power(4, 0.5), 2.0)
        self.assertAlmostEqual(power(27, 1/3), 3.0, places=5)

    def test_power_zero_base(self):
        """Test zero as base."""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)  # 0^0 is conventionally 1


class TestSquareRoot(unittest.TestCase):
    """Test cases for the square_root function."""

    def test_square_root_perfect_squares(self):
        """Test square root of perfect squares."""
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(1), 1.0)
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(100), 10.0)

    def test_square_root_non_perfect_squares(self):
        """Test square root of non-perfect squares."""
        self.assertAlmostEqual(square_root(2), 1.414213562)
        self.assertAlmostEqual(square_root(3), 1.732050807)
        self.assertAlmostEqual(square_root(5), 2.236067977)

    def test_square_root_negative(self):
        """Test that square root of negative raises error."""
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-100)


class TestPercentage(unittest.TestCase):
    """Test cases for the percentage function."""

    def test_percentage_simple(self):
        """Test simple percentage calculations."""
        self.assertEqual(percentage(25, 100), 25.0)
        self.assertEqual(percentage(50, 100), 50.0)
        self.assertEqual(percentage(100, 100), 100.0)

    def test_percentage_fractions(self):
        """Test percentage of fractions."""
        self.assertAlmostEqual(percentage(1, 3), 33.33333333333333)
        self.assertAlmostEqual(percentage(1, 2), 50.0)
        self.assertAlmostEqual(percentage(2, 3), 66.66666666666666)

    def test_percentage_negative_values(self):
        """Test percentage with negative values."""
        self.assertEqual(percentage(-25, 100), -25.0)
        self.assertEqual(percentage(25, -100), -25.0)

    def test_percentage_zero_whole(self):
        """Test that zero as whole raises error."""
        with self.assertRaises(ZeroDivisionError):
            percentage(25, 0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""

    def test_large_numbers(self):
        """Test operations with large numbers."""
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(multiply(10000, 10000), 100000000)
        self.assertEqual(power(10, 6), 1000000)

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        self.assertAlmostEqual(add(0.0001, 0.0002), 0.0003)
        self.assertAlmostEqual(multiply(0.01, 0.01), 0.0001)

    def test_operations_with_zero(self):
        """Test various operations involving zero."""
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(power(5, 0), 1)


class TestInputValidation(unittest.TestCase):
    """Test cases for input type validation."""

    def test_add_with_string(self):
        """Test that add raises TypeError for string input."""
        with self.assertRaises(TypeError):
            add("5", 3)
        with self.assertRaises(TypeError):
            add(5, "3")

    def test_subtract_with_string(self):
        """Test that subtract raises TypeError for string input."""
        with self.assertRaises(TypeError):
            subtract("10", 3)
        with self.assertRaises(TypeError):
            subtract(10, "3")

    def test_multiply_with_list(self):
        """Test that multiply raises TypeError for list input."""
        with self.assertRaises(TypeError):
            multiply([5], 3)
        with self.assertRaises(TypeError):
            multiply(5, [3])

    def test_divide_with_dict(self):
        """Test that divide raises TypeError for dict input."""
        with self.assertRaises(TypeError):
            divide({"a": 10}, 2)
        with self.assertRaises(TypeError):
            divide(10, {"b": 2})

    def test_power_with_none(self):
        """Test that power raises TypeError for None input."""
        with self.assertRaises(TypeError):
            power(None, 2)
        with self.assertRaises(TypeError):
            power(2, None)

    def test_square_root_with_string(self):
        """Test that square_root raises TypeError for string input."""
        with self.assertRaises(TypeError):
            square_root("16")

    def test_percentage_with_tuple(self):
        """Test that percentage raises TypeError for tuple input."""
        with self.assertRaises(TypeError):
            percentage((25,), 100)
        with self.assertRaises(TypeError):
            percentage(25, (100,))


class TestNewValidations(unittest.TestCase):
    """Test cases for new validation features."""

    def test_power_large_exponent_positive(self):
        """Test that power raises ValueError for very large positive exponents."""
        with self.assertRaises(ValueError):
            power(2, 1001)

    def test_power_large_exponent_negative(self):
        """Test that power raises ValueError for very large negative exponents."""
        with self.assertRaises(ValueError):
            power(2, -1001)

    def test_power_boundary_value(self):
        """Test that power works at the boundary (1000)."""
        result = power(2, 1000)
        self.assertIsInstance(result, float)

    def test_divide_custom_error_message(self):
        """Test that divide provides clear error message."""
        try:
            divide(10, 0)
            self.fail("Should have raised ZeroDivisionError")
        except ZeroDivisionError as e:
            self.assertIn("Cannot divide by zero", str(e))

    def test_square_root_custom_error_message(self):
        """Test that square_root provides clear error message."""
        try:
            square_root(-4)
            self.fail("Should have raised ValueError")
        except ValueError as e:
            self.assertIn("Cannot calculate square root of negative number", str(e))


def run_tests():
    """Run all tests and display results."""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestAddition))
    suite.addTests(loader.loadTestsFromTestCase(TestSubtraction))
    suite.addTests(loader.loadTestsFromTestCase(TestMultiplication))
    suite.addTests(loader.loadTestsFromTestCase(TestDivision))
    suite.addTests(loader.loadTestsFromTestCase(TestPower))
    suite.addTests(loader.loadTestsFromTestCase(TestSquareRoot))
    suite.addTests(loader.loadTestsFromTestCase(TestPercentage))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestInputValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestNewValidations))

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
