#-*- coding: utf-8 -*-
u"""
MOD 02: global, globals and locals
"""


# Let's continue with a small exercise before diving into scopes and namespaces


#===============================================================================
# EXERCISE: pycourse/advanced/exercises/exercises/mod_02_globals_and_locals/exercise_mod_02
#
# - Modify our simple in-memory cache:
#     - Add a method to clear the cache content (don't use dict.clear())
#
# - Check the documentation
#
# - Run the tests in 'tests_mod_02.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_02.py'
#===============================================================================


import time
from collections import OrderedDict


CACHE = OrderedDict()
CACHE_SIZE = 5
CACHE_TTL = 10


def set_key(key, value, ttl=None):
    """Set a key value in the cache with its expiration time.
    If no ttl is provided CACHE_TTL is taken by default.
    If cache length exceeds CACHE_SIZE when adding a key, the oldest (first inserted) key is removed (FIFO)
    """
    CACHE[key] = (time.time() + (ttl or CACHE_TTL), value)
    if len(CACHE) > CACHE_SIZE:
        CACHE.popitem(last=False)


def get_key(key):
    """Retrieve a key value from the cache.
    Returns None if does not exist or the key expired.
    If the key expired it is removed from the cache.
    """
    content = CACHE.get(key, None)
    if content:
        if content[0] > time.time():
            return content[1]
        else:
            del CACHE[key]
    return None


def clear_keys():
    """Remove all cache keys content
    """
    global CACHE  # global statement does all the magic
    CACHE = OrderedDict()


set_key("my_key", "my_value")
print CACHE
print CACHE["my_key"]
print get_key("my_key")
clear_keys()
print CACHE
print get_key("my_key")


# Another example
my_global_var = 0


def func_a():
    global my_global_var
    my_global_var = "A"  # Value (binding) is changed in module's global scope
    print "INSIDE func_a:", my_global_var


def func_b():
    my_global_var = "B"  # Value (binding) is changed only in local scope
    print "INSIDE func_b:", my_global_var


func_a()
print "AFTER func_a:", my_global_var
func_b()
print "AFTER func_b:", my_global_var  # Value was changed only in local scope


#==============================================================================
# - Python 'global' statement
#    - Listed identifiers are to be interpreted as globals
#        - They are defined in CURRENT module's namespace
#        - Their value can be modified
#    - This declaration holds for the entire current code block
#    - There are some restrictions on how global names can be used
#
# - Python 'nonlocal' statement (ONLY IN Py3k!)
#    - Listed identifiers refer to previously bound variables in the nearest enclosing scope
#    - It allows rebinding variables outside of the local scope and besides the global (module) scope
#    - It must refer to pre-existing bindings in an enclosing scope!
#==============================================================================


# Let's see more useful stuff


def func_a():
    print "INSIDE func_a globals:", globals().keys()  # Even 'func_a' appears in globals
    print
    print "INSIDE func_a locals:", locals()
    print
    global another_global_var  # This time we use a different attribute
    another_global_var = "AAA"
    print "INSIDE func_a:", another_global_var
    print
    print "EXITING func_a globals:", globals().keys()  # The value has been updated directly in globals
    print
    print "EXITING func_a locals:", locals()  # Locals remains empty


def func_b():
    print "INSIDE func_b globals:", globals().keys()
    print
    print "INSIDE func_b locals:", locals()
    print
    another_global_var = "BBB"
    print "INSIDE func_b:", another_global_var
    print
    print "EXITING func_b globals:", globals().keys()  # The value remains unchanged in globals
    print
    print "EXITING func_b locals:", locals()  # Now locals is not empty


func_a()

func_b()


#===============================================================================
# EXERCISE:
#
# - Open python interpreter in current folder
#
# - Declare a new attribute
#    >>> new_global_var = "xyz"
#
# - Check gobals() and locals()
#
# - Import func_c and execute it
#    >>> from mod_02_globals_and_locals import func_c
#    ...
#    >>> func_c()
#
# - WHAT HAPPENED WITH YOUR NEW GLOBAL ATTRIBUTE?
#===============================================================================


def func_c():
    g = globals()
    for k in g:
        if k != "__builtins__":
            print k, "==>", g[k]
    print "new_global_var ==>", g.get("new_global_var")


#==============================================================================
# - globals()
#    - Return a dictionary representing the current global symbol table
#    - This is always the dictionary of the current module (inside a function or
#      method, this is the module where it is defined, not the module from which
#      it is called)
#
# - locals()
#    - Update and return a dictionary representing the current local symbol table
#    - The contents of this dictionary should not be modified
#==============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces
#  - http://docs.python.org/2/reference/simple_stmts.html#global
#  - http://docs.python.org/3/reference/simple_stmts.html#nonlocal
#  - http://docs.python.org/2/library/functions.html#globals
#  - http://docs.python.org/2/library/functions.html#locals
#===============================================================================
