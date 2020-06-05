"""
Zoo Checker : Check the number of 'z' characters and 'o' characters in a sample repeating 'z,o' characters
with max length of 20, with satisfying 2*x = y equation, x is no of 'o' char and y being 'z'

Time Complexity : O(N) : N being the length of the test string
Space Complexity : O(1) : only z_count and o_count variables are taken care of
"""


def zoo_checker(zoo_str):
    z_count = 0
    o_count = 0
    for each_char in zoo_str:
        if each_char == "z":
            z_count += 1
        elif each_char == "o":
            o_count += 1
        else:
            pass
    print(z_count)
    print(o_count)
    return 2 * z_count == o_count


def zoo_caller(zoo_string):
    if len(zoo_string) <= 20:
        if zoo_checker(zoo_string):
            print("Yes")
        else:
            print("No")
    else:
        print("String is longer than 20")

# Yes
zoo_caller("zzzoooooo")
# No
zoo_caller("zzoooooooo")