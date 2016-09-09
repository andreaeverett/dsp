# Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
# Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
# Q3. Search for email addresses and put them in a list. Print the list of email addresses.
# Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).
#     Print the list of unique email domains.


import csv
import re

faculty_members = csv.DictReader(open('faculty.csv'))

degrees = {}
titles = {}
emails = []
domains = set()

for member in faculty_members:

# Degrees
    degree = member[' degree'].upper()
    degree = degree.replace('.', '')
    degreesearch = re.search( r'(\w*)\s?(\w*)?\s?(\w*)?\s?(\w*)?\s?(\w*)?', degree)
    i = 1
    while i < 6:
        try:
            degrees[degreesearch.group(i)] = degrees[degreesearch.group(i)] + 1
        except KeyError:
            degrees[degreesearch.group(i)] = 1
        i += 1
    del degrees['']

# Titles
# I'm not too happy with how I solved this: I looked at the options and realized
# there was an error in one entry where 'in' should have been 'of'.  To capture
# that person correctly the only other way I could find to design the search term
# was by using the fact that the titles began with 'Word Professor' or 'Professor.'
# I've included the more general way I initially tried to do it, commented out,
# below.  But that incorrectly returns four distinct titles. I'd appreciate any
# tips for how to build a better regex here.
    title = re.search( r'(\w*\sProfessor|Professor)', member[' title'])
    # title = re.search( r'(\w.+)', member[' title'])
    try:
        titles[title.group(1)] = titles[title.group(1)] + 1
    except KeyError:
        titles[title.group(1)] =  1


# Emails & email domains
    email = re.search( r'(.+)@(.+)', member[' email'])
    emails.append(email.group(1) + '@' + email.group(2))
    domains.add(email.group(2))

print "The number of unique degrees is %d" % len(degrees)
print degrees
print "The number of unique titles is %d" % len(titles)
print titles
print emails
domains = list(domains)
print "The number of unique email domains is %d" % len(domains)
print domains
