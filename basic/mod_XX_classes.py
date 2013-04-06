#-*- coding: utf-8 -*-
u'''
MOD 10: Classes
'''


# Let's see how to define custom classes


class Spam:          # class keyword, camel case class name and colon :
    pass

spammer = Spam()     # Class instantiation, spammer becomes an instance of Spam

print spammer
print type(spammer)


# Easy, right?

#==============================================================================
# - Why type says it is an instance?
#==============================================================================


class Spam(object):  # Ancestor superclasses inside parentheses after class name
    pass

spammer = Spam()

print spammer
print type(spammer)

#===============================================================================
# - All classes must inherit from object (or from a subclass of object)
#    - More about this in new-style vs old-style module
#===============================================================================


class Eggs(Spam):                                   # Ancestor superclasses inside parentheses
    this_is_a_class_attrib = "class_attrib_value"   # Class attributes inside the body, outside class methods

    def __init__(self, instance_attrib_val):        # __init__ is the method called in the instances initialization (not constructor)
        self.instance_attrib = instance_attrib_val

    def method(self, arg1, arg2=None):              # All methods must receive self (the instance) as first parameter
        print "This is 'method' of", self
        print self.instance_attrib, arg1, arg2      # Access instance attributes through self with a dot .

    def second_method(self):
        self.method("from 2nd method")              # Methos may call other methods using self with a dot .


# Still easy?


my_instance_attrib_value = 12.345
egger = Eggs(my_instance_attrib_value)              # Provide __init__ arguments in the instantiation

print egger
print type(egger)


print egger.instance_attrib                         # Retrieve instance attributes with a dot

print egger.this_is_a_class_attrib                  # Retrieve class attributes with a dot

print Eggs.this_is_a_class_attrib

print Eggs

#===============================================================================
# - Class attributes can be retrieved directly from the class too
# - Classes are objects too
#===============================================================================


egger.method("arg1_value", "arg2_value")            # Call instance methods with a dot . and Python passes it as self

print egger.method

print Eggs.method

inst_method = egger.method
inst_method("arg1_value", "arg2_value")

#===============================================================================
# - Methods are also attributes (bounded) of classes and instances
#===============================================================================


class Spam(object):
    spam_class_attrib = "spam"                             # Class attributes must have value always (you may use None...)

    def spam_method(self):
        print "spam_method", self, self.spam_class_attrib
        print self.__class__                               # __class__ is a reserved attribute containing the class of any object


class Eggs(object):
    eggs_class_attrib = "eggs"

    def eggs_method(self):
        print "eggs_method", self, self.eggs_class_attrib
        print self.__class__


class Fooo(Spam, Eggs):                                    # Specify a list of ancestor superclasses
    fooo_class_attrib = "fooo"

    def fooo_method(self):
        self.spam_method()
        self.eggs_method()                                 # Retrieve superclasses attributes as if they were yours
        print "fooo_method", self, self.fooo_class_attrib
        print self.__class__

foooer = Fooo()

foooer.fooo_method()

foooer.spam_method()

foooer.eggs_method()  # self is ALWAYS an instance of the same class

print foooer.spam_class_attrib
print foooer.eggs_class_attrib
print foooer.fooo_class_attrib  # We have access to all own and ancestors' attributes


# Given that Python is a dynamic language...

class Spam(object):
    pass

spammer = Spam()
spammer.name = "John"
spammer.surname = "Doe"
spammer.age = 65
spammer.male = True      # ... this is legal

print spammer.name
print spammer.surname
print spammer.age
print spammer.male


# What about static or class methods?

class Spam(object):
    def method(self, arg=None):
        print "Called 'method' with", self, arg

    @classmethod                                    # This is a decorator
    def cls_method(cls, arg=None):
        print "Called 'cls_method' with", cls, arg

    @staticmethod                                   # This is another decorator
    def st_method(arg=None):
        print "Called 'st_method' with", arg

spammer = Spam()

spammer.method(10)

Spam.method(spammer, 100)   # Although it works, this is not exacty the same

print spammer.method
print Spam.method           # It is unbounded, not related with an instance

spammer.cls_method(20)

Spam.cls_method(200)

print spammer.cls_method
print Spam.cls_method     # Both are a bounded method... to the class

spammer.st_method(30)

Spam.st_method(300)

print spammer.st_method
print Spam.st_method     # Both are plain standard functions


#===============================================================================
# REMEMBER:
#     - Classes are declared with the 'class' keyword, its name in camel case and a colon
#         - Specify ancestors superclasses list between parrentheses after the class name
#     - Use indentation for class body declaration
#     - Specify class attributes (with value) inside the class, outside any method
#     - Specify methods inside the body, with indentation (method body has 2x indentation)
#         - Method's first parameter is always self, the instance whose method is being called
#         - Use self to access attributes and other methods of the instance
#     - When inheriting, ancestors attributes and methods can be accessed transparently
#     - There are no private attributes in Python
#         - There is a convention to use underscore _ prefix
#     - Classes definition is not closed. At any time you can add (or delete) an attribute
#     - classmethod to specify class methods; bounded to the class, not its instances
#        - Used to implement alternative constructors (e.g. dict.copy)
#     - staticmethod to specify static methods; standard functions delcared inside the class
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#a-first-look-at-classes
#===============================================================================
