#!/bin/sh

# shellcheck disable=SC2046
black --check --diff $(git ls-files '*.py')