#!/usr/bin/env python3
"""
A useful utility script for file operations and git workflow demonstration.
Supports line counting, file analysis, and basic statistics.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List


def count_lines(filepath: str) -> Dict[str, int]:
    """Count lines in a file (total, code, blank, comments)."""
    total = 0
    blank = 0
    comments = 0

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                total += 1
                stripped = line.strip()
                if not stripped:
                    blank += 1
                elif stripped.startswith('#') or stripped.startswith('//'):
                    comments += 1
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    code = total - blank - comments
    return {
        'total': total,
        'code': code,
        'blank': blank,
        'comments': comments
    }


def analyze_directory(directory: str = '.') -> Dict[str, Dict[str, int]]:
    """Analyze all Python files in a directory."""
    stats = {}
    path = Path(directory)

    for py_file in path.glob('**/*.py'):
        if 'venv' not in str(py_file) and '__pycache__' not in str(py_file):
            file_stats = count_lines(str(py_file))
            if file_stats:
                stats[str(py_file)] = file_stats

    return stats


def print_stats(stats: Dict[str, Dict[str, int]]):
    """Print statistics in a formatted table."""
    if not stats:
        print("No Python files found.")
        return

    total_lines = sum(s['total'] for s in stats.values())
    total_code = sum(s['code'] for s in stats.values())

    print("\n" + "=" * 80)
    print(f"{'File':<50} {'Lines':<10} {'Code':<10} {'Blank':<10} {'Comments':<10}")
    print("=" * 80)

    for filepath, stat in stats.items():
        filename = filepath if len(filepath) < 50 else '...' + filepath[-47:]
        print(f"{filename:<50} {stat['total']:<10} {stat['code']:<10} {stat['blank']:<10} {stat['comments']:<10}")

    print("=" * 80)
    print(f"{'TOTAL':<50} {total_lines:<10} {total_code:<10}")
    print("=" * 80 + "\n")


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--analyze' or sys.argv[1] == '-a':
            directory = sys.argv[2] if len(sys.argv) > 2 else '.'
            print(f"\nAnalyzing Python files in: {directory}")
            stats = analyze_directory(directory)
            print_stats(stats)

        elif sys.argv[1] == '--file' or sys.argv[1] == '-f':
            if len(sys.argv) < 3:
                print("Usage: python hello.py --file <filepath>")
                return
            filepath = sys.argv[2]
            print(f"\nAnalyzing file: {filepath}")
            stats = count_lines(filepath)
            if stats:
                print(f"  Total lines: {stats['total']}")
                print(f"  Code lines: {stats['code']}")
                print(f"  Blank lines: {stats['blank']}")
                print(f"  Comment lines: {stats['comments']}")

        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("\nUsage: python hello.py [OPTIONS]")
            print("Options:")
            print("  -a, --analyze [dir]  Analyze all Python files in directory (default: current)")
            print("  -f, --file <file>    Analyze a specific file")
            print("  -h, --help           Show this help message")
            print("\nExample:")
            print("  python hello.py --analyze")
            print("  python hello.py --file hello.py")

        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help to see available options")

    else:
        print("Hello from claude-git-example!")
        print("This is a useful utility script for file analysis.")
        print("\nUse --help to see available features.")
        print("\nQuick demo - analyzing current directory:")
        stats = analyze_directory('.')
        print_stats(stats)


if __name__ == "__main__":
    main()
