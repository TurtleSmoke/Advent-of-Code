#!/bin/sh

# shellcheck disable=SC2046
pylint --rcfile=.pylintrc $(git ls-files '*.py')