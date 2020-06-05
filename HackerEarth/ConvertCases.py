"""
Convert Case of a string
"""

# Approach 1
str_Case = input()
new_str = ""
for each_char in str_Case:
    if each_char.islower():
        new_str += each_char.upper()
    elif each_char.isupper():
        new_str += each_char.lower()

print(new_str)

# Approach 2 : Shorthand
str_Case = input()
print(str_Case.swapcase())
