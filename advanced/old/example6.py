#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 6: Let's really use the __set__
'''

class TypedAttrib(object):
    def __init__(self, name, typ):
        self.name = name
        # Avoid using 'type' as attribute name
        self.typ = typ
    def __set__(self, inst, val):
        if isinstance(val, self.typ):
            inst.__dict__[self.name] = val
        else:
            raise TypeError("TypeError: Wrong data type '{0}'".format(val))

#===========================================================================
# Note that it is a really bad idea! Duck typing FTW!!
#===========================================================================

# Let's use it
class MyTypedClass(object):
    string = TypedAttrib('string', str)
    integer = TypedAttrib('integer', int)
inst = MyTypedClass()
inst.string = "123"
print(inst.__dict__)

# Let's make it fail
try:
    inst.string = 123
except TypeError, e:
    print e
print(inst.__dict__) # Note that no modification has been done
