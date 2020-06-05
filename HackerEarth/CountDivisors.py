"""
Count Divisors
Find the number of divisors of numbers in the range, l & r (inclusive) by k,
l,r,k are inputs

Complexity :
Time : O((R+1) - L) /O(N): where N is the range of numbers between L&R inclusive
Space : O(1) : Constant
"""


def divisor_counter(start, end, divisor):
    div_counter = 0
    for each_num in range(start, end+1):
        if each_num % divisor == 0:
            div_counter += 1

    return div_counter


print("Case 1")
print(divisor_counter(1, 10, 1))

print("Case 2")
print(divisor_counter(20, 50, 7))

