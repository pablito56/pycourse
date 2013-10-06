#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Oct 5, 2013

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 05 functools solution

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
from functools import partial


def power_of(x):
    """Generator returning powers of the provided number
    """
    for index in count():
        yield pow(x, index)


def power_of(x):
    """Generator returning powers of the provided number (faster)
    """
    return (pow(x, index) for index in count())


def power_of(x):
    """Generator returning powers of the provided number (fastest)
    """
    pow_of_x = partial(pow, x)
    return imap(pow_of_x, count())
