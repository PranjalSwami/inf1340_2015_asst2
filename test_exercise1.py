#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # Test case to check what is the result if we type integer  and  string .
    assert pig_latinify("34apple") == "Error: This input contains numbers or non-letter characters"

    # Test case to check what is the result if we type integers.
    assert pig_latinify(33434343) == "Error: This input contains numbers or non-letter characters"


