#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    word =  raw_input("Enter your word: ")

    if word[0] == "a" or word[0] == "e" or \
    word[0] == "i" or word[0] == "o" or \
    word[0] == "u":
        print word + "yay"
    elif word[0] != "a" or word[0] != "e" or \
    word[0] != "i" or word[0] != "o" or \
    word[0] != "u":
        print word[1:len(word)] + word[0] + "ay"

    return result


pig_latinify("hello")