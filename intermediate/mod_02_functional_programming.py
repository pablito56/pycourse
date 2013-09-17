#-*- coding: utf-8 -*-
u'''
MOD 02: Functional programming and iterables tools
'''

#===============================================================================
# - Standard library provides low level heavily optimized functions for functional
#   programming and iterables and sequences manipulation tools
# - Small introduction to functional programming in:
#   http://docs.python.org/2/howto/functional.html
#===============================================================================


# Let's start with filter


spam_eggs = "sPaM EggS"
print str.isupper
print filter(str.isupper, spam_eggs)  # filter returns elements evaluated as True by first argument


eggs = (1, 2, 3, None, 5, 6, None, 8)
print filter(None, eggs)               # If first argument is None the identity funtion is used


def my_filering_func(input):
    return input % 2 == 0

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print filter(my_filering_func, spam)  # You can provide your own functions


#==============================================================================
# filter
#     - If iterable is tuple or string, it returns an object of the same type
#     - http://docs.python.org/2/library/functions.html#filter
#==============================================================================


# It's time to use lambda


spam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print filter(lambda x: x % 2 == 0, spam)  # lambda keyword is used to create one-liner simple anonymous functions


def get_power(y):
    return lambda x: x ** y

cube = get_power(3)
print cube(2)
print cube(3)

#==============================================================================
# lambda
#     - Typically lambda expressions are only used as input argument or return value of functions
#     - http://docs.python.org/2/tutorial/controlflow.html#lambda-forms
#     - http://docs.python.org/2/reference/expressions.html#lambda
#==============================================================================


# Let's continue with map

spam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print map(lambda x: x ** 2, spam)   # map applies the first argument function to all elements of iterable


spam_eggs = "sPaM EggS"
print map(str.upper, spam_eggs)  # map always returns a list


eggs = (1, 2, 3, None, 5, 6, None, 8)
print map(None, eggs)


print map(lambda x, y: x * y, spam_eggs, spam)  # map can accept several iterables


print map(lambda x, y: (y, x), "spam", spam)  # map adds None in case one iterable has less elements


#==============================================================================
# map
#     - http://docs.python.org/2/library/functions.html#map
#==============================================================================


# Let's check reduce

spam = [1, 2, 3]
print reduce(lambda x, y: x + y, spam)   # reduce applies consecutively the function to each element of iterable

spam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print reduce(lambda x, y: x + y, spam)   # reduce accumulates the result of each iteration

spam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print reduce(lambda x, y: x + y, spam, 1000)   # Optionally reduce accepts an initializer as initial accumulated value


#==============================================================================
# reduce
#    - http://docs.python.org/2/library/functions.html#reduce
#==============================================================================


# Let's continue with any and all

spam = [1, 2, 3, 4, 5]
print any(spam)

spam = [0, 1, 2, 3, 4, 5]
print any(spam)

spam = [None, 1, 2, 3, 4, 5]
print any(spam)

spam = []
print any(spam)


#===============================================================================
# any
#     - Return True if any element of the iterable is true. If the iterable is empty, return False.
#     - http://docs.python.org/2/library/functions.html#any
#===============================================================================


spam = [1, 2, 3, 4, 5]
print all(spam)

spam = [0, 1, 2, 3, 4, 5]
print all(spam)

spam = [None, 1, 2, 3, 4, 5]
print all(spam)

spam = []
print all(spam)


#===============================================================================
# all
#     - Return True if all elements of the iterable are true (or if the iterable is empty).
#     - http://docs.python.org/2/library/functions.html#all
#===============================================================================


# enumerate

spam = "spam"
print list(enumerate(spam))  # Return an iterator of pairs (number, element) for elements in the iterable

spam = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
print list(enumerate(spam, 1))  # Optionally you can specify the first number

num = 0
spam = "spam"
for num, item in enumerate(spam, 1):     # Useful in for loops
    print item, "at index", num - 1

print "Number of items processed:", num

#==============================================================================
# enumerate
#    - http://docs.python.org/2/library/functions.html#enumerate
#==============================================================================


# zip

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
eggs = [1, 2, 3, 4, 5]
fooo = ("MO", "TU", "WD",
        "TH", "FR")
print zip(spam, eggs, fooo)  # Return a list of tuples taking one element of each iterable at the same time

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
eggs = [0, 1, 2, 3, 4,
        5, 6, 7, 8, 9]
fooo = ("MO", "TU", "WD")
print zip(spam, eggs, fooo)  # The resulting list is as long as the shortest input iterable

#==============================================================================
# zip
#    - http://docs.python.org/2/library/functions.html#zip
#==============================================================================


# sum

spam = [1, 2, 3, 4, 5]
print sum(spam)         # No explanation needed

print sum(spam, 100)    # Optional second argument with initial sum value

spam = [1.5, 2.5, 3.5, 4.5, 5.5]
print sum(spam)         # Not good performance with floating point. Check the documentation!

#==============================================================================
# sum
#    - http://docs.python.org/2/library/functions.html#sum
#==============================================================================


# range

print range(10)          # Returns a list of numbers lower than provided value

print range(1, 10)       # By default first number is 0, but you may specify it

print range(0, 10, 2)    # You may also specify the step to increase

print range(0, -10, -2)  # You may also specify negative values

print range(0)
print range(0, 0)
print range(0, 10, -2)   # Wrong values generate an empty list

# There is also xrange

print xrange(0, 10, 2)
print list(xrange(0, 10, 2))  # It is a generator, no resources waste, no list created

#==============================================================================
# range
#    - http://docs.python.org/2/library/functions.html#range
#
# xrange
#    - http://docs.python.org/2/library/functions.html#xrange
#==============================================================================


# sorted

spam = [2, 3, 1, 5, 4]
print sorted(spam)                                    # Returns a new list with iterable content sorted

spam = [2, 3, 1, 5, 4]
print sorted(spam, reverse=True)                      # Set reverse=True to get decremental sorting

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
print sorted(spam, key=lambda x: len(x))              # You may provide a function to return a weight or comparison key

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
print sorted(spam, cmp=lambda x, y: len(x) - len(y))  # Alternatively you may provide a function to compare pairs of elements

#==============================================================================
# sorted
#    - sorted applies high performance timsort, an hybrid of merge sort and insertion sort
#        - Worst case performance: O(n log n)
#        - Best case performance: O(n)
#        - Average case performance: O(n log n)
#        - Worst case space complexity O(n)
#    - http://docs.python.org/2/library/functions.html#range
#==============================================================================


# reversed

spam = [2, 3, 1, 5, 4]
print reversed(spam)    # Returns an iterator. Only works with sequences, collections which have index access
print list(reversed(spam))

#===============================================================================
# reversed
#     - http://docs.python.org/2/library/functions.html#reversed
#===============================================================================


##===============================================================================
##===============================================================================
## TIME TO PRACTICE!
##
## EXERCISE MOD 02:
## - Using functional and sequences manipulation     tools implement the required functions
##
## INSTRUCTIONS:
## - Go to exercises/mod_02_functional_programming and edit exercise.py
## - Change the functions and class implementation to let tests.py pass
## - Check tests executing 'nosetests -sv' or 'python tests.py -v'
##===============================================================================
##===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/howto/functional.html
#  - http://docs.python.org/2/tutorial/datastructures.html#functional-programming-tools
#  - http://docs.python.org/2/library/functions.html#filter
#  - http://docs.python.org/2/tutorial/controlflow.html#lambda-forms
#  - http://docs.python.org/2/reference/expressions.html#lambda
#  - http://docs.python.org/2/library/functions.html#map
#  - http://docs.python.org/2/library/functions.html#reduce
#  - http://docs.python.org/2/library/functions.html#all
#  - http://docs.python.org/2/library/functions.html#any
#  - http://docs.python.org/2/library/functions.html#enumerate
#  - http://docs.python.org/2/library/functions.html#zip
#  - http://docs.python.org/2/library/functions.html#sum
#  - http://docs.python.org/2/library/functions.html#range
#  - http://docs.python.org/2/library/functions.html#sorted
#  - http://en.wikipedia.org/wiki/Timsort
#===============================================================================
