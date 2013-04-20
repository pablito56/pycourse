#-*- coding: utf-8 -*-
u'''
DESCRIPTORS EXAMPLE 0: How attributes look up works
'''

# Let's define a class with 'class' and 'instance' attributes
class MyClass(object):
    class_attr = "Value of class attrib"
    def __init__(self):
        self.instance_attr = "Value of instance of {0} attrib".format(self.__class__.__name__)
    def a_method(self):
        print "A method was called on", self
        
# Let's instantiate it and access the attributes
inst = MyClass()
print inst.class_attr
print inst.instance_attr

# Let's access attributes in a different way
print inst.__getattribute__("class_attr") # http://docs.python.org/2/reference/datamodel.html#more-attribute-access-for-new-style-classes
print getattr(inst, "instance_attr")
print getattr(inst, "unknown_attr", "This attribute was not found!!") # http://docs.python.org/2/library/functions.html#getattr

# Let's check the instance and class __dict__
print inst.__dict__
print MyClass.__dict__

#===========================================================================
# _ __dict__ is the object dictionary. All (new style) Python objects have it
# - So there is instance and class __dict__
# - Class attributes are stored in class __dict__
#===========================================================================

# Let's change the attributes values
new_inst = MyClass()
inst.class_attr = 12345
inst.instance_attr = 67890
new_inst.instance_attr = "BBBB"

# Let's check what was changed
print inst.__dict__
print MyClass.__dict__
print new_inst.__dict__

#===========================================================================
# - Instance __dict__ overrides the classes __dict__ (or is looked up in first place)
# - Changed attributes value is stored in the instance __dict__
#===========================================================================

# Let's see how inheritance works
class MyClassInh(MyClass):
    pass
inst_inh = MyClassInh()
print inst_inh.class_attr
print inst_inh.instance_attr # Note that now it prints a different message

# Let's check their __dict__
print inst_inh.__dict__
print MyClassInh.__dict__

#===========================================================================
# - Each superclass holds its own __dict__
# - They are looked up in order
#===========================================================================

# Let's try to list all __dict__ elements for an instance
lst = MyClass.__dict__.keys()
lst.extend(MyClassInh.__dict__.keys())
lst.extend(inst_inh.__dict__.keys())
print sorted(list(set(lst)))

# Trick: http://docs.python.org/2/library/functions.html#dir
print dir(inst_inh)

# Let's manually add a new instance attribute
inst_inh.__dict__['new_instance_attr'] =  "New value of instance of MyClassInh attrib"
print inst_inh.new_instance_attr
print inst_inh.__dict__

# Let's try to go a bit further
try:
    MyClassInh.__dict__['new_class_attr'] = 9
except TypeError, e:
    print e
