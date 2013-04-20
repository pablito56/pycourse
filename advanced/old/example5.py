#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 5: Let's set values to attributes
'''

# Let's create a descriptor just with __set__
class VerboseDescriptor(object):
    def __set__(self, inst, val):
        print("Calling __get__ on instance of {0}".format(self.__class__.__name__))
        print("\tself:", self)
        print("\tinst:", inst)
        print("\tval:", val)
class MyVerboseClass(object):
    attr = VerboseDescriptor()
    
#===========================================================================
# Note that it receives the new value instead of the class
#===========================================================================

# Let's check how it works
inst = MyVerboseClass()
print(inst)
print(inst.__dict__)
print(MyVerboseClass.__dict__)
inst.attr = 12345
print(inst)
print(inst.__dict__)
print(MyVerboseClass.__dict__)

#===========================================================================
# Note that NO modification have been done to __dict__
#===========================================================================
