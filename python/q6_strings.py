# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


# 1
def donuts(count):
    """Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count."""
    if count < 10:
        print 'Number of donuts: %s' % count
    else:
        print 'many'

donuts(4)
donuts(9)
donuts(10)
donuts(99)


# 2
def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string."""
    if len(s) < 2:
        print ''
    else:
        print '%s%s' % (s[0:2], s[-2:])

both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')


# 3
def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more."""
    replace_letter = s[0]
    for i in s:
        if i == replace_letter:
            s = s.replace(i, '*')
    s = s.replace('*', replace_letter, 1)
    print s

fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')


# 4
def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more."""
    start_a = a[0:2]
    end_a = a[2:]
    start_b = b[0:2]
    end_b = b[2:]
    print '%s%s %s%s' % (start_b, end_a, start_a, end_b)

mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')


# 5
def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string."""
    ing = 'ing'
    ly = 'ly'
    if len(s) >= 3 and s[-3:] != ing:
        s = s + ing
    elif len(s) >=3:
        s = s + ly
    print s

verbing('hail')
verbing('swiming')
verbing('do')


# 6
def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'"""
    good = "good"
    if 'not' in s and 'bad' in s and s.find('not') < s.find('bad'):
        pre_not = s[0:s.find('not')]
        post_bad = s[s.find('bad') + 3:]
        s = pre_not + good + post_bad
    print s

not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")


# 7
def front_back(a, b): # Sorry, I don't think this one is very pythonic! I tried to loop over a and b but couldn't get that to work.
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back"""
    if len(a) % 2 == 0:
        a_front = a[0:len(a)/2]
        a_back = a[len(a)/2:]
    else:
        a_front = a[0:len(a)/2 + 1]
        a_back = a[len(a)/2 + 1:]
    if len(b) % 2 == 0:
        b_front = b[0:len(b)/2]
        b_back = b[len(b)/2:]
    else:
        b_front = b[0:len(b)/2 + 1]
        b_back = b[len(b)/2 + 1:]
    print a_front + b_front + a_back + b_back

front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')
