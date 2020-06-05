"""
Palindrome Checking
"""

"""
Anagrams
"""
anagram_check = lambda x1,x2 : sorted(x1) == sorted(x2)
print(anagram_check("elvis","levis"))

# Single approach (prob : converting the strings to lower case)
def singleLineApproach(stringCheck):
    if str.lower(stringCheck) == str.lower(stringCheck[::-1]):
        return True
    else:
        return False

single_line_lambda = lambda stringCheck : stringCheck == stringCheck[::-1]
print(single_line_lambda("nayan"))

# print(singleLineApproach("Nayan"))
# print(singleLineApproach("Kiran"))

# Reverse String character approach
def charReverseApproach(stringCheck):
    reverseString = []
    for char in reversed(range(len(stringCheck))):
        reverseString.append(stringCheck[char])
    reversedString = "".join(reverseString)

    if stringCheck == reverseString:
        return True
    else:
        return False


print(charReverseApproach("Nayan"))
print(charReverseApproach("Kiran"))


