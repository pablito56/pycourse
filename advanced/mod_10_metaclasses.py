#-*- coding: utf-8 -*-
u'''
MOD 10: creation and instantiation: __new__ and metaclasses
'''


class VerboseCreator(object):
    def __new__(cls, *args, **kwargs):      # This is the real constuctor of instances
        print "CALLED __new__", cls, args, kwargs
        res = super(VerboseCreator, cls).__new__(cls, *args, **kwargs)
        print "RETURN TYPE:", type(res)
        return res

    def __init__(self, *args, **kwargs):      # This is only the instance initialization method
        print "CALLED __init__", self, args, kwargs
        super(VerboseCreator, self).__init__(*args, **kwargs)


verb_inst = VerboseCreator()


#===============================================================================
# - __new__ is a special static method called to create a new instance of the class
#    - No need to be defined as static
#    - Called when you 'call' the class
# - It takes the class as first argument followed by all object constructor arguments
# - It returns the new instance
#    - Later __init__ will be called on that instance
# - When calling super inside __new__ you have to provide the class as first parameter
#===============================================================================


# What happens with inheritance?

class VerboseCreatorDict(VerboseCreator, dict):
    pass


verb_dict_inst = VerboseCreatorDict({'a': 1, 'b': 2})

print verb_dict_inst


# Let's see a real world example


class MySingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

inst_1 = MySingleton()
inst_2 = MySingleton()
print id(inst_1), 'vs.', id(inst_2)


# Another example

class RoundedFloat(float):
    def __new__(cls, *args, **kwargs):
        if args:
            args = [round(args[0], 2)]
        return super(RoundedFloat, cls).__new__(cls, *args, **kwargs)

print RoundedFloat(7.12345)


#===============================================================================
# Common uses of __new__:
#   - Singleton pattern, although the most recommended implementation is just a module
#   - Factory pattern, although we are gonna see a better solution
#   - When subclassing immutable types, to customize the instance creation
#   - In custom metaclasses in order to customize class creation
#===============================================================================


# Metaclasses? What's that?
print type(verb_dict_inst)
print type(type(verb_dict_inst))

print type(VerboseCreatorDict)


#===============================================================================
# - The metaclass is the type of a class.
# - New-style classes are constructed using type().
# - A class definition is read into a separate namespace and the value of class name
#   is bound to the result of calling type(name, bases, dict)
#
# More info: http://docs.python.org/2/reference/datamodel.html#customizing-class-creation
#===============================================================================


# A simple example
class MyMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        print "NEW CLASS"
        print "\t metaclass:", mcs
        print "\t name:", name
        print "\t bases:", bases
        print "\t attrs:", attrs
        new_class = super(MyMetaclass, mcs).__new__(mcs, name, bases, attrs)
        return new_class


class TrueFalseClass(object):
    __metaclass__ = MyMetaclass
    class_attrib = "class attrib value"

    def ret_false(self, *args, **kwargs):
        return False

    def ret_true(self, *args, **kwargs):
        return True


# Our metaclasses has been already called!


#===============================================================================
# - Classes are instantiated at import or evaluation time!
#    - Metaclasses run at that moment
#===============================================================================


# Let's see a real example


# Let's implement a logging decorator
def _logging_decorator(func):
    def logging_wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not res:
            print "CALL FAILED:", args, kwargs,
        return res
    return logging_wrapper


# Let's define a metaclass using it
from inspect import isfunction


def _decorate_attrs(attrs):
    decorated_attrs = {}
    for name, func in attrs.items():
        if isfunction(func):
            func = _logging_decorator(func)
        decorated_attrs[name] = func
    return decorated_attrs


class LoggingMetaclass(type):
    def __new__(mcs, name, bases, attrs):
#        print "NEW", mcs, name, bases, attrs
        new_class = super(LoggingMetaclass, mcs).__new__(mcs, name, bases, _decorate_attrs(attrs))
        return new_class


# Let's use this metaclass
class TrueFalseClass(object):
    __metaclass__ = LoggingMetaclass
    class_attrib = "class attrib value"

    def ret_false(self, *args, **kwargs):
        return False

    def ret_true(self, *args, **kwargs):
        return True


tf_inst = TrueFalseClass()
tf_inst.ret_true()

tf_inst.ret_false()

tf_inst.ret_false(1, "xyz", arg1=7)


#===============================================================================
# Metaclasses usage:
# - Modifying the class dictionary prior to the class being created
# - Returning an instance of another class – essentially performing the role of a factory function.
# - Really useful to modify classes (e.g. decorate classes methods) dynamically:
#    - Logging
#    - Timing or profiling
#    - Caching
#    - ...
#===============================================================================


#===============================================================================
# SOURCES:
# - http://docs.python.org/2/reference/datamodel.html#customizing-class-creation
# - http://www.voidspace.org.uk/python/articles/metaclasses.shtml
#===============================================================================
