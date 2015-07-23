# durhamatletico.com
Website for durhamatletico.com

## Updating the schedule

### Dependencies

First, install the dependencies:

- `npm install -g csv2json`
- `pip install --user csvkit`

If you're on a Mac, you'll want to add `export PATH=$HOME/Library/Python/2.7/bin:$PATH` to your `~/.bashrc`. If on Linux it will be `export PATH=$HOME/.local/bin:$PATH`.

Check if `which csv2json` and `which csvgrep` both work.

### Update the build script

Yes, the build script is a little hacky. Sorry. You'll need to edit the `_scripts/build.sh` file.

Edit all the lines that start with `cat`. This example is for the week of games on `8/3/2015|8/4/2015`

1. `cat /tmp/futsal.csv | csvgrep -c 1 -r "7/27/2015|7/28/2015" | csv2json > _data/2015/summer/week.json` becomes `cat /tmp/futsal.csv | csvgrep -c 1 -r "8/3/2015|8/4/2015" | csv2json > _data/2015/summer/week.json`
2. `cat /tmp/futsal.csv | csvgrep -i -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/2015" | csv2json > _data/2015/summer/schedule.json` becomes `cat /tmp/futsal.csv | csvgrep -i -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/2015|7/27/2015|7/28/2015" | csv2json > _data/2015/summer/schedule.json`
3. `cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/201" | csv2json > _data/2015/summer/past.json` becomes `cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/201|7/27/2015|7/28/2015" | csv2json > _data/2015/summer/past.json`
4. `cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/201" | csv2json > _data/2015/summer/matches.json` becomes `cat /tmp/futsal.csv | csvgrep -c 1 -r "6/15/2015|6/16/2015|6/22/2015|6/23/2015|6/29/2015|6/30/2015|7/6/2015|7/7/2015|7/9/2015|7/13/2015|7/14/2015|7/20/2015|7/21/201|7/27/2015|7/28/2015" | csv2json > _data/2015/summer/matches.json`

Update the `index.html` file and change the H2 to reference the upcoming dates. e.g. `<h2>Matches for July 27-28</h2>` becomes `<h2>Matches for August 3-4</h2>`.

### Download the CSV

Go to https://docs.google.com/spreadsheets/d/1VnXQQHZ7ZBemXg2ab5EZ9ZYYf_NhJwxwSk8pkQhpbvQ/edit#gid=1967459852 and click File > Download as > CSV. Save that CSV to `/tmp/futsal.csv`.

### Run the build script

In the root of the repo, run `./_scripts/build.sh`

Do a `git diff` for a quick sanity check. Then `git add .` followed by `git commit` and `git push origin master`.
