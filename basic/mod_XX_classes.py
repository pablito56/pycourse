#-*- coding: utf-8 -*-
u'''
MOD 10: Classes
'''


# Let's see how to declare custom classes


class Spam:       # 'class' keyword, camel case class name and colon :
    pass

spammer = Spam()  # Class instantiation: spammer becomes an instance of Spam

print spammer


# Easy, right?


class Eggs(Spam):                       # Ancestor superclasses inside parentheses for inheritance
    a_class_attr = "class_val"          # Class attributes inside the body, outside class methods. Must have value

    def __init__(self, attr_val):       # __init__ is called in the instances initialization (not constructor)
        self.attr = attr_val

    def method(self, arg1, arg2=None):  # Method declaration. Indented and receiving self (the instance)
        print "'method' of", self
        print self.attr, arg1, arg2     # Access instance attributes using self with a dot .

    def second_method(self):
        self.attr = 99.99
        self.method("FROM 2nd")         # Methos may call other methods using self with a dot .


# Still easy?


egger = Eggs(12.345)                    # Provide __init__ arguments in the instantiation

print egger

print egger.attr                        # Retrieve instance attributes with a dot

print egger.a_class_attr                # Retrieve class attributes with a dot

print Eggs.a_class_attr

egger.a_class_attr = "new value"

print egger.a_class_attr
print Eggs.a_class_attr

#===============================================================================
# - Class attributes can be retrieved directly from the class
# - Instances only modify class attributes value locally
#===============================================================================


print Eggs

#===============================================================================
# - Classes are objects too:
#    - Python evaluates its declaration and instantiates a special object
#    - This object is called each time a new class instance is created
#===============================================================================


egger.method("value1", "value2")

egger.second_method()

print egger.method

print Eggs.method

inst_method = egger.method
inst_method("valueA", "valueB")


#===============================================================================
# - Methods are also attributes (bounded) of classes and instances
#===============================================================================


# Time to talk about new-style classes


class Spam:
    def spam_method(self):
        print self.__class__  # __class__ is a special attribute containing the class of any object
        print type(self)

spammer = Spam()

spammer.spam_method()

print spammer
print type(spammer)

#==============================================================================
# - Why type says it is an 'instance' and not a 'Spam'?
#==============================================================================


class Spam(object):           # Inherit from 'object'
    def spam_method(self):
        print self.__class__
        print type(self)

spammer = Spam()

print spammer
print type(spammer)           # This is a new-style class

#===============================================================================
# - New-style classes were introduced in Python 2.2 to unify classes and types
# - Provide unified object model with a full meta-model (more in the Advanced block)
# - Other benefits: subclass most built-in types, descriptors (slots, properties, static and class methods)...
# - By default all classes are old-style until Python 3
#    - In Python 2 you have to inherit from 'object' to use new-style
#    - You must avoid old-style
#    - So you must inherit ALWAYS from 'object'
#
# - Other changes introduced Python 2.2: __new__, new dir() behavior, metaclasses, new MRO (also in 2.3)
#
# - More info: http://www.python.org/doc/newstyle/
#===============================================================================


class OldStyleClass():
    pass

old_inst = OldStyleClass()
print type(old_inst)


# Let's inherit from an old-style class
class NewStyleSubClass(OldStyleClass, object):  # Multiple inheritance
    pass

new_inst = NewStyleSubClass()
print type(new_inst)

#===============================================================================
# - Inherit from both old-style classes and 'object' to obtain new-style classes
#===============================================================================


# Let's play a bit with inheritance


class Spam(object):
    spam_class_attr = "spam"                             # Class attributes must have value always (you may use None...)

    def spam_method(self):
        print "spam_method", self, self.spam_class_attr
        print self.__class__


class Eggs(object):
    eggs_class_attr = "eggs"

    def eggs_method(self):
        print "eggs_method", self, self.eggs_class_attr
        print self.__class__


class Fooo(Spam, Eggs):                                  # Specify a list of ancestor superclasses
    fooo_class_attr = "fooo"

    def fooo_method(self):
        self.spam_method()
        self.eggs_method()                               # Retrieve superclasses attributes as if they were yours
        print "fooo_method", self, self.fooo_class_attr
        print self.__class__

foooer = Fooo()

foooer.fooo_method()

foooer.spam_method()

foooer.eggs_method()  # self is ALWAYS an instance of the subclass

print foooer.spam_class_attr
print foooer.eggs_class_attr
print foooer.fooo_class_attr  # We have access to all own and ancestors' attributes


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
print Spam.st_method     # Both are a plain standard functions


# What happens with the class methods and inheritance?

class Eggs(Spam):
    pass

egger = Eggs()

egger.cls_method(20)

Eggs.cls_method(200)

print egger.cls_method
print Eggs.cls_method     # Now it is bounded to the subclass


#===============================================================================
# REMEMBER:
#     - Classes are declared with the 'class' keyword, its name in camel case and a colon
#         - Specify ancestors superclasses list between parrentheses after the class name
#         - So you must inherit ALWAYS from 'object' to have new-style classes
#     - Use indentation for class body declarations (attributes and methods)
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
#     - staticmethod to specify static methods; standard functions declared inside the class
#        - Only for organisation, it is equivalent to declare the function in the class module
#===============================================================================


# ===============================================================================
# TIME TO START WORKING:
#   - http://www.itmaybeahack.com/book/python-2.6/html/p03/p03c03_patterns.html#state
#   - how would you implement such a game?
#   - open basic/exercises/mod_XX_classes.py and implement it in there
# ===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#a-first-look-at-classes
#  - http://docs.python.org/2/library/functions.html#classmethod
#  - http://docs.python.org/2/library/functions.html#staticmethod
#  - http://docs.python.org/2/reference/compound_stmts.html#function
#  - http://docs.python.org/2/reference/datamodel.html#types (see Classes and Class instances)
#===============================================================================
