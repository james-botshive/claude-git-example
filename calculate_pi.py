#!/usr/bin/env python3
"""
Pi Calculator - A tool to calculate Pi using various algorithms
"""

import argparse
import math
import random
import sys
from typing import Callable


def leibniz_formula(iterations: int = 1000000) -> float:
    """
    Calculate Pi using the Leibniz formula (Gregory-Leibniz series).

    Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

    Args:
        iterations: Number of terms to calculate (default: 1,000,000)

    Returns:
        Approximation of Pi
    """
    pi = 0.0
    sign = 1.0

    for i in range(iterations):
        denominator = 2 * i + 1
        pi += sign / denominator
        sign *= -1.0

    return pi * 4


def nilakantha_series(iterations: int = 1000000) -> float:
    """
    Calculate Pi using the Nilakantha series.

    Pi = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - 4/(8×9×10) + ...

    Args:
        iterations: Number of terms to calculate (default: 1,000,000)

    Returns:
        Approximation of Pi
    """
    pi = 3.0
    sign = 1.0

    for i in range(iterations):
        start = 2 * i + 2
        term = 4.0 / (start * (start + 1) * (start + 2))
        pi += sign * term
        sign *= -1.0

    return pi


def monte_carlo_simulation(samples: int = 1000000) -> float:
    """
    Calculate Pi using the Monte Carlo method.

    Generates random points in a square and counts how many fall within
    the inscribed circle.

    Args:
        samples: Number of random points to generate (default: 1,000,000)

    Returns:
        Approximation of Pi
    """
    inside_circle = 0

    for _ in range(samples):
        x = random.random()
        y = random.random()

        # Check if point is within the unit circle
        if x**2 + y**2 <= 1.0:
            inside_circle += 1

    # Pi = 4 * (points inside circle / total points)
    return 4.0 * inside_circle / samples


def gauss_legendre(iterations: int = 5) -> float:
    """
    Calculate Pi using the Gauss-Legendre algorithm.

    This algorithm converges very quickly - each iteration doubles the
    number of correct digits.

    Args:
        iterations: Number of iterations (default: 5 gives ~45 digits)

    Returns:
        Approximation of Pi
    """
    a = 1.0
    b = 1.0 / math.sqrt(2.0)
    t = 0.25
    p = 1.0

    for _ in range(iterations):
        a_new = (a + b) / 2.0
        b = math.sqrt(a * b)
        t -= p * (a - a_new) ** 2
        p *= 2.0
        a = a_new

    return (a + b) ** 2 / (4.0 * t)


def bailey_borwein_plouffe(digits: int = 10) -> str:
    """
    Calculate Pi using the Bailey-Borwein-Plouffe (BBP) formula.

    This algorithm can calculate the nth digit of Pi without calculating
    previous digits.

    Args:
        digits: Number of digits to calculate (default: 10)

    Returns:
        String representation of Pi with specified digits
    """
    pi = 0.0

    for k in range(digits * 10):  # Calculate extra terms for precision
        # BBP formula: Pi = sum(1/16^k * [4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)])
        term = (
            1.0 / (16.0 ** k) *
            (
                4.0 / (8.0 * k + 1.0) -
                2.0 / (8.0 * k + 4.0) -
                1.0 / (8.0 * k + 5.0) -
                1.0 / (8.0 * k + 6.0)
            )
        )
        pi += term

    return f"{pi:.{digits}f}"


def run_comparison(iterations: int = 1000000) -> None:
    """
    Compare different Pi calculation algorithms.

    Args:
        iterations: Number of iterations/samples for algorithms
    """
    print(f"Comparing Pi calculation algorithms (iterations: {iterations:,})")
    print("=" * 70)
    print(f"{'Algorithm':<25} {'Result':<20} {'Error':<20}")
    print("=" * 70)

    actual_pi = math.pi

    algorithms = [
        ("Leibniz Formula", lambda: leibniz_formula(iterations)),
        ("Nilakantha Series", lambda: nilakantha_series(iterations)),
        ("Monte Carlo (1M samples)", lambda: monte_carlo_simulation(iterations)),
        ("Gauss-Legendre (5 iter)", lambda: gauss_legendre(5)),
        ("math.pi (standard)", lambda: actual_pi),
    ]

    for name, func in algorithms:
        result = func()
        error = abs(result - actual_pi)
        print(f"{name:<25} {result:<20.15f} {error:.2e}")


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Calculate Pi using various algorithms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run default comparison of all algorithms
  python calculate_pi.py

  # Use Leibniz formula with 10 million iterations
  python calculate_pi.py --leibniz --iterations 10000000

  # Use Monte Carlo method with 5 million samples
  python calculate_pi.py --monte-carlo --iterations 5000000

  # Use Gauss-Legendre algorithm (very fast convergence)
  python calculate_pi.py --gauss-legendre

  # Calculate Pi to 20 decimal places using BBP formula
  python calculate_pi.py --bbp --digits 20

  # Compare all algorithms
  python calculate_pi.py --compare --iterations 1000000
        """
    )

    parser.add_argument(
        '--leibniz',
        action='store_true',
        help='Use Leibniz formula'
    )
    parser.add_argument(
        '--nilakantha',
        action='store_true',
        help='Use Nilakantha series'
    )
    parser.add_argument(
        '--monte-carlo',
        action='store_true',
        help='Use Monte Carlo simulation'
    )
    parser.add_argument(
        '--gauss-legendre',
        action='store_true',
        help='Use Gauss-Legendre algorithm'
    )
    parser.add_argument(
        '--bbp',
        action='store_true',
        help='Use Bailey-Borwein-Plouffe formula'
    )
    parser.add_argument(
        '--compare',
        action='store_true',
        help='Compare all algorithms (default)'
    )
    parser.add_argument(
        '--iterations',
        '-i',
        type=int,
        default=1000000,
        help='Number of iterations/samples (default: 1,000,000)'
    )
    parser.add_argument(
        '--digits',
        '-d',
        type=int,
        default=10,
        help='Number of decimal digits for BBP formula (default: 10)'
    )

    args = parser.parse_args()

    # If no specific algorithm is chosen, run comparison
    if not any([args.leibniz, args.nilakantha, args.monte_carlo,
                args.gauss_legendre, args.bbp]):
        args.compare = True

    try:
        if args.compare:
            run_comparison(args.iterations)
        elif args.leibniz:
            result = leibniz_formula(args.iterations)
            print(f"Leibniz Formula ({args.iterations:,} iterations):")
            print(f"Pi ≈ {result:.15f}")
            print(f"Error: {abs(result - math.pi):.2e}")
        elif args.nilakantha:
            result = nilakantha_series(args.iterations)
            print(f"Nilakantha Series ({args.iterations:,} iterations):")
            print(f"Pi ≈ {result:.15f}")
            print(f"Error: {abs(result - math.pi):.2e}")
        elif args.monte_carlo:
            result = monte_carlo_simulation(args.iterations)
            print(f"Monte Carlo Simulation ({args.iterations:,} samples):")
            print(f"Pi ≈ {result:.15f}")
            print(f"Error: {abs(result - math.pi):.2e}")
        elif args.gauss_legendre:
            result = gauss_legendre(args.iterations)
            print(f"Gauss-Legendre Algorithm ({args.iterations} iterations):")
            print(f"Pi ≈ {result:.15f}")
            print(f"Error: {abs(result - math.pi):.2e}")
        elif args.bbp:
            result = bailey_borwein_plouffe(args.digits)
            print(f"Bailey-Borwein-Plouffe Formula ({args.digits} digits):")
            print(f"Pi ≈ {result}")
            print(f"Actual Pi: {math.pi:.{args.digits}f}")

    except KeyboardInterrupt:
        print("\n\nCalculation interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
