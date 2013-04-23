#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module XY (cooperative super call pattern) exercise: apply cooperative super call pattern
"""
from datetime import datetime
import unittest
import exercise_mod_07 as src
# import solution_mod_07 as src


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestAmazingDict(VerboseTestCase):
    '''Check AmazingDict MRO
    '''
    def test_attr_update(self):
        d = src.AmazingDict({'id': 1234})
        expected = {'id': 0000}
        d.id = expected['id']
        self.assertEqual(d, expected)

    def test_date_str(self):
        now = datetime.now()
        expected = {'date': now.isoformat()}
        d = src.AmazingDict()
        d['date'] = now
        self.assertEqual(d, expected)

    def test_attr_lower_update(self):
        d = src.AmazingDict({'id': 1234})
        expected = {'id': 0000}
        d.ID = expected['id']
        self.assertEqual(d, expected)

    def test_attr_lower_date_str_update(self):
        old = datetime.now()
        from time import sleep
        sleep(1)
        now = datetime.now()
        expected = {'date': now.isoformat()}
        d = src.AmazingDict({'date': old.isoformat()})
        d.DaTe = now
        self.assertEqual(d, expected)

    def test_mro(self):
        expected = (src.AmazingDict,
                    src.Attr,
                    src.Lower,
                    src.DateStr,
                    src.Verbose,
                    dict,
                    object)
        self.assertEqual(src.AmazingDict.__mro__, expected, "Wrong AmazingDict MRO")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
