#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: Implement the following classes 
'''

class VerboseDict:
    '''
        >>> verbose = VerboseDict()
        >>> verbose['item'] = 5
        __setitem__, item, 5
        >>> verbose.item 
        __getattribute__, item
        >>> verbose['item']
        __getitem__, item
        >>> verbose.item = 2
        __setattribute__, item
        >>> verbose.it
        __getattribute__, it
        __getattr__, it
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "<stdin>", line 16, in __getattr__
        AttributeError: type object 'dict' has no attribute '__getattr__'
    '''
    pass

class AttrDict:
    '''
        Access to dict keys by attribute
        Update dict keys if setting an existing key by attribute
        del if exists

        >>> attrdict = AttrDict()
        >>> attrdict['non_existing_key']
        KeyError: 'non_existing_key'
        >>> attrdict.non_existing_key
        AttributeError: 'non_existing_key'
        >>> attrdict['item'] = 5
        >>> attrdict.item = 6
        >>> attrdict.item
        6
        >>> attrdict['item']
        6
    '''
    pass

