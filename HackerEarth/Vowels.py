"""
Count the number of vowels in each test case of the string input given

Complexity :
Time : O(N) : N is the length of the string
Space : O(N) : N is the length of the string, as its stored in a list

"""

# Flaw : substring code takes too much time for bigger inputs, min version find the logic


def vowel_counter_substring(test_string_list, vowel):

    vowel_count = 0

    while len(test_string_list) > 0:

        for j in range(1, len(test_string_list)+1):
            nl = test_string_list[0: j]
            print(nl)
            # each_count = len([each for each in nl if each in vowel])
            for each in nl:
                if each in vowel:
                    vowel_count += 1
            # vowel_count += each_count
        str_list.pop(0)

    return vowel_count


def vowel_counter_min(test_string, vowel):
    vowel_counter = 0

    str_len = len(test_string)

    for i in range(str_len):
        if test_string[i] in vowel:
            # find how this works???
            vowel_counter += (i + 1) * (str_len - i)

    return vowel_counter


test_cases = int(input())

for each_case in range(test_cases):
    test_str = input()
    # ln_str = len(test_str)

    str_list = list(test_str)

    vowels = 'AEIOUaeiou'

    print(vowel_counter_substring(str_list, vowels))
    print(vowel_counter_min(test_str, vowels))


