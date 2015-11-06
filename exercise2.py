#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function
    We first compare each letter in the input string with the first character of the substring.
    If there is a match, then we try to get as many characters from the input string as there are in the substring.
    If these characters match with the substring we return the letter position.
    If no match is found we return -1

    :param :
    :return:
    :raises:

    """
    input_char_array = list(input_string)
    substring_char_array = list(substring)
    substring_first_char = substring_char_array[0]
    substring_length = len(substring)

    position = start
    for input_char in input_char_array[start:end]:
        if input_char == substring_first_char:
            possible_substring = ""
            for substring_char in input_char_array[position:position + substring_length]:
                possible_substring = possible_substring + substring_char
            if  possible_substring == substring:
                return position

        position = position + 1

    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""
    substring_position = start
    has_more_substring = True
    while has_more_substring:
        substring_position = find(input_string,substring,start,end)
        if substring_position != -1:
            result = result + str(substring_position) + ","
            start = substring_position + len(substring)
        else:
            has_more_substring = False

    if len(result) > 0:
        result = result[:-1]



    return result

