#/bin/sh

year=2022
day="$1"
dir="$year/day_$day"

[ -d "$dir" ] && echo 'Folder already exists' && exit 1

mkdir "$dir"
touch "$dir/test_input"
touch "$dir/input"
echo '#!/bin/python3' > "$dir/main.py"
chmod u+x "$dir/main.py"
