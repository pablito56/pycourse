#-*- coding: utf-8 -*-
u'''
MOD 13: Modules and packages
'''


#===============================================================================
# WHAT IS A PYTHON MODULE?
#===============================================================================


#===============================================================================
# - A module is a file containing Python definitions and statements.
# - Python interpreter reads the file and evaluates its definitions and statements.
#    - Python does not accept dashes - in modules names
#===============================================================================


print "'__name__' value:", __name__


#===============================================================================
# - The file name is the module name with the suffix .py appended.
# - Global variable '__name__' contains the name of current module.
# - Functions and classes also have a variable containing their module name
#===============================================================================


def func():
    print "Called func in", __name__

print "'func.__module__' value:", func.__module__


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Execute this module with Python:
##    $ python mod_13_modules_and_packages.py.py
##
## - Open Python interpreter and import this module:
##    $ python
##      ...
##    >>> import mod_13_modules_and_packages.py
##
## - WHAT HAPPENED? Where is the 'Inside if...' trace?
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
# - The module name can take a special value such as '__main__', '__console__'...
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - The module name depends on how the module is being evaluated (imported or executed)
# - The module name can take a special value such as '__main__', '__console__'...
#    - Use if __name__ == "__main__": to detect when a module (script) is imported or executed
#===============================================================================


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Without closing the Python interpreter import the module again:
##    >>> import mod_13_modules_and_packages.py
##
## - WHAT HAPPENED? Where are all the output traces?
##
##===============================================================================
##===============================================================================


#===============================================================================
# - All code is evaluated (executed) only once the first time it is imported
#===============================================================================


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Go to parent folder, open Python interpreter and import the module:
##    $ cd ..
##    $ python
##      ...
##    >>> import basic.mod_13_modules_and_packages.py
##
## - Close the interpreter
##
## - Create the file basic/__init__.py with the content 'print "This is the __init__.py", __name__'
##    $ echo -e 'print "This is the __init__.py", __name__\n' > basic/__init__.py
##
## - Open Python interpreter and try to import the module again:
##    $ python
##      ...
##    >>> import basic.mod_13_modules_and_packages.py
##
## - WHAT HAPPENED? What is the module name? What does the __init__.py file mean?
##
##===============================================================================
##===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Packages are folders with a __init__.py file
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Packages are folders with a __init__.py file
#    - This __init__.py is also evaluated, so it may contain code
#    - The __init__.py is actually the package (check its module name)
#===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Packages are folders with a __init__.py file
#    - This __init__.py is also evaluated, so it may contain code
#    - The __init__.py is actually the package (check its module name)
# - The module name depends on the packages path
#===============================================================================


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Without closing Python interpreter, execute the function we defined:
##    >>> basic.mod_13_modules_and_packages.py.func()
##
## - Close the Python interpreter
##
## - Open Python interpreter and import this module in a different way:
##    $ python
##      ...
##    >>> from basic import mod_13_modules_and_packages.py
##
## - WHAT HAPPENED? What is the module name?
##
## - Execute the function again:
##    >>> mod_13_modules_and_packages.py.func()
##
## - Import and execute the function again in a different way:
##    >>> from basic.mod_13_modules_and_packages.py import func
##    >>> func()
##
## - Execute the following:
##    >>> print mod_13_modules_and_packages.py
##
## - Import again the module in a different way and execute the function:
##    >>> from basic import mod_13_modules_and_packages.py as the_module
##    >>> the_module.func()
##    >>> print the_module.__name__
##
## - WHAT HAPPENED? What is the module name?
##
##===============================================================================
##===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Modules are objects too, and their variables, functions and classes are their attributes
# - Modules can be imported in different ways:
#    - import packages.path.to.module.module_name
#    - from packages.path.to.module import module_name_1, module_name_2
#    - from packages.path.to.module import (module_name_1, module_name_2,
#                                           module_name_3, module_name_4)
#    - from packages.path.to.module import module_name as new_module_name
#        - You are binding the module to another name, like you do with lists or strings
# - Modules is indepent on how you call (bind) them when importing
#===============================================================================


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Without closing Python interpreter, execute the following:
##    >>> print dir(the_module)
##    >>> import basic
##    >>> print dir(basic)
##
## - Close the Python interpreter
##
## - Open Python interpreter and repeat last two commands:
##    >>> import basic
##    >>> print dir(basic)
##
## - WHAT HAPPENED? Where is our module?
##
## - Close the interpreter
##
## - Edit the file basic/__init__.py and add at the end 'from mod_13_modules_and_packages.py import func'
##    $ echo -e 'from mod_13_modules_and_packages.py import func\n' >> basic/__init__.py  # Don't forget double >
##
## - Open Python interpreter and try again:
##    $ python
##      ...
##    >>> import basic
##    >>> print dir(basic)
##
## - WHAT HAPPENED? How they appeared?
##
##===============================================================================
##===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Importing a package does not import its whole content
# - __init__.py is used for package initialization and for exposing desired content
#     - Avoids that 3rd parties using your code have to know its internal structure
#===============================================================================


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Close the interpreter
##
## - Edit the file basic/__init__.py and add at the end '__all__ = ["mod_03_numbers"]'
##    $ echo -e '__all__ = ["mod_03_numbers"]\n' >> basic/__init__.py  # Don't forget double >
##
## - Open Python interpreter and try again:
##    $ python
##      ...
##    >>> import basic
##    >>> print dir(basic)
##
## - Now execute the following:
##    >>> from basic import *
##    >>> print dir(basic)
##
## - WHAT HAPPENED? What is that text?
##
##===============================================================================
##===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - It is possible to import all contents of a package or module
#    - from packages.path.to.module import *
#    - It is inefficient if you don't need everything
# - __all__ is used to define what will be imported with the asterisk *
#===============================================================================


#===============================================================================
# THERE IS STILL MORE:
# - You could use relative imports
#    - from . import mod_03_strings
#    - from .. import advaqnced
#    - from ..advaqnced import mod_XX_data_model_customisation
#        - Single dot . represents current package
#        - Additional dots represent parent packages
# - Note that these imports are resolved with the __name__ of the importing module,
#   so they don't work in main modules (executed directly)
#===============================================================================


# How does module lookup work?


##===============================================================================
##===============================================================================
## EXERCISE:
##
## - Close the interpreter
##
## - Go to your home folder:
##    >>> cd
##
## - Open Python interpreter and try to import the package:
##    $ python
##      ...
##    >>> import basic
##
## - Close the interpreter
##
## - Set an environment variabe called PYTHONPATH with the path to pycourse. For example:
##    $ export PYTHONPATH=$PYTHONPATH:/Users/pev/wspace/pycourse/
##
## - Open Python interpreter and try to import:
##    $ python
##      ...
##    >>> import basic
##    >>> print basic.__file__
##
## - Execute the following:
##    >>> import sys
##    >>> print sys.path
##
## - Add the folder of the course basic block to this list:
##    >>> sys.path.append("/Users/pev/wspace/pycourse/basic")
##
## - Import again this module:
##    >>> import mod_13_modules_and_packages.py
##    >>> print mod_13_modules_and_packages.py.__file__
##
## - WHAT HAPPENED? What is the module name?
##
##===============================================================================
##===============================================================================


#===============================================================================
# LESSONS LEARNT:
# - Modules attribute __file__ contains the its full file path
#    - Useful to ensure that you are importing what you really want
#
# - Python modules look up process:
#    - Current folder, or
#    - The PYTHONPATH environment variable, or
#    - The installation dependant default (site-packages or dist-packages)
#        - This folder is built on startup relatively to Python binary location
#
# - It is possible to retrieve and even modify the look up path
# - It is possible to permanently add folders to Python path with .pth files
#    - Those files must contain full folder paths (in different lines) and must
#      be added to a location already in Python path (e.g. site-packages)
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/modules.html
#  - https://colabora.pdi.inet/kbportal/PLCwiki/Guidelines/DEV/Standard%20directory%20structure%20for%20projects/in%20Python/Django.aspx
#===============================================================================
