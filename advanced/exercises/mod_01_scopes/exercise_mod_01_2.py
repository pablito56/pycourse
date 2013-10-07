#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: exercise to an adapted story
'''
import unittest

def power_factory():
    '''function that implements the following interface
        
        >>> power_2 = power_factory(2)
        >>> power_2(10)
        1024
        >>> power_3(10)
        59040
    '''
    pass


class PowerFactoryTest(unittest.TestCase)

    def test_power_2(self):
        power_2 = power_factory(2)
        self.assertTrue(power_2(10), 1024)

    def test_power_3(self):
        power_3 = power_factory(3)
        self.assertTrue(power_3(10), 59049)

    def test_power_2_3(self):
        power_2 = power_factory(2)
        power_3 = power_factory(3)
        self.assertTrue(power_2(10), 1024)
        self.assertTrue(power_3(10), 59049)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

