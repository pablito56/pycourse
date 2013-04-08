#-*- coding: utf-8 -*-
u'''
Solution MOD 15: mutable and immutable types common errors
'''


# Multiple assignment of mutables
def split_even_odd(numbers):
    '''Split incoming numbers iterable in two lists with even and odd numbers
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    even = []
    odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd


# Mutable as class attribute
class NumbersList(object):
    '''Class which handles even and odd numbers lists
    '''
    even = None
    odd = None

    def __init__(self):
        self.even = []
        self.odd = []

    def append_number(self, num):
        '''Add a number to its corresponding list (even or odd)
        '''
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)


# Mutable as function default value
def update_even_odd(numbers, even=None, odd=None):
    '''Update incoming even and odd numbers lists with corresponding values of numbers iterable
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    if even is None:
        even = []
    if odd is None:
        odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd
