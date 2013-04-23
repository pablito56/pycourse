#-*- coding: utf-8 -*-
u'''
Test exercise 0: mutable and immutable types common errors
'''
import unittest
import exercise_1 as source
# import solution_1 as source


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestNewStyle(VerboseTestCase):
    '''Test exercise 1: new-style classes
    '''
    def test_old_style_inheritance(self):
        '''Check inheritance from old-style class as new-style
        '''
        custom_parser = source.CustomOptionParser()
        self.assertEqual(type(custom_parser), custom_parser.__class__, "Type and class difer in CustomOptionParser")


class TestCustomOrderedDict(VerboseTestCase):
    '''Test exercise 1: data model
    '''
    def test_slicing(self):
        '''Check __getitem__ customization (slicing) of CustomOrderedDict
        '''
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        slice_vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU")[2:4])
        #=======================================================================
        # CustomOrderedDict([('i', 'I'), ('o', 'O')])
        #=======================================================================
        self.assertEqual(vowels[2:4], slice_vowels, "Wrong slicing in CustomOrderedDict")
        self.assertEqual(vowels[2:-1], slice_vowels, "Wrong slicing in CustomOrderedDict")
        self.assertEqual(vowels[2:-10], source.CustomOrderedDict(), "Wrong slicing in CustomOrderedDict")

    def test_addition(self):
        '''Check __add__ customization of CustomOrderedDict
        It returns a new CustomOrderedDict with content of the first
        CustomOrderedDict updated with the second (it may be a list of pairs)
        '''
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        letters = zip("aixy", ["AA", "II", "XX", "Y"])
        expected = source.CustomOrderedDict(zip("aeiouxy", ["AA", "E", "II", "O", "U", "XX", "Y"]))
        #=======================================================================
        # CustomOrderedDict([('a', 'AA'), ('e', 'E'), ('i', 'II'), ('o', 'O'), ('u', 'U'), ('x', 'XX'), ('y', 'Y')])
        #=======================================================================
        self.assertEqual(vowels + letters, expected, "Wrong addition in CustomOrderedDict (list)")
        self.assertEqual(vowels + source.CustomOrderedDict(letters), expected, "Wrong addition in CustomOrderedDict (CustomOrderedDict)")
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")), "Wrong addition in CustomOrderedDict (modified self)")

    def test_substraction(self):
        '''Check __sub__ customization of CustomOrderedDict
        It returns a new CustomOrderedDict with content of the first
        CustomOrderedDict without the second's items (it may be a list of keys)
        '''
        vowels = source.CustomOrderedDict(zip("aeiou", "AEIOU"))
        #=======================================================================
        # CustomOrderedDict([('a', 'A'), ('e', 'E'), ('i', 'I'), ('o', 'O'), ('u', 'U')])
        #=======================================================================
        letters = "aixy"
        letters_cod = source.CustomOrderedDict(zip("aixy", ["AA", "II", "XX", "Y"]))
        expected = source.CustomOrderedDict(zip("eou", ["E", "O", "U"]))
        #=======================================================================
        # CustomOrderedDict([('a', 'AA'), ('e', 'E'), ('i', 'II'), ('o', 'O'), ('u', 'U'), ('x', 'XX'), ('y', 'Y')])
        #=======================================================================
        self.assertEqual(vowels - letters, expected, "Wrong substraction in CustomOrderedDict (list)")
        self.assertEqual(vowels - letters_cod, expected, "Wrong substraction in CustomOrderedDict (CustomOrderedDict)")
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")), "Wrong substraction in CustomOrderedDict (modified self)")


class TestAttrDict(VerboseTestCase):
    '''Test exercise 1: data model and customization of basic type
    '''
    def test_setattr_existent(self):
        '''Check __setattr__ customization of AttrDict
        It must update a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.a = 0
        self.assertTrue('a' not in attr_d.__dict__, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d['a'], 0, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.a, 0, "Wrong attribute assignment in AttrDict")

    def test_setattr_new(self):
        '''Check __setattr__ customization of AttrDict
        It must update a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.f = 6
        self.assertTrue('f' not in attr_d, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.__dict__['f'], 6, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.f, 6, "Wrong attribute assignment in AttrDict")

    def test_delattr_new(self):
        '''Check __delattr__ customization of AttrDict
        It must delete a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.f = 6
        del attr_d.f
        self.assertTrue('f' not in attr_d, "Wrong attribute deletion in AttrDict")
        self.assertTrue('f' not in attr_d.__dict__, "Wrong attribute deletion in AttrDict")

    def test_delattr_existent(self):
        '''Check __delattr__ customization of AttrDict
        It must delete a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        del attr_d.a
        self.assertTrue('a' not in attr_d, "Wrong attribute deletion in AttrDict")
        self.assertTrue('a' not in attr_d.__dict__, "Wrong attribute deletion in AttrDict")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
