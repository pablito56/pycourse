#-*- coding: utf-8 -*-
u'''
MOD XX: Classes: data model & customization
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


# Let's create a fractions class
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

# Let's instantiate a fraction
fract1 = MyFraction(5, 2)
print fract1
print repr(fract1)


# Let's customize our class representation
class MyFraction(object):
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

# Let's instantiate again
fract1 = MyFraction(5, 2)
print fract1
print repr(fract1)


#===============================================================================
# - There are special method names to customize your classes behavior
# - Python invokes these methods (if present) when special syntax is executed
#    - Instatiation and object creation
#    - Representation
#    - Rich comparison
#    - Arithmetic operations
#    - Attribute access
#    - Container types emulation
#    - Context managers emulation
#    - Callable objects emulation
#
# - http://docs.python.org/2.7/reference/datamodel.html#basic-customization
#===============================================================================


# Let's customize our class rich comparison
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def value(self):
        return float(self.num) / self.den

    def __lt__(self, other):
        '''Called to implement evaluation of self < other
        '''
        try:
            return self.value() < other.value()
        except AttributeError:
            return self.value() < other

    def __le__(self, other):
        '''Called to implement evaluation of self <= other
        '''
        try:
            return self.value() <= other.value()
        except AttributeError:
            return self.value() <= other

    def __eq__(self, other):
        '''Called to implement evaluation of self == other
        '''
        try:
            return self.value() == other.value()
        except AttributeError:
            return self.value() == other

    def __ne__(self, other):
        '''Called to implement evaluation of self != other
        '''
        try:
            return self.value() != other.value()
        except AttributeError:
            return self.value() != other

fract1 = MyFraction(5, 2)  # 2.5
fract2 = MyFraction(3, 2)  # 1.5
fract3 = MyFraction(25, 10)  # 2.5

print fract1 != fract3  # 2.5 != 2.5
print fract1 == fract3  # 2.5 == 2.5
print fract2 < fract3  # 1.5 < 2.5

# Let's try the other way
print fract1 >= fract2   # 2.5 >= 1.5
print fract2 >= fract3  # 1.5 >= 2.5

# Let's try with other types
print fract1 >= 2  # 2.5 >= 2
print fract2 == 1.5  # 1.5 == 1.5

# Let's try the other way with other types
print 2 <= fract1  # 2 <= 2.5
print 1.5 == fract2   # 1.5 == 1.5


#===============================================================================
# - You don't have to define all the possible methods, Python can take the opposite
# - Python will try the opposite when a comparison method of a type raises TypeError
# - It's up to you to implement compatibility with other types
#===============================================================================


# Let's try again
print 10 > fract1  # 10 > 2.5
print 10 < fract1  # 10 < 2.5
print fract1 < 10  # 2.5 < 10
print fract1 > 10  # 2.5 > 10


# Let's define all comparison methods
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def value(self):
        return float(self.num) / self.den

    def __lt__(self, other):
        try:
            return self.value() < other.value()
        except AttributeError:
            return self.value() < other

    def __le__(self, other):
        try:
            return self.value() <= other.value()
        except AttributeError:
            return self.value() <= other

    def __eq__(self, other):
        try:
            return self.value() == other.value()
        except AttributeError:
            return self.value() == other

    def __ne__(self, other):
        try:
            return self.value() != other.value()
        except AttributeError:
            return self.value() != other

    def __gt__(self, other):
        try:
            return self.value() > other.value()
        except AttributeError:
            return self.value() > other

    def __ge__(self, other):
        try:
            return self.value() >= other.value()
        except AttributeError:
            return self.value() >= other

fract1 = MyFraction(5, 2)  # 2.5

print 10 > fract1  # 10 > 2.5
print 10 < fract1  # 10 < 2.5
print fract1 < 10  # 2.5 < 10
print fract1 > 10  # 2.5 > 10


#===============================================================================
# - You don't have to define all the possible methods, Python can take the opposite
#    - But you should do it to support other types!!
#    - You can also define __cmp__ (invoked if no other methods defined)
# - Python will try the opposite when a comparison method of a type raises TypeError
# - It's up to you to implement compatibility with other types
#===============================================================================


# Let's emulate a container
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def __str__(self):
        return "{0} / {1}".format(self.num, self.den)

    def __len__(self):
        '''Called to implement the built-in function len()
        '''
        return 2

    def __getitem__(self, key):
        '''Called to implement evaluation of self[key]
        '''
        if key == 0 or key == 'num':
            return self.num
        elif key == 1 or key == 'den':
            return self.den
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        '''Called to implement assignment of self[key] = value
        '''
        if key == 0 or key == 'num':
            self.num = value
        elif key == 1 or key == 'den':
            self.den = value
        else:
            raise KeyError(key)


f1 = MyFraction(7, 2)
print len(f1)
print f1['num'], "/", f1[1]
f1[0] = 5
f1['den'] = 3
print f1


#===============================================================================
# More info on emulating container types:
# - http://docs.python.org/2.7/reference/datamodel.html#emulating-container-types
#===============================================================================


# Let's emulate numeric types
class MyFraction(object):
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        self.den = int(denominator)

    def __str__(self):
        return "{0} / {1}".format(self.num, self.den)

    def __add__(self, other):
        '''Called to implement the binary arithmetic operation self + other
        '''
        try:
            if self.den == other.den:
                return MyFraction(self.num + other.num, self.den)
            else:
                return MyFraction(self.num * other.den + other.num * self.den, self.den * other.den)
        except AttributeError:
            return MyFraction(self.num + other * self.den, self.den)

    __radd__ = __add__

fract1 = MyFraction(5, 3)
fract2 = MyFraction(2, 3)
print fract1 + fract2
print fract1 + 5
print 3 + fract1


#===============================================================================
# More info on emulating numeric types:
# - http://docs.python.org/2.7/reference/datamodel.html#emulating-numeric-types
#===============================================================================


# Let's customize dicts
class AttrDict(dict):
    def __getattr__(self, name):
        '''Called when an attribute lookup has not found the attribute in the usual places
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

d = dict(zip("abcde", range(1, 6)))
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


##===============================================================================
##===============================================================================
## TIME TO START WORKING!
##
## EXERCISE 1:
## - Solve old-style class inheritance issue in CustomOptionParser
## - Implement slicing and + and - operators in CustomOrderedDict
## - Modify AttrDict to access the dictionary only if key already exists (otherwise act as normal attributes)
## - http://docs.python.org/2.7/reference/datamodel.html
##
## INSTRUCTIONS:
## - Go to exercices/exercise_1 and edit exercise_1.py
## - Change the functions and class implementation to let tests_1.py pass
## - Check tests with nosetests
##===============================================================================
##===============================================================================


# Wrong old-style class inheritance
from optparse import OptionParser
class CustomOptionParser(OptionParser):
    def __str__(self):
        return self.__class__.__name__

# Right old-style class inheritance
class CustomOptionParser(OptionParser, object):
    def __str__(self):
        return self.__class__.__name__

inst = CustomOptionParser()
print inst.__class__, type(inst)


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
# - As we will see in next examples, this implementation is wrong
#===============================================================================

#===============================================================================
# MORE INFO:
# - http://docs.python.org/2.7/reference/datamodel.html#special-method-names
# - http://www.python.org/doc/newstyle/
# - http://www.python.org/download/releases/2.2.3/descrintro/
#===============================================================================
