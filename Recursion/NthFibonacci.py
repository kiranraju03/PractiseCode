"""
Question : Find the nth fibonacci number in the sequence by taking the position of the fibonacci as input
"""
#Answers:

"""
Naive Method :

Time complexity : O(2^n)
As each call has 2 calls back to the function in each level.

Space complexity : O(n)
As the call stack is filled with recursive calls to the function, which is n calls.
"""
def getNthFibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFibonacci(n-1) + getNthFibonacci(n-2)

"""
Memoization (Caching) Technique :

Time & Space complexity : O(n)
As each call will store a value into the cache m/y
"""

def getNthFibonacci(n, memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibonacci(n-1, memoize) + getNthFibonacci(n-2, memoize)
        return memoize[n]

"""
Iterative Solution:

Time complexity : O(n)
As each call is made to change the array values.

Space complexity : O(1)
As each call will manipulate just 2 values in the array.
"""

def getNthFibonacci(n):
    fibArray = [0, 1]
    counter = 3
    while counter <= n:
        nextFibValue = fibArray[0] + fibArray[1]
        fibArray[0] = fibArray[1]
        fibArray[1] = nextFibValue
        counter += 1
    if n>1:
        return fibArray[1]
    else:
        return fibArray[0]

print(getNthFibonacci(100))

