#!/bin/bash
# TODO: Use curl/wget to download the CSV.
# TODO: Get dates programatically
cat /tmp/futsal.csv | csvgrep -c 1 -r "6/22/2015|6/23/2015" | csv2json > _data/2015/summer/week.json
cat /tmp/futsal.csv | csvgrep -i -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015" | csv2json > _data/2015/summer/schedule.json
cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015" | csv2json > _data/2015/summer/matches.json
python _scripts/process.py
