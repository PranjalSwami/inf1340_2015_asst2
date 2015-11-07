#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    is_same_schema = check_same_schema(table1, table2)
    if is_same_schema == False:
        raise MismatchedAttributesException("Schemas do not match")

    # Adds contents of table1 and table2 into a single list. This addition might contain duplicates
    union_table = table1 + table2

    # Some duplicates will be here. Remove them
    union_table = remove_duplicates(union_table)

    return union_table



def intersection(table1, table2):
    """
    Describe your function

    """
    def intersection(table1, table2):
    """
     Perform the intersection set operation on tables, table1 and table2.

    """
    is_same_schema = check_same_schema(table1, table2)
    if not is_same_schema:
        raise MismatchedAttributesException("Schemas do not match")

    # Intersection means: only add rows in table1 that also exist in table2
    index = 0
    result_table = []
    for table1_row in table1:
        is_row_in_table2 = check_row_in_table(table2, table1_row)
        # If row in table1 is also present in table2, it's an intersection. Add it to result table
        if is_row_in_table2:
            result_table.append(table1_row)

        index += 1

    return result_table



def difference(table1, table2):
    """
    Describe your function

    """
    return []


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

