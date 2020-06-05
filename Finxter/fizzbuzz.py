"""
FizzBuzz implementation
Print "Fizz", if number is a mulitple of 3
Print "Buzz", if number is a multiple of 5
Print "FizzBuzz", if number is a multiple of 5 & 3
"""


# Approach 1
def fizzbuzz_operation(first_value, mod_value):
    return (first_value % mod_value) == 0


def fizzbuzz_caller(array, fizz: int = 3, buzz: int = 5):
    for i in array:
        print("fizz"*fizzbuzz_operation(i, fizz)+"buzz"*fizzbuzz_operation(i, buzz) or i)


fizzbuzz_caller(list(range(20)), 3, 5)

