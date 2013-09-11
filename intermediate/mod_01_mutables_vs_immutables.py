#-*- coding: utf-8 -*-
u'''
MOD 01: mutables vs. immutables, deep copy
'''


# Let's instantiate a string and check its id, type and value
str_inst = 'abcd'
print id(str_inst)
print type(str_inst)
print str_inst


# Let's compare the ids of two bool values
bool_inst_1 = True
bool_inst_2 = True
print bool_inst_1 is bool_inst_2
print bool_inst_1 is True


#===============================================================================
# - Every object has an identity (its address up to now), a type and a value
# - Use 'id' and 'is' to retrieve or compare the id of an object
# - The interpreter may reuse values!
#===============================================================================


# Let's do the same with lists
lst_inst = []
print lst_inst is []


# WTF!? Let's try again with ints
int_inst_1 = 7
int_inst_2 = 7
print id(int_inst_1), 'vs.', id(int_inst_2)

# Ok. Let's try again with other types
none_inst = None
print id(none_inst), 'vs.', id(None)

list_inst_1 = []
list_inst_2 = []
print id(list_inst_1), 'vs.', id(list_inst_2)


#===============================================================================
# - Objects whose value can change are said to be mutable (dicts, lists)
# - Objects whose value is unchangeable once they are created are called immutable (numbers, strings, tuples)
# - Mutable types allow in-place modifications (append in a list, pop in a dictionary...)
# - Immutable types values may be reused by the interpreter (so their id is the same)
# - id is guaranteed to be unique and constant during the lifecycle of an object
# - To check the type of an object, use the builtin function isinstance
#===============================================================================


# Let's check how immutable values are reused
sevens = [7, 7, 7, 7, 7]
print map(id, sevens)
abcs = ["abc", "abc", "abc", "abc", "abc"]
print map(id, abcs)
tuples = [(), (), ()]
print map(id, tuples)
lists = [[], [], []]
print map(id, lists)


# Let's change a string value (reassign!)
str_inst = 'instance value'
print str_inst, '@', id(str_inst)
str_inst = str_inst + ' updated'
print str_inst, '@', id(str_inst)


# Let's change a list content (in-place modification!)
lst_inst = ['instance', 'value']
print lst_inst, '@', id(lst_inst)
lst_inst.append('updated')
print lst_inst, '@', id(lst_inst)


#===============================================================================
# EXERCISE:
#  - Play a bit with http://www.pythontutor.com/visualize.html to understand Python
#    binding and mutables and immutables behaviour
#===============================================================================


# Now let's play with dicts
dict1 = {(1, 2): "1, 2", (3, 4): "3, 4"}
dict2 = {[1, 2]: "1, 2", [3, 4]: "3, 4"}


#===============================================================================
# - Mutable types are not stable, so they can not be used as dict keys
#===============================================================================


#===============================================================================
# WARNING!
# - Mutable and immutable types behavior differences can lead to some common errors!!
#===============================================================================


# Multiple assignment with ints (immutable)
intA = intB = 0
print "intA:", intA, '@', id(intA)
print "intB:", intB, '@', id(intB)


# Let's modify one of the ints
intA += 1
print "intA:", intA, '@', id(intA)
print "intB:", intB, '@', id(intB)


# Ok. Multiple assignment with lists (mutable)
lstA = lstB = []
print "lstA:", lstA, '@', id(lstA)
print "lstB:", lstB, '@', id(lstB)


# Let's modify one of the lists
lstA.extend([1, 2, 3])
print "lstA:", lstA, '@', id(lstA)
print "lstB:", lstB, '@', id(lstB)


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignments
#    - The same applies with shallow copy or constructor by copy
#===============================================================================


# Use mutable types as class attributes
class MutablesClass(object):
    list_inst = []
    int_inst = 0

# Let's instantiate the class twice
inst_A = MutablesClass()
inst_B = MutablesClass()


# Let's change one of the instances and check the other instance values
inst_A.int_inst += 1
inst_A.list_inst.extend([5, 7, 9])
print "inst_B.int_inst:", inst_B.int_inst
print "inst_B.list_inst:", inst_B.list_inst
print inst_A.list_inst is inst_B.list_inst


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment
# - Class attributes
#===============================================================================


# Let's create a function which returns a modified list
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

# Let's call this function twice
result1 = add_to_list(1)
result2 = add_to_list(2)
print result1 is result2
print result1, 'vs', result2


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment
#    - The same applies with shallow copy or constructor by copy
# - Class attributes
# - Functions parameters default value (created at import time)
#===============================================================================


# Let's create a function which accidentally modifies input parameters
def get_middle_item(input_lst):
    return input_lst.pop(len(input_lst) / 2)

# Let's call this function
input = range(1, 6)
print input
print get_middle_item(input)
print input


# name binding with mutables might lead to error
def list_changer(input_list):
    input_list[0] = 10

    input_list = range(1, 10)
    print input_list
    input_list[0] = 10
    print input_list

test_list = [5, 5, 5]
list_changer(test_list)

# what do you expect to be test_list?
# >>> [10, 1, 2, 3, 4, 5, 6, 7, 8, ,9]
# >>> [10, 5, 5]

print test_list


#===============================================================================
# Mutable and immutable types common errors:
# - Multiple assignment
#    - The same applies with shallow copy or constructor by copy
# - Class attributes
# - Functions parameters default value
# - In-place modifications of function's mutable parameters
#   - when expecting in-place modifications of function's mutable parameters, consider name binding
#===============================================================================


##===============================================================================
##===============================================================================
## TIME TO START WORKING!
##
## EXERCISE MOD 01:
## - Solve common mutable / immutable types usage errors
##
## INSTRUCTIONS:
## - Go to exercices/mod_01 and edit exercise.py
## - Change the functions and class implementation to let tests.py pass
## - Check tests with nosetests (if you have them)
##===============================================================================
##===============================================================================


# Wrong multiple assignment of mutables
def split_even_odd(numbers):
    even = odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print split_even_odd(range(0, 11))


# Solution multiple assignment of mutables: avoid them
def split_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print split_even_odd(range(0, 11))


# Wrong class attributes of mutable type
class NumbersList(object):
    even = []
    odd = []

    def append_number(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

num_lst_A = NumbersList()
num_lst_A.append_number(7)
num_lst_B = NumbersList()
print num_lst_B.even, num_lst_B.odd


# Solution mutable as class attribute: instantiate in the __init__
class NumbersList(object):
    even = None
    odd = None

    def __init__(self):
        self.even = []
        self.odd = []

    def append_number(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

num_lst_A = NumbersList()
num_lst_A.append_number(7)
num_lst_B = NumbersList()
print num_lst_B.even, num_lst_B.odd


# Wrong mutable as function default value
def update_even_odd(numbers, even=[], odd=[]):
    '''Update incoming even and odd numbers lists with corresponding values of numbers iterable
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print update_even_odd(range(0, 11))
print update_even_odd(range(100, 111))


# Solution mutable as function default value: use None as default value and instantiate inside the function
def update_even_odd(numbers, even=None, odd=None):
    if even is None:
        even = []
    if odd is None:
        odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd

print update_even_odd(range(0, 11))
print update_even_odd(range(100, 111))


#===============================================================================
# To sum up, mutable and immutable types common errors and solution:
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy
# - Class attributes --> Instantiate in the __init__
# - Functions parameters default value --> Use None as default value and instantiate inside the function
# - In-place modifications of function's mutable parameters --> Avoid it. Keep in mind what you are doing
#===============================================================================

# Reference assignment and copy:
a = {"1": [1, 2, 3]}
b = a
c = a.copy()
print "@a:", id(a), "@b:", id(b), "@c:", id(c)
print id(a['1']) == id(c['1'])
print id(a['1']) == id(b['1'])
print a, b, c

# b is a reference to a (they point to the same object)
# c is a shallow copy of a: they are isolated but points to the same object
# lets change keys
b["1"].append(4)
c["1"].append(4444)

# What do you expect to be in a and c:
# a={"1": [1, 2, 3, 4]}
# c={"1": [1, 2, 3, 4444]}

print a, c

# But what if we add new keys to c:
c["2"] = "new_key"
print a, b, c

# Changing c does not change a (they share the reference to the object value)
c.pop("1")
print a, b, c

# And, what about deep copy?

spam = [1, 2, 3]
eggs = {"spam": spam}

import copy
fooo = copy.deepcopy(eggs)

print id(spam)
print id(eggs["spam"])

print id(fooo["spam"])

fooo["spam"].append("shouldn't appear in 'eggs' or 'spam'")
print fooo["spam"]

print eggs["spam"]
print spam


#===============================================================================
# - Use 'copy' to perform copies on demand:
#    - Function 'copy' for shallow copies
#    - Function 'deepcopy' for deep copies
#        - Recursive, this is, slow
# - You can define how your custom classes are copied or deepcopied (see Advanced Block)
#===============================================================================


#===============================================================================
# SOURCES:
# - http://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types
# - http://docs.python.org/2/reference/executionmodel.html#naming-and-binding
# - http://docs.python.org/2/library/copy.html#copy.deepcopy
#===============================================================================
