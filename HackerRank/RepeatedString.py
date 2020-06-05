"""
Repeated Strings

Create a string using the given input string to the length of given 'n' value and find the number of 'a' characters in it.

Complexity :
Time : O()
Space : O()
"""


def repeatedString(given_string, expected_length):
    curr_len = len(given_string)
    return given_string.count('a') * (expected_length // curr_len) + given_string[:expected_length % curr_len].count('a')


print(repeatedString('aba', 10))

