#-*- coding: utf-8 -*-
u"""
MOD 08: descriptors
"""


# Let's define a descriptor
class RandAttr(object):
    def __init__(self, n=10):
        self.n = n

    def __get__(self, inst, cls):
        from random import randint
        print "Called __get__ of instance of {0}".format(self.__class__.__name__)
        return randint(0, self.n)


# Let's define a class with a descriptor attribute
class RandAttrClass(object):
    rand_attr = RandAttr(20)  # Descriptors are always class attributes


# Let's instantiate and access this attribute
inst = RandAttrClass()
print inst.rand_attr


# Let's do it again
print inst.rand_attr


# And again
print inst.rand_attr


# Let's do it in a different way
print getattr(inst, "rand_attr")


#===========================================================================
# Python descriptos:
#    - A descriptor is an object attribute with “binding behavior”, one whose
#      attribute access has been overridden by methods in the descriptor protocol
#        - It may intercept attribute retrieval, modification and/or deletion
#
#    - Descriptor protocol implements at least one of the following:
#        - descr.__get__(self, obj, type=None) --> value
#        - descr.__set__(self, obj, value) --> None
#        - descr.__delete__(self, obj) --> None
#===========================================================================


# Let's try to understand descriptor __get__ parameters


class VerboseGetDescriptor(object):
    def __get__(self, inst, cls):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        print "\tself:", self
        print "\tinst:", inst
        print "\tcls:", cls


class VerboseGetClass(object):
    attr = VerboseGetDescriptor()


# Let's check how it works
inst = VerboseGetClass()
print inst
print inst.__dict__
print VerboseGetClass.__dict__

print inst.attr

# Now with the class
print VerboseGetClass.attr


#===============================================================================
# - Descriptors are class attributes, so you can access them directly through the class
#===============================================================================


# Let's see a real world example that you use at all time


class MyClass(object):
    def a_method(self):
        print "Called a_method on", self


# Let's instantiate it and call the method
inst = MyClass()
inst.a_method()
print inst.a_method


# Let's check its __dict__ content
print inst.__dict__
print MyClass.__dict__
print MyClass.__dict__['a_method']


# Let's play around with this method
print MyClass.__dict__['a_method']
print MyClass.__dict__['a_method'].__get__
print MyClass.__dict__['a_method'].__get__(inst, MyClass)
print MyClass.__dict__['a_method'].__get__(None, MyClass)


#===========================================================================
# - This is the "magic" behind bounded or unbounded methods
#
# - Function class implements the descriptors protocol, and its __get__ is in
#   charge of returning bounded or unbounded (to classes or instances) methods
#    - Good example of how descriptors can take instances or only classes
#===========================================================================


#===============================================================================
# WARNING!
# - If you use a class decorator to decorate (class) methods you must implement
#    the descriptor protocol in your decorator
#    - Otherwise you will loose the reference to 'self' inside decorated methods
#        (the instance of the decorated method class)
#===============================================================================


# Let's see another real world example


class DeferredAttribute(object):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __get__(self, inst, cls):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        inst.__dict__[self.name] = self.func(inst)
        return inst.__dict__[self.name]  # Let's add the result to the INSTANCE


# Let's use it
class DeferredAttrClass(object):
    def expensive_operation(self):
        print "\tCalled expensive_operation"
        from time import sleep
        sleep(3)
        return 12345
    attr = DeferredAttribute('attr', expensive_operation)  # We give the same name than the descriptor

# Let's instantiate the class
inst = DeferredAttrClass()
print DeferredAttrClass.__dict__
print inst.__dict__

# Let's recover the deferred attribute for first time
print inst.attr
print DeferredAttrClass.__dict__
print inst.__dict__

# Let's do it again
print inst.attr
print DeferredAttrClass.__dict__
print inst.__dict__


# It's time to practice with descriptors


#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_08_descriptors/exercise_mod_08
#
# - Use descriptor protocol to cache during a certain TTL the return value of a function as an attribute
#
# - Run the tests in 'tests_mod_08.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_08.py'
#===============================================================================


# Let's try to understand descriptor __set__ parameters


# Let's create a descriptor just with __set__
class VerboseSetDescriptor(object):
    def __set__(self, inst, val):
        print "Calling __get__ on instance of {0}".format(self.__class__.__name__)
        print "\tself:", self
        print "\tinst:", inst
        print "\tval:", val    # It receives the new value instead of the class


class VerboseSetClass(object):
    attr = VerboseSetDescriptor()


# Let's check how it works
inst = VerboseSetClass()
print inst
print inst.__dict__
print VerboseSetClass.__dict__

inst.attr = 12345

print inst
print inst.__dict__             # NO modification has been done to __dict__
print VerboseSetClass.__dict__

VerboseSetClass.attr = 12345

print inst
print inst.__dict__
print VerboseSetClass.__dict__  # We have "removed" (rebound to a new value) the descriptor!


# Let's see a real world example


class TypedAttrib(object):
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ  # Avoid using 'type' as attribute name

    def __set__(self, inst, val):
        if isinstance(val, self.typ):
            inst.__dict__[self.name] = val
        else:
            raise TypeError("TypeError: Wrong data type '{0}'".format(val))


#===========================================================================
# Note that I wouldn't recommend this! Duck typing FTW!!
#===========================================================================


# Let's use it
class MyTypedClass(object):
    string = TypedAttrib('string', str)
    integer = TypedAttrib('integer', int)  # Despite using the same name the descriptor will ALWAYS intercept the call


inst = MyTypedClass()
inst.string = "123"
print inst.__dict__


# Let's make it fail
try:
    inst.string = 123
except TypeError, e:
    print e

print inst.__dict__  # Note that no modification has been done


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/howto/descriptor.html
#===============================================================================
