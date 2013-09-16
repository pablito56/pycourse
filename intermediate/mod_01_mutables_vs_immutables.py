#-*- coding: utf-8 -*-
u'''
MOD 01: mutables vs. immutables, deep copy
'''


# Let's instantiate a string and check its identity, type and value
str_inst = 'abcd'
print "identity:", id(str_inst)
print "type:", type(str_inst)
print "value:", str_inst

# Let's use the 'is' operator
print str_inst is 'abcd'


# What happened here?


# Let's compare the ids of two int values
int_inst_1 = 7
int_inst_2 = 7
print int_inst_1 is int_inst_2
print int_inst_1 is 7
print id(int_inst_1), 'vs.', id(int_inst_2)


# Why both have the same id?


#===============================================================================
# - Every object has an identity (its address up to now), a type and a value
# - Both id and type are unchangeable
# - Use 'id' function to retrieve the id of an object
# - Use 'type' function to retrieve the type of an object
#    - Remeber to be Pythonic (Duck Typing, EAFP...)
# - Use 'is' operator to compare the id of two objects
# - The interpreter may reuse objects binding them to different labels
#===============================================================================


# Let's do the same with lists
lst_inst = []
print lst_inst is []
print id(lst_inst), 'vs.', id([])


# What!? Let's try again with bools
bool_inst_1 = True
bool_inst_2 = True
print id(bool_inst_1), 'vs.', id(bool_inst_2)

# Ok. Let's try with other types
none_inst = None
print id(none_inst), 'vs.', id(None)

# 'None' is a constant and is the only accepted value of types.NoneType

list_inst_1 = []
list_inst_2 = []
print id(list_inst_1), 'vs.', id(list_inst_2)


# Why it does not work with lists?


#===============================================================================
# - Objects whose value can change are said to be mutable
#    - dicts, lists, sets
# - Objects whose value is unchangeable once they are created are called immutable
#    - numbers, strings, tuples, NoneType, boolean
# - Mutable types allow in-place modifications (append in a list, pop in a dictionary...)
# - Immutable types instances may be reused by the interpreter (so their id is the same)
#===============================================================================


# Let's check how immutables are reused
sevens = [7, 7, 7, 7, 7]
print map(id, sevens)

abcds = ["abcd", "abcd", "abcd", "abcd", "abcd"]
print map(id, abcds)

empty_tuples = [(), (), ()]
print map(id, empty_tuples)

empty_lists = [[], [], []]
print map(id, empty_lists)

empty_dicts = [{}, {}, {}]
print map(id, empty_dicts)

seven_tuples = [(7,), (7,), (7,)]
print map(id, seven_tuples)


# Best effort: it is not possible to reuse absolutely everything


# Let's change a string value
str_inst = 'instance value'
print str_inst, '@', id(str_inst)

# Reassign
str_inst = str_inst + ' updated'
print str_inst, '@', id(str_inst)


# Let's change a list content
lst_inst = ['instance', 'value']
print lst_inst, '@', id(lst_inst)

# In-place modification
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
# - Mutable types are not stable, so they can not be hashed
#===============================================================================


#===============================================================================
# WARNING!
# - Mutable and immutable types behavior differences can lead to some common errors!!
#    - Though sometimes it is the desired behaviour
#===============================================================================


# Multiple assignment with ints (immutable)
intA = intB = 0
print "intA:", intA, '@', id(intA)
print "intB:", intB, '@', id(intB)


# Let's modify one of the ints
intA += 1
print "intA:", intA, '@', id(intA)
print "intB:", intB, '@', id(intB)


# Notice how we are binding a new value (intA + 1) to the same label (intA)


# Ok. Multiple assignment with lists (mutable)
lstA = lstB = []
print "lstA:", lstA, '@', id(lstA)
print "lstB:", lstB, '@', id(lstB)


# Let's modify (in-place) one of the lists
lstA.extend([1, 2, 3])

# What do you expect to be lstB?

print "lstA:", lstA, '@', id(lstA)
print "lstB:", lstB, '@', id(lstB)


#===============================================================================
# Mutable and immutable types common errors:
#
# - Multiple assignments
#===============================================================================


# Name binding or shallow copy with immutables might lead to error too
initial_list = [2, 3, 5]

new_list = initial_list
for idx in range(len(new_list)):
    new_list[idx] = new_list[idx] ** 2

print "new_list:", new_list

# What do you expect to be initial_list?

print "initial_list:", initial_list


# And the same happens with constructor by copy
initial_dict = {"ones": [1, 1, 1], "twos": [2, 2, 2]}

upper_dict = dict(initial_dict)
for key in upper_dict:
    upper_dict[key.upper()] = upper_dict.pop(key)

print "upper_dict:", upper_dict

# What do you expect to be initial_dict?

print "initial_dict:", initial_dict

# Looks good

upper_dict["TWOS"].append(7)

# And now?

print "initial_dict:", initial_dict


#===============================================================================
# Mutable and immutable types common errors:
#
# - Multiple assignments
#    - The same applies with shallow copy or constructor by copy
#===============================================================================


# Use of mutable types as class attributes
class MutablesClass(object):
    list_inst = []
    int_inst = 0

# Let's instantiate the class twice
inst_A = MutablesClass()
inst_B = MutablesClass()


# Let's change one of the instances
inst_A.int_inst += 1
inst_A.list_inst.extend([5, 7, 9])
print "inst_A.int_inst:", inst_A.int_inst
print "inst_A.list_inst:", inst_A.list_inst

# What do you expect to have inst_B?

print "inst_B.int_inst:", inst_B.int_inst
print "inst_B.list_inst:", inst_B.list_inst

print inst_A.list_inst is inst_B.list_inst

print MutablesClass.list_inst

# Class arguments are stored in the class and created on import time


#===============================================================================
# Mutable and immutable types common errors:
#
# - Multiple assignment
#    - The same applies with shallow copy or constructor by copy
#
# - Class attributes
#===============================================================================


# Let's implement a function to add the power of a number to a list
def add_power_to_list(item, powers_lst=[]):
    powers_lst.append(item ** 2)
    return powers_lst

# Let's call this function
result1 = add_power_to_list(2)
print result1

# Let's call the function again with a different argument
result2 = add_power_to_list(3)

# What do you expect to be result2?

print result1, 'vs', result2
print result1 is result2

print add_power_to_list.func_defaults

# Functions default values are stored in the function object and created on import time


#===============================================================================
# Mutable and immutable types common errors:
#
# - Multiple assignment
#    - The same applies with shallow copy or constructor by copy
#
# - Class attributes
#
# - Functions arguments default value
#===============================================================================


# Let's create a function which returns the middle value of a list
def get_middle_item(input_lst):
    return input_lst.pop(len(input_lst) / 2)

# Let's call this function
input_lst = range(1, 6)
print input_lst

print get_middle_item(input_lst)

# What do you expect to be input_lst?

print input_lst


#===============================================================================
# Mutable and immutable types common errors:
#
# - Multiple assignment
#    - The same applies with shallow copy or constructor by copy
#
# - Class attributes
#
# - Functions arguments default value
#
# - In-place modification of function's mutable arguments
#===============================================================================


##===============================================================================
##===============================================================================
## TIME TO START WORKING!
##
## EXERCISE 1:
## - Solve common mutable / immutable types usage errors
##
## INSTRUCTIONS:
## - Go to exercises/exercise_1 and edit exercise_1.py
## - Change the functions and class implementation to let tests_1.py pass
## - Check tests executing 'nosetests -sv'
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
print "num_lst_B.even:", num_lst_B.even
print "num_lst_B.odd:", num_lst_B.odd


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
#
# - Multiple assignment --> Avoid multiple assignment of mutable types
#    - The same applies with shallow copy or constructor by copy --> Use copy.deepcopy
#
# - Class attributes --> Instantiate in the __init__
#
# - Functions arguments default value --> Use None as default value and instantiate inside the function
#
# - In-place modification of function's mutable arguments --> Avoid it. Keep in mind what you are doing
#===============================================================================


# Let's try to copy an object

dict_inst = {"a": [1, 2, 3]}
assign_copy = dict_inst         # Copy by assignment
method_copy = dict_inst.copy()  # Alternative constructor by copy
print dict_inst
print assign_copy
print method_copy

print "@dict_inst:  ", id(dict_inst)
print "@assign_copy:", id(assign_copy)
print "@method_copy:", id(method_copy)

# assign_copy is a reference to dict_inst: they point to the same object
# method_copy is a shallow copy of dict_inst: they are different objects

# lets change their content
assign_copy["a"].append(4)
method_copy["a"].append(4444)

# What do you expect to be inside dict_inst and method_copy?
# dict_inst = {"1": [1, 2, 3, 4]}
# method_copy = {"1": [1, 2, 3, 4444]}

print dict_inst
print method_copy

print id(dict_inst['a']) == id(assign_copy['a'])
print id(dict_inst['a']) == id(method_copy['a'])

# They are different objects but they contain (point to) the same list thanks to shallow copy

# But what if we add new keys to method_copy?
method_copy["b"] = "new_key"
print dict_inst
print assign_copy
print method_copy

# Changing method_copy content does not change dict_inst
method_copy.pop("a")
print dict_inst
print assign_copy
print method_copy


# And, what about deep copy?


spam = [1, 2, 3]
eggs = {"spam": spam}

import copy
eggs_shallow_copy = copy.copy(eggs)
eggs_deep_copy = copy.deepcopy(eggs)
print eggs_shallow_copy
print eggs_deep_copy

print "@eggs:             ", id(eggs)
print "@eggs_shallow_copy:", id(eggs_shallow_copy)
print "@eggs_deep_copy:   ", id(eggs_deep_copy)

print "@spam:        ", id(spam)
print "@eggs['spam']:", id(eggs["spam"])

print "@eggs_shallow_copy['spam']:", id(eggs_shallow_copy["spam"])
print "@eggs_deep_copy['spam']:   ", id(eggs_deep_copy["spam"])

eggs_shallow_copy["spam"].append("it has to appear in 'eggs' and 'spam'")
print eggs_shallow_copy["spam"]

eggs_deep_copy["spam"].append("shouldn't appear in 'eggs' or 'spam'")
print eggs_deep_copy["spam"]

print eggs["spam"]
print spam


#===============================================================================
# - Assignment does not copy an object, just copies its reference
# - Use 'copy' to perform copies on demand:
#    - Function 'copy' for shallow copies
#    - Function 'deepcopy' for deep copies
#        - Recursive, this is, slow
# - Some standard library data types also have constructor by copy (shallow)
# - You can define how your custom classes are copied or deepcopied (see Intermediate Block)
#===============================================================================


#===============================================================================
# SOURCES:
# - http://docs.python.org/2.7/reference/datamodel.html#objects-values-and-types
# - http://docs.python.org/2/reference/executionmodel.html#naming-and-binding
# - http://docs.python.org/2/library/copy.html#copy.deepcopy
# - http://www.pythontutor.com/visualize.html
#===============================================================================
