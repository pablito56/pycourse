#-*- coding: utf-8 -*-
u'''
MOD XW: Cooperative super call pattern
'''


# Let's implement a verbose dict intercepting attribs and items access
class VerboseDict(dict):
    def __getattribute__(self, name):
        print "__getattribute__", name
        return dict.__getattribute__(self, name)

    def __getitem__(self, key):
        print "__getitem__", key
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return dict.__setitem__(self, key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return dict.__getattr__(self, name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return dict.__setattr__(self, name, value)


# Let's try it
vd = VerboseDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
print vd.a
print vd


#===============================================================================
# What if we want to mix this behavior with our AttrDict?
#===============================================================================

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
            dict.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            dict.__delattr__(self, name)


# Option 1: new class inheriting from both
class VerboseAttribDict(VerboseDict, AttrDict):
    pass

# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
vd.a
vd


# Option 2: new class inheriting from both (change the order)
class VerboseAttribDict(AttrDict, VerboseDict):
    pass

# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
vd.a
vd

#===============================================================================
# WARNING!
# - Ancestors (superclasses) order when inheriting matters!
#===============================================================================


# Option 3: implement new class with both verbose and attrib behavior --> new code
# Option 4: change VerboseDict to inherit from AttribDict --> change code to call right ancestor
# ...


#===============================================================================
# The solution is 'super' and cooperative methods!!
# - super(type[, object-or-type])
#    - Typically: super(CurrentClass, self).current_method(*current_args, **current_kwargs)
# - Returns a proxy object that delegates method calls to a parent or sibling class of type.
#
# - http://docs.python.org/2/library/functions.html#super
#===============================================================================


# Let's implement verbose dict with super
class VerboseDict(dict):
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(VerboseDict, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(VerboseDict, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(VerboseDict, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(VerboseDict, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(VerboseDict, self).__setattr__(name, value)


# Let's implement attribs dict with super
class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            # super(AttrDict, self).__setitem__(name, value)
            # self.__setitem__(name, value)
            self[name] = value
        else:
            super(AttrDict, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            super(AttrDict, self).__delattr__(name)


# Option 1: new class inheriting from both... wiht super!!
class VerboseAttribDict(VerboseDict, AttrDict):
    pass


# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
vd.a
vd


# Option 4: change VerboseDict to inherit from AttribDict --> with super no changes are required!
class VerboseDict(AttrDict):
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(VerboseDict, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(VerboseDict, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(VerboseDict, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(VerboseDict, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(VerboseDict, self).__setattr__(name, value)


# Let's use this dict
vd = VerboseDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
vd.a
vd


#===============================================================================
# - super is an implicit ancestors' methods invocation mechanism
# - super is the key of Guido's "cooperative super call" pattern
#    - aka. "call-next-method"
#
# - http://www.python.org/download/releases/2.2.3/descrintro/#cooperation
#===============================================================================


# Let's see in detail how super and MRO work

class A(object):
    def meth(self):
        print type(self), "A's method"


class B(A):
    def meth(self):
        print type(self), "B's method"
        super(B, self).meth()


class C(A):
    def meth(self):
        print type(self), "C's method"
        super(C, self).meth()


class D(B, C):
    def meth(self):
        print type(self), "D's method"
        super(D, self).meth()


#==============================================================================
# We have a diamond inheritance schema:
#
#    A
#   / \
#  B   C
#   \ /
#    D
#==============================================================================


# Let's instantiate D and call the method
d_inst = D()
d_inst.meth()


# Another example

class A2(object):
    def meth(self):
        print type(self), "A2's method"


class C2(A2):
    def meth(self):
        print type(self), "C2's method"
        super(C2, self).meth()


class B2(C2):
    def meth(self):
        print type(self), "B2's method"
        super(B2, self).meth()


class D2(B2):
    def meth(self):
        print type(self), "D2's method"
        super(D2, self).meth()


#==============================================================================
# We have a linear inheritance schema:
#
#    A2
#    |
#    C2
#    |
#    B2
#    |
#    D2
#==============================================================================


# Let's instantiate D and call the method again
d_inst = D2()
d_inst.meth()


# Let's check its Method Resolution Order (MRO)
print D.__mro__
print D2.__mro__


#===============================================================================
# Let's see it step by step:
#
# 1- In D's meth, super(D, self).meth() will find and call B.meth(self), since B is the first base class following D in D.__mro__ that defines meth.
#    - If meth was not defined in B the process would continue to next base class.
# 2- In B.meth, super(B, self).meth() is called. Since self is a D instance, the MRO is (D, B, C, A, object) but given that we are in B, the next base class is C.
# 3- In C again meth is declared so it is called, and in turn it calls super(C, self).meth().
# 4- Still using the same MRO, we see that the class following C is A, so A.meth is called. No super call is made at this point and the cahon of invocations finishes.
#===============================================================================


#===============================================================================
# - This process ensures that all ancestors of a class are always inspected before the ancestors of its ancestors
# - The same process applies when a class declaration is empty, like our fist implementation of VerboseAttribDict
#
# - http://www.python.org/download/releases/2.2.3/descrintro/#mro
#===============================================================================


# Let's see what happens with attributes (getattr)

class A3(object):
    class_attr = "A3"


class B3(A3):
    pass


class C3(A3):
    class_attr = "C3"


class D3(B3, C3):
    pass


#==============================================================================
# We have a diamond inheritance schema:
#
#    A3 (class_attr = "A3")
#   /  \
#  B3   C3 (class_attr = "C3")
#   \  /
#    D3
#==============================================================================


# Let's instantiate D and call the method again
d_inst = D3()
d_inst.class_attr


#===============================================================================
# MRO was changed in 2.2 (and 2.3) because with new-style all classes inherit from 'object', so suddenly diamond diagrams would appear:
# - old-tyle multiple inheritance diagram:
#
#  B   C
#   \ /
#    D
#
#
# - the same implementation with new-tyle:
#
#  object
#   / \
#  B   C
#   \ /
#    D
#
# - With the old version (wrong) MRO would be: D, B, object, C, object!!
# - With the new one it is: D, B, C, object
#===============================================================================


# Let's go back again to our verbose attribute dict...

class Verbose(object):
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(Verbose, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(Verbose, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(Verbose, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(Verbose, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(Verbose, self).__setattr__(name, value)


class Attr(object):
    def __getattr__(self, name):
        try:
            return super(Attr, self).__getitem__(name)
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            super(Attr, self).__setitem__(name, value)
        else:
            super(Attr, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name in self:
            super(Attr, self).__delitem__(name)
        else:
            super(Attr, self).__delattr__(name)


# Option 5: exploit cooperative super call with mixins
class VerboseAttribDict(Verbose, Attr, dict):
    pass


# Let's use this dict
vd = VerboseAttribDict({'a': 1, 'b': 2})
vd['c'] = 3
vd.x = 7
vd.a = 0
vd.a
vd
VerboseAttribDict.__mro__


# It's time to exercise with super


#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_XW_super/exercise_mod_XW
#
# - Implement all needed changes to let the tests pass. In particular, implement AmazingDict:
#    - Access keys as attributes only if they already exist
#    - Lower attributes and key names for query or modification
#    - Convert attributes or keys datetime values to strings when they are modified
#    - Print all attributes and keys accesses for query or modification
# - Check: http://docs.python.org/2/reference/datamodel.html?highlight=__contains__#object.__contains__
#
# - Run the tests in 'tests_mod_XW.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_XW.py'
#===============================================================================


# Solution step 1: implement __contains__ in Lower class
class Lower(object):
    def __getattribute__(self, name):
        return super(Lower, self).__getattribute__(name.lower())

    def __getitem__(self, key):
        return super(Lower, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setitem__(key.lower(), value)

    def __getattr__(self, name):
        return super(Lower, self).__getattr__(name.lower())

    def __setattr__(self, name, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setattr__(name.lower(), value)

    def __contains__(self, item):
        return super(Lower, self).__contains__(item.lower())


# Nothing to change in Attr class implementation
class Attr(object):
    '''Access keys as attributes only if they already exist
    '''
    def __getattr__(self, name):
        try:
            return super(Attr, self).__getitem__(name)
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            super(Attr, self).__setitem__(name, value)
        else:
            super(Attr, self).__setattr__(name, value)


# Solution step 2: make Verbose class inherit from object
class Verbose(object):
    '''Print all attributes and keys accesses for query or modification
    '''
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(Verbose, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(Verbose, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(Verbose, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(Verbose, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(Verbose, self).__setattr__(name, value)


# Nothing to change in DateStr class implementation
from datetime import datetime
class DateStr(object):
    def __setitem__(self, key, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setitem__(key, value)

    def __setattr__(self, name, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setattr__(name, value)


# Solution step 2: setup correct order of AmazingDict class ancestorts
class AmazingDict(Attr, Lower, DateStr, Verbose, dict):
    pass


# Let's check the result
d = AmazingDict({'id': 1234})
print d.iD

now = datetime.now()
d2 = AmazingDict()
d2['date'] = now
print d2.date

print type(d2.date)

print d2.date == now.isoformat()

d3 = AmazingDict({'id': 1234})
print d3
d3.ID = 1111

print d3

#===============================================================================
# MORE INFO:
# - http://docs.python.org/2/library/functions.html#super
# - http://www.python.org/download/releases/2.2.3/descrintro/#cooperation
# - http://www.python.org/download/releases/2.2.3/descrintro/#mro
#===============================================================================
