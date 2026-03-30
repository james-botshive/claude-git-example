# claude-git-example

A collection of Python utilities demonstrating Claude Code integration with Git workflows.

## Overview

This project provides multiple command-line tools for various tasks:
1. **Code Analysis** - Analyze Python files and directories for code metrics
2. **Pi Calculator** - Calculate Pi using multiple mathematical algorithms

## Tools

### 1. Code Analysis Tool (`hello.py`)

Features:
- **File Analysis**: Analyze individual Python files with detailed line counting
  - Total lines
  - Code lines
  - Comment lines
  - Blank lines

- **Directory Analysis**: Recursively analyze all Python files in a directory
  - Aggregate statistics across multiple files
  - Automatic filtering of virtual environments and cache directories
  - Excludes `__pycache__`, `venv`, `.git`, and other common non-code directories

- **Command-Line Interface**: Easy-to-use CLI with multiple options
  - Interactive demo mode
  - File-specific analysis
  - Directory-wide analysis
  - Built-in help documentation

## Usage

### Run the demo (default behavior):
```bash
python hello.py
```

### Analyze a specific file:
```bash
python hello.py --file path/to/file.py
# or
python hello.py -f path/to/file.py
```

### Analyze all Python files in a directory:
```bash
python hello.py --analyze
# or
python hello.py -a

# Analyze a specific directory:
python hello.py --analyze path/to/directory
```

### Display help:
```bash
python hello.py --help
# or
python hello.py -h
```

### 2. Pi Calculator Tool (`calculate_pi.py`)

Calculate Pi using various mathematical algorithms:
- **Leibniz Formula**: Classic infinite series (slow convergence)
- **Nilakantha Series**: Faster converging infinite series
- **Monte Carlo Simulation**: Statistical method using random sampling
- **Gauss-Legendre Algorithm**: Very fast convergence (quadratic)
- **Bailey-Borwein-Plouffe (BBP)**: Can calculate nth digit directly

#### Compare all algorithms (default):
```bash
python calculate_pi.py
```

#### Use a specific algorithm:
```bash
# Leibniz formula with 10 million iterations
python calculate_pi.py --leibniz --iterations 10000000

# Monte Carlo method with 5 million samples
python calculate_pi.py --monte-carlo --iterations 5000000

# Gauss-Legendre (very fast - only 5 iterations needed)
python calculate_pi.py --gauss-legendre

# BBP formula to calculate 20 decimal places
python calculate_pi.py --bbp --digits 20
```

#### Display help:
```bash
python calculate_pi.py --help
```

## Example Output

### Code Analysis Tool:
When analyzing a directory, you'll see output like:
```
Analyzing directory: .
hello.py: 120 total lines, 85 code lines, 20 comment lines, 15 blank lines
```

### Pi Calculator Tool:
When comparing algorithms, you'll see output like:
```
Comparing Pi calculation algorithms (iterations: 100,000)
======================================================================
Algorithm                 Result               Error
======================================================================
Leibniz Formula           3.141582653589720    1.00e-05
Nilakantha Series         3.141592653589786    6.66e-15
Monte Carlo (1M samples)  3.143160000000000    1.57e-03
Gauss-Legendre (5 iter)   3.141592653589794    8.88e-16
math.pi (standard)        3.141592653589793    0.00e+00
```

## Project Structure

- `hello.py` - Code analysis utility for Python files
- `calculate_pi.py` - Pi calculator with multiple algorithms
- `.gitignore` - Git ignore configuration for Python projects
- `README.md` - This file

## Purpose

This project serves two purposes:
1. **Practical Utilities**: Functional tools for Python development including:
   - Code analysis and metrics
   - Mathematical calculations and algorithm demonstrations
2. **Educational Example**: Demonstrates Claude Code integration with Git workflows and best practices
