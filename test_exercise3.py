#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

UNIQUE_TABLE_1 = [["Number", "Name", "Age"],
                    [1111, "Adam", 40],
                    [2222, "Bob", 41],
                    [3333, "Jack", 42]]
UNIQUE_TABLE_2 = [["Number", "Name", "Age"],
                    [4444, "George", 31],
                    [5555, "Steve", 32],
                    [6666, "Ron", 33]]

INVALID_SCHEMA = [["Number", "Name", "Age","Gender"],
                    [4444, "George", 31, "M"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    dummy = sorted(t1)
    dummy2 = sorted(t2)
    # return t1.sort() == t2.sort()
    return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result_unique_table = [["Number", "Name", "Age"],
                             [1111, "Adam", 40],
                             [2222, "Bob", 41],
                             [3333, "Jack", 42],
                            [4444, "George", 31],
                            [5555, "Steve", 32],
                            [6666, "Ron", 33]]

    assert is_equal(result_unique_table, union(UNIQUE_TABLE_1, UNIQUE_TABLE_2))

    # If schema is invalid MismatchedAttributesException raised
    is_invalid_schema = False
    try:
        assert is_equal(result, union(GRADUATES, INVALID_SCHEMA))
    except MismatchedAttributesException:
        is_invalid_schema = True

    assert is_invalid_schema == True







def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    result_unique_table = []

    assert is_equal(result_unique_table, intersection(UNIQUE_TABLE_1, UNIQUE_TABLE_2))

    # If schema is invalid MismatchedAttributesException raised
    is_invalid_schema = False
    try:
        assert is_equal(result, intersection(GRADUATES, INVALID_SCHEMA))
    except MismatchedAttributesException:
        is_invalid_schema = True

    assert is_invalid_schema == True


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

    result_unique_table = [["Number", "Name", "Age"],
                           [1111, "Adam", 40],
                            [2222, "Bob", 41],
                            [3333, "Jack", 42]]


    assert is_equal(result_unique_table, difference(UNIQUE_TABLE_1, UNIQUE_TABLE_2))

    result_same_table = []

    # If tables are the same the difference should return an empty list
    assert is_equal(result_same_table, difference(GRADUATES, GRADUATES))

    # If schema is invalid MismatchedAttributesException raised
    is_invalid_schema = False
    try:
        assert is_equal(result, difference(GRADUATES, INVALID_SCHEMA))
    except MismatchedAttributesException:
        is_invalid_schema = True

    assert is_invalid_schema == True

