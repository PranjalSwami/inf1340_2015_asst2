##!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin
This module converts English words to Pig Latin words
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

VOWELS = ["a","e","i","o","u"]

def pig_latinify(word):
    """
 
    :param : word should be a string
    :return: the pig-latinified word as a string
    :raises: ValueError
    """

    pyg = 'ay'
    pyg_yay = "yay"
    original = raw_input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if "aeiou".find(first) != -1:
            new_word = word + pyg_yay
            print new_word
        else:
            new_word = word[1:len(word)] + first + pyg
            print new_word
    else:
        print 'Entry did not contain all letters'

pig_latinify("word")