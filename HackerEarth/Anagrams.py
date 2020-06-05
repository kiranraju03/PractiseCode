"""
Make Anagrams
Given 2 strings, make both of them anagrams, by specifying the min number of deletions to be made
Any characters can be deleted from either of the strings

Time : O(N + M) : M, N being the lengths of the strings
Space : O(1) / O(26) : As dict is created to keep track of the characters
"""


# Method 1 : Manual process
def char_dict_creater(char_str):
    char_dict = {}
    for each_char in char_str:
        if each_char not in char_dict.keys():
            char_dict[each_char] = 1
        else:
            char_dict[each_char] += 1
    return char_dict


# Takes in 2 strings and checks the min deletions to make them anagrams
def anagramChecker(str1, str2):
    # creating dict's for both the strings
    str1_dict = char_dict_creater(str1)
    str2_dict = char_dict_creater(str2)
    # min deletions counter
    diff_counter = 0
    # Traverse 1st string dict wrt 2nd string
    for each_char_key in str1_dict.keys():
        # check if the char matches in the 2nd string
        if each_char_key in str2_dict:
            # if match found, remove the second string characters
            diff_counter += max(0, str1_dict[each_char_key] - str2_dict[each_char_key])
        else:
            # if char is not found in 2nd string, then char's have to be deleted in the 1st
            diff_counter += str1_dict[each_char_key]

    # Traverse 2nd string wrt 1st string
    for each_char_key in str2_dict.keys():
        # check if char is in 1st string
        if each_char_key in str1_dict:
            diff_counter += max(0, str2_dict[each_char_key] - str1_dict[each_char_key])
        else:
            diff_counter += str2_dict[each_char_key]

    return diff_counter


print(anagramChecker("abc", "cde"))

# Method 2 : Short-hand using collections
from collections import Counter

str1_count = Counter("abc")
str2_count = Counter("cde")

# String 1 to be an anagram of string 2, no of deletions
str1_str2 = str1_count - str2_count
print(str1_str2)

str2_str1 = str2_count - str1_count
print(str2_str1)

# Total no of edits
print( str2_str1 + str1_str2 )

