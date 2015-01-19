#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Exercises MOD 04: Strings
'''
import unittest


def sum_chars_text(text):
    '''given a text str, add all chars by its code
        tip:
            >>> c = 'c'
            >>> ord(c)
            99
    '''
    pass


def reverse_text_by_word(text):
    '''given a text, reverse it by words

        >>> reverse_text_by_word('Sparse is better than dense.')
        'dense. than better is Sparse'
    '''
    pass


def remove_identation_multiline_string(text):
    '''given a multiline text, removes identation

        >>> remove_identation_multiline_string("""Complex is better than complicated.
                                                  Flat is better than nested.""")
        "Complex is better than complicated. Flat is better than nested."
    '''
    pass


class ModStringTestCase(unittest.TestCase):

    def test_sum_chars_text(self):
        '''implement sum_chars_text'''
        text = 'In the face of ambiguity, refuse the temptation to guess.'
        assert sum_chars_text(text) == 5307

    def test_reverse_text_by_word(self):
        '''implement reverse_text_by_word'''
        text = "rules. the break to enough special aren't cases Special"
        assert reverse_text_by_word(text) == "Special cases aren't special enough to break the rules."

    def test_remove_identation_multiline_string(self):
        '''implement remove_identation_multiline_string'''
        text = """ Complex is better than complicated.
                    Flat is better than nested."""
        assert remove_identation_multiline_string(text) == 'Complex is better than complicated. '\
                                                           'Flat is better than nested.'


if __name__ == '__main__':
    unittest.main()
