#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 4: Let's see descriptors real usage
'''

# Let's create a class with a method
class MyClass(object):
    def a_method(self):
        print("Called a_method on", self)

# Let's instantiate it and call the method
inst = MyClass()
inst.a_method()
print(inst.a_method)

# Let's check its __dict__ content
print(inst.__dict__)
print(MyClass.__dict__)
print(MyClass.__dict__['a_method'])

# Let's play around with this method
print(MyClass.__dict__['a_method'].__get__)
print(MyClass.__dict__['a_method'].__get__(inst, MyClass))
print(MyClass.__dict__['a_method'].__get__(None, MyClass))

#===========================================================================
# - Functions are objects
# - Function class implements descriptors protocol
# - Good example of how descriptors can take instances or not 
#===========================================================================
