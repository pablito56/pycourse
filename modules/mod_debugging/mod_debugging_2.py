#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD: Debugging
"""


#===========================================================================
# EXERCISE:
# - Execute this file with ipthon debugger
#    $ ipython --pdb mod_debugging_2.py
#
# - Type 'h' or 'help' to check available debugger commands
#===========================================================================


def another_func(arg1, arg2):
    print "Another func was called:", arg1, arg2


def func_to_fail():
    my_string = "This is a string"
    my_float = 123.456
    another_func(my_string, my_float)
    raise ValueError(13)


def caller_func():
    func_to_fail()


if __name__ == "__main__":
    caller_func()
