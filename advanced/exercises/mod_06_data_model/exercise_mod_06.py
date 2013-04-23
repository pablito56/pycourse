#-*- coding: utf-8 -*-
u'''
Exercise 1: old-style vs. new-style, classes customization
'''


from optparse import OptionParser
from collections import OrderedDict


class CustomOptionParser(OptionParser):
    def __str__(self):
        return self.__class__.__name__


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        return OrderedDict.__getitem__(self, key)


class AttrDict(dict):
    def __getattr__(self, name):
        '''Called when an attribute lookup has not found the attribute in the usual places
        '''
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        '''Called when an attribute assignment is attempted
        '''
        self[name] = value

    def __delattr__(self, name):
        '''Called when an attribute deletion is attempted
        '''
        del self[name]
