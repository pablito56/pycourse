#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 1: Simple descriptor example
A descriptor is an object attribute with “binding behavior”,
one whose attribute access has been overridden by methods in the descriptor protocol    
'''

# Let's define a descriptor
class RandAttr(object):
    def __init__(self, n=10):
        self.n = n
    def __get__(self, inst, cls):
        from random import randint
        print "Called __get__ of instance of {0}".format(self.__class__.__name__)
        return randint(0, self.n)

# Let's define a class with a descriptor attribute
class MyClass(object):
    rand_attr = RandAttr(20)

# Let's instantiate and access this attribute
inst = MyClass()
print inst.rand_attr

# Let's do it again
print inst.rand_attr

# And again
print inst.rand_attr

# Let's do it in a different ways
print inst.__getattribute__("rand_attr")
print getattr(inst, "rand_attr")

#===========================================================================
# Descriptor protocol implements at least one of the following:
# - descr.__get__(self, obj, type=None) --> value
# - descr.__set__(self, obj, value) --> None
# - descr.__delete__(self, obj) --> None
#
# It may intercept attribute retrieval, modification and/or deletion
#
# http://docs.python.org/2/howto/descriptor.html
#===========================================================================
