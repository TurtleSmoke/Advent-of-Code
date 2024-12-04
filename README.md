# :christmas_tree: Advent of Code :christmas_tree:

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/TurtleSmoke/Advent-of-Code/actions/workflows/ruff.yml/badge.svg?branch=main)](https://github.com/TurtleSmoke/leetcode/actions/workflows/ruff.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/TurtleSmoke/Advent-of-Code)
![Github last commit](https://img.shields.io/github/last-commit/TurtleSmoke/Advent-of-Code)

This repository contains my solutions to the [Advent of Code](https://adventofcode.com/) puzzles. Each folder contains
all the Python solutions for a given year, and each file contains the solution for a given day.

## About Advent of Code

Advent of Code is an Advent calendar of small programming puzzles that has been running since 2015. The puzzles are
released daily, and each puzzle is unlocked after the previous one is solved. The puzzles are designed to be solved in
any programming language.

## Purpose

I'm using this repository to have fun using python syntax and learn new and interesting way of solving problems. If you
are not afraid of oneliners and/or pythonic code, you are welcome to have a look at the code.

## Usage

### Prerequisites

The project uses [uv](https://docs.astral.sh/uv/) to manage dependencies and virtual environments, but you can also use
pip or your global python installation if you have the packages listed in `pyproject.toml` installed. To install the
project packages, run:

```bash
uv sync
```

### Run solutions

Before running the solution, you must add your input in the correct folder with the name `input`.

While being in a python env, you can run each day's solution with `./main.py` directly from the day's folder. Otherwise,
use `uv run main.py`.

### New day

To generate the directory for the current day, save your session cookie in the `session_cookie` file and run
`./generate.py dd`.

### CI

The project uses ruff for linting and formating the code. You can use `ruff format` to format and `ruff check` to lint

## License

The contents of this repository are covered under the [MIT License](LICENSE).
