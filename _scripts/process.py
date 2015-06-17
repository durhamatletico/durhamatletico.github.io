#!/usr/bin/env python
import yaml
import json

teams = yaml.load(open("_data/2015/summer/teams.yml", 'r'))
matches = json.load(open("_data/2015/summer/matches.json", 'r'))
team_data = dict()

for team in teams:
    team_data[team] = {'points': 0, 'goals_for': 0, 'goals_against': 0, 'wins': 0, 'losses': 0, 'draws': 0, 'goal_differential': 0}
    # 1. Create points tally per team.
    # 2. Track goals for / goals against
    for match in matches:
        if team in match['Team 1']:
            team_data[team]['goals_for'] += int(match['Team 1 score'])
            team_data[team]['goals_against'] += int(match['Team 2 score'])
            if int(match['Team 1 score']) > int(match['Team 2 score']):
                team_data[team]['points'] += 3
                team_data[team]['wins'] += 1
            elif int(match['Team 1 score']) == int(match['Team 2 score']):
                team_data[team]['draws'] += 1
                team_data[team]['points'] += 1
            else:
                team_data[team]['losses'] +=1
        elif team in match['Team 2']:
            team_data[team]['goals_for'] += int(match['Team 2 score'])
            team_data[team]['goals_against'] += int(match['Team 1 score'])
            if int(match['Team 2 score']) > int(match['Team 1 score']):
                team_data[team]['points'] += 3
                team_data[team]['wins'] += 1
            elif int(match['Team 2 score']) == int(match['Team 1 score']):
                team_data[team]['points'] += 1
                team_data[team]['draws'] += 1
            else:
                team_data[team]['losses'] += 1

pprint.pprint(team_data)                
# Calculate goal differential
for team in teams:
    team_data[team]['goal_differential'] = team_data[team]['goals_for'] - team_data[team]['goals_against']

# Sort the data
unsorted_data = list()
for key, data in team_data.iteritems():
    data['team'] = key
    unsorted_data.append(data)

from operator import itemgetter
sorted_data = sorted(unsorted_data, key=itemgetter('points', 'goal_differential'), reverse=True)

# Output new YAML document for processing by Jekyll
output = yaml.dump(sorted_data)
with open('_data/2015/summer/results.yml', 'w') as outfile:
    outfile.write(yaml.dump(sorted_data, default_flow_style=True) )
