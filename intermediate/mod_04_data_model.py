#-*- coding: utf-8 -*-
u'''
MOD 04: data model & customisation
'''


#===============================================================================
# REMEMBER:
# - New-style classes were introduced in Python 2.2 to unify classes and types
# - Provide unified object model with a full meta-model
# - Other benefits: subclass most built-in types, descriptors (slots, properties, static and class methods)...
# - By default all classes are old-style until Python 3
#    - In Python 2 you have to inherit from 'object' to use new-style
#    - You must avoid old-style
#    - So you must inherit ALWAYS from 'object'
#
# - Other changes introduced Python 2.2: __new__, new dir() behavior, metaclasses, new MRO (also in 2.3)
#
# - More info: http://www.python.org/doc/newstyle/
#===============================================================================


# Let's see what is this unified object model


# Let's create a class to manage fractions
class Fraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

# Let's print a Fraction instance
fract1 = Fraction(5, 2)
print fract1
print repr(fract1)


# Let's customize our class representation
class Fraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def __str__(self):
        '''Called by the str() built-in function and by the 'print' statement
        to compute the "informal" string representation of an object
        '''
        return "{0} / {1}".format(self.num, self.den)

    def __repr__(self):
        '''Called by the repr() built-in function and by string conversions
        (reverse quotes) to compute the "official" string representation of an object
        '''
        return "{0}({1}, {2})".format(self.__class__.__name__, self.num, self.den)


# Let's try again
fract1 = Fraction(5, 2)
print fract1
print repr(fract1)


#===============================================================================
# From Python documentation:
#
#    A class can implement certain operations that are invoked by special syntax
#    (such as arithmetic operations or subscripting and slicing) by defining methods
#    with special names.
#===============================================================================


#===============================================================================
# - There are special method names to customize your classes behavior
#    - Python’s approach to operator overloading, allowing classes to define
#      their own behavior with respect to language operators
# - Python invokes these methods (if present) when special syntax is executed
#
#    - Instatiation and object creation and deletion
#        - __init__, __new__, __del__
#
#    - Representation
#        - __str__, __repr__
#
#    - Rich comparison
#        - __eq__, __ne__, __lt__ , __gt__, __le__, __ge__
#
#    - Numeric operations
#        - __add__, __radd__, __iadd__, __sub__, __mul__...
#
#    - ...
#
#===============================================================================


#===============================================================================
#    - ...
#
#    - Hashing (i.e. use as dict key) and truth value testing
#        - __hash__ and __nonzero__
#
#    - Objects copy and deepcopy
#        - __copy__ and __deepcopy__
#
#    - Attribute access
#        - __getattr__, __setattr__, __delattr__, __getattribute__
#
#    - Container types emulation
#        - __len__, __getitem__, __setitem__, __contains__ ...
#
#    - Slicing
#        - __getslice__ (deprecated by __getitem__), __setslice__
#
#    - ...
#
#===============================================================================


#===============================================================================
#    - ...
#
#    - Iterator protocol
#        - __iter__, __reversed__, next
#
#    - Context managers emulation
#        - __enter__, __exit__
#
#    - Callable objects
#        - __call__
#
#    - Descriptors and slots
#        - __get__, __set__, __delete__, __slots__
#
# - Python applies coercion in some cases, but it has been removed in Py3k
#
# - http://docs.python.org/2.7/reference/datamodel.html#basic-customization
#===============================================================================


# Let's see some examples


class Coefficients(object):
    """Store a sequence of numeric coefficients
    """
    def __init__(self, coeffs):
        self.coeffs = tuple(coeffs)

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, self.coeffs)

    def __gt__(self, other):
        '''Called to implement evaluation of self > other
        '''
        try:
            return sum(self.coeffs) > sum(other.coeffs)
        except AttributeError:
            return sum(self.coeffs) > other

    def __mul__(self, other):
        '''Called to implement the binary arithmetic operation self * other
        '''
        try:
            return Coefficients(map(lambda x, y: x * y, self.coeffs, other.coeffs))
        except AttributeError:
            return Coefficients(map(lambda x: x * other, self.coeffs))

    def __add__(self, other):
        '''Called to implement the binary arithmetic operation self + other
        '''
        try:
            return Coefficients(map(lambda x, y: x + y, self.coeffs, other.coeffs))
        except AttributeError:
            return Coefficients(map(lambda x: x + other, self.coeffs))

    __radd__ = __add__
    '''Called to implement the binary arithmetic operation other + self
    '''

c1 = Coefficients([1, 2, 3, 4, 5])
c2 = Coefficients([6, 7, 8, 9, 10])

print c1 * c2

print c1 > c2

print c1 > 1

print c1 < 100000000  # Despite we only defined __gt__

print c1 + 4

print 4 + c1

print 4 * c1

#===============================================================================
# - You don't have to define all the possible methods, Python can try to call the opposite
#    - But you should do it to be compatible with other types!!
# - Remember that Python 2.X could try to coerce, but this behaviour has been removed in Py3k
# - It's up to you to implement compatibility with other types
#
# More info on numeric and comparisson operators:
# - http://docs.python.org/2.7/reference/datamodel.html#emulating-numeric-types
# - http://docs.python.org/2.7/reference/datamodel.html#basic-customization
#===============================================================================


# Let's customize dicts attribute access


class AttrDict(dict):
    def __getattr__(self, name):
        '''Called when an attribute lookup has NOT found the attribute in
        the usual places (__dict__)
        '''
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        '''Called when an attribute assignment is attempted
        '''
        # self.__setitem__(key, value)
        self[name] = value

    def __delattr__(self, name):
        '''Called when an attribute deletion is attempted
        '''
        del self[name]

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
attr_d = AttrDict(d)
print attr_d

attr_d.f = 6
print attr_d.f
print attr_d

del attr_d.f
print attr_d


#===============================================================================
# - Thanks to new-style classes you can customize basic types
#    - Be careful!
#
# More info on emulating container types:
# - http://docs.python.org/2.7/reference/datamodel.html#customizing-attribute-access
#===============================================================================


# Time to start practicing with classes customisation


#===============================================================================
# EXERCISE: advanced/exercises/mod_04_data_model/exercise_mod_04.py
#
# - Implement slicing and + and - operators in CustomOrderedDict
#    - __getslice__ is deprecated by __getitem__ passing an slice object
# - Modify AttrDict to access the dictionary ONLY if key already exists,
#    otherwise act as with normal attributes
# - Implement all required methods of Fraction to customise:
#    - Full rich comparisson with Fractions and other numbers
#    - + and * operator with Fractions and other numbers
#    - Index access to numerator and denominator (0 and 1)
#    - Key access to numerator and denominator ("num" and "den")
#    - Length (always 2)
# - http://docs.python.org/2.7/reference/datamodel.html
#
# - Run the tests in 'tests_mod_04.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_04.py'
#===============================================================================


# CustomOrderedDict with slicing and + and - operators
from collections import OrderedDict


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.items()[key])
        return OrderedDict.__getitem__(self, key)

    def __add__(self, other):
        res = self.__class__(self)
        res.update(other)
        return res

    def __sub__(self, other):
        res = self.__class__(self)
        [res.pop(k, None) for k in other]
        return res

cod_inst = CustomOrderedDict(zip("abcde", range(1, 6)))
print cod_inst
print cod_inst[0:3] + cod_inst[3:10]


# AttrDict accessing the dict only if key already exists
class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        else:
            # self.__dict__[name] = value  # Perform action instead of delegating
            dict.__setattr__(self, name, value)  # Always call the method of an ancestor!

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            # del self.__dict__[name]  # Perform action instead of delegating
            dict.__delattr__(self, name)

ad_inst = AttrDict(zip("abcde", range(1, 6)))
print ad_inst
ad_inst.f = 6
ad_inst.a = 0
del ad_inst.b
print ad_inst
print ad_inst.f

#===============================================================================
# WARNING!
# - As we will see in next module, this implementation is wrong
#===============================================================================

#===============================================================================
# RESOURCES:
# - http://docs.python.org/2.7/reference/datamodel.html#special-method-names
# - http://docs.python.org/2.7/reference/datamodel.html#coercion-rules
# - http://www.python.org/doc/newstyle/
#===============================================================================
