
# Code Repeated from Part 1:

import csv
import re

faculty_members = csv.DictReader(open('faculty.csv'))

emails = []

for member in faculty_members:
    email = re.search( r'(.+)@(.+)', member[' email'])
    emails.append(email.group(1) + '@' + email.group(2))


# New Code Part 2

with open('emails.csv', 'w') as f:
    emailwriter = csv.writer(f, delimiter = '\n')
    emailwriter.writerow(emails)
