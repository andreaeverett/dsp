# Code Carried Over from Part 1

import csv
import re

faculty_members = csv.DictReader(open('faculty.csv'))

# New Code Part 3
faculty_dict = {}
professor_dict = {}

for member in faculty_members:
    lastname = re.search( r'(\w*$)', member['name'])
    firstname = re.search( r'(^\w*)', member['name'])
    name_firstlast = (firstname.group(1), lastname.group(1))
    title = re.search( r'(.*Professor)', member[' title'])
    email = member[' email']
    degree = member[' degree']

# Code for Question 6: Create a dictionary that looks like: {'Lastname': ['degree', 'title', 'email']}
    try:
        faculty_dict[lastname.group(1)].append([degree, title.group(1), email])
    except KeyError:
        faculty_dict[lastname.group(1)] = [[degree, title.group(1), email]]

# Code for Question 7: Create a new dictionary with keys ('First', 'Last')
    try:
        professor_dict[name_firstlast].append(degree, title.group(1), email)
    except KeyError:
        professor_dict[name_firstlast] = [degree, title.group(1), email]

print faculty_dict
print professor_dict

# Code for Question 8: Print the dictionary key value pairs based on alphabetical
# orders of the last name of the professors

# Return a list of tuples each containing: name tuple, value list, then print them 1 by 1
alphabetical_list = sorted(professor_dict.items(), key = lambda(key): key[0][1])
for i in alphabetical_list:
    print "%s : %s" % (i[0], i[1])
