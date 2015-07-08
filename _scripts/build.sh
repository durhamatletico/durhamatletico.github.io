#!/bin/bash
# TODO: Use curl/wget to download the CSV.
# TODO: Get dates programatically
# Set dates for upcoming week
cat /tmp/futsal.csv | csvgrep -c 1 -r "7/13/2015|7/14/2015" | csv2json > _data/2015/summer/week.json
# Set schedule for beyond upcoming week
cat /tmp/futsal.csv | csvgrep -i -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015" | csv2json > _data/2015/summer/schedule.json
# Get previous games
cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015" | csv2json > _data/2015/summer/past.json
# Get results for processing
cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015" | csv2json > _data/2015/summer/matches.json
python _scripts/process.py
