"""
Product Sum
Time : O(N) : N is the total number of elements including the sub-arrays
Space : O(D) : Depth of the array, ie., number of recursive calls made

Input Type :
[x+y] : x+y
[x, [y,z]] : x + 2(y+z)

Output : Sum of product of sub-list elements
"""


def product_sum(array, multiplier=1):
    sum_of_all = 0
    for each_element in array:
        if type(each_element) is list:
            sum_of_all += product_sum(each_element, multiplier + 1)
        else:
            sum_of_all += each_element

    return sum_of_all * multiplier


print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
