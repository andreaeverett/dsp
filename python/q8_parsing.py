#  Write a program to read the file football.csv.
# Then print the name of the team with the smallest difference in 'for' and 'against' goals.

import csv

football_scores = csv.DictReader(open('football.csv'))

mindifference = None
city = None
for teamstats in football_scores:
    goaldifferential = abs(int(teamstats['Goals']) - int(teamstats['Goals Allowed']))
    if mindifference == None or mindifference > goaldifferential:
        mindifference = goaldifferential
        city = teamstats['Team']

print city

# I have several questions after trying several methods to get this to work:

# Question 1: Why do I need to say 'import csv' here, instead of 'from csv import *'?
#   The latter didn't work at all, but that's the syntax I've learned for other modules.

# Question 2: Is there no need / way to close the file when using csv.DictReader?
#   I tried multiple ways and it didn't work

# Question 3: I tried this first using 'with open('football.csv') as f:', and then
#   opening the file as above.  I wrote an initial 'for' loop, then wanted to move
#   on to a different 'for' loop, and the program would do nothing at all after
#   the initial one.  Is this standard when reading data from files?
#   I would love to know what I am missing here.  Here's what I tried initially:

# goaldifferentials = []
# for teamstats in football_scores:
#    teamstats['Goal Differential'] = int(teamstats['Goals']) - int(teamstats['Goals Allowed'])
#    goaldifferentials.append(abs(teamstats['Goal Differential']))
#    mindifference = min(goaldifferentials)

# for teamstats in football_scores:
#   if abs(teamstats['Goal Differential']) == mindifference:
#       print teamstats['Team']
