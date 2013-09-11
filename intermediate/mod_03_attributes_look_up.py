#-*- coding: utf-8 -*-
u'''
MOD 03: Attribute look up
'''


# Let's define a class with 'class' and 'instance' attributes
class MyClass(object):
    class_attr = "Value of class attrib"

    def __init__(self):
        self.instance_attr = "Value of instance attrib of {0}".format(self.__class__.__name__)

    def a_method(self):
        print "A method was called on", self


# Let's instantiate it and access the attributes
inst = MyClass()
print inst.class_attr
print inst.instance_attr


# Let's access attributes in a different way

print getattr(inst, "class_attr")

print getattr(inst, "instance_attr")

print getattr(inst, "unknown_attr")

print getattr(inst, "unknown_attr", "This attribute was not found!!")


# What about the other way?


setattr(inst, "instance_attr", "New instance attrib value")
print getattr(inst, "instance_attr")


#===============================================================================
# - getattr returns the value of the named attribute of an object:
#    - getattr(x, 'foobar') is equivalent to x.foobar
#    - A default value can be provided in case attribute is not found
#
# - setattr is its counterpart:
#    - setattr(x, 'foobar', 5) is equivalent to x.foobar = 5
#===============================================================================


# How do these functions work?

# Do you remember everything in Python is an object? It turns out objects are actually dicts


print inst.__dict__.get("instance_attr")

print inst.__dict__.get("unknown_attr", "This attribute was not found!!")

print inst.__dict__


# Where is the class attribute?


print MyClass.__dict__


#===========================================================================
# _ __dict__ is the object dictionary. All (new-style) Python objects have it
#    - There is instance and class __dict__
#    - Class attributes are stored in class __dict__
#===========================================================================


# Let's create a new instance and change some attributes values
new_inst = MyClass()
new_inst.instance_attr = "BBBB"

inst.class_attr = 12345
inst.instance_attr = 67890


# Let's check what has changed
print inst.__dict__

print new_inst.__dict__

print MyClass.__dict__


#===========================================================================
# - Instance __dict__ overrides the classes __dict__ (or is looked up in first place)
# - All changed (class or instance) attributes value is stored in the instance __dict__
#===========================================================================


# Let's see how inheritance works
class MyClassInh(MyClass):
    sub_class_attr = "Value of subclass attrib"


inst_inh = MyClassInh()
print inst_inh.class_attr
print inst_inh.instance_attr  # Note that now it prints a different message


# Let's check their __dict__
print inst_inh.__dict__

print MyClassInh.__dict__

print MyClass.__dict__

#===========================================================================
# - Each superclass holds its own __dict__
# - They are looked up in order
#===========================================================================


# Let's try to list all __dict__ elements for an instance
lst = MyClass.__dict__.keys()
lst.extend(MyClassInh.__dict__.keys())
lst.extend(inst_inh.__dict__.keys())
print sorted(list(set(lst)))


# Do you remember 'dir' function to list content (attributes) of a module? It also works here
print dir(inst_inh)


# Let's manually add a new instance attribute
inst_inh.__dict__['new_instance_attr'] = "New value of instance of MyClassInh attrib"

print inst_inh.new_instance_attr
print inst_inh.__dict__


# Let's try to go a bit further
try:
    MyClassInh.__dict__['new_class_attr'] = 9
except TypeError, e:
    print "TypeError", e


#===========================================================================
# - Although it looks like a dict, it is not a conventional dict
#===========================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/functions.html#getattr
#  - http://docs.python.org/2/library/functions.html#setattr
#  - http://docs.python.org/2/library/functions.html#getattr
#===============================================================================
