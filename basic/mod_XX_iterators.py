#-*- coding: utf-8 -*-
u'''
MOD 11: Iterators
'''


lst = range(5)

for item in lst:
    print item
else:
    print "Looped whole list"


# What is really happening here?


it = iter(lst)                            # Obtain an iterator
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
print it.next()


#===============================================================================
# Python Iterators
#  - Objects to loop over collections or other container objects
#    - Fast and efficient, no copies or new objects created
#  - Iterators implement method 'next'. Each time called it returns an item
#     - When no more items are available it raises a StopIteration exception
#  - Function 'iter' returns an iterator from an object
#     - Internally it calls the method '__iter__' to retrieve the iterator
#===============================================================================


# Let's implement a custom class and a custom iterator


class WorkingDaysIter(object):
    def __init__(self, working_days_instance):
        self.wd_instance = working_days_instance
        self.index = 0

    def next(self):
        if self.index >= len(self.wd_instance.wd):
            raise StopIteration
        to_return = self.wd_instance.wd[self.index]
        self.index += 1
        return to_return


class WorkindDays(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __iter__(self):
        return WorkingDaysIter(self)                               # Did I say "efficient, no copies or new objects created"?


my_working_days_instance = WorkindDays()

for workind_day in my_working_days_instance:
    print workind_day


# Let's optimise this example


class WorkindDays(object):
    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self                               # Our custom object is the container and the iterator at the same time

    def next(self):
        if self.index >= len(self.wd):
            raise StopIteration
        to_return = self.wd[self.index]
        self.index += 1
        return to_return


my_working_days_instance = WorkindDays()

for workind_day in my_working_days_instance:
    print workind_day


#===============================================================================
# - Implement iterators protocol to enhance your custom classes usage
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#iterators
#  - http://docs.python.org/2/library/stdtypes.html#iterator-types
#===============================================================================
