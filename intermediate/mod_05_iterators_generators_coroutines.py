#-*- coding: utf-8 -*-
u'''
MOD 05: Iterators, generators and coroutines
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
#        - And it is not possible to restart the iteration
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
# - Used to operate with I/O, with big amounts of data (e.g. DB queries)...
#===============================================================================


# Let's play a bit with iterators protocol of objects data model


# Let's implement a custom iterator
class WorkingDaysIterator(object):
    def __init__(self, working_days_instance):
        self.wd_instance = working_days_instance
        self.index = 0

    def next(self):
        if self.index >= len(self.wd_instance.wd):
            raise StopIteration
        to_return = self.wd_instance.wd[self.index]
        self.index += 1
        return to_return


# Let's implement a custom generator
class WorkindDaysGenerator(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __iter__(self):
        return WorkingDaysIterator(self)  # Did I say iterators are "efficient, no copies or new objects created"?


my_working_days_instance = WorkindDaysGenerator()

for workind_day in my_working_days_instance:
    print workind_day


# Let's optimise this example using only one class. Any idea?


class WorkindDaysGenerator(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self      # Our custom object is the container and the iterator at the same time

    def next(self):
        if self.index >= len(self.wd):
            raise StopIteration
        to_return = self.wd[self.index]
        self.index += 1
        return to_return


my_working_days_instance = WorkindDaysGenerator()

for workind_day in my_working_days_instance:
    print workind_day


# However, in this case the most efficient implementation is...

class WorkindDaysGenerator(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __iter__(self):
        return iter(self.wd)  # This is the most efficient implementation


my_working_days_instance = WorkindDaysGenerator()

for workind_day in my_working_days_instance:
    print workind_day


#===============================================================================
# More info on iterators protocol:
# - http://docs.python.org/2/library/stdtypes.html?highlight=__iter__#iterator-types
#===============================================================================


# But there is still more


class WorkindDaysGenerator(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def iter_days(self):
        print "...called iter_days"
        for item in self.wd:
            print "...yielding", item
            yield item              # Let me introduce the 'yield' statement

    def __iter__(self):
        print "...called __iter__"
        return self.iter_days()


my_working_days_instance = WorkindDaysGenerator()

for workind_day in my_working_days_instance:
    print workind_day


# How many times is called each method?


print my_working_days_instance.iter_days()  # iter_days returns a generator


it = my_working_days_instance.iter_days()

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

# Of course it raises StopIteration when it is exhausted
print it.next()


#===============================================================================
# - yield expression can only be used in the body of a function definition
# - In such case yield makes it a generator function instead of a normal function
#===============================================================================


# Let's see another example with yield

from random import seed, randint
seed()


def random_ints(max_int):
    while max_int > 0:
        ret = randint(0, max_int)
        new_max = yield ret
        max_int -= 1
        if new_max is not None:
            max_int = new_max
            print "Yielded {}, updated to {}".format(ret, max_int)
        else:
            print "Yielded {}, decreased to {}".format(ret, max_int)


it = random_ints(3)
print it.next()
print it.next()
print it.next()

print it.next()

# Let's try again

it = random_ints(100)
print it.next()
print it.next()
print it.next()
print it.send(5)  # We can send arguments back inside the yield loop

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()


# Generator functions are quite similar to coroutines


from random import choice, seed
from string import letters, digits, whitespace


def write_random_words(f, num_words=10):
    """Write randomly generated words to given file
    """
    available_chars = letters + digits + whitespace
    for i in range(num_words):
        seed()
        word = u"".join([choice(available_chars) for l in xrange(20)])
        f.write(word + "\n")

# Let's fill a file
with open('input.txt', 'w+') as f:
    write_random_words(f)


# Let's create some generator functions


def read_stripped_file_lines(f):
    """Generator which reads lines from a file and strips them
    """
    for file_line in f:
        print "<< Retrieved line '{}'".format(file_line)
        yield file_line.strip(whitespace)


def split_lines_in_words(lines_to_split):
    """Generator which splits incoming iterator's lines into words
    """
    for line in lines_to_split:
        for word in line.split():
            yield word


def filter_words_first_upper(words_to_filter):
    """Generator which filters incoming iterator's words
        so its first letter must be uppercase
    """
    for word in words_to_filter:
        if word[0].isupper():
            yield word


def write_words_to_file(f, words):
    """Function to write incoming iterator's words as lines in a file
    """
    for out_word in words:
        print ">> Writing word '{}'\n".format(out_word)
        f.write(out_word + "\n")


# Let's use our generators


f = open('input.txt', 'r')
stripped_lines = read_stripped_file_lines(f)

words = split_lines_in_words(stripped_lines)

filtered_words = filter_words_first_upper(words)


#===============================================================================
# - Notice how nothing happened up to now
#     - So no resources were taken up to now
#===============================================================================


with open('output.txt', 'w+') as out_f:
    write_words_to_file(out_f, filtered_words)  # Real driver of all the process


f.close()


#===============================================================================
# - Use generators to create your own coroutines
#     - Save resources processing only the data you really need on each iteration
#     - Unlikely coroutines, generators do not hold the control of the process
# - This is a typical design pattern in Python
#===============================================================================


# Let's try again, but manually

f = open('input.txt', 'r')
stripped_lines = read_stripped_file_lines(f)
words = split_lines_in_words(stripped_lines)
filtered_words = filter_words_first_upper(words)  # Generators where exhausted

print filtered_words.next()

print filtered_words.next()

print filtered_words.next()

print filtered_words.next()


for word in filtered_words:
    print word


f.close()


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#iterators
#  - http://docs.python.org/2/library/stdtypes.html#iterator-types
#  - http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
#  - http://www.python.org/dev/peps/pep-0274/
#  - http://docs.python.org/2/reference/expressions.html#yieldexpr
#===============================================================================
