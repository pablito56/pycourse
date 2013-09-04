#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod 06: Iterator Tools
'''


#===============================================================================
# itertools - Functions creating iterator for efficient looping
#
#   - The module standardizs a core of set of fast, memory efficient tools that 
#       are useful themselves or in combinations
#
#===============================================================================


#===============================================================================
# Infinite iterators
#===============================================================================


# itertools.count(start, [step]) -> an infinite sequence of integer values


from itertools import *

stop_flag = 1 # it is infinite!
for i in count(10):
    print i
    stop_flag = i
    if stop_flag >= 20:
        break


# with step argument
for i in count(10, 2):
    print i
    stop_flag = i
    if stop_flag >= 20:
        break


# itertool.cycle(iterable) -> cycle an iterable infinitely
stop_flag = 0
for i in cycle('ABCD'):
    print i
    stop_flag += 1
    if stop_flag >= 12:
        break



# itertool.repetat(iterable, n) -> cycle an iterable a number of times
for i in repeat('ABCD', 3):
    print i


#===============================================================================
# Merging and Splitting Iterators:
#===============================================================================

# itertools.chain(*iterables)


for i in chain([1,2,3,4], ['a', 'b', 'c']):
    print i


# itertools.izip(*iterables) -> combines the elements of several iterators into tuples


for i in izip([1, 2, 3], ['a', 'b', 'c'], ['A', 'B', 'C']):
    print i


# itertools.islice(iterables, [start], end, step) -> returns selected items from the input iterators, by index


print 'By tens to 100:'
for i in islice(count(), 0, 100, 10):
    print i


# itertools.tee(iterable[, n=2]) -> return n independent iterators from a single iterable
r = islice(count(), 5)
i1, i2 = tee(r)

for i in i1: 
    print 'i1:', i

for i in i2: 
    print 'i2:', i


# WARNING!: since new iterators share the input ('r' iterator), you should not consume the input ('r')


#===============================================================================
# Converting Inputs
#===============================================================================


# imap(function, *iterables) - make an iterator that computes the funciton using args from each of the iterables
#                            - it stops when the shortest iterable is exhausted, instead filling with None 
#                            - it allows thus to use infinite iterators


print 'Doubles:'
for i in imap(lambda x:2*x, xrange(5)):
    print i


# using multiple arguments
print 'Multiples:'
for i in imap(lambda x,y:(x, y, x*y), xrange(5), xrange(5,10)):
    print '%d * %d = %d' % i


# starmap(function, iterable) - instead of imap, it takes only one iterable that has prezipped the input


values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x,y:(x, y, x*y), values):
    print '%d * %d = %d' % i


#===============================================================================
# Filtering Inputs
#===============================================================================

# dropwhile(predicate, iterable) -> Make an iterator that drops elements from the iterable 
#                                       as long as the predicate is true; afterwards, returns every element. 
# Note, the iterator does not produce any output until the predicate first becomes false

def should_drop(x):
    print 'Testing:', x
    return x < 1

for i in dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


# takewhile(predicate, iterable) -> The opposite to dropwhile. return items as long as predicate is true


def should_take(x):
    print 'Testing:', x
    return x < 2

for i in takewhile(should_take, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


# ifilter(predicate, sequence) -> returns an iterator that works like the built-in filter() does for lists, 
#                                  including only items for which the test function returns true. 
# ifilterfalse(predicate, sequence) -> returns only items from which the test function return false
# Note, It is different from dropwhile() in that every item is tested before it is returned.


def check_item(x):
    print 'Testing:', x
    return x < 1

for i in ifilter(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i

for i in ifilterfalse(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


#===============================================================================
# Grouping Data
#===============================================================================


# groupby(iterable[, key]) -> returns an iterator that produces sets of values grouped by a common key.


from operator import itemgetter
# taken from the docs, the example will use a new function:
# operator.itemgetter ->  - return a callable object that fetches the item from its 
#                           operand using the operand's __getitem__() method

itemgetter(1)('ABCDEFG')

itemgetter(1,3,5)('ABCDEFG')


d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.iteritems(), key=itemgetter(1))

for k, g in groupby(di, key=itemgetter(1)):
    print k, map(itemgetter(0), g)


# we could also have used a lambda function for key
df = sorted(d.iteritems(), key=lambda x: x[1])


#===============================================================================
# SOURCES:
#  - http://doughellmann.com/2007/10/pymotw-itertools.html
#  - http://docs.python.org/2/library/itertools.html
#===============================================================================
