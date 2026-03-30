# claude-git-example

A Python code analysis utility demonstrating Claude Code integration with Git workflows.

## Overview

This project provides a command-line tool for analyzing Python code files and directories. It counts lines of code, comments, and blank lines, providing detailed statistics about your codebase.

## Features

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

## Example Output

When analyzing a directory, you'll see output like:
```
Analyzing directory: .
hello.py: 120 total lines, 85 code lines, 20 comment lines, 15 blank lines
```

## Project Structure

- `hello.py` - Main utility script with file analysis functions
- `.gitignore` - Git ignore configuration for Python projects
- `README.md` - This file

## Purpose

This project serves two purposes:
1. **Practical Utility**: A functional code analysis tool for Python projects
2. **Educational Example**: Demonstrates Claude Code integration with Git workflows and best practices
