#-*- coding: utf-8 -*-
u"""
MOD: Testing, library to test
"""


def sum(x, y):
    """Sums two numbers
    """
    return x + y


def subs(x, y):
    """Substract two numbers
    """
    return x - y


def mul(x, y):
    """Multiply two numbers
    """
    return x * y


def div(x, y):
    """Divide two numbers
    """
    return x / y


def fail(x, y):
    """Raises ValueError(x, y)
    """
    raise ValueError(x, y)
