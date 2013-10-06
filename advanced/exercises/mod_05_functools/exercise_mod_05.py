#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 5, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 05 functools exercise

>>> it = power_of(2)

>>> it.next()
1

>>> it.next()
2

>>> it.next()
4

>>> it.next()
8

>>> it.next()
16

>>> it = power_of(3)

>>> it.next()
1

>>> it.next()
3

>>> it.next()
9
"""
from itertools import imap, count


def power_of(x):
    """Generator returning powers of the provided number
    """
    # Try to use imap and count (from itertools module)
    # You MUST use pow function in this exercise
    return count(1)
