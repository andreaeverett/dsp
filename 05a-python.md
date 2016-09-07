# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are indexed (ordered) sequences of values.  They can be used in many of the same situations, but lists are mutable whereas tuples are immutable (that is, you can change the value of an element within a list, but not for an element in a tuple).  Because of this difference, only tuples are suitable to serve as keys in dictionaries.  The reason is that dictionaries store and look up their key-value pairs through the use of hash functions, which will become confused and may make mistakes in storing the dictionary items if the values they are using to do so change between one point in time and another.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are like lists in that they are collections of values.  However, sets are immutable and they contain only unique elements (no duplicate entries).  Sets are also unordered whereas lists are indexed.  Sets are suitable for identifying distinct items from a list, and they are also faster for finding a specific item than lists.  With lists, you have to check each element in the list against the potential list member, whereas sets use hash functions and hash tables.  My understanding of how a hash function / hash table works is very elementary, but I believe the idea here is this: take a potential member of a set, run it through the hash function, get an output, and then use that output to see if the potential set member matches any known member of the set that returns the same output when put through the hash function.  Compared with lists, this reduces (perhaps dramatically) the number of comparisons that need to be made in order to determine if a potential set member is indeed in the set.   

**Examples**  
*First use a list to count how often a given item shows up:*  
*Note: Sorry about the function, I couldn't figure out how to get markdown to show my indentations.*

letters = ['a', 'b', 'c', 'i', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'i']  
def count_letters(list):  
  count = 0   
  for letter in letters:  
    if letter == 'i':  
      count += 1  
  return count  

print count_letters(letters)  

*Next use a set to determine whether an item is there:*

letters_set = set(letters)  
print 'i' in letters_set  



---


###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a statement that is typically used to create simple functions that will be used only once.  Because they won’t be called repeatedly, these functions don’t receive names (they are anonymous).  Here is a simple example that helps to sort a list of characters in backwards alphabetical order:  

>>> list = ['d', 'z', 'x', 'f', 'b', 'l']  
>>> backwards_list = sorted(list, key = lambda(i): i, reverse = True)  
>>> backwards_list  
	['z', 'x', 'l', 'f', 'd', 'b']  

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





