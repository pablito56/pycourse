#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD: Debugging
"""


#===============================================================================
# - 'pdb' is Python's interactive debugger
# - It provides command line and programmatic interfaces
#===========================================================================


#===========================================================================
# EXERCISE:
# - Execute mod_debugging_2.py with pdb from command line:
#    $ python -m pdb mod_debugging_2.py
#
# - Type 'h' or 'help' to check available debugger commands
# - Type 'next' several times and check the backtrace
#===========================================================================


#===========================================================================
# EXERCISE:
# - Execute mod_debugging_2.caller_func with pdb from a Python interpreter:
#    $ python
#     >>> import pdb
#     >>> import mod_debugging_2
#     >>> pdb.run('mod_debugging_2.caller_func()')
#     > <string>(1)<module>()
#     (Pdb)
#
# - Type 'h' or 'help' to check available debugger commands
# - Type 'next' and check the backtrace
#===============================================================================


import ipdb  # Much better than standard library debugger


#===========================================================================
# EXERCISE:
# - Execute this file with Python
#    $ python mod_debugging.py
#
# - Type 'h' or 'help' to check available debugger commands
#    - Besides debugger commands you can execute Python code, check variables...
# - Try to call another_func(123, 456)
# - Check the backtrace
#===========================================================================


def another_func(arg1, arg2):
    print "Another func was called:", arg1, arg2


def func_to_fail():
    ipdb.set_trace()  # It will open ipdb debugger console
    my_string = "This is a string"
    my_float = 123.456
    another_func(my_string, my_float)
    raise ValueError(13)


def caller_func():
    func_to_fail()


if __name__ == "__main__":
    caller_func()
