"""
Find Product : find and print the product of all the number in the array Modulo (10^9+7).

product = (product * array[value]) % (10 ** 9 + 7)

Time : O(N) : N is the size of the array
Space : O(1)
"""


def modulo_calc(update_num, arr_num):
    mod_num = (update_num * arr_num) % (10 ** 9 + 7)
    return mod_num


if __name__ == "__main__":
    array_size = int(input("Array size : "))
    # converting the space delimited input into a array of integers
    array_num = list(map(int, input("Array Elements : ").split()))
    mul_val = 1
    for each_ele in array_num:
        mul_val = modulo_calc(mul_val, each_ele)
    print(mul_val)
