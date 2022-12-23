# :christmas_tree: Advent of Code :christmas_tree:

[![Lint](https://github.com/TurtleSmoke/Advent-of-Code/actions/workflows/lint.yml/badge.svg)](https://github.com/TurtleSmoke/Advent-of-Code/actions/workflows/lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/TurtleSmoke/Advent-of-Code)
![Github last commit](https://img.shields.io/github/last-commit/TurtleSmoke/Advent-of-Code)

This repository contains my solutions to the [Advent of Code](https://adventofcode.com/)
puzzles. Each folder contains all the Python solutions for a given year, and
each file contains the solution for a given day.

## About Advent of Code

Advent of Code is an Advent calendar of small programming puzzles that has
been running since 2015. The puzzles are released daily, and each puzzle
is unlocked after the previous one is solved. The puzzles are designed to be
solved in any programming language.

## Purpose

I'm using this repository to have fun using python syntax and learn new and
interesting way of solving problems. If you are not afraid of oneliners
and/or pythonic code, you are welcome to have a look at the code.

## Usage

### Prerequisites

The project uses poetry to manage dependencies and virtual environments, but
you can also use pip or your global python installation if you have the
packages listed in `pyproject.toml` installed. To install the project
packages, run:

```bash
poetry install
```

### Run solutions

Before running the solution, you must add your input in the correct folder with
the name `input`.

While being in a python env, you can run each day's solution with `./main.py`
directly from the day's folder. Otherwise, use `python main.py`.

### New day

To generate the directory for the current day, save your session cookie in
the `session_cookie` file and run `./generate.py`.

### Linting

The project uses black and pylint to lint the code. To lint the code, run
`pylint path/to/file.py`. To run black, simply use `black path/to/file.py` in
the root directory.

## License

The contents of this repository are covered under the [MIT License](LICENSE).
