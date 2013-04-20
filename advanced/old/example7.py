#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 7: Introducing the slots
'''

class MySlottedClass(object):
    __slots__ = ['a', 'b']

# Let's instantiate
inst = MySlottedClass()
inst.a = 12345
inst.b = 67890

# Ok. Nothing strange...
try:
    inst.c = 54321
except AttributeError, e:
    print e

# WTF! Let's check the __dict__'s
try:
    print inst.__dict__
except AttributeError, e:
    print e
print MySlottedClass.__dict__

# How it works internally
print MySlottedClass.__dict__['a'].__get__(inst, MySlottedClass)
MySlottedClass.__dict__['a'].__set__(inst, 100001)
print inst.a

#===========================================================================
# Slots:
# - Light control of objects structure (can be bypassed!)
# - Faster access
# - Lower size
# - Improve efficiency (storage and speed)
# - Really useful to handle huge amounts of objects 
#===========================================================================
