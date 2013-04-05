#-*- coding: utf-8 -*-
u'''
MOD 06: Dictionaries
'''

# Let's play with dicts


spam = {"one": 1, "two": 2, "three": 3}  # This is a dictionary
print spam

print type(spam)

eggs = {1: "one",
        2: "two",
        3: "three"}  # Again, no problem with multiline declaration
print eggs


# Still more ways to declare dictionaries

spam = dict(one=1, two=2, three=3)  # Use keyword arguments (we will talk about them in short)
print spam

eggs = dict([(1, "one"), (2, "two"), (3, "three")])  # Sequence of two elements sequences (key and object)
print eggs                                           # Note that these tuples require the parentheses just to group

spam = dict(eggs)  # Shallow copy constructor
print spam


#===============================================================================
# Python mappings
#  - dict:
#     - Comma-separated list of hashable key, colon and arbitrary object between curly brackets
#     - Mutable
#     - Unordered
#     - Access by key
#     - Heavily optimized:
#         - Creation with n items is O(n)
#         - Arbitrary access is O(1)
#         - Adding a new key is amortized O(1)
#  - dictview:
#     - Dynamic subset of a dictionary data which is kept updated
#     - Improved in Py3k (specially items, keys and values methods)
#===============================================================================


# Let's play a bit with dictionaries

spam = {"one": 1, "two": 2, "three": 3}
print spam["two"]                        # Access by key, may raise an exception

spam = {"one": 1, "two": 2, "three": 3}
print "two" in spam                      # Check keys membership
print 2 not in spam                      # Check keys membership

spam = {"one": 1, "two": 2, "three": 3}
print spam.get("two")
print spam.get("four")
print spam.get("four", 4)                # Safer access by key, never raises an exception, optional default value

spam = {"one": 1, "two": 2, "three": 3}
print spam.keys()                        # Retrieve keys list (copy) in arbitrary order
print spam.values()                      # Retrieve values list (copy) in arbitrary order
print spam.items()                       # Retrieve key, values pairs list (copy) in arbitrary order


# Let's play a bit with inplace modifications of dicts content

spam = {"one": 1, "two": 2, "three": 3}
spam["two"] = 22                         # Set or replace a key value
spam["four"] = 44                        # Set or replace a key value
print spam

spam = {"one": 1, "two": 2, "three": 3}
print spam.popitem()
print spam

spam = {"one": 1, "two": 2, "three": 3}
print spam.pop("two")                    # Pop (remove and return) given item, may raise an exception
print spam.pop("four", 4)                # Pop (remove and return) given item with optional default value
print spam

spam = {"one": 1, "two": 2, "three": 3}
eggs = {"three": 33, "four": 44}
spam.update(eggs)                        # Update dictionary with other dict content
print spam

spam = {"one": 1, "two": 2, "three": 3}
eggs = {1: "one", 2: "two", 3: "three"}
spam.update(two=22, four=44)             # Like dict constructor, it accepts keyword arguments
eggs.update([(0, "ZERO"), (1, "ONE")])   # Like dict constructor, it accepts a sequence of pairs
print spam
print eggs


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#mapping-types-dict
#  - http://stackoverflow.com/a/1419324
#  - http://wiki.python.org/moin/TimeComplexity
#===============================================================================
