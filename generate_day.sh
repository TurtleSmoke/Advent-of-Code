#!/bin/sh

AOC_YEAR="${AOC_YEAR:-2022}"
AOC_DAY="$1"
AOC_SESSION=$(cat session_cookie)
dir="$AOC_YEAR/day_$AOC_DAY"

[ -d "$dir" ] && echo 'Folder already exists' && exit 1

mkdir "$dir"
touch "$dir/test_input"
curl https://adventofcode.com/"$AOC_YEAR"/day/"$AOC_DAY"/input --cookie "session=$AOC_SESSION" -o "$dir/input"
echo '#!/bin/python3' > "$dir/main.py"
chmod u+x "$dir/main.py"
