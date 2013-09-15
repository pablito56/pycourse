#-*- coding: utf-8 -*-
u'''
Test exercise 0: mutable and immutable types common errors
'''
import unittest
import exercise_mod_04 as source
# import solution_mod_04 as source


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestCustomOrderedDict(VerboseTestCase):
    '''Test exercise mod 06 CustomOrderedDict
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
        self.assertEqual(vowels + source.CustomOrderedDict(letters), expected,
                         "Wrong addition in CustomOrderedDict (CustomOrderedDict)")
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")),
                         "Wrong addition in CustomOrderedDict (modified self)")

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
        self.assertEqual(vowels, source.CustomOrderedDict(zip("aeiou", "AEIOU")),
                         "Wrong substraction in CustomOrderedDict (modified self)")


class TestAttrDict(VerboseTestCase):
    '''Test exercise mod 06 AttrDict
    '''
    def test_setattr_existent(self):
        '''Check __setattr__ customization of AttrDict. It must update a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.a = 0
        self.assertTrue('a' not in attr_d.__dict__, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d['a'], 0, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.a, 0, "Wrong attribute assignment in AttrDict")

    def test_setattr_new(self):
        '''Check __setattr__ customization of AttrDict. It must update a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.f = 6
        self.assertTrue('f' not in attr_d, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.__dict__['f'], 6, "Wrong attribute assignment in AttrDict")
        self.assertEqual(attr_d.f, 6, "Wrong attribute assignment in AttrDict")

    def test_delattr_new(self):
        '''Check __delattr__ customization of AttrDict. It must delete a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        attr_d.f = 6
        del attr_d.f
        self.assertTrue('f' not in attr_d, "Wrong attribute deletion in AttrDict")
        self.assertTrue('f' not in attr_d.__dict__, "Wrong attribute deletion in AttrDict")

    def test_delattr_existent(self):
        '''Check __delattr__ customization of AttrDict. It must delete a dictionary key only if it exists
        '''
        attr_d = source.AttrDict(zip("aeiou", range(1, 6)))
        del attr_d.a
        self.assertTrue('a' not in attr_d, "Wrong attribute deletion in AttrDict")
        self.assertTrue('a' not in attr_d.__dict__, "Wrong attribute deletion in AttrDict")


class TestFraction(VerboseTestCase):
    """Test exercise mod 06 Fraction
    """
    def test_fraction_rich_comparisson(self):
        """Test fractions rich comparisson operators overloading
        """
        fract1 = source.Fraction(5, 2)  # 2.5
        fract2 = source.Fraction(3, 2)  # 1.5
        fract3 = source.Fraction(25, 10)  # 2.5

        self.assertFalse(fract1 != fract3)  # 2.5 != 2.5
        self.assertTrue(fract1 == fract3)  # 2.5 == 2.5
        self.assertTrue(fract2 < fract3)  # 1.5 < 2.5

        # Let's try the other way
        self.assertTrue(fract1 >= fract2)   # 2.5 >= 1.5
        self.assertFalse(fract2 >= fract3)  # 1.5 >= 2.5

        # Let's try with other types
        self.assertTrue(fract1 >= 2)  # 2.5 >= 2
        self.assertTrue(fract2 == 1.5)  # 1.5 == 1.5

        # Let's try the other way with other types
        self.assertTrue(2 <= fract1)  # 2 <= 2.5
        self.assertTrue(1.5 == fract2)   # 1.5 == 1.5

        self.assertTrue(10 > fract1)  # 10 > 2.5
        self.assertFalse(10 < fract1)  # 10 < 2.5
        self.assertTrue(fract1 < 10)  # 2.5 < 10
        self.assertFalse(fract1 > 10)  # 2.5 > 10

    def test_fraction_math_ops(self):
        """Test fractions math operators overloading
        """
        fract1 = source.Fraction(5, 3)
        fract2 = source.Fraction(2, 3)
        self.assertEqual(fract1 + fract2, source.Fraction(7, 3))
        self.assertEqual(fract1 + 5,  source.Fraction(20, 3))
        self.assertEqual(3 + fract1, source.Fraction(14, 3))
        self.assertEqual(fract1 * fract2, source.Fraction(10, 9))
        self.assertEqual(5 * fract2, source.Fraction(10, 3))

    def test_fraction_item_access(self):
        """Test fractions math operators overloading
        """
        f1 = source.Fraction(7, 2)
        self.assertEqual(len(f1), 2)
        self.assertEqual(f1['num'], 7)
        self.assertEqual(f1[1], 2)
        f1[0] = 5
        f1['den'] = 3
        self.assertEqual(str(f1), "5/3")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
