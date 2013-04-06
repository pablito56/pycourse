#-*- coding: utf-8 -*-
u'''
MOD 10: Modules and packages
'''


#===============================================================================
# WHAT IS A PYTHON MODULE?
#===============================================================================


#===============================================================================
# - A module is a file containing Python definitions and statements.
# - Python interpreter reads the file and evaluates its definitions and statements.
#===============================================================================


print "'__name__' value:", __name__


#===============================================================================
# - The file name is the module name with the suffix .py appended.
# - Global variable '__name__' contains the name of current module.
# - Functions and classes also have a variable containing their module name
#===============================================================================


def func():
    pass

print "'func.__module__' value:", func.__module__


##===============================================================================
##===============================================================================
## EXERCISE:
## - Execute this module with Python:
##    $ python mod_10_modules.py
##
## - Open Python interpreter and import this module:
##    $ python
##      ...
##    >>> import mod_10_modules
##
## - Go to parent folder, open Python interpreter and import this module:
##    $ cd ..
##    $ python
##      ...
##    >>> import basic.mod_10_modules
##
## - Without closing Python interpreter, import the module again:
##    >>> import basic.mod_10_modules
##
## - WHAT HAPPENED? ANY IDEA?
##
##===============================================================================
##===============================================================================


if __name__ == "__main__":
    print "Inside if. This is evaluated only when the module is executed."

print "Outside if. This is evaluated always."


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
#    - It also depends on the packages path used in the import
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
#    - It also depends on the packages path used in the import
# - The module name can be a special values such as '__main__', '__console__'...
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
#    - It also depends on the packages path used in the import
# - The module name can be a special values such as '__main__', '__console__'...
#    - Use if __name__ == "__main__": to detect when a module (script) is imported or executed
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
#    - It also depends on the packages path used in the import
# - The module name can be a special values such as '__main__', '__console__'...
#    - Use if __name__ == "__main__": to detect when a module (script) is imported or executed
# - All code is evaluated (and executed) only once when imported
#===============================================================================
