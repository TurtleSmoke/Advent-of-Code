#!/bin/sh

find "20"* -name "*.py" | xargs pylint
