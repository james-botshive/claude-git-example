#!/usr/bin/env python3
"""
Simple Calculator Module

A basic calculator module providing fundamental arithmetic operations.
"""

from __future__ import annotations

import math
from typing import Union


# Define number types for type hints
Number = Union[int, float]


def _validate_number(value, param_name: str = "value") -> None:
    """
    Validate that a value is a number (int or float).

    Args:
        value: Value to validate
        param_name: Name of the parameter for error messages

    Raises:
        TypeError: If value is not an int or float
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{param_name} must be a numeric type (int or float), got {type(value).__name__}")


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Raises:
        TypeError: If a or b are not numeric types

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first.

    Args:
        a: First number
        b: Second number to subtract

    Returns:
        Difference of a and b

    Raises:
        TypeError: If a or b are not numeric types

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b

    Raises:
        TypeError: If a or b are not numeric types

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Divide first number by second.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a and b

    Raises:
        TypeError: If a or b are not numeric types
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """
    Raise base to the power of exponent.

    Args:
        base: Base number
        exponent: Exponent

    Returns:
        base raised to the power of exponent

    Raises:
        TypeError: If base or exponent are not numeric types
        ValueError: If exponent is too large (potential DoS)

    Examples:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    _validate_number(base, "base")
    _validate_number(exponent, "exponent")

    # Prevent potential DoS from extremely large exponents
    if abs(exponent) > 1000:
        raise ValueError(f"Exponent too large (must be between -1000 and 1000), got {exponent}")

    return math.pow(base, exponent)


def square_root(n: Number) -> float:
    """
    Calculate the square root of a number.

    Args:
        n: Number to calculate square root of

    Returns:
        Square root of n

    Raises:
        TypeError: If n is not a numeric type
        ValueError: If n is negative

    Examples:
        >>> square_root(9)
        3.0
        >>> square_root(2)
        1.4142135623730951
    """
    _validate_number(n, "n")
    if n < 0:
        raise ValueError(f"Cannot calculate square root of negative number: {n}")
    return math.sqrt(n)


def percentage(part: Number, whole: Number) -> float:
    """
    Calculate percentage of part relative to whole.

    Args:
        part: The part value
        whole: The whole value

    Returns:
        Percentage (part / whole * 100)

    Raises:
        TypeError: If part or whole are not numeric types
        ZeroDivisionError: If whole is zero

    Examples:
        >>> percentage(25, 100)
        25.0
        >>> percentage(1, 3)
        33.33333333333333
    """
    _validate_number(part, "part")
    _validate_number(whole, "whole")
    if whole == 0:
        raise ZeroDivisionError("Cannot calculate percentage with zero as whole")
    return (part / whole) * 100


# Export all functions
__all__ = [
    'add',
    'subtract',
    'multiply',
    'divide',
    'power',
    'square_root',
    'percentage',
]
