#-*- coding: utf-8 -*-
u'''
MOD 01: mutable and immutable types common errors
'''


def split_even_odd(numbers):
    '''Split incoming numbers iterable in two lists with even and odd numbers
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    even = odd = []
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd


class NumbersList(object):
    '''Class which handles even and odd numbers lists.
    Even numbers can be retrieved at any time with even attribute,
    Odd numbers with odd attribute
    '''
    even = []
    odd = []

    def append_number(self, num):
        '''Add a number to its corresponding list (even or odd)
        '''
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)


def update_even_odd(numbers, even=[], odd=[]):
    '''Update incoming even and odd numbers lists with corresponding values of numbers iterable.
    When no even or odd are provided, a default value is used.
    :param numbers: iterable with numbers
    :return (even, odd) lists with corresponding values
    '''
    for num in numbers:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    return even, odd
