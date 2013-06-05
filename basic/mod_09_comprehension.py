#-*- coding: utf-8 -*-
u'''
MOD 09: List and dict comprehension
'''


spam = [0, 1, 2, 3, 4]
eggs = [0, 10, 20, 30]
fooo = []

for s in spam:
    for e in eggs:
        if s > 1 and e > 1:
            fooo.append(s * e)

print fooo

# Short code, right?

spam = [0, 1, 2, 3, 4]
eggs = [10, 20, 30]
fooo = [s * e for s in spam for e in eggs if s > 1 and e > 1]
print fooo

# What about now?

fooo = [s * s for s in spam]  # This is the most basic list comprehension construction
print fooo

fooo = [s * s for s in spam if s > 1]  # We can add 'if' clauses
print fooo

spam = [1, 2, 3, 4]
eggs = [0, -1, -2, -3]
fooo = [l.upper() * (s + e) for s in spam
        for e in eggs
        for l in "SpaM aNd eGgs aNd stuFf"
        if (s + e) >= 1
        if l.islower()
        if ord(l) % 2 == 0]                 # We can add lots of 'for' and 'if' clauses
print fooo                                  # list comprehension always returns lists (not tuples or strings)


spam = [1, 2, 3, 4]
eggs = [10, 20, 30, 40]
fooo = [[s * e for s in spam] for e in eggs]  # It is possible to nest list comprehensions
print fooo


#===============================================================================
# - List comprehension is faster than standard loops (low level C optimizations)
# - However, built-in functions are still faster (see Functional and iterables tools module)
#===============================================================================


# There is also dict comprehension (2.7 or higher)

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
fooo = {s: len(s) for s in spam}  # The syntax is a merge of list comprehension and dicts
print fooo

spam = [(0, 'monday'), (1, 'tuesday'),
        (2, 'wednesday'), (3, 'thursday'),
        (4, 'friday')]
fooo = {s: idx for idx, s in spam}  # Tuple unpacking is useful here
print fooo

spam = ['monday', 'tuesday',
        'wednesday', 'thursday',
        'friday']
fooo = {s: len(s) for s in spam if s[0] in "tm"}  # Ofc, you can add more 'for' and 'if' clauses
print fooo


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#iterators
#  - http://docs.python.org/2/library/stdtypes.html#iterator-types
#  - http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
#  - http://www.python.org/dev/peps/pep-0274/
#===============================================================================
