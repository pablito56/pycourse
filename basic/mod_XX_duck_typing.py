#-*- coding: utf-8 -*-
u'''
MOD XX: Duck typing
'''


# Check this

spam = [0, 1, 2, 3, 4]
print spam[3]

eggs = {"zero": 0, "one": 1, "two": 2}
print eggs["one"]

print spam["one"]  # Uuuups


def my_sum(x, y):
    return x + y

print my_sum(2, 3)

print my_sum("spam", "eggs")

print my_sum("spam", 3)  # Uuuups


def my_mul(x, y):
    return x * y

print my_mul(2, 3)

print my_mul("spam", 3)

print my_mul("spam", "eggs")  # Uuuups


# A less abstract example

class Duck(object):
    def __init__(self, name):
        self.name = name

    def quack(self):
        print self.name, "quack"

    def swim(self):
        print self.name, "swim"


def let_duck_swim_and_quack(d):
    if type(d) == Duck:
        d.swim()
        d.quack()
    else:
        raise TypeError

donald = Duck("Donald Duck")

let_duck_swim_and_quack(donald)


# Ok, but...

class Mallard(Duck):
    pass

advice_mallard = Mallard("Advice Mallard")

let_duck_swim_and_quack(advice_mallard)  # But... it is a duck!


# Let's try again

def let_duck_swim_and_quack(d):
    d.swim()
    d.quack()

let_duck_swim_and_quack(advice_mallard)

let_duck_swim_and_quack(donald)


# And there is still more

class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print self.name, "swim"

nemo = Fish("Nemo")

let_duck_swim_and_quack(nemo)  # Sorry Nemo, you are not a duck


# This is duck typing, and it is everywhere although you did not notice it


#===============================================================================
# Duck typing:
#
#     When I see a bird that walks like a duck and swims like a duck and quacks
#     like a duck, I call that bird a duck.
#
#===============================================================================


# In other words


#===============================================================================
# Duck typing:
#
#     You have to worry and care about the methods and attributes of an used object,
#     rather than about its exact type
#
# - You make your code more extendable, portable, reusable, mantenible...
# - It requires testing, ofc
# - Typical approach: treat your system as black box and only check inputs and outputs
#===============================================================================


# Here we also applied another Pythonic principle


#===============================================================================
# EAFP:
#
#     It is Easier to Ask for Forgiveness than Permission
#
#===============================================================================


# Compare

def let_duck_swim_and_quack(d):
    if hasattr(d, "swim") and hasattr(d, "quack"):
        d.swim()
        d.quack()
    else:
        print "It does not look like a duck"
        raise AttributeError

def let_duck_swim_and_quack(d):
    try:
        d.swim()
        d.quack()
    except AttributeError:
        print "It does not look like a duck"
        raise

#===============================================================================
# EAFP:
#     - In positive cases try / except is faster than if / else
#     - More understandable
#     - You don't have to know all cases to check
#===============================================================================


# However... there is always THAT case

def get_three_keys_value(d):
    it = iter(d)
    try:
        key1 = it.next()
        key2 = it.next()
        key3 = it.next()
        return d[key1], d[key2], d[key3]
    except (StopIteration, KeyError, IndexError):
        return None

eggs = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}
print get_three_keys_value(eggs)

spam = [0, 1, 2, 3, 4]
print get_three_keys_value(spam)  # Uuuups


def multi_upper(texts):
    return map(str.upper, texts)

spam = ['zero', 'one', 'two', 'three', 'four']
print multi_upper(spam)

eggs = "eggs"
print multi_upper(eggs)  # Uuuups


# Sadly, in some cases you may need type checking


def multi_upper(texts):
    if isinstance(texts, basestring):  # basestring is the superclass of str and unicode
        texts = [texts]
    return map(str.upper, texts)

print multi_upper(spam)
print multi_upper(eggs)


def get_three_keys_value(d):
    if isinstance(d, (tuple, list)):  # You can provide several types inside a tuple
        return None
    it = iter(d)
    try:
        key1 = it.next()
        key2 = it.next()
        key3 = it.next()
        return d[key1], d[key2], d[key3]
    except (StopIteration, KeyError, IndexError):
        return None

eggs = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}
print get_three_keys_value(eggs)

spam = [0, 1, 2, 3, 4]
print get_three_keys_value(spam)


print isinstance(advice_mallard, Duck)  # You can provide also classes instead of types

#===============================================================================
# - Use 'isinstance' to efficiently check objects type
# - Provide one or several (in a tuple) types or classes
#    - It supports subclassing!
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://en.wikipedia.org/wiki/Duck_typing
#  - http://pyvideo.org/video/650/permission-or-forgiveness
#  - http://docs.python.org/2/library/functions.html#isinstance
#===============================================================================
