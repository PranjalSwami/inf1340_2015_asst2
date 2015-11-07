#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    # If the substring is not found it returns -1.

    assert find("This is an ex-parrot", "orange", 0, 20) == -1

    # Test case to find a substring

    assert find ("Humpty dumpty sat on the wall", "wall", 0, 30) == 25

    # Test case to find special characters.

    assert find ("what does the # do?", "#", 0, 20) ==  14




def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    # If the substring is not found it returns an empty string.
    assert multi_find("Ni! Ni! Ni! Ni!", "do", 0, 20) == ""

    # Test case for finding  the position of blank spaces.
    assert multi_find("Ni! Ni! Ni! Ni!", " ", 0, 20) == "3,7,11"

    # Test case to find special characters  in the main string .
    assert multi_find( "Ni! Ni! Ni! Ni!", "!", 0, 20) == "2,6,10,14"

    # Test case to find mutiple words.
    assert multi_find( "HAHAHA! That was so funny", "was so funny", 0, 25) == "13"



