#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 3: Let's understand descriptors parameters
'''

class VerboseDescriptor(object):
    def __get__(self, inst, cls):
        print("Calling __get__ on instance of {0}".format(self.__class__.__name__))
        print("\tself:", self)
        print("\tinst:", inst)
        print("\tcls:", cls)

class MyVerboseClass(object):
    attr = VerboseDescriptor()

# Let's check how it works
inst = MyVerboseClass()
print(inst)
print(inst.__dict__)
print(MyVerboseClass.__dict__)
print(inst.attr)

# Now with the class
print(MyVerboseClass.attr)
