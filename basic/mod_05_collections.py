#-*- coding: utf-8 -*-
u'''
MOD 05: Collections
'''


# Let's start with lists

spam = ["eggs", 7.12345]  # This is a list, a comma-separated sequence of values between square brackets
print spam

print type(spam)

eggs = [spam,
        1.2345,
        "fooo"]           # No problem with multi-line declaration
print eggs

#===============================================================================
# - You can mix all kind of types inside a list
#    - Even other lists, of course
#===============================================================================

spam = ["eggs"]  # Actually just square brackets is enough to declare a list
print spam

spam = []  # And this is an empty list
print spam


# What about tuples?

spam = ("eggs", 7.12345)  # This is a tuple, a comma-separated sequence of values between parentheses
print spam

print type(spam)

eggs = (spam,
        1.2345,
        "fooo")           # Again, no problem with multiline declaration
print eggs

#===============================================================================
# - Again, you can mix all kind of types inside a tuple
#===============================================================================

spam = ("eggs", )  # Single item tuple requires the comma
print spam

spam = "eggs",  # Actually, it is enough with the comma
print spam

spam = "eggs", 7.12345  # This is called tuple packing
print spam

val1, val2 = spam  # And this is the opposite, tuple unpacking
print val1
print val2


# What about both together?

spam = "spam"
eggs = "eggs"
eggs, spam = spam, eggs
print spam
print eggs


#===============================================================================
# - Use packing and unpacking to generate new tuples, extract its content or swap values
#===============================================================================


spam = ()  # This is an empty tuple, the only tuple declaration where parentheses are required
print spam


# Let's go back to lists

spam = ["eggs", 7.12345]
val1, val2 = spam         # Unpacking also works with lists (but packing always generates tuples)
print val1
print val2


# And what about strings? Remember they are sequences too...

spam = "spam"
s, p, a, m = spam  # Unpacking even works with strings
print s
print p
print a
print m

#===============================================================================
# - str and unicode are also sequences
#===============================================================================


#===============================================================================
# Python ordered sequence types (arrays in other languages, not linked lists):
#  - They are arrays, not linked lists, so they have constant O(1) time for index access
#  - list:
#     - Comma-separated with square brackets
#     - Mutable
#     - Kind of dynamic array implementation (reserve space in advanced)
#         - Resizing is O(n)
#         - Arbitrary insertion is O(n)
#         - Appending is amortized O(1)
#  - tuple:
#     - Comma-separated with parentheses
#     - Parentheses only required in empty tuple
#     - Immutable
#     - Slightly better traversing performance than lists
#  - str and unicode:
#     - One or three single or double quotes
#     - They have special methods
#     - Immutable
#
#  - Standard library also provides other built-in collection formats:
#     - set and frozenset: unordered, without repeated values (content must be hashable)
#        - High performant in operations like intersection, union, difference, membership check
#     - bytearray, buffer, xrange: special sequences for concrete use cases
#     - collections module, with deque, namedtuple, Counter, OrderedDict and defaultdict
#===============================================================================


# Let's a play a bit with sequences operations


spam = ["1st", "2nd", "3rd", "4th", "5th"]
eggs = (spam, 1.2345, "fooo")

print "eggs" in spam
print "fooo" not in eggs
print "am" in "spam"      # Check items membership
print "spam".find("am")   # NOT recommended for membership

print spam.count("1st")   # Count repetitions (slow)

print spam + spam
print eggs + eggs
print "spam" + "eggs"  # Concatenation (shallow copy), must be of the same type

print spam * 5
print eggs * 3
print "spam" * 3  # Also "multiply" creating shallow copies concatenated

print len(spam)
print len(eggs)
print len("spam")  # Obtain its length


# Let's obtain min and max values (slow)
print min([5, 6, 2])
print max("xyzw abcd XYZW ABCD")


# Let's see how indexing works
spam = ["1st", "2nd", "3rd", "4th", "5th"]
eggs = (spam, 1.2345, "fooo")

print spam[0]
print eggs[1]
print "spam"[2]  # Access by index, starting from 0 to length - 1, may raise an exception

print spam[-1]
print eggs[-2]
print "spam"[-3]  # Access by index, even negative

print eggs[0]
print eggs[0][0]
print eggs[0][0][-1]  # Concatenate index accesses


# Let's see how slicing works
spam = ("1st", "2nd", "3rd", "4th", "5th")
print spam[1:3]                             # Use colon and a second index for slicing
print type(spam[1:4])                       # It generates a brand new object (shallow copy)


#===============================================================================
# WARNING! Slicing is syntactic sugar, but it may be harmful
#     - It creates a new object looping over the whole original collection, so
#       it may be slow
#     - It creates a shallow copy (i.e. it reuses objects inside original list),
#       which can be problematic with mutables. Check "Mutables vs. immutables
#       module" in the Intermediate block.
#===============================================================================


spam = ["1st", "2nd", "3rd", "4th", "5th"]
print spam[:3]
print spam[1:7]
print spam[-2:7]                            # Negative indexes are also valid
print spam[3:-2]

print spam[:]                               # Without indexes it performs a shallow copy

print spam[1:7:2]                           # Use another colon and a third int to specify the step

print spam[::2]
print spam[::-2]                             # A negative step traverse the sequence in the other way

print spam[::-1]                             # Useful to reverse a sequence


#===============================================================================
# - In slicing Python is able to cleverly set the indexes
#     - No IndexError when slicing index is out of range
#     - First (0) and last (-1) index is automatically filled
#     - Step is 1 by default and does not need to be multiple of sequence length
#===============================================================================


# Let's try something different

spam = ["1st", "2nd", "3rd", "4th", "5th"]
spam[3] = 1
print spam                                  # Index direct modification, may raise an exception


#===============================================================================
# - lists and bytearray are mutable sequences, so they allow in place modifications
#===============================================================================

# Let's see more modification operations

spam = [1, 2, 3, 4, 5]
eggs = ['a', 'b', 'c']
spam[1:3] = eggs
print spam              # We can use slicing here too!

spam = [1, 2, 3, 4, 5, 6, 7, 8]
eggs = ['a', 'b', 'c']
spam[1:7:2] = eggs
print spam                       # We can use even slicing with step!!

spam = [1, 2, 3, 4, 5]
spam.append("a")
print spam              # We can append an element at the end (amortized O(1))

spam = [1, 2, 3, 4, 5]
eggs = ['a', 'b', 'c']
spam.extend(eggs)
print spam              # We can append another sequence elements at the end (amortized O(1))

spam = [1, 2, 3, 4, 5]
eggs = ['a', 'b', 'c']
spam.append(eggs)
print spam              # Take care to not mix both commands!!

spam = [1, 2, 3, 4, 5]
spam.insert(3, "a")
print spam              # The same like spam[3:3] = ["a"]

spam = [1, 2, 3, 4, 5]
print spam.pop()
print spam              # Pop (remove and return) last item
print spam.pop(2)
print spam              # Pop (remove and return) given item

spam = [1, 2, 3, 4, 5]
del spam[3]
print spam              # Delete an item

spam = tuple([1, 2, 3, 4, 5, 6, 7, 8])
eggs = list(('a', 'b', 'c'))            # Shallow copy constructors
print spam
print eggs


#===============================================================================
# EXERCISE:
# - How would you work with a list to emulate a LIFO stack?
# - Would it be efficient?
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
#  - http://docs.python.org/2/tutorial/introduction.html#lists
#  - http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences
#  - http://wiki.python.org/moin/TimeComplexity
#  - http://docs.python.org/2/tutorial/datastructures.html#sets
#  - http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
#===============================================================================
