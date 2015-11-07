##!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin
This module converts English words to Pig Latin words
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def pig_latinify(word):
    """

    :param : Input is a string
    :return: The piglatin translation of an alphabetic string
    :raises: Error if illegal input is entered
    """
    #Create varable to hold list of vowels in case list used more than once
    vowels = ["a","e","i","o","u"]
    #Varable pyg holds string "ay"
    pyg = 'ay'
    #Varable pyg_yay holds string "yay"
    pyg_yay = 'yay'
    #Input must be both a string and alphabetic letter
    if type(word) is str and word.isalpha():
    #Input with capital letters are transformed to lower case
        word = word.lower()
    #Counter variable is initialize to zero
        counter = 0
    #For indivual letters inside the legal input
        for letter in word:
        #first_letter represents the first letter of the legal input
            first_letter = word[0]
            #if the first letter of the legal input is in the vowels list, the word is concatanated with string "yay"
            if first_letter in vowels:
                return word + pyg_yay
            #Check if the first letter in the word is in the vowels list
            elif word[counter] in vowels:
                #When a vowel is reached, place the consonants in front the vowel at the end of the word
                #Concatenate the prefix "ay"
                return word[counter:] + word[:counter] + pyg
            # if the first letter is not in vowels list loop through the word until a vowel is found
            counter = counter + 1
    else:
        #if the input is not alphabetic or a number return an error
        return "Error: This input contains numbers or non-letter characters"




