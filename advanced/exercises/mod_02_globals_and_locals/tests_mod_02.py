#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Created on Nov 13, 2012

@author: pablito56

@license: MIT

@contact: pablito56@gmail.com

Module 02 (globals and locals) exercise: add a clear method

>>> import exercise_mod_02 as cache_mod

>>> cache_mod.set_key("my_key", "my_value")

>>> print cache_mod.CACHE["my_key"]
(1366544507.87305, 'my_value')  # (expiration time, value)

>>> print cache_mod.get_key("my_key")
my_value

>>> print cache_mod.clear()

>>> print cache_mod.get_key("my_key")
None
"""
import unittest
import exercise_mod_02 as cache_mod
# import solution_mod_02 as cache_mod


class TestClearCache(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Increase output detail in case of errors
        """
        cls.maxDiff = None
        cls.longMessage = True

    def setUp(self):
        """Setup: ensure cache is empty before each test
        """
        cache_mod.clear_keys()

    def tearDown(self):
        pass

    def test_set_get(self):
        """Test that we can set and get a key value in the cache
        """
        key = "key1"
        value = "value1"
        cache_mod.set_key(key, value)
        self.assertEqual(cache_mod.get_key(key), value,
                         "Wrong value returned in test_set_get")
        self.assertTrue(len(cache_mod.CACHE) == 1,
                        "Wrong size of cache in test_set_get")

    def test_cache_ttl(self):
        """Test that values ttl is taken into account
        """
        key1 = "key_ttl_1"
        value1 = "value_ttl_1"
        key2 = "key_ttl_2"
        value2 = "value_ttl_2"
        ttl = 0.2
        cache_mod.set_key(key1, value1)
        cache_mod.set_key(key2, value2, ttl)
        self.assertEqual(cache_mod.get_key(key1), value1,
                         "Wrong key1 value returned in test_cache_ttl before sleep")
        self.assertEqual(cache_mod.get_key(key2), value2,
                         "Wrong key2 value returned in test_cache_ttl before sleep")
        self.assertTrue(len(cache_mod.CACHE) == 2,
                        "Wrong size of cache in test_cache_ttl before sleep")
        from time import sleep
        sleep(ttl)
        self.assertEqual(cache_mod.get_key(key2), None,
                         "Wrong expired key2 value returned in test_cache_ttl after sleep")
        self.assertEqual(cache_mod.get_key(key1), value1,
                         "Wrong key1 value returned in test_cache_ttl after sleep")
        self.assertTrue(len(cache_mod.CACHE) == 1,
                        "Wrong size of cache in test_cache_ttl after sleep")
        sleep(cache_mod.CACHE_TTL)
        self.assertEqual(cache_mod.get_key(key1), None,
                         "Wrong expired key1 value returned in test_cache_ttl after second sleep")
        self.assertTrue(len(cache_mod.CACHE) == 0,
                        "Wrong size of cache in test_cache_ttl after second sleep")

    def test_cache_size(self):
        """Test that cache size is never exceeded and older (first) items are removed
        """
        key = "key_size"
        value = "value_size"
        for index in xrange(10):
            cache_mod.set_key(key + str(index), value + str(index))
        self.assertTrue(len(cache_mod.CACHE) == cache_mod.CACHE_SIZE,
                        "Wrong size of cache in test_cache_size")
        for index in xrange(5):
            self.assertEqual(cache_mod.get_key(key + str(index)), None,
                             "Wrong old {} value value returned in test_cache_size".format(key + str(index)))
        for index in xrange(5, 10):
            self.assertEqual(cache_mod.get_key(key + str(index)), value + str(index),
                             "Wrong {} value value returned in test_cache_size".format(key + str(index)))

    def test_clear(self):
        """Test that we can clear the whole cache content
        """
        key = "key_size"
        value = "value_size"
        for index in xrange(cache_mod.CACHE_SIZE):
            cache_mod.set_key(key + str(index), value + str(index))
        self.assertTrue(len(cache_mod.CACHE) == cache_mod.CACHE_SIZE,
                        "Wrong size of cache in test_clear before clear")
        cache_mod.clear_keys()
        self.assertTrue(len(cache_mod.CACHE) == 0,
                        "Wrong size of cleared cache in test_clear after clear")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
