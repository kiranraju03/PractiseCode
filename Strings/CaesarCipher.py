"""
Caesar Cipher
Create an encrypted string using the key as the number of shifts to be made
"""

# Solution 1 : 26 characters Approach
# Time : O(1) : as we are dealing with only 26 characters, O(26), i.e., O(1) constant operation
# Space : O(n) : n is the length of the string that needs to be encrypted

def caesar_cipher(string, key):
    all_characters = "abcdefghijklmnopqrstuvwxyz"
    encrypted_format = ""
    for each_char in string:
        encrypted_format += all_characters[(all_characters.find(each_char) + key) % 26]
    return encrypted_format
print("Approach1")
print(caesar_cipher("kiranraju", 50))

# Solution 2 : 26 characters approach, with more focus on the key value, in scenarios where key>100, we need to keep in the 26 char range

def caesar_cipher2(string, key):
    all_char_str = "abcdefghijklmnopqrstuvwxyz"
    new_reduced_key = key % 26
    encry_str = ""
    for each_letter in string:
        encry_str_pos = all_char_str.index(each_letter) + key
        encry_str += (all_char_str[encry_str_pos] if encry_str_pos <= 25 else all_char_str[encry_str_pos % 26])
    return encry_str
print("Approach2")
print(caesar_cipher2("kiranraju", 50))

# Solution 3 : using ord function

def caesar_cipher_ord(string, key):
    all_char_str = "abcdefghijklmnopqrstuvwxyz"
    new_reduced_key = key % 26
    encry_str = ""
    for each_char in string:
        encry_pos = ord(each_char) + new_reduced_key
        encry_str += (chr(encry_pos) if encry_pos <=122 else chr(96 + encry_pos % 122))

    return encry_str

print("Approach3")
print(caesar_cipher2("kiranraju", 50))

