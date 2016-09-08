# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# 1
def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same."""
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count + 1
    print count

match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'be', 'abc', 'hello'])


# 2
def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']."""
    x_words = []
    for word in words:
        if word.startswith('x'):
            x_words.append(word)
    for word in x_words:
            words.remove(word)
    sorted_list = sorted(x_words) + sorted(words)
    print sorted_list

front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])


# 3
def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)]."""
    sorted_by_last = sorted(tuples, key = lambda(item): item[-1])
    print sorted_by_last

sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(2, 3), (1, 2), (3, 1)])
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


# 4
def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list."""
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1
    print nums

remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])


# 5
def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists."""
    merged_list = []
    merged_length = len(list1) + len(list2)
    i = 0
    j = 0
    while len(merged_list) < merged_length:
        try:
            if list1[i] <= list2[j]:
                merged_list.append(list1[i])
                i += 1
            elif list2[j] < list1[i]:
                merged_list.append(list2[j])
                j += 1
        except IndexError:
            if len(list1) == i:
                merged_list = merged_list + list2[j:]
            if len(list2) == j:
                merged_list = merged_list + list1[i:]
    print merged_list

linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
