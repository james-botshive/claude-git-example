#!/usr/bin/env python3
"""
Simple Calculator Module

A basic calculator module providing fundamental arithmetic operations.
"""

import math
from typing import Union


# Define number types for type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first.

    Args:
        a: First number
        b: Second number to subtract

    Returns:
        Difference of a and b

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
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
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
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

    Examples:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    return math.pow(base, exponent)


def square_root(n: Number) -> float:
    """
    Calculate the square root of a number.

    Args:
        n: Number to calculate square root of

    Returns:
        Square root of n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> square_root(9)
        3.0
        >>> square_root(2)
        1.4142135623730951
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
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
        ZeroDivisionError: If whole is zero

    Examples:
        >>> percentage(25, 100)
        25.0
        >>> percentage(1, 3)
        33.33333333333333
    """
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
