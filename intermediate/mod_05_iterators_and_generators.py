#-*- coding: utf-8 -*-
u'''
MOD 05: Iterators and generators
'''


spam = [0, 1, 2, 3, 4]

for item in spam:
    print item
else:
    print "Looped whole list"


# What is really happening here?


it = iter(spam)                            # Obtain an iterator
try:
    item = it.next()                      # Retrieve first item through the iterator
    while True:
        # Body of the for loop goes here
        print item
        item = it.next()                  # Retrieve next item through the iterator
except StopIteration:                     # Capture iterator exception
    # Body of the else clause goes here
    print "Looped whole list"

#===============================================================================
# - Remember that for loops are really optimized at low level (C)
#===============================================================================


# Another example

spam = "spam"
it = iter(spam)

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()  # Once the StopIteration is raised an iterator is useless, there is no 'restart'

it = iter(spam)
s, p, a, m = it  # Ierators also support unpacking (you have to know the number of items to unpack)
print s
print p
print a
print m


#===============================================================================
# Python Iterators
#  - Objects to loop over collections or other container objects
#    - Fast and efficient, no copies or new objects created
#  - Iterators implement method 'next'. Each time called it returns an item
#     - When no more items are available it raises a StopIteration exception
#  - Function 'iter' returns an iterator from an object
#  - Used for reading external resources or big amounts of data (e.g. DB cursors)
#===============================================================================


# Python also has generators, the next level of simplification and optimisation


spam = [0, 1, 2, 3, 4]
fooo = (2 ** s for s in spam)  # Syntax similar to list comprehension but between parentheses
print fooo

print fooo.next()
print fooo.next()
print fooo.next()
print fooo.next()
print fooo.next()
print fooo.next()


#===============================================================================
# - Generators are a simple and powerful tool for creating iterators.
# - Each iteration is computed on demand
# - In general terms they are more efficient than list comprehension or loops
#    - If not the whole sequence is traversed
#        - When looking for a certain element
#        - When an exception is raised
#    - So they save computing power and memory
# - It is possible to create more complex generators (check Advanced block)
#  - Used to return external data or big amounts of data (e.g. DB queries)
#===============================================================================


# TODO: Add itertools explanation


# TODO: Add objects data model stuff for iterators


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#iterators
#  - http://docs.python.org/2/library/stdtypes.html#iterator-types
#  - http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
#  - http://www.python.org/dev/peps/pep-0274/
#===============================================================================
