#-*- coding: utf-8 -*-
u'''
MOD 05: Iterators, generators and coroutines
'''
import unittest
import exercise as source
# import solution as source


class VerboseTestCase(unittest.TestCase):
    '''Base unit tests class for verbose output
    '''
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.longMessage = True


class TestRepeatItems(VerboseTestCase):
    '''Test mod 05 repeat_items exercise
    '''

    def test_repeat_items(self):
        '''Test repeat_items([1, 2, 3])
        '''
        sequence = [1, 2, 3]
        expected = [1, 1, 2, 2, 3, 3]
        self.assertEqual(list(source.repeat_items(sequence)), expected)

    def test_repeat_items_empty_list(self):
        '''Test repeat_items([])
        '''
        sequence = expected = []
        self.assertEqual(list(source.repeat_items(sequence)), expected)

    def test_repeat_items_single_item(self):
        '''Test repeat_items([1])
        '''
        sequence = [1]
        expected = [1, 1]
        self.assertEqual(list(source.repeat_items(sequence)), expected)

    def test_repeat_items_4_times(self):
        '''Test repeat_items([1, 2, 3], 4)
        '''
        sequence = [1, 2, 3]
        expected = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        self.assertEqual(list(source.repeat_items(sequence, 4)), expected)

    def test_repeat_items_once(self):
        '''Test repeat_items([1, 2, 3], 1)
        '''
        sequence = [1, 2, 3]
        expected = sequence
        self.assertEqual(list(source.repeat_items(sequence, 1)), expected)

    def test_repeat_items_0_times(self):
        '''Test repeat_items([1, 2, 3], 0)
        '''
        sequence = [1, 2, 3]
        expected = []
        self.assertEqual(list(source.repeat_items(sequence, 0)), expected)


class TestIzip(VerboseTestCase):
    '''Test mod 05 izip exercise
    '''

    def test_izip(self):
        '''Test izip([1, 2, 3], ['a', 'b', 'c'])
        '''
        sequence_1 = [1, 2, 3]
        sequence_2 = ['a', 'b', 'c']
        expected = [[1, 'a'], [2, 'b'], [3, 'c']]
        self.assertEqual(list(source.izip(sequence_1, sequence_2)), expected)

    def test_izip_second_longer(self):
        '''Test izip([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])
        '''
        sequence_1 = [1, 2, 3]
        sequence_2 = ['a', 'b', 'c', 'd', 'e']
        expected = [[1, 'a'], [2, 'b'], [3, 'c']]
        self.assertEqual(list(source.izip(sequence_1, sequence_2)), expected)

    def test_izip_first_longer(self):
        '''Test izip([1, 2, 3, 4, 5], ['a', 'b', 'c'])
        '''
        sequence_1 = [1, 2, 3, 4, 5]
        sequence_2 = ['a', 'b', 'c']
        expected = [[1, 'a'], [2, 'b'], [3, 'c']]
        self.assertEqual(list(source.izip(sequence_1, sequence_2)), expected)

    def test_izip_no_sequences(self):
        '''Test izip([1, 2, 3, 4, 5], ['a', 'b', 'c'])
        '''
        expected = []
        self.assertEqual(list(source.izip()), expected)

    def test_izip_3_sequences(self):
        '''Test izip([1, 2, 3, 4, 5], ['a', 'b', 'c'], [None, True, False])
        '''
        sequence_1 = [1, 2, 3, 4, 5]
        sequence_2 = ['a', 'b', 'c']
        sequence_3 = [None, True, False]
        expected = [[1, 'a', None], [2, 'b', True], [3, 'c', False]]
        self.assertEqual(list(source.izip(sequence_1, sequence_2, sequence_3)), expected)

    def test_izip_empty_sequences(self):
        '''Test izip([1, 2, 3], [], [])
        '''
        sequence_1 = [1, 2, 3]
        sequence_2 = sequence_3 = expected = []
        self.assertEqual(list(source.izip(sequence_1, sequence_2, sequence_3)), expected)


class TestMerge(VerboseTestCase):
    '''Test mod 05 merge exercise
    '''

    def test_merge(self):
        '''Test merge([1, 2, 3], ['a', 'b', 'c'])
        '''
        sequence_1 = [1, 2, 3]
        sequence_2 = ['a', 'b', 'c']
        expected = [1, 'a', 2, 'b', 3, 'c']
        self.assertEqual(list(source.merge(sequence_1, sequence_2)), expected)

    def test_merge_second_longer(self):
        '''Test merge([1, 2, 3], ['a', 'e', 'i', 'o', 'u'])
        '''
        sequence_1 = [1, 2, 3]
        sequence_2 = ['a', 'e', 'i', 'o', 'u']
        expected = [1, 'a', 2, 'e', 3, 'i', 'o', 'u']
        self.assertEqual(list(source.merge(sequence_1, sequence_2)), expected)

    def test_merge_first_longer(self):
        '''Test merge(['a', 'e', 'i', 'o', 'u'], [1, 2, 3])
        '''
        sequence_1 = ['a', 'e', 'i', 'o', 'u']
        sequence_2 = [1, 2, 3]
        expected = ['a', 1, 'e', 2, 'i', 3, 'o', 'u']
        self.assertEqual(list(source.merge(sequence_1, sequence_2)), expected)

    def test_merge_3_sequences(self):
        '''Test merge(['a', 'e', 'i', 'o', 'u'], [None, True, False], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        '''
        sequence_1 = ['a', 'e', 'i', 'o', 'u']
        sequence_2 = [None, True, False]
        sequence_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = ['a', None, 0, 'e', True, 1, 'i', False, 2, 'o', 3, 'u', 4, 5, 6, 7, 8, 9]
        self.assertEqual(list(source.merge(sequence_1, sequence_2, sequence_3)), expected)

    def test_merge_empty_sequences(self):
        '''Test merge([], [], [])
        '''
        sequence_1 = sequence_2 = sequence_3 = expected = []
        self.assertEqual(list(source.merge(sequence_1, sequence_2, sequence_3)), expected)


class FlattenList(VerboseTestCase):
    '''Test mod 05 flatetn exercise
    '''

    def test_flatten(self):
        '''Test flatten of several lists works
        '''
        self.assertEquals(list(source.flatten([])), [])
        self.assertEquals(list(source.flatten([[]])), [])
        self.assertEquals(list(source.flatten([0])), [0])
        self.assertEquals(list(source.flatten([0, [1]])), [0, 1])

        self.assertEquals(list(source.flatten([0, [1, [3]]])), [0, 1, 3])

        L = [0, 1, [2, 3], 4, [5]]
        import copy
        M = copy.deepcopy(L)
        self.assertTrue(list(source.flatten(L)) == [0, 1, 2, 3, 4, 5])
        self.assertTrue(L == M)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
