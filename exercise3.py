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
    :return: returns the union of two tables
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
    Perform the intersection set operation on tables, table1 and table2.
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: returns the intersection of two tables
    :raises: MismatchedAttributesException:

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

    #  If only one row is present in return table it is the header row.
    #  We should return an empty list
    if len(result_table) > 1:
        return result_table
    else:
        return []


def difference(table1, table2):
    """
    Describe your function
    Perform the difference set operation on tables, table1 and table2
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: returns the difference of two tables
    :raises: MismatchedAttributesException:

    """
    is_same_schema = check_same_schema(table1, table2)
    if not is_same_schema:
        raise MismatchedAttributesException("Schemas do not match")


    # Difference means: only add rows in table1 that do not exist in table2

    index = 0
    result_table = []
    # We manually add schema headers to result table
    result_table.append(table1[0])
    for table1_row in table1:
        is_row_in_table2 = check_row_in_table(table2, table1_row)
        # If row in table1 is not present in table2, it's a difference. Add it to result table
        if not is_row_in_table2:
            result_table.append(table1_row)

        index += 1

    # If only one row is present in return table it is the header row.
    #  We should return an empty list
    if len(result_table) > 1:
        return result_table
    else:
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

def check_same_schema(table1, table2):
    # If size of either table is zero then return False
    if (len(table1) == 0 or len(table2) == 0):
        return False

    # If number of headers is different, return False
    table1_headers = table1[0]
    table2_headers = table2[0]
    if (len(table1_headers) != len(table2_headers)):
        return False

    # Check if each header matches
    index = 0
    is_same_schema = True
    for table1_header in table1_headers:
        # Check if table1 header matches table2 header. If not, set is_same_schema as False and get out of loop
        if(table1_header != table2_headers[index]):
            is_same_schema = False
            break

        index = index + 1
    return is_same_schema


def check_row_in_table(table, row):
    is_row_in_table = False
    # Check if row matches any of the rows present in table
    for table_row in table:
        # For each row in table, try and compare values with the original row
        index = 0
        is_row_match = True
        for row_value in table_row:
            if row_value != row[index]:
                is_row_match = False
                break

            index = index + 1

        # If a matching row is found, is_row_match would be true
        if is_row_match:
            # Return true since match is found
            is_row_in_table = True
            break

    return is_row_in_table



class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

